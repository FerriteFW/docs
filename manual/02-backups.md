## 2. Before you start: backups and the way back to stock

### What it's for

Installing Ferrite erases stock's data in the SPI flash. The backup is your way back to a fully working stock radio.

### Using it

1. Keep your stock `.BTF` from Radtel: it's how you go back, and Firmware › Add SSB takes the SSB patch from it if the install didn't find it on the radio.
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
>     - **BACKUP-1.4** A backup of a chip Ferrite has already set up (Ferrite's layout header, at layout 3's or layout 2's place, or a migration mark, each with a good CRC) isn't a stock backup: Console refuses it for installing and for Back to stock, and says it is a backup of Ferrite, not of stock firmware.
>     - **BACKUP-1.5** The name also carries the local date and time it was taken (`rt950pro-backup-<ID>-<YYYYMMDD>-<HHMMSS>.fbin`), so a second backup the same day never takes the first one's name and can't replace it.
> - **BACKUP-2** No erase until the backup is saved and confirmed.
>     - **BACKUP-2.1** Ferrite goes only into the radio the backup was taken from. Just before installing, Console reads the radio's MCU ID again (the reader's `sys`) and refuses, writing nothing, when it isn't the backup's, when the radio doesn't answer as the reader, or when the backup has no ID. Another radio's ID, or disconnecting, forgets the backup: that radio needs its own.
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
>     - **BACKUP-9.6** The backup goes over the cable at the cable's own 115200, with no rate switch, with the reader's `fdumpz`: 16 KB chunks, each sent as all-erased (0xFF), raw DEFLATE (fixed Huffman codes) or raw, whichever is smallest. Every frame keeps its CRC and the end frame the CRC-32 of the whole range as read, so integrity is unchanged. A short or bad frame is asked again at once. One rate for every setup: faster rates lost bytes on long transfers through a USB extension, and a backup that finishes beats one that is a few seconds quicker. Since Nov 25, 2026 (Alex) not even 230400 with High speed on: switching back closed and reopened Web Serial's port while the reader sent its result line (console#87), and the sync windows around the switch were the other failures (console#88). About a minute slower over a whole chip (fdumpz's compression keeps it near 2½ min).
>     - **BACKUP-9.7** After a dump the reader goes back to 115200 and waits 500 ms before its result line (`fdump end` or `fdump stopped`), so a host that reopens its port to change speed (Web Serial does, slowly on Windows) still hears it. Console writes the line, or that none came, to its debug log, and a failed read's message carries the reader's reason.
>     - **BACKUP-9.8** Console sends its sync for 2.5 s from the reader's "ready" line, inside the reader's own 3 s, so none of it reaches a reader already back at 115200. Before trying again it waits for the reader's `> ` prompt (3 s at most), not a fixed time. It takes the reader's answers only as whole lines, and `?  (help)` as "this reader has no `fdumpz`" only right after its own command's echo.
>     - **BACKUP-9.9** A bad or short frame: Console waits until the cable has been quiet for 30 ms (the rest of the frame), drops what came, then sends the NAK. After the ACK of a frame it sent again, the reader waits 100 ms and drops what came: the host may have had two copies and ACKed both, and the second ACK would count for the next frame.
> - **BACKUP-10** As SAFE-4: the first-boot erase spares calibration and the update area and comes after the verified backup.

> **Spec: return to stock**
>
> - **BACKUP-7** `STOCK_RESTORE` runs over the cable only (LINK-8) and skips calibration (0x00F000) and the update area (0x300000 up).
>     - **BACKUP-7.1** It writes only Ferrite's own writable ranges (the SPI driver's guard, SAFE-9): Ferrite writes nowhere else, so everything outside them still holds stock's data. Calibration and the update area are refused on the radio and left out by the PC, whatever ranges the radio names.
>     - **BACKUP-7.2** Its `START` answer carries the calibration sector's CRC-32; the PC refuses a backup whose calibration differs (a damaged file) and writes nothing. It doesn't prove which radio the backup is from: two radios can have byte-identical calibration (BACKUP-7.4).
>     - **BACKUP-7.3** Each range is read back by CRC before the stock `.BTF` goes; after `FINISH` the radio resets into the bootloader without saving anything.
>     - **BACKUP-7.4** The PC tells which radio a backup is from by the MCU's unique ID (About's radio ID). The `START` answer ends with it, after the ranges, so an older PC still reads its part. The backup file carries the ID in its name (`rt950pro-backup-<ID>-<date>-<time>.fbin`) and in its manifest (BACKUP-14), and Console keeps each backup's SHA-256 with its ID in the browser. A backup from another radio is refused and nothing is written. When Console doesn't know the backup's ID (a renamed file, another browser), it is refused the same way until the owner types this radio's ID.
> - **BACKUP-8** After the restore, the web app flashes the stock `.BTF` through the bootloader.
>     - **BACKUP-8.1** The stock `.BTF` goes only in the bootloader's own window right after `FINISH`. Missed, the radio may start Ferrite again, which sets up its storage over the restored data: Console says to start Back to stock again and never reports it done. After a cut, "Send the stock firmware only" is offered only when every range was written and read back, `FINISH` was accepted and the bootloader had taken stock's first block (Ferrite can't start again); otherwise the only way on is Back to stock again, which writes and checks everything again.
> - **BACKUP-11** The SPI flash's block-protect bits are never set: the firmware's own guard refuses writes to calibration and the update area (SAFE-9), with tests, and protect bits left behind could confuse stock, nicFW or their tools after you leave Ferrite.
> - **BACKUP-12** Ferrite may use the MCU's top 64 KB (0x080F0000, decision 338), where stock firmware alone writes one word, `UV85` or `BJ90`, the model name on its info page. The backup records its first 16 bytes before the first Ferrite image that reaches them is flashed, and the way back to stock puts them back or leaves them erased.
>     - **BACKUP-12.1** The reader reads them with `mdump 0x080F0000 16` (hwtest's command: the MCU's main flash only, read only). Console keeps them with the backup: in the browser by the backup's SHA-256, a stock word in the file name (`rt950pro-backup-<ID>-<date>-<time>-UV85.fbin`), and the bytes in the backup file's manifest (BACKUP-14). `fw/tools/backup.py` writes them to `marker.bin` beside `flash.bin`, where `flash.py` finds them. A reader that can't read them (an older one) leaves them unrecorded: they count as blank, and Console says so.
>     - **BACKUP-12.2** The stock image goes padded with 0xFF through 0x080F07FF, so the bootloader erases that 2 KB page (it erases only the pages it writes). When the recorded bytes hold a stock word, they go back at 0x080F0000; otherwise the page stays erased and stock shows its default model name. The longer file stays within the bootloader's limit (offsets below 0xFD000).
>     - **BACKUP-12.3** Stock's main-menu tiles live in the MCU's own flash too: 24 images of 58 x 58 pixels (12, then the same 12 highlighted), 161,472 bytes from 0x08080000, past the end of every stock image. The factory writes them; stock firmware never does, and a stock `.BTF` doesn't carry them. Every Ferrite image reaches past 0x08080000 and writes over them. The backup reads them with the reader's `mdump` (read only, about 35 s) and keeps them when they are stock's tiles, not a Ferrite image's code left by an earlier install: in the backup file (BACKUP-14), in the browser by the backup's SHA-256, and as a file of their own on request (`rt950pro-menu-icons-<ID>.bin`). The way back puts them into the stock image's padding at 0x08080000, from the backup file, that record or an icons file (one radio's, for another radio whose tiles an earlier install wrote over); without them the area stays erased and stock draws its menu tiles blank.
> - **BACKUP-13** The way back to stock also works for a radio that isn't running Ferrite (stock, nicFW, or a Ferrite that won't start): Console loads the restorer image through the stock bootloader (the owner turns the radio off and on), and the restorer serves the same `STOCK_RESTORE` requests as Ferrite (BACKUP-7): the same checks and code, writes only inside Ferrite's writable ranges, plain frames only, the radio's ID in its `START` answer (BACKUP-7.4). `FINISH` restarts it into the bootloader for the stock file; a missed window starts the restorer again, never Ferrite.
>     - **BACKUP-13.1** The restorer is its own image (`restorer/`, about 25 KB), never part of the reader, which stays read only (BACKUP-9.5). It is built and signed by the release workflow with the reader and bundled with Console.
> - **BACKUP-14** The backup is one file, `.fbin`: a zip of `spi.bin` (the whole SPI flash as read, what a `.bin` backup held before Console 0.9.3), `icons.bin` (stock's menu tiles when they were stock's, BACKUP-12.3) and `manifest.json` (format `ferrite-backup` version 1, the radio's ID, when, the Console version, the chip, the marker's 16 bytes, each part's size and SHA-256, and, when the backup found the SSB patch in stock's image, where and its SHA-256, never its bytes, INST-10.1). Save reads back the whole file. The way back (Console, `flash.py --backup`) takes a `.fbin`, every part checked against its manifest, or an older `.bin`.

### Under the hood


### Status

Roadmap 1b (flash.py), then 3e (web app). Done when a backup restores to a working stock radio.


### Settled details

- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - BACKUP-11: decision 73, Oct 7, 2026; stock doesn't set them.
  - BACKUP-1.4, BACKUP-1.5, BACKUP-2.1, BACKUP-8.1: Nov 24, 2026, from the Nov 20 outside code review (console#81 – console#83): radios swapped on the cable after the backup got Ferrite with no backup; a cut Back to stock could be finished with stock over unchecked or reformatted ranges; a backup of a radio already on Ferrite passed as a stock backup, and a same-day backup took the stock one's name.
  - BACKUP-14: decision 407, Nov 16, 2026 (Alex: "put both of those files into one").
  - BACKUP-12.3: decision 406, Nov 16, 2026 (black back on stock showed its menu tiles blank; the reverse of V0.29 0x08018130 found them drawn from 0x08080000; nicFW's images, under 280 KB, leave them alone). BACKUP-13: decision 405, Nov 16, 2026 (a radio on stock had no way back to its own data; Alex: "provide a way to bootstrap back even if Ferrite is not running").
  - BACKUP-7.1 – BACKUP-7.3: decision 261, Oct 22, 2026 (Ferrite Console's Install page); BACKUP-7.2 narrowed and BACKUP-7.4, BACKUP-9.4 added by decision 263 (clear's backup was accepted on black: their calibration sectors are byte-identical). BACKUP-9.6: decision 265, Oct 23, 2026 (230400 fixed, `fdumpz`). BACKUP-9.7 – BACKUP-9.9: Nov 24, 2026 (the Nov 17 serial code review's findings, Console issues #87, #88 and #90). BACKUP-9.5 and BACKUP-9.1's "the reader image" (was "the hwtest reader image"): decision 264, Oct 22, 2026 (the reader is Ferrite's `reader/`, in Rust; fw/apps/hwtest retires once an on-radio backup with it matches hwtest's). Stock's own way back is a full reflash from its `.BTF`, which never touches the SPI flash's data.

### Open points

None.

---

