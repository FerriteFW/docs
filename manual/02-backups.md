## 2. Before you start: backups and the way back to stock

### What it's for

Installing Ferrite erases stock's data in the SPI flash. The backup is your way back to a fully working stock radio.

### Using it

1. Keep your stock `.BTF` from Radtel: it's how you go back, and the SSB receiver needs it.
2. The installer (Ferrite Console's Install page, or `flash.py`) first loads the reader image (a small read-only image: it has no code that writes) through the bootloader, reads the whole 4 MB SPI flash to your computer and verifies it, and only then flashes Ferrite. Ferrite erases on its first boot. Keep that file. It holds stock's channels, settings, splash, fonts and voice prompts.
3. **Back to stock** (Ferrite Console's Install page): drop in the saved file and your stock `.BTF`. Console writes the backup back into what Ferrite used (over the cable, chapter 29), checks it, then flashes the stock `.BTF`.

Calibration and the bootloader's update area are never erased, so they need no restore. Without the backup, stock runs without its channels, fonts or prompts.

Without Console: with the reader (or the older hwtest) running, `fw/tools/flashdump.py <port> cal.bin --cal` and `flashdump.py <port> flash.bin` (about 7 min per 2 MB).

### Screens

No mock-up yet.

> **Spec: backup**
>
> - **BACKUP-1** Before any erase, the whole flash is backed up on the user's computer.
>     - **BACKUP-1.1** Before any erase, read the whole 4 MB and save it on the user's computer.
>     - **BACKUP-1.2** The backup is named with the radio's ID.
>     - **BACKUP-1.3** It carries a CRC-32 per region.
> - **BACKUP-2** No erase until the backup is saved and confirmed.
> - **BACKUP-3** Ferrite records the backup's CRC in its layout header.
> - **BACKUP-4** Store the calibration sector's CRC at install (in the layout header, and with the backup); at every boot a mismatch locks transmit and About and Status say why.
> - **BACKUP-5** The backup file is the user's own copy and is never published.
> - **BACKUP-6** As SAFE-5: calibration has a read-only copy (`CAL_READ`); there is no `CAL_WRITE`.
> - **BACKUP-9** The installers take the backup themselves.
>     - **BACKUP-9.1** The backup is taken by loading the reader image through the bootloader and reading all 4 MB to the PC, verified.
>     - **BACKUP-9.2** `flash.py` takes it itself, then flashes Ferrite.
>     - **BACKUP-9.3** The web flasher takes it itself, then flashes Ferrite.
>     - **BACKUP-9.4** While the reader runs for Console, the radio's screen says "Backing up your radio", keep the cable in, don't turn it off, with the read's progress, instead of hwtest's diagnostics pages (Console sends the reader's `reader` command first).
>     - **BACKUP-9.5** The reader image is read only by construction: it holds no SPI flash program, erase or status-register write, and no MCU flash write, so nothing it is sent can change the radio. It speaks the hwtest reader's protocol unchanged (`sys` with the MCU's unique ID, `flash`, `fdump`, `flashcrc`, `reader`), so every installer and tool reads either image.
>     - **BACKUP-9.6** The backup goes over the cable at one fixed rate, 230400, with the reader's `fdumpz`: 16 KB chunks, each sent as all-erased (0xFF), raw DEFLATE (fixed Huffman codes) or raw, whichever is smallest. Every frame keeps its CRC and the end frame the CRC-32 of the whole range as read, so integrity is unchanged. A short or bad frame is asked again at once. One rate for every setup: faster rates lost bytes on long transfers through a USB extension, and a backup that finishes beats one that is a few seconds quicker.
> - **BACKUP-10** As SAFE-4: the first-boot erase spares calibration and the update area and comes after the verified backup.

> **Spec: return to stock**
>
> - **BACKUP-7** `STOCK_RESTORE` runs over the cable only (LINK-8) and skips calibration (0x00F000) and the update area (0x300000 up).
>     - **BACKUP-7.1** It writes only Ferrite's own writable ranges (the SPI driver's guard, SAFE-9): Ferrite writes nowhere else, so everything outside them still holds stock's data. Calibration and the update area are refused on the radio and left out by the PC, whatever ranges the radio names.
>     - **BACKUP-7.2** Its `START` answer carries the calibration sector's CRC-32; the PC refuses a backup whose calibration differs (a damaged file) and writes nothing. It doesn't prove which radio the backup is from: two radios can have byte-identical calibration (BACKUP-7.4).
>     - **BACKUP-7.3** Each range is read back by CRC before the stock `.BTF` goes; after `FINISH` the radio resets into the bootloader without saving anything.
>     - **BACKUP-7.4** The PC tells which radio a backup is from by the MCU's unique ID (About's radio ID). The `START` answer ends with it, after the ranges, so an older PC still reads its part. The backup stays a raw flash image: its file name carries the ID (`rt950pro-backup-<ID>-<date>.bin`), and Console keeps each backup's SHA-256 with its ID in the browser. A backup from another radio is refused and nothing is written. When Console doesn't know the backup's ID (a renamed file, another browser), it is refused the same way until the owner types this radio's ID.
> - **BACKUP-8** After the restore, the web app flashes the stock `.BTF` through the bootloader.
> - **BACKUP-11** The SPI flash's block-protect bits are never set: the firmware's own guard refuses writes to calibration and the update area (SAFE-9), with tests, and protect bits left behind could confuse stock, nicFW or their tools after you leave Ferrite.
> - **BACKUP-12** Ferrite may use the MCU's top 64 KB (0x080F0000, decision 338), where stock firmware alone writes one word, `UV85` or `BJ90`, the model name on its info page. The backup records its first 16 bytes before the first Ferrite image that reaches them is flashed, and the way back to stock puts them back or leaves them erased.
>     - **BACKUP-12.1** The reader reads them with `mdump 0x080F0000 16` (hwtest's command: the MCU's main flash only, read only). Console keeps them with the backup: in the browser by the backup's SHA-256, and a stock word in the file name (`rt950pro-backup-<ID>-<date>-UV85.bin`). `fw/tools/backup.py` writes them to `marker.bin` beside `flash.bin`, where `flash.py` finds them. A reader that can't read them (an older one) leaves them unrecorded: they count as blank, and Console says so.
>     - **BACKUP-12.2** The stock image goes padded with 0xFF through 0x080F07FF, so the bootloader erases that 2 KB page (it erases only the pages it writes). When the recorded bytes hold a stock word, they go back at 0x080F0000; otherwise the page stays erased and stock shows its default model name. The longer file stays within the bootloader's limit (offsets below 0xFD000).

### Under the hood


### Status

Roadmap 1b (flash.py), then 3e (web app). Done when a backup restores to a working stock radio.


### Settled details

- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - BACKUP-11: decision 73, Oct 7, 2026; stock doesn't set them.
  - BACKUP-7.1 – BACKUP-7.3: decision 261, Oct 22, 2026 (Ferrite Console's Install page); BACKUP-7.2 narrowed and BACKUP-7.4, BACKUP-9.4 added by decision 263 (clear's backup was accepted on black: their calibration sectors are byte-identical). BACKUP-9.6: decision 265, Oct 23, 2026 (230400 fixed, `fdumpz`). BACKUP-9.5 and BACKUP-9.1's "the reader image" (was "the hwtest reader image"): decision 264, Oct 22, 2026 (the reader is Ferrite's `reader/`, in Rust; fw/apps/hwtest retires once an on-radio backup with it matches hwtest's). Stock's own way back is a full reflash from its `.BTF`, which never touches the SPI flash's data.

### Open points

None.

---

