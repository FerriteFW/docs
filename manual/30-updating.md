## 30. Updating the firmware

### What it's for

Ferrite installs and updates through the radio's stock bootloader, so a broken image can always be replaced and going back to stock is the same step.

### Using it

1. Get the Ferrite update file, `ferrite-VERSION.ffw`: one file with the firmware and its SPI parts (the text pack, the boot logo, the terminal's pages), signed.
2. Install it with Ferrite Console (Firmware › Update, or Install for a radio on stock firmware), or `flash.py <port> ferrite-VERSION.ffw --backup flash.bin`. Both check it first, flash the firmware, then write its parts over the cable; the radio restarts once more at the end. Other flashers (Radtel's updater, nicsure's web flasher) take the `firmware.btf` inside it (the `.ffw` is a zip): the radio then runs with short messages, the plain terminal and no logo until the update file is installed.
3. The tool catches the bootloader at the next restart. If it can't restart the radio, power-cycle it while the tool waits (30 s), or power on holding the **bottom two side buttons**.
4. To add SSB: in Ferrite Console, Firmware › Add SSB… with your stock `.BTF` (no update needed, INST-10.2); on the command line, `--ssb-from <stock .BTF>` with an update.

**An update that changes the flash layout** (layout 2 to 3, decision 333): flash it with Ferrite Console. After the new firmware starts, the radio shows "Finish the update" and leaves your channels and settings where they are; Console reads them over the cable, keeps a copy on your computer, writes them in the new layout and restarts the radio. Flashed any other way, the radio stays on that screen (it works, but saves nothing) until Console has done it.

**Back to stock:** in the web app, restore your SPI backup, then flash Radtel's `.BTF`. With `flash.py`, the same command with Radtel's file.

About (MENU 0 9 8) says how to enter the bootloader.

### Screens

No mock-up yet. There is no update screen: the bootloader does the update.

> **Spec: image**
>
> - **UPD-1** The image runs from 0x08003000 and is at most 1,012 KB, to the chip's end at 0x080FFFFF (decision 338). Past 948 KB it covers stock's marker sector at 0x080F0000, which the backup records (BACKUP-12).
> - **UPD-2** The image carries the model tag `RT-950      ` at 0x3E0 and 0x7E0 (INST-2).
> - **UPD-3** `.BTF`: first 1 KB plain, key block, the rest encrypted; zero key; last block plain; padded with 0xFF to whole 1 KB blocks.
> - **UPD-4** `btf.py` and `flash.py` refuse an image that fails a check: stack pointer, Thumb reset vector inside the image, model tag, size.
> - **UPD-5** The image carries a CRC in a trailer, checked at boot; if it fails, TX stays locked.

> **Spec: never harm the update path**
>
> - **UPD-6** As SAFE-3: Ferrite never writes MCU flash, the bootloader or the option bytes; the marker sector changes only through the bootloader, under an image that reaches it or the way back to stock (BACKUP-12).
> - **UPD-7** As SAFE-2: the SPI update area is never written; the storage driver refuses it and the installer refuses a stale header (INST-5).
> - **UPD-8** At boot, if 0x300000 holds the 0xA55A magic, About shows "pending stock update in flash".
> - **UPD-9** PA13/PA14 are never remapped, so SWD stays a last resort.

> **Spec: updates**
>
> - **UPD-10** Updates go through the stock bootloader at its own fixed rate on UART4; Ferrite needs no update code.
> - **UPD-11** An update leaves the SPI flash alone: settings, channels and the SSB patch stay. One that changes the flash layout (UPD-16) has Ferrite Console move them (LINK-62).
> - **UPD-12** On a new settings version, the firmware migrates the old settings and keeps what it can.
> - **UPD-13** A bundled SSB patch is found after the image, checked (framing, size, SHA-256) and copied to SPI flash; an unknown hash is stored only after on-screen confirmation.
> - **UPD-14** Ferrite reacts to no power-on combo except MENU (settings reset); the bootloader's side-button combo is left alone.
> - **UPD-16** The layout header (0x000000: magic "FRRT", the layout version, 10 installer bytes, CRC-32; Appendix G) says which layout the chip's data is in. At power-on the firmware reads it first: its own version (3) mounts as usual; a Ferrite header with another version, or layout 2's header at its old place 0x02C000 with no layout 3 header, means another layout's data, and the firmware leaves it alone: no format, no write anywhere (not the scratch ring's recovery, not the SSB patch install, not the calibration CRC), nothing read as records, nothing saved this power-on. The radio shows D25 "Finish the update" (BACK uses the radio without saving) and says so over the link: `HELLO` and `INFO` end with this firmware's layout and the chip's (LINK-62), and the raw data messages work (LINK-59, LINK-60), so Console can move the data and stamp the header (decision 333). A migration mark at 0x00E000 (decision 339: a move Console began and hasn't stamped) comes first: the same, with the chip's layout said as 255, half moved. No header at all is a first install, formatted (INST-6), only when none of Ferrite's records are there either (a blank chip, or stock's data); a chip with no header but a Ferrite settings record (layout 3's place or layout 2's) or a channel record in the first channel sector waits for Console the same way (255), never formatted silently (decision 339). A firmware flashed without Console's migration therefore never misreads old data, and an interrupted migration, cut at any point, starts again from Console's copy.
>     - **UPD-16.1** While Console or `flash.py` writes the radio's flash over the cable (the raw writes of the layout move or the update's SPI parts), the page says so instead: "Updating...", "Writing the update to the radio's flash. Keep the cable in; the radio restarts when it's done.", with a moving bar (Alex, Nov 3: a spinner, so the update isn't confusing). It goes back to D25 when the writes stop.
>     - **UPD-16.2** While the update's SPI parts are written, the page's second line counts them and says whether the part is being written or read back for its CRC: "Part 2 of 4: writing", then "Part 2 of 4: checking" (Alex, Nov 3: the bar starts again for each part, twice, so say which and why). The installers send `DATA_WRITE` `PART` (LINK-60) before each part's erases; a firmware without it answers `bad argument` and the installers go on. The layout move sends none: the line stays empty.
> - **UPD-15** Releases carry a SHA-256 checksum and a minisign signature for each file; `flash.py` and the web app check both before flashing and refuse a mismatch. The bootloader checks no signature, so this protects the download (tampered or corrupted files), not the radio; the image CRC (UPD-5) still guards the flash.

> **Spec: the update file**
>
> - **UPD-20** A Ferrite update is one file, `.ffw` (decision 335): a zip, every entry stored. Its first entry is `manifest.json` (format `ferrite-update-1`): the build ID, the version, the model (the bootloader's tag, `RT-950`), the build kind, the SPI layout it needs, and every file with its size, SHA-256 and target: `mcu` for `firmware.btf` (the image as today), `spi` with the address and the most it may take for each part under `spi/`. Then `manifest.minisig` when signed (minisign, the release key, over the manifest's bytes), `firmware.btf` and the parts. `tools/mkbtf.sh` packs one, unsigned, beside every image; the release workflow signs the manifest with the release key and ships `ferrite-VERSION.ffw` with the reader image (no separate Ferrite `.btf` or `.minisig`).
> - **UPD-21** The installers (`flash.py`, Console's Update and Install) check the whole file before writing anything: the signature against Ferrite's key (an unsigned file only with the developer flag: `flash.py --dev-unsigned`, Console's "Allow unsigned files"), every file's size and SHA-256, and each part's header naming the manifest's build. Then the backup as today, the image through the bootloader, then, once Ferrite answers on the cable, each part's sectors erased, its bytes programmed and its CRC read back over the link's raw writes (LINK-59 – LINK-62), and the layout stamped: the radio restarts with its parts. A radio whose data waits in another layout gets its data moved by Console first (UPD-16). Each part starts with a 32-byte header (magic, format, the build ID, length, CRC-32 of the rest); at power-on the firmware checks each part once and uses it only when the header is its kind's, the build ID is its own and the CRC holds; otherwise every user of it falls back. The self-test lists "SPI parts" as how many of them are good (not a transmit lock).
> - **UPD-22** The text pack (`text-en.bin`, layout 3's text region at 0x090000, 64 KB at most): the long, rarely read text (menu, option-sheet and screen notes, setup's pages, tips, the terminal's `help`, usage lines and refusals) is kept there, not in MCU flash. A text is read when it is drawn or sent, never per frame. Without the pack a note is left out, a terminal refusal says the text pack is missing, `help` says so in one line and the self-test's note names it. Transmit refusals, the Extend TX warning, About's licence (SELF-10) and "Finish the update" stay in MCU flash.
> - **UPD-23** The boot logo's two masks (`logo.bin`, 0x240000) and the terminal's page templates (`term-vt.bin`, 0x248000; TERM-47) are SPI parts too. The logo streams from the SPI flash a row at a time while the boot screen draws it (no RAM kept); without it the boot screen shows the wordmark alone. The templates (the pages' program, decision 346) are read a page at a time, at most 4 KB with the code all pages share, once a terminal redraw, key, or step of a change to several channels; without them the terminal is the plain command line (TERM-47), chosen when it starts.
> - **UPD-24** A part aimed at calibration (0x00F000–0x00FFFF), the update area (0x300000 up), the layout header or the migration mark, or anywhere outside the layout 3 regions parts may use (the text pack, language packs, boot screens, fonts), is refused by both installers whatever the manifest says, before anything is written; the radio's raw write refuses calibration and the update area itself (LINK-60).
> - **UPD-25** Console looks for a newer Ferrite on the internet as well as the one it carries (decision 394): a small feed (format `ferrite-feed-1`: the latest Ferrite's version, the link protocol it speaks, its `.ffw`'s name, https address and SHA-256, and the latest Console's version). When the feed's Ferrite is newer than the bundled one and speaks Console's link protocol, Update offers it, downloads it, refuses it unless its SHA-256 matches, and checks the whole file as any other (UPD-21: Ferrite's signature), so a new Ferrite needs no new Console. A newer Ferrite on another protocol isn't offered: the page says it needs a newer Console. Off until the releases are public (Alex, Nov 13, 2026); nothing is fetched meanwhile.
>     - **UPD-25.1** The release Update offers (the feed's or the bundled one) is used only when its signed manifest names the version the feed (or Console's own manifest) names, and one from the feed only when that version is newer than the bundled release (console#84: the feed's version was never compared with the signed file's, so a feed could roll a radio back). A release older than the radio's running Ferrite is refused; a file chosen by hand under Advanced may be older (a deliberate downgrade), and Update says so.
>     - **UPD-25.2** Update shows Ferrite's release notes (console#42). They come in the update feed itself (`ferrite.notes`: the last 5 releases' notes, newest first, the Ferrite part of each release's notes without the Console and Install sections), so they always match the version offered; a Console that doesn't know the field ignores it. With a release on offer, Update shows the notes of every release newer than the radio's Ferrite up to that one, newest first, each one collapsible and the newest open; a radio older than every note listed gets a line saying the earlier releases' notes aren't shown. Not connected: the offered release's notes. A file chosen by hand shows its own release's notes when the feed has them, else none. Without the internet (or a feed without notes) a line says the release notes couldn't be loaded; the update works as before. The notes are rendered from Markdown with any HTML in them shown as text.
> - **UPD-26** The desktop Console updates itself (decision 394): it checks Console's latest release once a session, and the bar offers the newer version; on macOS and the Linux AppImage it downloads, installs and restarts, the update checked against Console's own updater key (never the firmware key); the web build and Windows' portable app link to the download instead. Off until the releases are public, as UPD-25.
> - **UPD-27** Console uses an image (Ferrite, the reader, the restorer; a .ffw or a bare .btf) only with a valid Ferrite signature: a bad one is always refused; none, only with the developer option Allow unsigned files (a local build; release Consoles bundle signed images). A release downloaded from the update feed is signed whatever the option, and is always a .ffw. (A review of Nov 20, 2026: a bare .btf installed unsigned, labelled only "Not signed", and the reader and restorer were taken unsigned.)

### Under the hood


### Status

`btf.py` and `flash.py` done and round-tripped against every stock `.BTF`. Roadmap 1b (installer with backup), 3e (web flasher with backup, erase and restore, SSB bundling). Done when a fresh radio installs from the browser and a backup restores to working stock.


### Settled details

- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - UPD-15: decision 73, Oct 7, 2026.
  - UPD-20 – UPD-24: decision 335, Oct 31, 2026 (Alex: "nice and fucking clean 1 update file.. not 2 or more"); built Nov 3, 2026 (decision 343). The parts saved 22.7 KB of MCU flash (tx 793,328 to 770,592 B).
  - UPD-16: decision 339, Nov 1, 2026: the migration mark and the format guard (a stamp cut by the restart formatted clear).
  - UPD-16: decision 333, Oct 31, 2026 (Alex: "we could back it up, translate, rewrite it and update the firmware.. cleanly.. and NO complex table mapping crap needed at runtime"). Built Nov 1, 2026. Layout 2's firmware formats a chip whose header at 0x02C000 it doesn't find, so flashing a layout 2 image over layout 3 data loses it on the radio (Console's copy keeps it): go back through Console.

### Open points

- The bootloader's buttons are PF1 + PF2 (PE5 + PA12): held at power-on, stock shows its UPDATE screen (confirmed Oct 8, 2026, day-zero).

---

