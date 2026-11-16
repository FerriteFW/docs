## 8. The status bar and the Status page

### What it's for

The status bar shows only what changes what a key does now, or needs attention. The Status page lists every active state in words.

### Using it

| Place | Item | Shown when |
| --- | --- | --- |
| Middle | Clock: `14:32`; `Z` added in UTC; `--:--` with no time source | Always |
| Left | Screen name (`Quick`, `Squelch`, `EDIT A`, `Scope`…) | Any screen but home |
| Left | Padlock | Keys locked (red when PTT is locked too, KEY-14.3) |
| Left | `SCN` | Scanning |
| Left | `TW` or `DW` | Watch on: three slots (TW) or two (DW) |
| Left | Envelope with a count; red for an alert | Unread messages, decodes or alerts |
| Left | Bell with a slash (alerts paused) | In HF mode with SAME on |
| Right | Satellite: outline searching, solid with a fix | GPS on |
| Right | Bluetooth | A device is connected |
| Right | Battery: amber below the warning, red and blinking at the transmit cut-off | Always |

**Status page:** # on home, or MENU 0 0. One row per state: transmit (ready, or why locked), region, Extend TX, inbox, scan (and its position), watch (and why it's off, if the relay cancelled it), jobs, beacon, Battery Save, broadcast, GPS, clock source (GPS or manual), Bluetooth (and the peer), the speaker mic (SND-12), battery (percentage, warning and cut-off levels; the volts are on About), the MCU's temperature, key lock, weather alerts ("Paused: HF mode" while in HF mode). OK on a row opens its setting.

### Screens

| | |
| --- | --- |
| ![Status bar states](img/screens/StatusBar.png) | ![Status page](img/screens/StatusPage.png) |
| Status bar states | Status page |

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| 0 6 6 | Clock | 24 h, 12 h; from GPS on/off; set manually | 24 h, from GPS |

> **Spec: status bar**
>
> - **SBAR-1** 20 px tall; device-wide state only. Per-slot state (power, tones, shift, mode) stays on the slot.
> - **SBAR-2** Clock centred: `14:32`, `Z` suffix in UTC. With no time source the callsign takes the clock's place (its first 6 characters, the slot's room); nothing shows there when no callsign is set.
> - **SBAR-3** Left, in order: screen name, padlock, `SCN`, `TW`/`DW`, inbox, alerts paused. Right: the satellite alarm's mark (SAT-20), `DRY` (SBAR-22), GPS, Bluetooth, battery at the right edge.
> - **SBAR-4** Nothing else is ever in the bar. Each item appears only when it applies and keeps a fixed position.
> - **SBAR-5** Screen name: the screen's own name, not its path, 8 characters or fewer; absent on home; cut short if the icons need the space (about 90 px on the left).
> - **SBAR-6** Inbox: one envelope with one count of unread messages, decodes and alerts; red while an alert (SAME, DSC distress) waits.
> - **SBAR-7** GPS shows only with GPS on: outline searching, solid with a fix.
> - **SBAR-8** Bluetooth's icon: grey while Bluetooth is on (0 9 2 1) with nothing connected, blue while a device is connected, none while off. Night red has only red, so there connected is the rune cut out of a filled badge and on the rune alone. The readback's `bar` says `bt_on` and `bt` (connected).
> - **SBAR-9** Battery always; its fill steps at the calibrated gauge's thresholds as stock's bars (full above the sixth, one step less below each of the sixth, fifth and fourth; PWR-22); amber below the warning level; red and blinking at the transmit cut-off.
>     - **SBAR-9.1** The fill's colour tells the level: green above 80 %, yellow (the theme's amber) down to 31 %, red at 30 % and below (the outline red with it), and red at the low warning or the cut-off whatever the percentage says. The LED heartbeat uses the same three (DISP-21). Decision 239.
> - **SBAR-10** Never in the bar: which PTT keys which slot, transmit and its timeout, Extend TX, Battery Save, beacon, jobs, broadcast, battery %.
> - **SBAR-22** Dry TX on (TX-48): `DRY` in amber, bold, left of the GPS and Bluetooth marks (inside the right half, 142 to 179 px), from the moment it is turned on until it is turned off or the radio powers off; in every theme by its token (night red's red, cyberpunk's magenta). The readback's `bar` line says `dry=1`.
> - **SBAR-24** Low Power Mode on (PWR-24): `LOW` in the battery's fill colour (a saving, not a warning), bold, left of where the GPS and Bluetooth marks would be (both are off in the mode) and of `DRY`, inside the right half; the readback's `bar` line says `lpm=1`. In the mode home draws its own bands (PWR-24.7), so the mark shows on the other screens.
> - **SBAR-11** Every state that changes what a key does (lock, scan) is in the bar.
> - **SBAR-12** Colour by exception (amber attention, red critical), and every colour also has a shape.
> - **SBAR-16** Watch shows as `TW` when three slots are watched and `DW` when two; nothing when watch is off, or cancelled because the watched slots need different relay states (WATCH-11). It shows only on home, the Status page and Watch and scan settings (MENU 0 1); other screens keep the room for their name.

> **Spec: Status page**
>
> - **SBAR-13** MENU 0 0 opens the Status page; so does # on home (HOME-10).
> - **SBAR-14** It lists every active state in words, including why transmit is locked, if it is.
> - **SBAR-15** OK on a row opens that row's setting.
> - **SBAR-18** Alerts paused: a small bell with a slash, left of the clock after the inbox, shown while in HF mode with SAME on (HF-6); the Status page's Weather alerts row says "Paused: HF mode".
> - **SBAR-20** The System page's MCU temp row (SELF-9; on Status until Oct 19, 2026) shows the AT32F403A's die temperature in whole degrees, °C or °F by 0 6 4's units, "Not read yet" until the first reading. The Radio task reads the internal sensor (ADC channel 16, scaled by the internal reference, with the datasheet's typical V25 1.28 V and Avg_Slope −4.26 mV/°C: the voltage rises with temperature) every 10 s and smooths it; it is shown as read, with no calibration (decision 112), and is informational only: it sets nothing. With the cable log on, every 10 s a line gives the sensor's and the reference's raw ADC counts and the computed temperature.
> - **SBAR-23** The System page's Stack free row (SELF-9) shows the main stack's room never used since power-on (its high-water mark, from the painted stack: `hal::sys::stack_free`), measured every 10 s and in the cable log ("stack free N B"), so the RAM budget is a measurement, not a guess.
> - **SBAR-21** Retired (decision 112): MCU temp offset (0 9 9 3) was a one-point calibration in whole degrees, ±40, added to the reading, with "(uncalibrated)" on the Status and About rows until it was set. The die temperature can't be measured on the assembled radio, so the reading is shown as read (SBAR-20); the cable log line moved to SBAR-20.
> - **SBAR-19** The battery shows as an icon only, with no setting for it; the percentage is on the Status page and the volts on About ("Battery as" removed, S-meter moved up to 0 7 3 1).
> - **SBAR-17** While the relay cancels watch (WATCH-11), the Watch row says so: "Off: HF needs the relay".

### Under the hood


### Status

- MCU temperature row built Oct 8, 2026 (SBAR-20); the sensor reads the die, not the PA, and its typical values leave a few degrees of spread (about ±1.5 °C typical): bench-check it against a thermometer at room temperature.


### Settled details

- The Status page also has rows for broadcast state, scan position, clock source (GPS or manual), the Bluetooth peer, and the battery warning and cut-off levels (decided Oct 6, 2026).
- A latched monitor (SIDE1 tap) shows as a MON tag on the slot's card, where RX/idle shows, not in the bar (decided Oct 6, 2026).
- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - SBAR-16: decided Oct 3, 2026; changed Oct 3, 2026.
  - SBAR-18: decided Oct 3, 2026.
  - SBAR-8: changed Oct 19, 2026 (Alex, daily use; decision 194): it showed only while connected, so you couldn't tell Bluetooth was on.
  - SBAR-23: Oct 19, 2026 (decision 194): the RAM review found the stack's room unmeasured (`stack_free` existed, unused). Moved from Status to System the same day (decision 195), with SBAR-20's row.
  - SBAR-20: decided Oct 8, 2026, decision 91; changed Oct 13, 2026: the slope is the AT32's −4.26 mV/°C (Table 55), not STM32F1's +4.1 as hwtest has it. The old sign read about 12 °C in a warm room, falling as the radio warmed (black radio, Oct 12, 2026). Changed Oct 13, 2026 (decision 112): no calibration; the cable log line (from SBAR-21) stays here.
  - SBAR-21: decided Oct 12, 2026 (user), built Oct 13, 2026. The datasheet allows the sensor's offset to differ by up to 50 °C between chips, so only a calibrated reading means anything absolute. Retired Oct 13, 2026 (user, decision 112): there is no way to measure the die on the assembled radio, and the corrected reading looks right.
  - SBAR-19: decided Oct 6, 2026.
  - SBAR-22, SBAR-3: decided Oct 16, 2026 (Alex), built Oct 16, 2026, decision 190: a switch that removes RF from every key-up must never be on unseen. Neither stock nor nicFW has one.
  - SBAR-2: changed Oct 15, 2026 (user, decision 183): with no time the callsign in the clock's place (it showed `--:--`).
  - SBAR-9: changed Oct 15, 2026 (decision 184): the icon's fill steps at the calibrated thresholds as stock's bars; amber and red now follow the calibrated gauge (the firmware never set them before).

### Open points

None.

---

