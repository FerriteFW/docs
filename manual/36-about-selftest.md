## 36. About and the self-test

### What it's for

Says what the radio is, what's installed, whether each part checked out, and why transmit is locked, if it is. Its Help pages put the manual's address (as a QR code) and the key card on the radio.

### Using it

- **About:** MENU 0 9 9.
- **System:** ▶ from About: the live numbers (CPU, RAM, stack, MCU temperature, battery, uptime).
- **Help:** ▶ from System: Manual (a QR code to this manual), Keys (home), Side+PTT, Holds (the hold digits, hold \* and hold #) and Menu nos (the numbers most often wanted), then the self-test; ◀ goes back.
- **Self-test:** runs at every power on, quietly behind the boot screen (chapter 5): a slow check is named, a failed one shows in red and waits for a key.
- **Key test:** MENU 0 9 1 2.
- **Updating:** About says how to enter the stock bootloader (chapter 30).

### Screens

| | | |
| --- | --- | --- |
| ![Boot, self-test running](img/screens/BootA.png) | ![Boot, a check failed](img/screens/BootAFail.png) | |
| Self-test | A check failed | |

> **Spec: self-test**
>
> - **SELF-1** At every boot, read the MCU's DEBUG_IDCODE (expect 0x70050344, AT32F403AVGT7) and the SPI flash JEDEC ID; the flash size comes from the JEDEC ID.
> - **SELF-2** Transmit stays locked unless the MCU is the expected part and the calibration checks out.
> - **SELF-3** The self-test shows nothing while it is quick: no bar, no count (decision 215). A check still running after half a second is named on the status line ("Checking GPS…"); a failed check shows in red, names the check and waits for a key.
> - **SELF-4** A failed check never stops receive; it says what won't work.

> **Spec: About**
>
> - **SELF-5** Shows version and build; MCU and SPI flash identity and the MCU's unique ID (SELF-8); calibration status; why transmit is locked, if it is; hardware checks; the SI4732's firmware, chip and component revisions, read at the boot check ("Not read" when it didn't answer); SSB patch state; how to enter the bootloader. The live numbers are System's (SELF-9).
> - **SELF-6** Without an SSB patch, About says "not installed" and the menu path that installs it.
> - **SELF-7** There is no firmware-update screen; About explains the stock bootloader route.
> - **SELF-8** About shows the MCU's 96-bit factory unique ID (0x1FFFF7E8, which stock reads too) as 20 Crockford base32 digits (no I, L, O or U; the 12 stored bytes read as a bit stream, nothing lost) in groups of five on two rows, "R28JM FRR1S" / "27V4T WPTH0"; "Not read" while it is all zero.
> - **SELF-9** System, the page after About, holds the numbers that change: CPU, RAM, Stack free (SBAR-23), MCU temp (SBAR-20), battery voltage and uptime, "Measuring" until the first reading, and a note saying what CPU and RAM mean.
>     - **SELF-9.1** CPU is the share of the last 10 s the MCU was awake: 100 % less the time the thread-mode executor slept (WFE), so the Radio, DSP and input executors and the interrupt handlers count as busy; measured every 10 s, also in the cable log.
>     - **SELF-9.2** RAM is what was ever used of the 96 KB: all of it less the stack's room never used (the statics are fixed at build time, the rest is the stack's peak), in whole KB ("45 of 96 KB").
>     - **SELF-9.3** Over the same 10 s, the CPU at each speed (dynamic clocking, PWR-26): the share awake while at 24 MHz and while at the build's speed, each left out when the window spent under 0.1 s there, and the share of the window at 24 MHz. On the readback's bar line beside `mcu=`: `cpu=` (SELF-9.1), `cpu24=`, `cpu120=`, `at24=`. A speed switch happens while awake, so its moment counts toward the speed switched from. Alex, Nov 3, 2026: "add the cpu counter" (to size the decoders' headroom at 24 MHz).
> - **SELF-10** About's note names the copyright holder and the licence (Copyright 2026 Alex Harvey; PolyForm Noncommercial 1.0.0, free for any noncommercial use), with the update hint.

> **Spec: Help**
>
> - **HELP-1** ◀▶ on About go round its pages: About, System (SELF-9), Manual, Keys, Side+PTT, Holds, Menu nos, Self-test; ▶ on, ◀ back. The hint bar names the page ▶ goes to; BACK leaves. Every page's status bar name fits 8 characters (SBAR-5).
> - **HELP-2** Manual shows a QR code of the online manual's address in the theme's own colours, text colour on the background with a 4-module quiet zone (inverted on the dark and night red themes, which phone cameras read; plain dark on light in daylight), and the address as text under it. The address is one constant in `tools/mkqr.py`, which makes the code at build time; nothing is encoded on the radio. The own domain is still to be chosen (decision 98).
> - **HELP-3** Keys and Side+PTT are the key card (Appendix B) as key | action rows, every row one line at 240 px: shortened, never wrapped.
> - **HELP-4** Holds lists the key holds first, hold ABC (edit the slot, EDIT-1), hold V/M (zones, KEY-26), hold MENU (more settings, MENU-2), hold BACK (home, KEY-5), hold \* (the quick menu, HOME-17) and hold # (the key lock, KEY-13), then the ten hold-digit shortcuts from the same table as the shortcut list (MENU 0 9 1 3, KEY-21), which runs them; one line each at 240 px, in 16 px rows so the 16 fit (decision 376).
> - **HELP-5** Menu nos lists the menu numbers most often wanted (MENU, then the number): Status, channels, zones, FM broadcast, band scope, the counter, HF mode, tone search, the event log, APRS heard, messages, home layout, Bluetooth and setup.

### Under the hood


### Status

Boot mock-ups approved (0b); About has none. Boot screen with self-test in 1c; self-test finished in 7. Done when every SELF rule passes on the radio, including a forced calibration failure.


### Settled details

- The key test is at 0 9 1 3 (Keys and lock); About shows the self-test only (decision 76, Oct 7, 2026). It moved up to 0 9 1 2 when Lock covers went (decision 304).
- Help lives inside About rather than as its own menu item: every MENU 0 9 number is taken (decision 98, Oct 8, 2026).
- HELP-1, HELP-4: changed Oct 15, 2026 (user, decision 187): the "Hold 0-9" page is "Holds" and lists hold \* and hold # too.
- The manual QR code (HELP-2) points at `https://ferritefw.dev/manual` (the domain chosen Oct 16, 2026), a fixed address on the main site that forwards to the user guide at `manual.ferritefw.dev` (Oct 29, 2026): the code in every radio stays valid wherever the guide moves. The guide links Console, and Console's sidebar and About link the guide.

### Open points

None.

---

