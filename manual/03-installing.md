## 3. Installing Ferrite

### What it's for

Puts Ferrite on the radio through the stock bootloader, erasing stock's data after the backup (chapter 2).

### Using it

1. Radio off. Hold the bottom two side buttons and turn it on. The screen stays dark: the bootloader is waiting. (The flasher can also catch any power-on by sending probes.)
2. Install:
   - Ferrite Console: the Install page (`#install`): connect, back up and save the file, install. The backup finds the SSB patch on a stock radio by itself; if it can't, Ferrite installs without USB, LSB and CW, and Firmware › Add SSB adds them later from your stock `.BTF`;
   - command line: `python3 fw/tools/flash.py <port> ferrite.btf --ssb-from <stock .BTF>`.
3. The installer first loads the hwtest reader, saves and verifies the 4 MB backup (chapter 2), then flashes Ferrite. If the backup shows a pending stock update at 0x300000, it stops and explains instead.
4. Turn the radio off and on. On first boot Ferrite erases the SPI flash, except calibration and the update area, then starts setup (chapter 4).

Nothing is imported from stock: add channels on the radio (hold 9 on a VFO) or load them with the web app (CHIRP CSV, RepeaterBook).

Putting Ferrite back on after Back to stock, with a Console backup (`.ferrite`) of your channels and settings: finish setup on the radio first, since it asks for your region and only the radio can set that. Then open the backup on Console's Radio Settings and Channels & Zones pages and write each. The region, Extend TX, the PIN lock, the cable and KISS ports stay as the radio has them (LINK-21.4): set the PIN lock again on the radio if you had one.

Updates use the same path. The bootloader is never touched, so step 2 always works, whatever state the firmware is in.

### Screens

No mock-up yet.

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| 0 9 6 | SSB patch | Installed or not; source | — |

> **Spec: flashing**
>
> - **INST-1** Install and update only through the stock bootloader; Ferrite has no update code.
>     - **INST-1.1** A block whose reply never came is sent again. When the bootloader answers that resend E2 (block out of order), the first copy was written: Console counts the block as sent and goes on. E2 to a first send, or after a garbled-frame reply (E1), still stops the flash. Not yet seen on stock's bootloader: whether it checks the order is unchecked.
> - **INST-2** The image carries the model tag `RT-950      ` at 0x080033E0 (the stock updater reads it) and again at 0x080037E0 (the bootloader compares it at every power-on and shows "Firmware Error!" instead of starting the app without it; found on the radio Oct 11, 2026); `btf.py` refuses images without both.
> - **INST-3** The app lives at 0x08003000–0x080FFFFF, the bootloader's own limit; `btf.py` refuses images over 1,012 KB. Until decision 338 it stopped at 948 KB, below stock's marker sector at 0x080F0000; an image past that overwrites the marker, which the backup records first (BACKUP-12).
> - **INST-4** As SAFE-3: never write the MCU option bytes.

> **Spec: erasing**
>
> - **INST-5** Check the backup for a valid 0xA55A header at 0x300000. If one is there, refuse to install and explain: only a stock phone or Bluetooth update leaves one, and the bootloader would reflash the MCU from it. Never clear it (UPD-7).
> - **INST-6** As SAFE-4: on first boot (no Ferrite layout header on the chip and none of Ferrite's records: blank, or stock's data; decision 339), erase the regions this firmware uses (layout 3, decision 333: the header, settings, trims, presets, channels, zones, the APRS records, waypoints and the event log), never calibration, the SSB patch or the update area; stock's old codeplug, record and voice prompts are in the install's 4 MB backup and their space is layout 3's. A chip with another Ferrite layout's header, a migration mark, or Ferrite's records without a header is never formatted (UPD-16).
> - **INST-7** Only 4 KB sector erases; chip erase and 32/64 KB block erase don't exist in the API.
> - **INST-8** The overlap check applies to the erase unit, not the requested range.
> - **INST-9** Nothing is imported from stock.

> **Spec: SSB patch**
>
> - **INST-10** Never ship the patch: extract it on the user's machine from their own stock `.BTF`, or from their own radio (INST-10.1).
>     - **INST-10.1** On a radio still on its stock firmware, the install's backup looks for the patch in the MCU's own flash, where stock's image carries it: the reader's `mdump` of 0x08024000-0x0803BFFF (read only, about 20 s; stock V0.21-V0.30 keep it between 0x0802B8A0 and 0x08032323, and the reader itself ends far below), the same run of patch records the `.BTF` import finds. Console takes it only when its SHA-256 is the known stock patch's, keeps it in memory for Install, which bundles it as INST-11 says, and notes in the backup file only where it was and its SHA-256, never its bytes (BACKUP-14). The wizard asks for no file for SSB (decision 457): there is no SSB step. The Install step says, in one line, either that the patch was found on the radio (USB, LSB and CW will work), or that it wasn't (none found, one Ferrite doesn't know, the read failed, the radio not on stock) and Ferrite installs without it: USB, LSB and CW stay hidden, and Firmware › Add SSB adds them later from the stock `.BTF` (INST-10.2). A stock `.BTF` dropped elsewhere (Back to stock) never feeds Install. A radio whose menu icons aren't stock's (already on Ferrite, BACKUP-12.3) isn't searched. Nothing of the patch is logged but where it was, its size and its hash.
>     - **INST-10.2** A radio already on Ferrite gets the patch without a reinstall (decision 457): Console's Firmware page shows whether the radio holds it (`SSB_WRITE` `CHECK`, LINK-73) and offers Add SSB… for the owner's stock `.BTF` only. Console finds the patch in it on this computer (as INST-10), takes only the known stock patch, and sends it with `SSB_WRITE` (LINK-73) over the cable, or Bluetooth past the PIN (LINK-8); it then says it was added and checked, or that it didn't go in and why. The radio uses it at once: no restart. A backup keeps only the patch's hash (BACKUP-14), so it is never a source.
> - **INST-11** The flasher appends it at the first 1 KB boundary after the image (64-byte `FERRSSB1` header + patch); the combined image is never published.
> - **INST-12** At boot, check framing, size and SHA-256, then copy it to SPI 0x008000 (layout 3, decision 333). A known hash is "verified"; an unknown one is stored only after on-screen confirmation.
> - **INST-13** Later updates, with or without the patch, leave the stored patch alone.
> - **INST-14** Without a patch, USB, LSB and CW in HF mode are hidden; everything else works (HF-20).

### Under the hood


### Status

`btf.py` round-trips every stock `.BTF`; erase and backup in roadmap 1b; web flasher in 3e. Done when a fresh radio installs from the browser (milestone 3 gate).


### Open points

- The web app's name is open (hosted on GitHub Pages, decision 77; needed before milestone 3).

---

