## 15. Transmitting: where, how much power, and the checks

### What it's for

Transmit works out of the box on the amateur bands of your region, at the power you pick. The firmware checks every transmission and refuses, saying why, when one would be out of band or unsafe for the radio.

### Using it

Press the slot's PTT (A, B or C) and talk; release to stop. The side connector's PTT transmits on the active slot. Hold 2 on home cycles power; MENU 2 sets it.

**Where you can transmit** = your region's amateur bands ∩ the calibration's TX windows ∩ what the hardware can do. Region is set in setup (page 3) or MENU 0 9 4 (MHz):

| Region | 2 m | 1.25 m | 70 cm | 6 m |
| --- | --- | --- | --- | --- |
| United States | 144–148 | 222–225 | 420–450 | 50–54 |
| Canada | 144–148 | 219–225 | 430–450 | 50–54 |
| United Kingdom | 144–146 | — | 430–440 | 50–52 |
| Europe (IARU Region 1) | 144–146 | — | 430–440 | 50–52 |
| Australia | 144–148 | — | 420–450 | 50–54 |
| New Zealand | 144–148 | — | 430–440 | 50–54 |
| Japan | 144–146 | — | 430–440 | 50–54 |
| Other (ITU common) | 144–146 | — | 430–440 | 50–52 |

Every region also has 17 m (18.068–18.168), 15 m (21.0–21.45), 12 m (24.89–24.99) and 10 m (28.0–29.7). Where your licence allows less, staying inside it is your call. **Extend TX** (MENU 0 8 8 4, off) widens this to everything the calibration and hardware allow, as stock: all of 18–64 MHz, and 136–174, 200–260 and 400–520 MHz within the calibration's windows, after a one-time warning: outside the amateur bands may be illegal where you are, and you are responsible. Every band uses the calibration's power curves at the level you pick, as stock does; on 1.25 m and HF that power isn't measured yet. Nothing is blocked outright, but on the emergency frequencies (406.0–406.1, 243.0 and 121.5 MHz) the first PTT only shows "Emergency frequency. PTT again to transmit" for 5 s; a second PTT within 5 s transmits.

The Transmit screen names the power level (LOW, MID, HIGH); its meter shows the mic level; no power or drive figure, never watts.

When transmit is refused, the screen names the reason and the menu path that fixes it: OK goes there (for a missing callsign, just the callsign page), BACK closes. Leaving the fix returns to where you were.

### Screens

| | | |
| --- | --- | --- |
| ![Transmitting](img/screens/Transmit.png) | ![Transmitting, daylight](img/screens/TransmitDay.png) | ![Transmit refused](img/screens/TxRefused.png) |
| Transmitting | Transmitting, daylight | Refused, with the fix |
| ![Transmitting, night red](img/screens/TransmitNight.png) | ![Setup, region and Extend TX](img/screens/SetupRegion.png) | |
| Transmitting, night red | Setup page 3: region, Extend TX | |

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| MENU 2 | TX power | Low, mid, high | Low |
| 0 8 1 | TX timeout | 30–600 s in 30 s steps (always on) | 120 s |
| 0 8 7 | Busy lockout default | Off, on | Off |
| 0 8 8 4 | Extend TX (0 8 8 alone in the terminal) | Off, on (warned once) | Off |
| 0 8 8 5 | Dry TX | Off, on: off at every power-on, never stored; on the radio's keys only | Off |
| 0 9 4 | Region | US, Canada, UK, Europe, Australia, New Zealand, Japan, Other | None until chosen in setup |
| Channel | RX only | On, off | Off |
| Channel | Busy lockout | Off, on | Off |

> **Spec: where you can transmit**
>
> - **TX-1** Transmit is allowed only where the region's band plan, the calibration's TX windows and the hardware range all allow it.
>     - **TX-1.1** Allowed = region band plan (table in code) ∩ calibration TX windows ∩ hardware range: outside the region's band plan, transmit is refused.
>     - **TX-1.2** Outside the calibration's TX windows (CAL-11), transmit is refused.
>     - **TX-1.3** Outside the hardware range, transmit is refused.
> - **TX-2** Extend TX: off by default; turning it on (setup or 0 8 8 4) shows its warning once; then allowed = calibration windows ∩ hardware range, and all of 18–64 MHz as stock (TX-41). Its state shows on Status, never in the status bar.
> - **TX-3** Emergency frequencies: nothing is always blocked, but they need PTT twice.
>     - **TX-3.1** Nothing is always blocked: on the emergency frequencies 406.0–406.1, 243.0 and 121.5 MHz (each ±25 kHz) the first PTT doesn't key and shows "Emergency frequency. PTT again to transmit" for 5 s.
>     - **TX-3.2** A second PTT within 5 s transmits.
>     - **TX-3.3** They lie outside the amateur bands, so in practice only Extend TX reaches them; 243.0 MHz is on the 200–300 MHz PA path, at the slot's level like the rest of it (TX-10).
> - **TX-4** HF (18–64 MHz), as stock: the region's amateur bands there transmit: 17 m (18.068–18.168), 15 m (21.0–21.45), 12 m (24.89–24.99) and 10 m (28.0–29.7 MHz) everywhere, and 6 m at 50–54 MHz in the US, Canada, Australia, New Zealand and Japan, 50–52 MHz in the UK, Europe and Other (the national allocations; IARU Region 1's common 50–52 where countries differ). With Extend TX all of 18–64 MHz transmits, CB included (TX-41). HF always uses the HF path (chip 1, PE14) with the relay energised, the PA drive from the calibration's HF rows at the chosen level (0xF190, entry (MHz − 15)/5, at most 11), as stock. HF transmit (FM on chip 1; AM is receive only: the BK4829 has no AM modulator) works from a home slot on 18–64 MHz and from HF mode, with every rule here: region, Extend TX, calibration.
> - **TX-5** Refuse any frequency the BK4829 can't tune.
> - **TX-6** Check the final TX frequency, after offset or split, reverse, talkaround and trims: the carrier frequency itself against the band edges, with no half-bandwidth margin (as stock, decision 97).
> - **TX-7** The TX chip's registers are read back before the PA is driven.
>     - **TX-7.1** Before driving the PA, read back REG_38/39, REG_30, REG_36 and REG_3B from the TX chip.
>     - **TX-7.2** Refuse on any mismatch.

> **Spec: power**
>
> - **TX-8** Low, mid, high; default Low. PA drive comes only from the calibration curve for that band and level, clamped to the highest calibrated value.
> - **TX-9** 1.25 m (the 200–300 MHz PA path, 243.0 MHz included) always transmits at Low, whatever level is set (decision 260): the PA drive from the calibration's Low 200–300 MHz row, entry (MHz − 200)/5 (CAL-14). Mid and High draw more current there for no more RF out and only stress the finals. The setting keeps its level for other bands; the Transmit screen and the readback say LOW on 1.25 m. Output at Low not measured yet (TX-10.6).
> - **TX-10** The 200–300 MHz PA path is open as soon as the calibration is valid: no bench lock (decision 224).
>     - **TX-10.1** Retired (decision 224): until a 0.25 W ceiling was measured, a key-up in the 1.25 m band (219–225 MHz) was refused.
>     - **TX-10.2** Retired (decision 224): until then 243.0 MHz was refused too, the emergency double PTT included.
>     - **TX-10.3** Retired (decision 224): once measured, the path was to keep a 0.25 W cap.
>     - **TX-10.4** A key-up in the region's 1.25 m band (the US 222–225, Canada 219–225 MHz) transmits at the slot's level.
>     - **TX-10.5** 243.0 MHz (Extend TX) transmits after the emergency double PTT (TX-3), at the slot's level.
>     - **TX-10.6** The output on 1.25 m at each level is compared with stock's on the same radio, into a dummy load.
> - **TX-11** The PA lookup refuses any frequency outside its row's span; it never falls through or reads past a 16-byte row.
> - **TX-12** Power is a level name, never watts.
>     - **TX-12.1** Power shows as its level name only (LOW / MID / HIGH), 1.25 m too.
>     - **TX-12.2** The Transmit screen shows no power or drive figure, never watts.
>     - **TX-12.3** Its meter is the mic level, amber near full deviation (drive only ever read ~100%).

> **Spec: calibration and identity**
>
> - **TX-13** Calibration is checked, never replaced: stock's built-in TX limits and PA curves are never compiled in. A blank or invalid sector locks transmit on every band; receive still works.
> - **TX-14** Valid means: programmed flag (0xF0E0) not 0xFF; every PA byte plausible (not 0x00 or 0xFF); low < mid < high; a marked factory crystal trim within ±20 ppm (applied, CAL-12); tone gains fit 7 bits; TX windows not blank, each enable byte 0x00, 0x01 or 0xFF, each enabled window valid BCD with lo < hi (CAL-11); CRC unchanged since install.
> - **TX-15** Transmit is also locked unless the MCU reads as AT32F403AVGT7. About and Status name the failed check.
> - **TX-16** As SAFE-9: none of stock's power-on modes exist.

> **Spec: pressing PTT**
>
> - **TX-17** Every transmission (PTT, VOX, DTMF, APRS, KISS, remote KEY) runs one sequence in the Radio task, with the same checks.
> - **TX-18** PTT A transmits on the active slot and PTT B on slot B from any screen, returning to home first (exceptions: KEY-7); side-connector PTT uses the active slot. PTT works with the keys locked unless they were locked in "All" (hold #, then \*: KEY-13, KEY-14.3).
> - **TX-19** As SAFE-14: a PTT held at power-on is ignored until released.
> - **TX-20** Refusals beep and show the TX refused screen (reason + fixing menu path).
>     - **TX-20.1** Refuse with the TX refused screen (reason + fixing menu path) when: outside the allowed range; RX-only channel; another transmission in progress; no callsign (automatic transmit); TX needs the other band relay state from RX (TX-37); the slot is in AM ("AM is receive only": the BK4829 has no AM modulator).
>     - **TX-20.2** Refuse the same way on busy lockout.
>     - **TX-20.3** Refuse the same way with the battery below cut-off.
>     - **TX-20.4** Refuse the same way when the calibration or hardware check failed.
>     - **TX-20.5** Each refusal beeps.
>     - **TX-20.6** A slot in WFM (broadcast FM on the SI4732, BCR-33) refuses as AM does, saying why: "WFM is broadcast FM, receive only. For 25 kHz two-way FM pick FM, for 12.5 kHz NFM.", with MENU 3 Mode as the fix (the toast: "WFM is broadcast: RX only"). It said "Receive only here", HF mode's words. Decision 417.
> - **TX-21** Busy lockout is on or off, as nicFW: on refuses PTT while the channel's squelch is open (a carrier); there is no wrong-tone mode (the record keeps its one bit).
>     - **TX-21.1** Busy lockout default (0 8 7) is the three VFOs' busy lockout, set on all of them as it changes, and a new channel's from Add repeater or HF mode; a channel saved from a VFO takes the VFO's. Channels keep their own.
> - **TX-22** While keyed: the red LED and the Transmit screen.
>     - **TX-22.1** While keyed: red LED.
>     - **TX-22.2** While keyed, the Transmit screen (slot, frequency, power level name, mic level, tone sent, timeout, battery under load).
>     - **TX-22.3** MENU does nothing while keyed.
> - **TX-34** Watched slots pause while any slot transmits and resume at unkey (WATCH-16).
> - **TX-37** RX and TX must need the band relay (PC4: chip 1's HF path below 64 MHz) in the same state; the relay never switches at key-up. A split or shift that crosses it is refused when set, on the radio (slot editor, MENU 5, channel editor), in the terminal's channel editor, `ch` and `load` ("Split TX needs the HF relay: not allowed with this RX frequency"); a VFO retuned under a split into a crossing pair is refused at PTT, with the TX refused screen and MENU 5 Offset as the fix. Cross-band pairs on the same side, such as RX 446.000 / TX 146.520, are allowed. The TX chip isn't flagged; PTT explains.
> - **TX-35** Automatic transmissions never key on an emergency frequency (TX-3); only a person's PTT pressed twice does.
>     - **TX-35.1** A remote `KEY` on an emergency frequency is refused: no carrier.
>     - **TX-35.2** An APRS beacon is refused on an emergency frequency.
>     - **TX-35.3** A KISS frame is refused on an emergency frequency.
>     - **TX-35.4** VOX is refused on an emergency frequency, and never opens the emergency prompt nor answers it.
>     - **TX-35.5** Each of these refusals shows a toast saying why ("No VOX: emergency frequency" for VOX).
>     - **TX-35.6** Only a person pressing PTT twice can transmit there.
>     - **TX-35.7** The APRS frequency on A or B while C is the APRS slot asks for PTT twice the same way, and refuses VOX and remote key-ups (APRS-21.3).
> - **TX-36** HF transmit (18–64 MHz) always starts on Low: each time you tune onto an HF frequency, the power is Low until you raise it, because nothing on the radio measures the antenna match.

> **Spec: key-up and unkey**
>
> - **TX-23** The key-up runs in a fixed order.
>     - **TX-23.1** Key-up: PA drive 0 → all path pins clear → relay and its settle time → TX path → BK4829 TX → read-back (TX-7) → PA ramp.
>     - **TX-23.2** The PA ramps to the calibrated level.
> - **TX-24** The SI4732 input (PA7/PC5) is switched away and the SI4732 muted before key-up; PTT in FM broadcast exits it first, with a broadcast slot it stops the broadcast first and starts it again after (BCR-29), and in HF mode transmits from HF mode (HF-23).
> - **TX-25** Unkey only when every PTT input is released (PE3, PE2 and PE6).
> - **TX-26** Unkey: tail tone, roger and CW ID while still keyed → PA drive 0 → wait ≥ 100 ms → paths back to RX.
> - **TX-27** Break before make: all path pins clear before one is set; RX and TX paths never on together (crossband's XB-6 is the one exception, on different chips).
> - **TX-28** The relay never switches while a chip is keyed or in the unkey wait.
> - **TX-29** Battery Save never writes path pins or sleeps a chip while either chip transmits or is in the unkey wait; the sleep itself refuses while keyed, whoever asks (decision 128).
> - **TX-45** Key-up writes the TX chip's bandwidth with every TX frequency, as stock: REG_43 0x3028 wide, 0x4008 narrow (0x0801DE38–0x0801DE52), from the keyed slot (HF mode: its NFM mode; crossband: the TX side's own, decision 95), whatever the chip last held.
> - **TX-47** Unkey in stock's order (PTT states 3 and 4, 0x08024D80 to 0x0801D224; decision 127), with a 400 ms carrier hold that a cut skips.
>     - **TX-47.1** At every voice unkey the carrier is held 400 ms after the end tone and CW ID (stock's +0x07 = 40 at every unkey, 0x08024DD8; tail elimination plays inside it); each starts with the generator's 200 ms silent lead-in (TONE-10), so a Quindar end tone keeps the carrier up about 450 ms before the hold.
>     - **TX-47.2** The steps in stock's order: end tone and CW ID while keyed (TONE-8), the audio stage on (PB8, as stock), the hold, PA drive 0, the 100 ms unkey wait (V0.29), the chip out of transmit (PA control off, REG_30 0; receive is set up by the next tune, not before the wait), then the TX path clear and the receive path back.
>     - **TX-47.3** A remote key-up's lost keepalive is a cut (LINK-20): no hold, no end tone or CW ID.
>     - **TX-47.4** The other cuts (timeout, duty limit, battery under load, a remote key-up's session closing) skip the hold and the tones too.
>     - **TX-47.5** A data key-up (APRS, KISS) also turns the audio stage on after the PA ramp, as stock before its AFSK (0x080091BC), until the unkey.
>     - **TX-47.6** A data unkey (APRS, KISS) holds nothing and plays no tail: the PA goes to 0 as the frame ends, then the unkey wait, so the digipeat or ack that follows is heard (decision 296; stock holds 400 ms after its APRS bursts too).
> - **TX-48** Dry TX (0 8 8 5, off): a switch in the full-power `tx` build for bench tests from the PC. While on, every key-up holds the PA drive at 0 at the one choke point (the firmware's `pa::set`); everything else runs as usual (the sequence, tones, the Transmit screen, timeouts, the duty limit). It is off at every power-on (but in the tx-bench build, TX-48.1) and never stored (not in the settings record, the saved state, `dump` or `load`), and it changes only with the radio's own keys: the terminal's and the link's `set` turn it on but never off (TX-48.2), the link's remote keys reach the row but never change it (greyed for them), `get 0 8 8 5` reads it. Greyed in a receive-only build ("no transmit in this build"). While on: "DRY" in the status bar (SBAR-22); on the Transmit screen while keyed "Dry TX: no RF" in place of "Battery under load" (the volts stay); the readback says `bar ... dry=1` and `transmit ... dry=1`; LINK-35's build byte says 3 (`tx+dry`); the cable sends while keyed (TX-43.2). The UI hands the switch to the PA's choke point before any command to the Radio task. `bench.py` and `tworadio.py` key a `tx` build only while it says `tx+dry` and its bar says `dry=1` before each key-up; what needs a bench command (`txtest`: the suites, the AFSK level sweep) is skipped with its reason.
>     - **TX-48.1** The bench radio's `tx-bench` build (full power with the bench commands) starts every power-on with Dry TX on and says so on the cable's boot report ("TX BENCH: Dry TX on at power-on"); turning it off by hand at 0 8 8 5 is the deliberate step before a real-power key-up. It replaced the `tx-dry` build (the PA held at 0 at build time; decision 193).
>     - **TX-48.2** `set 0 8 8 5 On` from the terminal or the link turns Dry TX on (it only takes power away; `bench.py --dry-on` asks for it). Off is refused ("Dry TX goes off only on the radio"): no PC can bring full power back. Still off at every power-on but in the tx-bench build.
> - **TX-49** No tone the user didn't ask for goes out: before every key-up the keyed chip's DTMF detection (DEC-6) is turned off (REG_70 = 0, the tone generator's register), and it is armed again by the receive tick after the unkey's retune (decision 306). Found on the bench Oct 27: with APRS mode off and 0 4 3 on (the default), every key-up carried 1000 Hz at 1.5 kHz and 3300 Hz at 1.2 kHz deviation under the voice.
> - **TX-50** A refusal from the Radio task ends only a key-up made before it: the Radio task counts its refusals (the sequencer's cut-offs too), the screen notes the count at each key-up (PTT and a satellite pass alike), and a refusal still in the status from an earlier key-up is not this one's. Taking a refusal, the screen also sends an unkey, in case the Radio task keyed. (A review of Nov 20, 2026: an old refusal read as the new key-up's answer left the screen showing "Transmit refused" while the Radio task keyed, with no unkey to come: the carrier stayed up to the 605 s backstop.)
> - **TX-46** The TX chip's set-up at every key-up is stock's TX start (0x0801EAF8; decision 126), whatever receive left: REG_30 = 0 and about 50 µs, REG_47 0x6142 (stock's route while keyed), the frequency and REG_43 (TX-45), the sub-tone with the calibration's deviation (TONE-1, TONE-16), REG_7D's mic gain (VOX-15, VOX-6), then REG_40 = (REG_40 & 0xF000) | 0x50A (0x0801E9E0). Keying (after the TX path, TX-23) writes REG_30 0x0200 on a wide channel or 0 on a narrow one, about 50 µs, then 0xC1FE (0x0801E5CC); a tone while keyed goes through the same step to 0xC3FA and back, with REG_47 back to 0x6142.

> **Spec: limits**
>
> - **TX-30** Every transmission has a timeout, always on (0 8 1).
>     - **TX-30.1** Timeout always on, 30–600 s in 30 s steps (0 8 1, as stock's TOT steps).
>     - **TX-30.2** No pre-alert setting: the Transmit screen's timeout bar is the warning, in its warning colour for the last 10 s. At the timeout (TX-30.3) the alert tone sounds once, about 0.4 s after the unkey, when the transmitter is off (a speaker mic hears it too), as most radios do.
>     - **TX-30.3** At the timeout, unkey by TX-26: the UI unkeys at the setting.
>     - **TX-30.4** The Radio task's sequencer, told the same setting, unkeys 5 s after it as the backstop.
>     - **TX-30.5** PTT must then be released before it transmits again; holding it does nothing.
> - **TX-31** Long transmissions are duty-limited.
>     - **TX-31.1** Long transmissions step power down or stop after a duty-cycle limit.
>     - **TX-31.2** That limit is set on the bench (the board reached about 86 °C after 2 min at full power on 2 m).
> - **TX-32** Battery: a warning before the cut-off; refuse below it; sample during transmit and unkey (TX-26) below the under-load threshold, with hysteresis: the reading must stay under it for 500 ms without a break (10 or more samples at the keyed tick), so one low sample never unkeys.
> - **TX-33** Power switched off while keyed (a crossband pass too): the safe state runs first, before any chip sleeps or the SI4732 is touched: PA drive 0, the repeat audio off, the chip out of transmit, the unkey wait, every select off; no end tone, CW ID or tail. Then power is released (PA11). Stock unkeys nothing here.
> - **TX-38** The duty limit (TX-31), until the bench sets it: keyed time fills a 120 s bucket, weighted by power because heat follows power: High fills it at full rate, Mid at half, Low at a quarter (continuous transmit from cold: High 2 min, Mid 4 min, Low 8 min). It drains at a quarter of real time while unkeyed; full, it unkeys (no end tone) and refuses with "The transmitter is cooling" until the bucket is half empty (about 4 min). The TX timeout (TX-30) is separate: it limits one transmission, this limits heat across many.
> - **TX-39** The Radio task's own refusals (TX-17) show the TX refused screen like the UI's: "AM is receive only" (fix MENU 3, Mode; HF mode's AM too), an emergency frequency without a person's second PTT on the prompt (TX-35), "Release PTT" after a timeout (TX-30), and the duty limit (TX-38). It also makes the UI's own refusals again from its own state, so no path to it skips them (decision 128): a receive-only channel (CHAN-4, sent with each slot), busy lockout with the squelch open (TX-21), HF mode on an SI4732 frequency or mode (HF-24), the SI4732 still playing a broadcast (TX-24), the relay in the other state (TX-37), and a frequency outside every PA curve row (TX-11).
> - **TX-40** CW ID goes after voice transmissions only (as the end tone, TONE-11), at the first unkey after power-on and then once 10 min have passed since the last (VOX-12); it is skipped at a timeout, battery or duty cut-off and stays due for the next unkey.
> - **TX-41** With Extend TX on, all of 18–64 MHz transmits (CB included), as stock's HF work mode: stock's loader replaces the calibration's TX windows with 18–64 MHz there, so a valid sector counts as a window on all of 18–64 MHz (CAL-11). Below 18 MHz never transmits (the SI4732's, HF-24). HF transmit starts on Low (TX-36; `txplan::check`, tested).
> - **TX-42** As SAFE-14: no transmission until every PTT input has read released once after boot; held over 1 s at boot shows "PTT stuck".
> - **TX-44** The keyed checks run for every transmission, HF mode's included.
>     - **TX-44.1** TX-30's backstop timeout and TX-31's duty limit run for every transmission, HF mode's included.
>     - **TX-44.2** TX-32's battery check runs for every transmission, HF mode's included.
> - **TX-43** While keyed the cable is quiet, so no data reaches TX audio (decision 130).
>     - **TX-43.1** While keyed, nothing is sent on UART4 (the cable): the terminal, link, KISS(UART) output, the cable log and XON/XOFF wait, so a bias resistor from pin 11 never carries data into TX audio. The Radio task marks the radio keyed just before the key-up's plan runs and the cable asks before every byte, so at most the byte in flight overlaps. Bluetooth isn't held.
>     - **TX-43.2** Dry TX on (TX-48: PA drive held at 0) sends on, so the bench can read the chips over the cable while keyed.
>     - **TX-43.3** PC10 stays a high GPIO whenever UART4 isn't sending, as stock.

### Under the hood


### Status

Mock-ups drawn Oct 2, awaiting review (0c). Built in roadmap 4a, measured in 4e. Done at the milestone 4 gate: power and frequency within stock's figures on every band and level, 1.25 m and HF included, no spurious worse than stock's.


### Settled details

- the mic meter reads PA0 (ADC2 ch 0), the mic-level tap stock's VOX samples (`analysis/audio_path.md` §2); the BK4829's REG_64 isn't needed (stock never reads it). Bench-confirm the scale. Written Oct 7, 2026 (decision 85): the `tx` build reads PA0 each tick while keyed into `TxLive::mic`, its top 8 bits with 160 counts as full deviation (`tonegen::mic_percent`, to confirm).
- After a timeout, PTT must be released before it transmits again: holding it does nothing (decided Oct 6, 2026).
- Band edge: the transmit check tests the carrier frequency only, as stock does; no half-bandwidth margin (decided Oct 8, 2026, owner: match stock). Staying clear of the very edge is the operator's call.
- tx-gotchas proposals now in the plan: PTT on AM is refused (33; TX-20; SSB and CW exist only in HF mode, on the SI4732, which never transmits, HF-24); automatic TX needing the other relay state waits, e.g. a beacon (12; APRS-20, SAFE-20). Settled (decision 76, Oct 7, 2026): the boot PTT guard (9) is adopted though stock has none (TX-42); UART4 stays quiet while keyed (30; TX-43); PB10 low during TX is copied from stock (31; GPS-22). An MCU temperature cut-back (14), which stock and nicFW don't have, is noted and skipped for now: the power-weighted duty limit (TX-38) budgets heat, and the MCU's sensor sits far from the PA (decision 77; roadmap's Later list).
- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - TX-4: changed Oct 3, 2026; changed Oct 21, 2026 (decision 224): 17 m, 15 m and 6 m added, all of 18–64 MHz with Extend TX, as stock.
  - TX-6: the margin in its old wording ("half the bandwidth as edge margin") was dropped on Oct 8, 2026 (decision 97) but the rule kept it until Oct 15, 2026 (decision 176): a bench test written to the old words expected 144.002 MHz refused.
  - TX-7: decision 97, Oct 8, 2026. Stock reads nothing back before driving the PA (it only checks the nominal TX frequency against its band limits); the full read-back is Ferrite's deliberate addition, approved by the owner (`analysis/tx-gotchas.md` item 7). REG_3B is compared with each chip's value after start-up, since Ferrite never writes it. Built in `ferrite_radio::chip::key_mic`; a mismatch names the register in the cable log and refuses as Locked.
  - TX-9: the 0.25 W cap was decided Oct 2, 2026; dropped Oct 21, 2026 (decision 224): stock caps nothing on 200–300 MHz.
  - TX-10: decided Oct 3, 2026; changed Oct 13, 2026 (decision 122): the whole 200–300 MHz path, 243.0 MHz included, until measured. The lock dropped Oct 21, 2026 (decision 224): TX-10.1 – TX-10.3 retired, TX-10.4 – TX-10.6 new.
  - TX-12: decided Oct 5, 2026; decided Oct 3, 2026.
  - TX-14: the windows and the trim lock built Oct 13, 2026 (decisions 120, 122).
  - TX-20: decided Oct 6, 2026.
  - TX-21: decided Oct 7, 2026, decision 74.
  - TX-37: decided Oct 4, 2026.
  - TX-36: decided Oct 3, 2026.
  - TX-30: decided Oct 6, 2026.
  - TX-38: decided Oct 7, 2026, weights to confirm on the bench.
  - TX-41: decision 73, Oct 7, 2026 (Extend TX stopped at 64 MHz); changed Oct 21, 2026 (decision 224): 18–64 MHz as stock. nicFW transmits wherever its own band plan allows, with its own power table.
  - TX-42: decision 76; Stock has no such guard; adopted from `tx-gotchas.md` item 9.
  - TX-43: decision 76. TX-43.2 changed Oct 16, 2026 (decision 190): Dry TX on sends too.
  - TX-48: decided Oct 16, 2026 (Alex), built Oct 16, 2026, decision 190. Neither stock nor nicFW has a dry key-up; Ferrite's `tx-dry` build had it at build time only. 0 8 8 became a list (Extend TX 0 8 8 4, Dry TX 0 8 8 5): the Transmit group had no free number; the terminal's `0 8 8` alone still names Extend TX.
  - TX-48.1: decided Oct 19, 2026 (Alex: "only build the full power tx... since the full tx has a drymode"; decision 193).
  - TX-33, TX-44, TX-45: decision 122, from the transmit audit (`research/tx-vs-stock.md`, M5–M7). TX-45 copies stock; TX-33's safe state is Ferrite's (stock unkeys nothing at power off).

### Open points

- Cross-band split (RX on one BK4829, TX on the other, e.g. RX 446.000 TX 146.520): verify on the radio that the RF path, the relay and the PA switch to the TX chip at key-up and back after (hwtest). Until then the UI and the TX checks treat it like any split.

---

