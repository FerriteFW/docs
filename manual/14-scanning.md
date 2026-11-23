## 14. Scanning

### What it's for

Walk channels or a frequency range on the active slot and stop on activity.

### Using it

1. SIDE2 scans the zone or the band: the active slot's zone on a channel, its band on a VFO. `SCN` shows in the status bar.
2. On a hit, the scan stops and resumes by the resume rule. Press \* to skip a nuisance hit for the rest of this scan (hint bar "\* Skip").
3. On the scan screen, digits add or remove zones from the set being scanned.
4. SIDE2 stops. The slot returns to where it started, or stays on the last hit.

**Three kinds of skip:** a channel's Skip flag (kept); a range preset's skipped frequencies (up to 48, kept); a nuisance skip (this scan only).

### Screens

No mock-up yet.

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| 0 1 2 | Resume | After 1–10 s, when the carrier drops, stop on hit | 5 s |
| 0 1 3 | Priority check | Off, every 1–5 s | 2 s |
| 0 1 4 | Range presets | Up to 16: name, start, end, step, mode, resume (Global or its own), 48 skips | 2 m, 70 cm, airband, marine |
| 0 1 5 | Skip list | View and clear this scan's nuisance skips | — |
| 0 1 6 2 | Direction | Up, down | Up |
| 0 1 6 3 | Scan inputs | Off, on: channel scans also listen on each channel's TX frequency (SCAN-22) | Off |
| 0 1 6 4 | Return to | Start, last hit | Last hit |

> **Spec: running a scan**
>
> - **SCAN-1** SIDE2 starts and stops a scan on the active slot; `SCN` shows in the status bar while it runs.
> - **SCAN-2** Targets: current zone, a zone set, All, a band view, Nearby, or a range preset. The target setting (once 0 1 3) is out of the menu until it is judged worth building (MENU-33, decision 256): SIDE2 scans the active slot's zone, or its band on a VFO; a range preset is scanned with SIDE2 in its list (SCAN-27).
> - **SCAN-3** The zone set is the slot's zone and the zones 0–9 picked with digits on the scan screen (a toast says "Zone 3 added" / "removed"; a 2-byte mask in the App). A channel scan walks the slot's zone first, then each added zone in turn, each in number order (decision 333: a list the UI answers position by position, SCAN-25). Zones marked "scan all" don't join it yet.
> - **SCAN-4** A channel scan walks channels in number order; a range scan walks start to end at the preset's step and mode (VFO-20).
> - **SCAN-5** Resume: after the set time, when the carrier drops, or never (stop on hit). A zone's own rule overrides the radio's.
> - **SCAN-6** Stopping with SIDE2 returns to the start or stays on the last hit, per Return to (0 1 6 4: Last hit by default, decision 434; a radio with saved settings keeps its choice). The last hit is the last frequency the scan stopped on: the slot's VFO moves there, or on a channel scan the slot goes to that channel, as a PTT on a hit does (SCAN-19).
> - **SCAN-7** The scan screen shows the target, resume rule, position, hits (time, frequency or name, signal) and skip count.
> - **SCAN-8** Scanning keeps the receivers awake; it pauses while the crossband repeater runs.

> **Spec: skip, priority, speed**
>
> - **SCAN-9** A channel's Skip flag leaves it out of every scan.
> - **SCAN-10** A range preset's skipped frequencies (up to 48) are never stopped on. They are kept with the preset and read and written over the link (LINK-58).
> - **SCAN-11** \* skips the current hit (hint bar "\* Skip"). A nuisance skip lasts for this scan only, held in RAM, never stored; it works while stopped on a signal and during the resume wait.
> - **SCAN-12** Priority check: the zone's priority 1 and 2 channels, and any channel with the Priority flag (CHAN-24), are checked at the set interval (0 1 3).
> - **SCAN-13** (Smart scan, replaced by SCAN-23's hit list in decision 72.)
> - **SCAN-14** A scan never switches the relay: a range or band target that needs a relay state other than the active slot's is refused, naming the reason. Channel scans pass HF channels by (CHAN-26), so they never need it. The range preset editor refuses a start or end that would make a preset span 18 or 64 MHz: a toast ("Can't span 64 MHz, one side only"), the edge stays where it was and the editor stays open.
> - **SCAN-15** A list spanning both bands scans on both chips at once.

> **Spec: scan keys** (decided Oct 6, 2026, after nicFW's scan keys)
>
> - **SCAN-16** On the scan screen, ▲ and ▼ set the direction the scan goes from here; stopped on a hit (or in the resume wait after one) they also leave it at once and go on that way, without counting a skip.
> - **SCAN-17** # on a hit skips it for every scan: a channel scan sets that channel's Skip flag (SCAN-9), saved like any channel edit, and goes on; a range scan adds the frequency to the preset's skipped list (SCAN-10), refused with a toast when its 48 are full; a band scan keeps no list and says so ("\* skips it once").
>     - **SCAN-17.1** # on the Skip list (MENU 0 1 5) clears it all only after the shared confirm ("Clear the skip list?", MENU-23), as the lists beside it ask before deleting; OK still lets one back in. A range scan's # on a hit adds it to the preset's list for good; once the scan has stopped, # adds to no preset.
> - **SCAN-18** \* stays the skip for this scan only (SCAN-11): ▲▼ leave a hit, \* leaves it and counts it as skipped until the scan ends, # leaves it for good.
> - **SCAN-19** PTT on a scanning slot ends the scan. Stopped on a hit (squelch open, or still on it in the resume wait), the slot moves there, onto that channel or its VFO, and transmits; otherwise it transmits where the scan started.
>     - **SCAN-19.1** Stopped on a hit means the scan holds there (the Radio task says so, through the resume wait): passing the last hit's frequency again, or a busy step the scan doesn't stop on, isn't a stop, so the scan screen's hints, \* and PTT stay with the scanning case.
> - **SCAN-20** Scan timings (defaults, to confirm on the bench).
>     - **SCAN-20.1** Each step listens 70 ms (stock's watch dwell), and a carrier counts as a hit from 35 ms after the step's retune on, once the chip's squelch has settled; a priority look listens 70 ms on each priority channel; a range scan's fast pass reads each step for 15 ms (SCAN-21). The chip listens to a step with its squelch open delay at 0 (SQL-17).
>     - **SCAN-20.2** On a hit, the resume wait after the carrier drops is 2 s, and a timed resume also goes on 2 s after the carrier drops if that comes first.
>     - **SCAN-20.3** Up to 8 nuisance skips are held per scan (SCAN-11), and a further \* still leaves the hit and counts it.
> - **SCAN-21** Range and band scans take a fast pass: each step reads only the RSSI, for 15 ms (bench-tuned), and a step over the noise floor is held for a full squelch check (the 70 ms step, SCAN-20.1) before it counts as a hit; a false alarm costs one step. The target is at least nicFW's 30 steps a second, measured on the bench. Channel scans keep the 70 ms step. While the active slot's range scan runs, the watch doesn't hop its chip to the other slots on it (but an APRS priority slot, APRS-21.1, keeps its turns), and the receive path stays with the scan's chip for 1 s between the other chip's watched turns (each a watched slot's 70 ms, or a priority slot's own); a watched slot's own scan takes its turns as before.
> - **SCAN-22** Scan inputs (0 1 6 3, off by default): channel scans also stop on each channel's transmit frequency when it has a shift or split, right after its receive one, to catch users talking direct on a repeater's input. Simplex channels add nothing. As nicFW's scan of the TX frequency.
> - **SCAN-23** A frequency scan keeps its last 16 hits with how often each stopped it (newest first; a hit seen again moves up and counts). OK on the scan screen opens the list; OK there stops the scan and puts the slot's VFO on the hit, hold 9 opens the save form on it (KEY-23; hold V/M does nothing there). It replaces the smart scan setting (0 1 6 3 and the zones' flag). 16 × 12 bytes in the App, shared with the counter's and tone search's last hits.
>     - **SCAN-23.1** Each hit also keeps how long its last stop lasted (from the stop to the carrier's last moment): the scan screen's last hits show when, what, how long and how strong ("2 min · Club rptr · 14 s · S9"), the list "3x  14 s  2 min". 12 bytes a hit.
>     - **SCAN-23.2** A channel scan keeps the list too: OK on its scan screen opens it (▲▼ still set the direction, unlabelled), the rows are the channels' names, and OK there stops the scan and puts the slot on that channel (no save: it is one already).
> - **SCAN-25** A channel scan runs in the Radio task without a copy of the channels and without a bit per channel (decision 333): its list is the UI's (SCAN-3: the slot's zone from its member list, CHAN-36, Local's nearest first, CHAN-34.2, then the added zones paged through flash), and the Radio task holds only the list's length and its priority positions (the zone's priority 1 and 2 at their place in the list, or just after it when outside it; then flagged channels), sent with the resume rule and the start at the slot's place in its zone. It asks what is at a position a few stops ahead (`LiveAll::want`: the slot and the position); the UI answers with the receive frequency, or 0 for a position that is no stop (a Skip-flagged or HF channel, SAFE-20, or none there now), which the scan passes at once; it keeps 16 answers for all slots and holds a step until its frequency has come, so every stop gets its full listen. When the channels change under a running scan, its list goes again (length and priorities; the scan goes on where it is, its frequencies asked again). RAM: about 300 bytes in the Radio task.
> - **SCAN-26** Direction (0 1 6 2) is the way a scan starts, up (the default) or down; ▲ and ▼ on the scan screen still change it while it runs (SCAN-16).
> - **SCAN-24** A range preset's resume is Global (the default: it follows the radio's rule, 0 1 2) or its own: after 1–10 s, carrier drop, or stop on hit, as a zone's (SCAN-5). Airband wants carrier drop, a busy band a time. As nicFW, whose resume is global, plus a per-range override.
> - **SCAN-27** SIDE2 on a range preset in MENU 0 1 4 scans it on the active slot (decision 428, ferrite#83): the slot's VFO goes to the preset's start (or stays where it is, if that's inside the range), at the preset's mode and step, and the scan walks only the preset's range at its step, its skipped frequencies left out (SCAN-10), with its resume rule (SCAN-24) and 0 1 6 2's direction. A scan running there stops first; Low Power Mode and an off slot refuse it as SIDE2 on home does. The list's hint bar shows SIDE2 Scan (\* still deletes). The Scan menu's Range presets row says how many there are (None, 1 preset, N presets). The skips reach the radio a few at a time before the scan starts, so all 48 are left out from the first step.

### Under the hood


### Status

No mock-up (scan screen not drawn). The screen and its keys (SCAN-16 – SCAN-19) are built in the simulators (Oct 6, 2026); the app's scans are zone and band scans so far, so SCAN-17's range-preset list waits for range scans. Built on the radio in 2d. Done when zone, zone-set and range scans with nuisance skip, priority, the fast pass, scan inputs and the hit list pass on the radio. The engine's fast pass and `WithTx` list are host-tested (Oct 7, 2026).


### Settled details

- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - SCAN-2: the Scan target row (0 1 3) left the menu Oct 22, 2026 (user, decision 256, MENU-33); SIDE2 scans the zone or the band. Resume, priority check, range presets, skip list and Advanced moved up two (0 1 2 – 0 1 6).
  - SCAN-14: changed Oct 3, 2026; decided Oct 7, 2026.
  - SCAN-20.1: changed Oct 15, 2026 (user, decision 166): 50 ms steps, a hit from 25 ms, never stopped on a carrier on the radio (with the chip's open delay at stock's 7; at 0 it stopped on 2 m but not on a 70 cm channel after a 2 m one, which also lost 10 ms of its step to the tick order). Now 70 ms, stock's watch dwell (`analysis/watch.md` §2: stock settles 10–20 ms after a retune and polls for 70 ms, wanting three open polls), with the open delay at 0 (SQL-17).
  - SCAN-21: decided Oct 7, 2026; nicFW's Ultra Scan is its fast VFO scan. Oct 15, 2026 (decision 164): measured 27.2 steps a second on the radio; the Radio task now ticks at each fast step's end instead of waiting for its next 10 ms tick (a step took the second tick past its 15 ms plus the ticks' own time); about 17 ms a step expected. Oct 15, 2026 (decision 165): that change hung the radio in a range scan (keys and the link dead until a power cycle); the Radio task now wakes on a step's end only while it is still ahead of the last tick's start, and never within 2 ms of a tick's end, so a due time a tick didn't move can't run it every 1 ms (host-modelled at the same 58 steps a second). Oct 15, 2026, re-measured in the host model with that wake switched off (`SCAN_WAKE_OFF`: the radio still hung with it) and the 70 ms stop (decision 166): on the 10 ms tick alone 35–45 steps a second (a tick costing 1–4 ms), 30 or more with a false alarm in 20 steps (`scan.rs` `fast_pass_on_the_ten_ms_tick`), watch off; with a watched slot on the other band the hop takes the scan's chip for its turns and the rate falls to 24–30, as the radio's 27.2 and 27.5. The UI test now measures with watch off. Changed Oct 15, 2026 (user, decision 189): with watch on, the active slot's range scan keeps its chip, and the path but for the other chip's turn once a second (host model: 39 steps a second with B watched on the other band, against 30 with the plain hop; 33 with an APRS-priority C on the scan's chip, which keeps its turns).
  - SCAN-22: decided Oct 7, 2026.
  - SCAN-19.1: Oct 19, 2026 (decision 192): the scan screen's hint bar flickered on a channel scan, flipping to the stopped hints each time the scan passed its last hit's channel or a busy step.
  - SCAN-23: decided Oct 7, 2026; nicFW's smart scan keeps 50 hits with a heat count. Changed Oct 14, 2026 (user, decision 159): hold 9 saves, not hold V/M (KEY-23).
  - SCAN-23.1, SCAN-23.2: decided Oct 19, 2026 (Alex, daily use; decision 192). The hit list was frequency scans' only; OK did nothing on a channel scan.
  - SCAN-25: decision 86. Changed Nov 1, 2026 (decision 333): positions in the UI's list instead of a bitmap of channel numbers, which at 4,000 channels would have taken 1.5 KB for the three slots.
  - SCAN-3: changed Nov 1, 2026 (decision 333): written as built (the digits' zones 0–9; "scan all" never joined the set).
  - SCAN-24: decided Oct 7, 2026, decision 75.

### Open points

None.

---

