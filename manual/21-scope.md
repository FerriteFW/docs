## 21. Band scope

### What it's for

Shows signal strength across a range of frequencies so you can find activity and tune to it.

### Using it

1. Hold **1** on home, or MENU 0 3 1 6. The screen name is **Scope**. It sweeps around the active slot's frequency; nothing is heard while it sweeps.
2. **◀▶** move the marker, the **knob** moves the centre, digits type a new centre, and **OK** (Go) tunes the active slot to the marker.
3. **#** centres on the strongest signal. **SIDE1** listens to the marker, **SIDE2** to the strongest; press it again or BACK to go back to sweeping. **\*** changes the mode (FM, NFM, AM).
4. **Hold a digit** sets the trigger line (1 low to 9 high, hold 0 clears it). What the trigger does is the Trigger setting: listen to the strongest, or just mark and log.
5. While you're listening to a signal, **PTT** transmits on it from the active slot.
6. **Hold MENU** opens the scope options (MENU-25; a short press is OK, which tunes to the marker).

The home layout *single + scope* shows a small scope strip under the active slot. It pauses while you tune, so you hear the frequencies you pass, and comes back half a second after the last step (MODE-4). It keeps an ear on your own frequency: a call there holds it so you hear it, and it sweeps on once the call ends. With broadcast FM playing on another slot it sweeps beside it, and a call mutes the broadcast as usual (MODE-5).

### Screens

| | | |
| --- | --- | --- |
| ![Band scope](img/screens/Scope.png) | ![Band scope, listening](img/screens/ScopeListen.png) | ![Band scope, daylight](img/screens/ScopeDay.png) |
| Scope: trigger line at 3, waterfall on | Listening to the marker (SIDE1) | Daylight, defaults |

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| 0 3 1 1 | Bars | 30, 60, 120, 240 (span = bars × step) | 60 |
| 0 3 1 2 | Step | The tuning step list (MENU 6) | 25 kHz |
| 0 3 1 3 | Sweep speed | 0.1–1 ms in 0.1 ms steps, then 2–10 ms | 10 ms (stock's) |
| 0 3 1 4 | Trigger | Off, monitor, log | Off |
| 0 3 1 5 | Waterfall row | Off, on | Off |
| 0 3 1 6 | Open band scope | Opens the scope (home: hold 1) | — |

> **Spec: scope**
>
> - **SCOPE-1** Hold 1 opens the scope from home; MENU 0 3 1 6 from the menu. BACK leaves it. Its centre starts on the active slot's frequency.
> - **SCOPE-2** The scope shows bars across the span, MHz labels under the graph, a centre marker, the marker readout (frequency, level), the trigger line, and an info line: bars, step, the time per sweep, and the trigger's action when one is set ("60 bars · 25k · 10.0 ms · Mon", Mon short for Monitor).
> - **SCOPE-3** Keys: ◀▶ marker; knob centre by one step; digits type the centre (18 MHz and up); OK tunes the active slot to the marker and goes home; # centres on the strongest; SIDE1 monitors the marker, SIDE2 the strongest (again or BACK: sweep again); \* mode FM, NFM, AM; hold 1–9 sets the trigger line, hold 0 clears it; hold MENU the scope options (MENU-25: OK is the same key, and tunes); ▲▼ and hold \* do nothing here.
> - **SCOPE-4** One BK4829 sweeps, the active slot's, with its audio off; the other chip and the active slot's audio are not used while sweeping. Per point, as stock (V0.27 0x08023808 / 0x080235E8): frequency set (REG_38/39), REG_30 0x0200 then 0xBFF1 (the VCO recalibration), the dwell (0 3 1 3; stock's is about 10 ms, its tick), then RSSI read (REG_67); each bar is the average of this sweep and the last. The chip gets its full receive setup once on the centre, muted; the other chip sleeps. They share nothing with the decoder waterfalls.
> - **SCOPE-5** A sweep never switches the band relay or the chip: points that need the other chip (across 64 or 300 MHz) or the other relay state are left blank (SAFE-20).
> - **SCOPE-6** Waterfall row (0 3 1 5): each sweep adds one 240-pixel row through the ST7789 hardware scroll. The history stays in panel memory, never in MCU RAM.
> - **SCOPE-7** Only changed bars are redrawn.
> - **SCOPE-8** Bars are drawn above the noise floor: height is the level minus the lowest bar of the last sweep, so weak signals stand out. Bars over the trigger line are drawn red. No peak hold.
> - **SCOPE-9** Bars 30, 60, 120 or 240 (8, 4, 2 or 1 px each); span = bars × step, step from the tuning step list.
> - **SCOPE-10** Trigger (0 3 1 4): Monitor listens to the strongest bar once it has been over the line for 3 sweeps in a row (skipping scan-ignored frequencies), until its squelch closes, then sweeps again; Log marks it and writes it to the event log, at most once a minute per frequency, without stopping.
> - **SCOPE-11** Monitoring sets the chip's receive path, filter and mode for the marker's frequency before it opens audio. Opening or using the scope never clears the scan ignore list.
> - **SCOPE-12** PTT on the band scope (like HF-23, an exception to KEY-7).
>     - **SCOPE-12.1** PTT works only while monitoring: the active slot goes to VFO on the monitored frequency (as OK does) and transmits there, with every chapter 15 check; it doesn't go home first.
>     - **SCOPE-12.2** While sweeping, PTT is ignored with a toast "Listen first: SIDE1 at the marker".
> - **SCOPE-13** While the scope is open, watch, scan, background jobs and Battery Save pause, and automatic transmissions (beacons, KISS, digipeating) wait; leaving resumes them.
> - **SCOPE-14** Input first: a key or knob step on the scope, or on home while its strip sweeps, stops the bars' redraw in progress (the rest is drawn on the next pass) and holds the sweep for 200 ms after the last step, its pass starting again from the first point. The input is handled and drawn first; the bars catch up after.

### Under the hood


### Status

Screen built to SCOPE-1 – SCOPE-13 in the simulator (Oct 6, 2026); the mock-ups are its renders. The Radio task's sweep (SCOPE-4, SCOPE-5, SCOPE-11) built Oct 12, 2026 after it did nothing on the black radio; the bring-up log prints each sweep's time to tune the dwell down from stock's 10 ms on the bench. Not built yet: SCOPE-6's waterfall through the ST7789's hardware scroll; today the waterfall scrolls in software (DISP-5 is the target). The radio's sweep is milestone 2e. The milestone 0 gate needs an approved scope mock-up.


### Settled details

- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - SCOPE-3: decided Oct 6, 2026, after nicFW.
  - SCOPE-5: Stock measures them on the wrong path.
  - SCOPE-14: added Oct 13, 2026 (UI backlog 7): on the radio, keys and the knob lagged behind the scope's redraw and the sweep, which runs above the UI.

### Open points

- The BK4829's real settle time per point: the default 1 ms dwell is a guess to confirm on the bench (nicFW allows 0.1 ms; stock uses about 20 ms).

---

