## 3. Installing Ferrite

### What it's for

Puts Ferrite on the radio through the stock bootloader, erasing stock's data after the backup (chapter 2).

### Using it

1. Radio off. Hold the bottom two side buttons and turn it on. The screen stays dark: the bootloader is waiting. (The flasher can also catch any power-on by sending probes.)
2. Install, adding your stock `.BTF` for SSB:
   - Ferrite Console: the Install page (`#install`): connect, back up and save the file, drop in your stock `.BTF`, install;
   - command line: `python3 fw/tools/flash.py <port> ferrite.btf --ssb-from <stock .BTF>`.
3. The installer first loads the hwtest reader, saves and verifies the 4 MB backup (chapter 2), then flashes Ferrite. If the backup shows a pending stock update at 0x300000, it stops and explains instead.
4. Turn the radio off and on. On first boot Ferrite erases the SPI flash, except calibration and the update area, then starts setup (chapter 4).

Nothing is imported from stock: add channels on the radio (hold 9 on a VFO) or load them with the web app (CHIRP CSV, RepeaterBook).

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
> - **INST-10** Never ship the patch: extract it on the user's machine from their own stock `.BTF`.
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

