## 19. Crossband repeater

### What it's for

Relays between a VHF and a UHF slot, both ways: what one side hears, the other transmits.

### Using it

1. Tune two slots, one VHF and one UHF, with their tones.
2. More › Tools › Crossband repeater (MENU 0 3 4). The knob picks each side's slot; check the settings grid and the pre-flight ticks.
3. **#** starts; any key stops it (**BACK**, a digit, MENU: anything but PTT and SIDE1); hold **SIDE1** to listen in.

While running, watch, scan, APRS and Battery Save pause. A pass that times out won't pass again until its signal drops.

From a PC or phone on the link (the cable or Bluetooth), `xb start` starts it and `xb stop` stops it, in every build (the terminal, or the link's `CMD`), with the same checks as #; remote keys can press # on its start page too. The radio then shows the repeater's screen, and a key pressed on the radio stops it.

### Screens

| | | |
| --- | --- | --- |
| ![Crossband start](img/screens/XbStart.png) | ![Crossband ready](img/screens/XbIdle.png) | ![Crossband passing](img/screens/XbRunning.png) |
| Start | Ready | Passing A → B |

### Settings

| Setting | Values | Default |
| --- | --- | --- |
| Side 1, Side 2 | Two slots, one VHF, one UHF | A, B |
| Power | Low, mid | Low |
| Timeout, per pass | 30 s – 10 min | 3 min |
| Hang time | 0 – 3 s | 1.0 s |
| Tone gate | On, off (carrier) | On |
| ID | Off, CW every 10 min (the repeater's own; 0 8 6 2 doesn't apply) | Off |
| Speaker | Off, on | Off |

> **Spec: starting**
>
> - **XB-1** Never on at power-up.
> - **XB-2** Refuse to start, saying why, unless: the sides are on **different BK4829s**; neither is HF and no relay change is needed; TX is allowed on both (chapter 15 rules); squelch isn't 0; ID has a callsign (or is off).
> - **XB-3** Power defaults to Low and is never above Mid: unattended transmitting heats the PA (about 86 °C after 2 min at full power on 2 m), and stock caps repeat at Mid too.

> **Spec: running**
>
> - **XB-4** Monitor both sides; a pass starts after 30 ms of open squelch plus a tone match (tone gate on).
> - **XB-5** One direction at a time; the transmitting side's input is ignored. A pass keys from the side that was heard: while ready the receive path takes turns on the two sides (50 ms each), so at the key-up it may be on the other side, whose chip is the one to transmit; the key-up selects the heard side's receiver first, then keys the other chip, never refusing for the turn, and the pass listens on the heard side until it ends (XB-7), the turns resuming after it (decision 163).
> - **XB-6** Key-up, as stock's: PB8 cleared unless the accessory detect (PC15) is low → PA at zero → TX path → BK4829 TX with the TX side's own tone, bandwidth, deviation → PA ramp → 15 ms (stock's PTT state 1, 10–20 ms after its TX start) → repeat audio selected (PA15 low, PB8 set). The RX side stays in RX (the one allowed RX + TX case, on different chips).
> - **XB-7** A pass ends 100 ms after squelch closes or the tone drops, plus the hang time. At the drop (100 ms) the mic is selected again while still keyed (PA15 high), as stock's receive end; a signal back inside the hang time selects the repeat audio again and continues the pass.
> - **XB-8** Unkey, as stock's: the mic selected (PA15 high) and the receive select cleared while still keyed → the end tone and tail as the transmitting slot's, the CW ID if due → the carrier held 400 ms (tail elimination plays inside it) → PA to zero → wait 100 ms (V0.29's) → the TX chip out of transmit → TX path off; the receive side is selected again on the next tick.
> - **XB-9** Each pass has its own timeout; after it, that side can't pass again until its squelch closes.
> - **XB-10** The TX duty and heat limit applies.
> - **XB-11** A receiver opening within 50 ms of the other side keying is self-hold and ignored.
> - **XB-12** The repeater's ID is its own setting, off by default and independent of 0 8 6 2: stock's repeater sends none, and people using the repeater may ID themselves. With it on, send the callsign in CW at the end of the first pass, then at the end of the first pass after each 10 minutes; the repeater never keys just to ID, so a series ending less than 10 minutes after its last ID gets none (decisions 93, 94).
> - **XB-13** Pause watch, scan, APRS and Battery Save while running: Battery Save holds the receivers awake, as when busy, and the radio stays as responsive as without the repeater (keys, display, the link; decision 163).
> - **XB-14** Local PTT while the repeater runs transmits on the slot that PTT keys (KEY-7), interrupting any pass; the Radio task holds the repeater meanwhile and it carries on after, back on its screen. Automatic transmissions (beacons, KISS) are still refused while it runs. Any other key stops it, unkeying first (XB-20.5).
> - **XB-15** Speaker per setting; SIDE1 held monitors the receiving side.
> - **XB-16** The running screen shows the last 30 minutes of activity: A → B above the line, B → A below, each bar in the colour of the slot it was heard on, the current pass in red.
> - **XB-17** The four cells under it never move: Passes, Duty (10 min), Next ID, Last pass ("now" while passing).
> - **XB-18** Simplex only: each side transmits on its own receive frequency, never through its slot's shift or split, so the repeater can't link into another repeater; the start page warns when a side's shift will be ignored and checks transmit on the receive frequencies.
> - **XB-19** An alert (SAME, DSC distress) that arrives while the repeater runs doesn't take the screen: it shows as a banner ("ALERT" and the event, with the inbox icon) and counts in the inbox; the repeater keeps running, since others depend on it, and the alert screen opens once the repeater stops.

> **Spec: from the link**
>
> - **XB-20** The link may start and stop the repeater, in every build, over the cable or Bluetooth, never with fewer checks than the radio's own # (decision 161).
>     - **XB-20.1** `xb start` (the terminal, and the link's `CMD`, LINK-34) opens the repeater's start page over home from wherever the radio is and starts it as # does: XB-2's checks, a refusal answered with the start page's reason (the radio shows it too) and nothing started. Refused while the radio transmits, while a modal screen is up (the PIN at power on, power off, a link write), in channel-only mode (PIN-5), and when already running. `xb stop` stops it as a key does; `xb` says whether it runs, its two sides and who started it.
>     - **XB-20.2** Remote keys start it as the radio's keys do: # on its start page (the one thing a remote key may start that transmits, LINK-19).
>     - **XB-20.3** Over Bluetooth only past the PIN while a PIN lock is on (LINK-30), as every request; `xb start` and `xb stop` are writes, `xb` alone a read (TERM-25).
>     - **XB-20.4** While it runs the radio shows its screen, whoever started it; leaving the screen stops it (MODE-1).
>     - **XB-20.5** Any key pressed while it runs, the radio's or a remote one, but PTT (XB-14) and SIDE1 (XB-15), stops it: lit or dark, locked or not; that press does nothing else (it wakes a dark screen, and the start page stays up).
>     - **XB-20.6** Every start and stop is logged with who did it (the radio's keys, remote keys, or the `xb` command; the cable, Bluetooth or the terminal) and, for a stop, why (a key, `xb stop`, its screen closed, the radio refused): a line in the cable log (TERM-28: `xb: started by cmd:bt`, `xb: stopped by radio: a key`), and `by=` in the readback's `xb` line (LINK-19).
>     - **XB-20.7** Nothing else changes: it is never on at power-up and a remote start isn't remembered (XB-1); power stays Low or Mid (XB-3), each pass keeps its timeout (XB-9) and the duty limit (XB-10); every pass meets the band plan and the power caps (chapter 15) as a start by # does.

### Under the hood


### Status

Built on Oct 8, 2026 (decision 93), in the `tx` build; not yet run on a radio. Started and stopped over the link (XB-20, decision 161) built Oct 14, 2026, with SIDE1's listen (XB-15) on the running screen; the two-radio tests (`tools/tworadio.py --sdr`, module `crossband`) key one radio with Dry TX on into a second one repeating, with an RTL-SDR on the output. Bench first, with a dummy load on each side:
- PA15 and PB8: does PA15 low route the receiving chip's audio into the transmitting chip, and the level and frequency response through EARO → MICin; how much internal mic goes out in stock's first 10–20 ms and from the drop to the unkey (decision 95);
- PC15: its level with nothing in the side connector (PB8 cleared at key-up only when high);
- desense: the 2 m transmitter's third harmonic on a 70 cm receiver (146 MHz × 3 = 438 MHz), at Low and Mid, and whether it opens or holds the UHF squelch (the self-hold window, 50 ms);
- the receive path turn (50 ms per side) against an unselected front end: if both chips hear without their path select, the turn can go;
- the key-up gap (detection to RF) and the unkey order on a scope;
- the CW ID and tail at a pass's end.


### Settled details

- Simplex only: each side transmits on its own receive frequency, never through a shift or split, so the repeater can't link into another repeater (decided Oct 6, 2026).
- End tone and tail elimination follow the transmitting slot's settings, as stock plays its ROGER and TAIL at a repeat's unkey (decision 95); power Low or Mid, never High (XB-3).
- Battery Save stays awake while it runs (XB-13); watch and scans don't run.
- The repeater's ID is off by default and never keys the radio just to ID (XB-12, decision 94).
- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - XB-5: the key-up from the heard side, decision 163.
  - XB-6: decision 95.
  - XB-7: decision 95.
  - XB-8: decision 95.
  - XB-13: Battery Save held awake while running, decision 163.
  - XB-14: changed Oct 6, 2026.
  - XB-18: decided Oct 6, 2026.
  - XB-19: decision 73, Oct 7, 2026.


---

