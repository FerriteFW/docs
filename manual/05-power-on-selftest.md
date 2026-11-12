## 5. Power on and the self-test

### What it's for

Shows the radio is Ferrite and whose it is, checks the hardware, and says what won't work if a check fails.

### Using it

Turn the volume knob on. The boot screen shows the logo, FERRITE, the version, your callsign; a step that takes a while is named under it. Then home (or setup, on first boot).

- **A check fails:** the bar and line turn red, naming it (e.g. "SPI flash: no answer"). Any key continues. Receive still works; About (MENU 0 9 8) and Status (MENU 0 0) say what's locked and why.
- **Owner card** (MENU 0 7 3 3): the boot screen shows "This radio belongs to…" instead; any key skips it.
- **Hold MENU** while powering on: settings reset (MENU confirms; a second confirm clears channels too).
- **PIN** set: the radio asks for it at power-on.
- **Bottom two side buttons** held: the stock bootloader (chapter 3), not Ferrite.

### Screens

| | | |
| --- | --- | --- |
| ![Boot, self-test running](img/screens/BootA.png) | ![Boot, a check failed](img/screens/BootAFail.png) | ![Boot, owner card](img/screens/BootC.png) |
| Self-test running | A check failed | Owner card |

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| 0 7 3 2 | Power-on message | Off, callsign, 16-character text | Callsign |
| 0 7 3 3 | Boot screen | Logo, owner card | Logo |
| 0 9 3 1 | PIN lock | Off, at power on, at power on and unlock | Off |
| 0 9 3 3 | Change PIN | 4–6 digits: the old PIN first, then the new one twice | — |
| 0 9 7 2 | Reset | Everything except calibration and the SSB patch (BOOT-14) | — |
| 0 9 8 | About, help, self-test | View; ◀▶ pages through Help (HELP-1) | — |

> **Spec: start-up**
>
> - **BOOT-1** As SAFE-7: safe state first, before RAM init.
> - **BOOT-2** As SAFE-8: the independent watchdog is on, from when the tasks start; a start after a fault or a hang says so (SAFE-8.2).
> - **BOOT-3** As SAFE-14: a PTT held at power-on is ignored until released.
> - **BOOT-4** None of stock's power-on modes (super mode, all band test) exist.
> - **BOOT-5** Leave the bootloader's key combo (bottom two side buttons) alone.

> **Spec: self-test**
>
> - **BOOT-6** Read DEBUG_IDCODE (expect 0x70050344, AT32F403AVGT7) and the SPI flash JEDEC ID; take the flash size from it.
> - **BOOT-7** Check calibration: programmed flag, PA bytes plausible (not 0x00/0xFF), low < mid < high, crystal trim within ±20 ppm, tone gains fit, TX windows parse, CRC matches install.
> - **BOOT-8** Transmit stays locked unless the MCU matches and calibration checks out; never fall back to stock's built-in defaults. Receive still works.
> - **BOOT-9** Boot screen: logo, wordmark, version, and the line Power-on message (0 7 3 2) picks: the callsign (the default), your 16-character text, or nothing (nothing also when the one picked is empty); no bar and no progress count (decision 215): the status line stays empty unless a check is still running after half a second ("Checking GPS…") or the SSB patch install runs past 300 ms ("Installing SSB patch"). With Boot screen set to owner card (MENU 0 7 3 3) and something on the card, the owner card instead: callsign, name, phone, e-mail, with the logo, version and self-test in its bottom line; shown at least 4 s, any key skips it. A failed check shows the logo screen (BOOT-10).
>     - **BOOT-9.1** The logo screen's foot says "Press # for help" (HOME-10), unless a failed check needs its "Any key: continue".
> - **BOOT-18** The logo screen opens with a short animation and sound, "Charge and flash" (decision 321), drawn by the radio from the logo's parts (no stored frames). The logo's masks are an SPI part (UPD-23): without it the screen shows the wordmark alone.
>     - **BOOT-18.1** The picture: the logo's 14 windings fill in dim one after another, 25 ms apart from 0.1 s; at 0.63 s the logo and the wordmark flash bright together with a glow that settles by 1.3 s. The last frame is the still boot screen. The version, the Power-on message line and the status line are on the screen from the first frame and never animated.
>     - **BOOT-18.2** The sound: one tone at a time from the speaker, as the key beeps: a rising note per winding (330 Hz up two octaves over the 14), the last gliding up a fifth into the flash and holding, then fading with the glow, with no fresh attack at the end. A fixed level (the volume knob sets how loud); the speaker comes on and goes off without a pop. Not over received audio, never while transmitting.
>     - **BOOT-18.3** Always the full length and always on (no setting). The self-test runs underneath and the logo still shows its 1.5 s, so the animation never makes a boot longer; a slow check still shows its name (BOOT-9) and a failed one shows as BOOT-10 says, then waits for a key.
>     - **BOOT-18.4** The owner card (MENU 0 7 3 3) isn't animated and has no sound.
> - **BOOT-10** A failed check turns bar and line red, names the check, and waits for any key.
> - **BOOT-11** About and Status say why transmit is locked, if it is.

> **Spec: after the self-test**
>
> - **BOOT-12** No layout header: write it and the defaults, then run setup.
> - **BOOT-13** PIN set: ask for it; three wrong entries wait 30 s.
> - **BOOT-14** One reset, reached two ways, that leaves a new radio.
>     - **BOOT-14.1** One reset, reached from 0 9 7 2: a screen listing what goes, OK, then hold # for 3 s.
>     - **BOOT-14.2** Holding MENU at power-on reaches the same reset, with the same steps.
>     - **BOOT-14.3** It clears everything Ferrite stored (settings, the PIN, channels, zones, presets, the home channel, messages, the event log, waypoints, trims).
>     - **BOOT-14.4** It never touches calibration or the SSB patch.
>     - **BOOT-14.5** It then runs first-run setup, as for a new radio: no region is set until setup picks one.
> - **BOOT-15** Otherwise, home.
> - **BOOT-17** Order at power-on: the self-test runs while held keys are read (MENU held through it: the reset, BOOT-14, which comes before the PIN), then the PIN (BOOT-13), then home; a first boot goes to setup. The reset comes before the PIN so a forgotten PIN can still be cleared by a full reset; the self-test comes before the PIN so faults show even on a locked radio.
> - **BOOT-16** The self-test has six checks: MCU, SPI flash, BK4829 VHF, BK4829 UHF, SI4732 and calibration. The SI4732 is checked by powering it up in FM (answering within 500 ms, its revision read), then powered down and held in reset again until FM broadcast or HF mode starts it (since Oct 12, 2026; before, it showed "not tested"); calibration passes when the factory sector at 0x00F000 isn't blank (read only; its CRC check comes with the installer, 1b).

### Under the hood


### Status

Mock-ups approved (0b); `ferrite-ui` boot screen drawn. Built in roadmap 1c; done when Ferrite boots on the radio, shows the logo and self-test, and every key shows in the key test.


### Settled details

- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - BOOT-14: decided Oct 7, 2026; replaces the two levels; decided Oct 7, 2026.
  - BOOT-17: decision 73, Oct 7, 2026; Stock also reads held keys first.
  - BOOT-18: decision 321, Oct 28, 2026 (Alex): animation 5 of `research/boot-animation/preview.html` with its "Lock" sound ending.
  - BOOT-16: decided Oct 6, 2026.

### Open points

None.

---

