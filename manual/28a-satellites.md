## 28a. Satellites

**Built (Nov 1, 2026): phase 1, the screens, prediction on the radio, Doppler and the Radio task's side; phase 2, the satellites in their SPI flash region, the link's messages, Ferrite Console's Satellites page with the declination and Keep satellites up to date, the terminal's `:sat` and the options page (decision 340). The simulators start with data.ferritefw.dev's fixture of Oct 31, 2026 in their store; a radio has none until Console or `:sat` loads them.**

### What it's for

Working FM satellites and the ISS from the radio alone: the radio predicts passes from its position and stored orbital elements, points you at the satellite, and corrects Doppler on both the uplink and the downlink while you talk. It's for the FM birds (SO-50, AO-91, AO-123, the ISS voice and APRS) with a handheld antenna.

### Using it

| To | Do |
| --- | --- |
| Load satellites and fresh elements | In Ferrite Console's Satellites page: pick from the list, Write. This also sets the radio's clock and the declination. Or paste a TLE or OMM CSV into the terminal (`:sat add`) |
| Keep them fresh | Console's "Keep satellites up to date" (on to start) rewrites the elements on connect when its file is newer, at most once a day |
| See the coming passes | MENU 0 3 6: the pass list, soonest first |
| Get ready for a pass | OK on a pass: the pass page, with the sky track, a countdown to AOS and the corrected frequencies |
| Be reminded | # on a pass: pick how long before AOS (5 minutes to start); at that time a toast and the alert tone, and a satellite in the status bar until the pass ends; OK on the toast opens the pass page |
| Talk | PTT on the pass page transmits on the corrected uplink, with the satellite's access tone (and its arming tone first, if it has one) |
| Fine-tune | ◀▶ on the pass page trims the downlink; the trim is kept per satellite |
| Pick a transponder | 1 to 5: voice, APRS, beacon and the rest, where the satellite has them |
| Change the satellite's options | Hold MENU on the pass list or a pass page: Doppler, uplink power, duplex, transponder, trim |
| Leave | BACK: home, as it was |

Nothing in satellite mode changes the home screen, the slots or the active slot by itself: the mode borrows both chips while its screen is open and gives them back when you leave.

### Screens

Pass list, pass page and pointing page, all 240 × 320 (mock-ups: https://claude.ai/artifact/ScfAxNJLH8UHkU5tHd18zh, Oct 31, 2026; drafts in `docs/research/satellite-mode.md` §9).

- **Pass list:** the elements' age at the top (amber, red: SAT-9), then one row per pass: satellite, AOS in local time, maximum elevation, duration; "up" with the time to LOS for a pass under way; low passes (under 10°) dimmed; a bell on a marked pass. ◀▶ shows the selected pass's satellite and all its passes (the selection staying on that pass); ◀▶ again step through the satellites, and past either end all of them again; BACK on one satellite's passes shows them all again, the selection kept (the hint bar says BACK All), and BACK again goes home.
- **Pass page:** a polar plot (north up, rings at 0°, 30°, 60°) with the predicted track and the satellite's position; azimuth and elevation; AOS countdown or time to LOS; the downlink (large) and uplink with their Doppler shifts; the tones; FD or HD (full or half duplex); the trim; the elements' age; under them the pass timeline (SAT-16).
- **Pointing page** (0 on the pass page, 0 again for the plot): azimuth and elevation large with which way each is moving, the compass bearing (SAT-18) and the sun aid (SAT-19), the downlink and the time to LOS.

| | |
| --- | --- |
| ![Pass list](img/screens/SatList.png) | ![Pass page before the rise](img/screens/SatPassBefore.png) |
| ![Pass page overhead](img/screens/SatPass.png) | ![Keyed up, full duplex](img/screens/SatKeyed.png) |
| ![Pointing page](img/screens/SatPoint.png) | ![Alarm picker](img/screens/SatAlarm.png) |

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| 0 3 6 | Satellites | Opens the pass list | — |

Per satellite, on its options page (hold MENU on any satellite page, SAT-22), kept with the satellite by its catalogue number, not in settings (row 6 is the one setting for every satellite, kept in the settings):

| Row | Values | Default |
| --- | --- | --- |
| 1 Doppler | Both sides, 70 cm only | Console's flag (both sides) |
| 2 Uplink power | Low, Mid, High | Low |
| 3 Duplex | Full, Half (also * on the pass page) | Console's flag (full) |
| 4 Transponder | 1 to 5 (also the digits on the pass page) | 1 |
| 5 Trim | ◀▶ on the pass page, 100 Hz a step; OK here sets it to 0 | 0 |
| 6 Lowest pass | 0°, 5°, 10°, 15°, 20°: passes peaking lower aren't listed (every satellite) | 10° |

> **Spec: satellites**
>
> - **SAT-1** Satellite mode is a screen at MENU 0 3 6, like HF mode (chapter 20a): a pass list and a pass page. Opening it never changes the home screen, the slots or the active slot; it takes both BK4829s while open (watch and scans pause, WATCH-16 style) and gives them back on BACK.
> - **SAT-2** Up to 32 satellites, kept in their own SPI flash region (8 KB at 0x006000, layout version 3, decision 333). Each record is 192 B: the link's 152-byte record (status active, inactive or unknown; the starting flags; the catalogue number; a 16-character name; 48 B of elements; up to five transponders of 16 B with their access and arming tones, some satellites carrying four or five modes), padding and a CRC; 16 a sector, so 32 records use 6 KB of the 8 KB (Alex, Oct 31: "32entries but richer"). The rest of each sector is a log: the info (the declination and the list's stamps, SAT-18, SAT-21) and each satellite's choices (trim, duplex, transponder, uplink power, by catalogue number, so a list written again keeps them), a change programming the next erased slot. Writes are crash-safe like every record (the scratch ring); a whole list from Console is one rewrite of each sector, then programs; the choices are written 2 s after the last change and at power off (decision 340). The 32 are enough: only about 20–30 satellites can be worked from an FM handheld. The firmware ships no satellites: the list lives in the web app (SAT-15) or comes from the terminal.
> - **SAT-3** Elements come as OMM (from the web app, which fetches Celestrak's OMM because 5-digit catalogue numbers ran out in July 2026) or as a pasted TLE (three lines) or OMM CSV in the terminal (`:sat add`, then the lines, then `end`): a satellite held with the same catalogue number gets the new elements (its name, transponders and choices stay); another is added in the first free place with no transponders (passes and pointing only). `:sat` lists the satellites, `:sat del N` deletes one. The web app's transfer sets the clock in the same step (`CLOCK`, LINK-65; the board keeps no time across power-off, GPS-23).
> - **SAT-4** Positions come from near-Earth SGP4 in single precision, with time kept as whole seconds since each element set's epoch (never as an f32 day count, which alone costs 2–3°). Checked on the PC against the f64 `sgp4` crate: pointing within 0.5°, Doppler within 100 Hz at 437.8 MHz and AOS within 10 s over 14 days.
> - **SAT-5** The observer is the GPS fix, else the fixed position (MENU 0 6 9); with neither, the pass list says so and predicts nothing. With only a manually set clock, the pass page shows "time ±1 min" in amber: Doppler on 70 cm needs the time to the second.
> - **SAT-6** Passes are predicted on the radio when the satellite screen opens (the next 24 h: a 30 s coarse step, AOS and LOS refined to 1 s; up to 64 entries in RAM, freed when the screen closes: with more, the earliest 64 by rise time, whatever order they were found in; a pass whose highest point is under the minimum elevation, SAT-22's Lowest pass, 10° to start, isn't listed), filling in as it goes: each satellite's passes join the list in rise-time order together as soon as it is done, the top line says "Predicting 7 of 19…" until the last, the selection stays on the pass it is on (not on a row number) as rows arrive, and the page works throughout (open a pass, scroll, BACK); a satellite up now or the one rising soonest is worked first: a coarse first look at each satellite finds its first pass not over yet, the satellites are worked in that order, and each full scan starts there (Alex, Oct 31: "show the ones that are done.. and the others as the calc is done.. rather then just LOCK Up or blank page") (the radio predicts in slices of 8 ms between keys and redraws, so a key waits at most a slice and a redraw (decision 341); the core goes to its top clock, 240 MHz, for the run and the governor brings it back after (PWR-26.8); the predictor's inner loop runs from the zero-wait flash; the coarse step lengthens to 2-3 minutes while a satellite is more than 20° below the horizon, since a low-orbit pass lasts at most about 15 minutes, so 19 satellites take well under a second; Alex, Oct 31), and again when the elements, the position (more than about 10 km) or the clock change while it is open. Nothing runs in the background (Alex, Oct 31: "we do it once the sat page is loaded... no need to do it in the background"), except for a pass with an alarm set (SAT-12): only that pass is kept, and refined again when the position or the clock changes, so its alarm stays on time.
> - **SAT-7** On the pass page, the selected satellite is tracked once a second: azimuth, elevation, range rate and Doppler.
> - **SAT-8** Doppler is corrected on both sides by default: the downlink chip is retuned each second; the uplink is set at key-up and, while transmitting, retuned each second if the bench shows the BK4829 retunes cleanly while keyed, else every 5 s. A per-satellite flag corrects the 70 cm side only (the FM operating habit). The trim (◀▶) adds to the downlink and is kept per satellite.
> - **SAT-9** Elements' age is shown on the list and the pass page: amber past 7 days (3 for the ISS, which reboosts), red past 30. Age only warns; prediction and Doppler keep working.
> - **SAT-10** The first key-up of a pass on a transponder with an arming tone sends the arming tone for about 2 s, then the access tone (SO-50: 74.4 Hz to arm, 67.0 Hz to use); later key-ups in the same pass send the access tone only.
> - **SAT-11** Full duplex by default: the downlink chip keeps receiving while the uplink chip transmits, as stock's crossband repeater runs. Half duplex (the downlink muted while transmitting) is optional and one key away: * on the pass page switches FD and HD at once, even mid-pass or while keyed, and the choice is kept with the satellite (Alex, Oct 31: "optional, and easy to turn on and off on the sat page as you operate"). A satellite's starting choice comes from the web app, FD unless the desense bench says otherwise (likely the ISS, whose uplink's third harmonic lands 170 kHz from its downlink). The pass page shows FD or HD by the * hint.
> - **SAT-12** A pass alarm is opt-in per pass: # on the pass list or the pass page opens a small picker for how long before AOS it goes off: 1, 2, 5 or 10 minutes, or Off, with **5 minutes** chosen to start (time to pick up the antenna, step outside and face the rise direction; Alex, Oct 31: "a popup that lets you set how many minutes before the pass, with a GOOD default"). The last choice becomes the next default. At that time: a toast with the satellite, time to AOS, maximum elevation and the rise direction, and the alert tone when Alert tones (0 7 5 3) is on. OK on the toast opens the pass page. It never takes the screen. A marked pass shows a bell and its lead time on the pass list.
> - **SAT-13** Transponders are 2 m and 70 cm only: a stored frequency outside 144–148 or 430–440 MHz is refused at load, so the band relay never moves in satellite mode (SAFE-20). Transmitting follows every normal rule (region, timeout, duty limit); a receive-only transponder never transmits.
> - **SAT-14** One satellite is worked at a time; watch, scans, decoders and APRS mode pause while the satellite screen is open, and resume on BACK.
> - **SAT-15** The web app keeps the satellite list (names, frequencies, tones, flags), fetches fresh elements, and shows the same passes the radio predicts, using the same Rust prediction code compiled to WebAssembly.
> - **SAT-16** The pass page shows the pass as a timeline: rise, highest point (time and elevation) and set, with a marker at now (amber before AOS, green while up), and under it the same satellite's next pass.
> - **SAT-17** The pointing page shows azimuth (true, with its compass point, e.g. 212° SSW) and elevation large, each with the way it is moving ("moving right, 2° a second", "rising"), so a hand-held antenna can be aimed without reading the plot. The radio has no compass (GPS-17): nothing claims to know which way the radio faces.
> - **SAT-18** The pointing page also gives the bearing on a magnetic compass ("On a compass 196°", with the declination it used). The declination is one value written by Console with the satellites (from the World Magnetic Model at the radio's position); the radio stores it and subtracts, with no table of its own. Without one, only the true bearing shows, labelled true.
> - **SAT-19** While the sun is more than 10° above the horizon, the pointing page says where the satellite is from the sun ("10° left, 45° above it"), from the clock and the observer's position (a short solar-position formula). Below 10° it is left off; there is no moon aid (flash, decision 334).
> - **SAT-20** While a pass alarm is set, the status bar shows a satellite riding its orbit (a small satellite over a dashed arc; Alex, Oct 31, option B of the mock-ups' artboard 6) and, every 2 s, swaps it with the time to AOS: minutes as two digits ("12") up to 99, then whole hours with an H ("3H"). White while the pass is more than an hour away, amber within the hour, green with "UP" while the satellite is overhead; it goes when the pass ends or the alarm is cleared.
> - **SAT-21** Console keeps the radio's satellites up to date by itself: with "Keep satellites up to date" on (a Console setting, on to start), every connect checks data.ferritefw.dev's satellite file and, when it is newer than what the radio holds (its `built` time against the info record's stamp, LINK-64), writes the fresh elements (and the declination for the radio's position, SAT-18, and the clock) with no prompt, and says so in a toast. At most one rewrite a day (the info's "written" more than 24 h ago); the satellites rewritten are the ones the radio holds, by catalogue number and in its order, so the user's own picks and per-satellite settings (trim, FD/HD, transponder, power: kept on the radio by catalogue number) stay. A radio holding no satellites is left alone (the user picks first).
> - **SAT-22** Each satellite has an options page (hold MENU on the pass list, a pass page, the pointing page or the alarm picker, which it closes; keyed, a toast says "after you release PTT"): Doppler on both sides or the 70 cm side only (SAT-8), the uplink's power (Low, Mid, High; **Low** to start, as the mock-ups drew: a hand-held Yagi's gain needs little), full or half duplex (SAT-11), the transponder, and the trim (OK sets it back to 0); row 6, Lowest pass, is for every satellite: the pass list's minimum elevation (0°, 5°, 10°, 15°, 20°; **10°** to start, Alex, Nov 1: the low passes, one peaking at 0° for 2 minutes, aren't worth showing; decision 341), kept in the settings, and a change predicts the list again. OK changes a row a step at a time; the change is sent to the radio at once and kept with the satellite (SAT-2); BACK returns; 0 opens the full menu, as every options page.

### Under the hood


### Status

Fixes built (Nov 3, 2026, decision 341): the pass list's lag and jumps and hold MENU on the satellite pages (keys first in the UI task, KEY-25), prediction in 8 ms slices at 240 MHz from the zero-wait flash, the soonest satellite first, the earliest 64 kept, the minimum elevation; the pass list reads the satellites' records only for the rows it draws. Phase 2 built (Nov 1, 2026, decision 340): the satellites region and records (`ferrite-store` `sats`), the link's `what` 12 and 13 and `CLOCK` (LINK-63 – LINK-65), the options page (SAT-22), `:sat`, Console's Satellites page with the WMM2025 declination and Keep satellites up to date (SAT-21), SO-50's arming tone in data.ferritefw.dev's file. Phase 1 built (Nov 1, 2026): the pass list, pass page (before the rise, overhead, keyed up), pointing page, alarm picker, toast and status bar mark in every build; near-Earth SGP4 in f32 checked against the f64 `sgp4` crate over 14 days (pointing 0.23°, Doppler 40 Hz at 437.8 MHz, rises within 1 s); the Radio task taking both chips, retuning the downlink each second and keying the uplink in full duplex (the path machine's `key_up_fd`) or half duplex. The firmware's `sat-predict` feature (on by default) predicts on the radio; without it the radio reads passes and tracks Console computes (`ferrite_core::sat::track`, 15 s samples, interpolated within 0.17° and 27 Hz). Not yet: every bench check below.


### Settled details

- Comparable radios: OpenGD77 (up to 25 satellites from its CPS, 24 h prediction, Doppler both sides, a polar plot, the arming tone on a held side key, an alarm a minute before a pass) and BTECH's DMR-6X2 PRO (pass list and details, automatic Doppler, elements from the CPS). Ferrite differs on the arming tone (automatic, SAT-10) and keeps the pass alarm to a toast (SAT-12).
- Linear satellites (RS-44, FO-29) are researched (research §12): CW by keying the 2 m carrier and USB/CW receive on 70 cm, decided by two bench checks; decision 32 stays for home VFOs and channels.

### Open points

- Console's tracks for a build without `sat-predict` (SAT-15's prediction in WebAssembly, written to the radio) aren't written yet: such a build shows no passes.
- Bench: BK4829 retune while keyed (clicks, unlock) for SAT-8: until it is measured the uplink is retuned every 5 s while keyed (`TX_RETUNE_S`), the key-up's frequency set exactly; full-duplex desense per satellite for SAT-11, and the speaker in full duplex (it plays the downlink while keyed: earphones advised, as with any full-duplex rig); prediction time for 32 satellites on the radio (host: 0.4 µs a propagation, about 1,130 a satellite for 24 h with the adaptive step; measured on black Nov 1: about 20 s for 19, bound by the UI tick's 150-propagation slices; since decision 341 the cable log's `sat:` line gives the satellites, propagations, the time taken and the time working, and µs a propagation at 240 MHz: read it on black).
- Bench, for linear phase 2: USB/CW receive on 70 cm with stock's mode-8 recipe and the UV-K5's AF 5 recipe; carrier keying on 2 m (leakage at DAC2 0, the keying envelope, spurs).

---

