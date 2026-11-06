## 35. Calibration and trims

### What it's for

Ferrite reads each radio's factory calibration for power, squelch and frequency, checks it before trusting it, and never writes it. Two user trims correct frequency and the battery reading.

### Using it

- **View:** MENU 0 9 9 2 shows calibration status, read only.
- **Crystal trim and battery reading trim:** not built; their rows left the menu Oct 23, 2026 until they are (decision 276). CAL-13, CAL-17, CAL-18 and PWR-14 stay as the spec for then.
- **Battery trim:** MENU 0 9 9 2. Match the reading to a meter.
- **Backup:** the installer saves the calibration sector with the full SPI backup (chapter 2).

### Screens

No mock-up yet.

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| 0 9 9 2 | Calibration | View only | — |

> **Spec: read-only**
>
> - **CAL-1** As SAFE-1: never erase or write 0x00F000–0x00FFFF.
> - **CAL-2** Erase only in 4 KB sectors, never block or chip erase.
> - **CAL-3** `CAL_READ` gives a read-only copy for backup.
> - **CAL-4** Never compile in or use stock's defaults (flat 200/150/100 PA; 136–174, 400–520, 220–260 MHz windows) or stock's power-on modes (super mode, all band test, the +0x49/+0x4A bytes).

> **Spec: validation**
>
> - **CAL-5** Check at every boot. Blank (0xF0E0 = 0xFF) or invalid: transmit locked on every band, receive still works, About says why.
> - **CAL-6** Valid means: programmed flag set; every PA byte plausible (not 0x00 or 0xFF); low < mid < high at every index; a factory crystal trim, when marked, within ±20 ppm (|k| ≤ 871; a bigger one also leaves receive untrimmed); tone gains fit their 7-bit fields; TX windows parse (CAL-11).
> - **CAL-7** The sector's CRC-32 is recorded in the layout header (bytes 6–9, outside the header's own CRC) on the first boot that checks it, which is the first boot after install (and with the backup); at every boot a mismatch, or no store to check against, locks transmit and the cable log says why (About and Status to follow). A format of the store records it again (decision 129).
> - **CAL-8** The level-to-row mapping is a type with a unit test: "low" reads the row whose default is 100.

> **Spec: use**
>
> - **CAL-9** PA drive comes only from the band's curve at the chosen level, clamped to the highest calibrated value.
> - **CAL-10** The PA lookup refuses any frequency outside its row's span, and any entry the factory left unprogrammed (0x00 or 0xFF), which stock would send to the DAC as it is (decision 222: both radios' 200–300 MHz rows end at 260 MHz, their UHF rows at 520 MHz).
> - **CAL-11** The TX windows (0xF230, 0xF240) are equipment limits, intersected with the region plan and hardware range (chapter 15). Four windows of five bytes (0xF230 + 0, 5, 10; 0xF240 + 0): an enable byte, then the low and high edges, each two BCD bytes of whole MHz (01 36 = 136 MHz); a frequency is inside when low ≤ f < high, as stock checks it. Enable 0x01 is on, 0x00 or 0xFF off (an erased 0xF240); 0xF230 byte 0 = 0xFF (blank), any other enable byte, or an enabled window that isn't BCD with low < high locks transmit. 18–64 MHz counts as a window on any valid sector, as stock's loader replaces the windows with 18–64 MHz in its HF work mode (TX-41, decision 224).
> - **CAL-12** Factory crystal trim applies only when 0xF210 byte 11 = 0xA0 on a programmed sector, to both chips, receive (every receive set-up and the scope's points) and transmit, as stock: the chip is tuned to f + (f / 100) × k / 435500 (f in 10 Hz, rounded toward zero; k = bytes 12–13, signed; one unit about 0.023 ppm). The user trim (0 9 9 3, not built yet) adds to k. Everything else (squelch tables, PA row, TX windows, region plan, the display) uses the frequency itself, since the trim only corrects the crystal (decision 222).
> - **CAL-13** The TX-7 read-back expects the frequency word after trims (the one written to REG_38/39); the band checks use the frequency itself (CAL-12).
> - **CAL-19** Retired (decision 222): a sector with the trim marker and k ≠ 0 locked transmit until CAL-12 was built; the trim is now applied (CAL-12), and only one over ±20 ppm locks (CAL-6).

> **Spec: power on every band**
>
> - **CAL-14** No per-band cap in code: every band's PA drive is the calibration curve at the chosen level, as stock's lookup (decision 224). 1.25 m and 243.0 MHz read the 200–300 MHz row, entry (MHz − 200)/5; HF the HF rows, entry (MHz − 15)/5, at most 11. Their entries the allowed ranges reach (200–260 MHz, 18–64 MHz) are checked as the other bands' (CAL-6).
> - **CAL-15** Retired (decision 224): no transmit on the 200–300 MHz path until a 0.25 W ceiling was measured.
> - **CAL-16** Retired (decision 224): the power setting showed "0.25 W", greyed, on 1.25 m.

> **Spec: user trims**
>
> - **CAL-17** Trims live at 0x003000 (layout 3, decision 333; two alternating copies), apart from calibration; "reset trims" clears only them.
> - **CAL-18** Limits: crystal trim within ±20 ppm; battery reading trim within ±0.30 V.

### Under the hood


### Status

No mock-up. Calibration backed up and its CRC recorded in 1b; validation and the transmit lock in 4a; power on 1.25 m and HF compared with stock in 4e. Done when every CAL rule passes in host tests against good, blank and corrupted dumps, and on the radio.


### Settled details

- the programmed test is stock's: 0xF0E0 byte 0 = 0xFF means blank (0x08011DC8); 0xF200 has its own test (byte 0 = 0x00 or 0xFF). CAL-7's CRC covers the rest.
- The TX windows and the trim lock are built (`txcal::TxCal::read`, decisions 120, 122): a fault names itself in the boot report's cable log ("tx calibration: locked, ..."). The black radio's windows are 136–174, 400–520, 200–260 and 330–400 MHz, all enabled; Ferrite never allows 330–400 (no region band or hardware range there), and has no trim marker (0xFF).
- REG_48 = 0xB00F | (0x2B << 4), as stock forces it; the stored bytes are ignored, as stock ignores them.
- What each value does in stock and in Ferrite, with the two radios' values: research/calibration-vs-stock.md (Oct 20, 2026).
- Not used, as stock doesn't use them at its defaults: 0xF210 byte 0 (stock's Mic Gain setting 2 only; VOX-15, decision 126), bytes 3–4 (REG_48, see above), byte 10 (stock reads it nowhere); the RSSI offsets for the S-meter (stock's S-meter reads raw REG_67).
- `calibration.md` (corrected) is right: below 18 MHz and at 64–130 MHz stock uses entry 0 of the High row; 180–200 MHz clamps to entry 15 of the chosen level. Ferrite doesn't copy either (CAL-10 refuses outside a row's span).
- No band is capped in code (decision 224): stock caps nothing beyond its TX windows, and the region plan and CAL-11 cover the rest. Both radios' sectors are the same factory template, byte for byte: the 200–300 MHz rows about flat (High 225, Mid 147–155, Low 125, to 260 MHz) and the HF rows flat (250, 150, 100), so power on 1.25 m and HF is whatever that generic drive gives, unmeasured.
- Power stays on stock's factory calibration curves (measured per radio), three levels (Low, Mid, High); nicFW's own table (five levels per 5 MHz from generic defaults) was considered and not taken (decided Oct 7, 2026).

### Open points

- PA-byte plausibility: `tx-gotchas.md` adds a per-band ceiling from the bench.

---

