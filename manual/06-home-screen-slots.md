## 6. The home screen and the slots

### What it's for

Home shows what you're listening to, whether anything's there, and whether you're transmitting. It's the power-on screen; hold BACK to return from anywhere.

### Using it

The radio has three **slots**, A, B and C, each on a VFO or a channel. PTT A transmits on the active slot and PTT B on slot B (KEY-7). The **active** slot is large and takes the keys; the others are **watched** (chapter 13).

**Layouts** (MENU 0 7 2; same keys on all three): **Watch** (default: one slot large, two cards), **Single + scope** (one slot with all its settings and a scope strip), **Watch + activity** (three equal slots with their last minute of activity).

| To | Channel mode | VFO mode |
| --- | --- | --- |
| Step | Knob or ▲▼ | Knob or ▲▼ |
| Big step | SIDE2 + knob: 10 channels | SIDE2 + knob: 1 MHz |
| Change group | ◀▶ zone | ◀▶ band |
| Go direct | Type the number | Type the frequency (\* = point) |
| Next slot | SLOT | SLOT |
| VFO ↔ channel | V/M | V/M |
| Zones (the zone list) | Hold V/M | Hold V/M |
| Copy (KEY-23) | Hold 9: copy the channel to the VFO (asks first) | Hold 9: save the VFO as a channel |
| Home channel | Hold 0 | Hold 0 |
| Shortcut (runs at once, a popup names it) | Hold a digit | Hold a digit |
| Shortcut list | MENU 0 9 1 3 | MENU 0 9 1 3 |
| Status page | # | # |
| Pause watch (a watched slot is receiving) | # | # |
| Mute this slot (it still receives) | \* | \* |
| Quick menu: reverse, night red, GPS, Bluetooth, brightness | Hold \* | Hold \* |

**Quick menu:** hold \* on home and a small box comes up over home, naming what the side keys and the knob do while it is up, with each one's state: PTT A reverse, PTT B night red, PF1 GPS, PF2 Bluetooth, the knob brightness. Each press acts at once and the box shows the new state. BACK, \* again or any other key closes it (that key does nothing else), and so do 5 s with no key or knob. While it is up PTT A and PTT B never transmit; a PTT you were holding when it closed has to be let go first. The side connector's PTT closes it and transmits as usual.

**Edit in place:** hold SLOT. The slot's settings fill the screen as a grid: arrows pick, the knob changes, changes apply at once. A VFO shows 9 settings; a channel also shows its zone, name and frequency, plus 12 settings. Leave with BACK, SLOT or 8 s idle; PTT keeps the changes and transmits.

### Screens

| | | |
| --- | --- | --- |
| ![Home, watch layout](img/screens/HomeA.png) | ![Home, single + scope](img/screens/HomeB.png) | ![Home, watch + activity](img/screens/HomeC.png) |
| Watch (default) | Single + scope | Watch + activity |
| ![Editing a VFO in place](img/screens/HomeEdit.png) | ![Editing a channel in place](img/screens/HomeEditCh.png) | ![A toast over home](img/screens/Toast.png) |
| Hold SLOT, VFO | Hold SLOT, channel | A message arrives |
| ![Channel mode, name first](img/screens/HomeChannel.png) | ![A channel with no name](img/screens/HomeChannelNoName.png) | |
| Channel mode: the name first (simulator) | A channel with no name: the frequency large | |

The three layout boards above predate the name-first channel cards (decision 54); the simulator shots show the current cards.

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| 0 7 1 | Theme | Dark, daylight, night red, cyberpunk | Dark |
| 0 7 2 | Home layout | Watch, single + scope, watch + activity | Watch |
| MENU 7 | Watch | Off, A+B, A+B+C | A+B |

> **Spec: home**
>
> - **HOME-1** 240 × 320 portrait: 20 px status bar, 280 px content, 20 px hint bar.
> - **HOME-2** Home appears after the self-test and after holding BACK anywhere.
> - **HOME-3** Three layouts; the layout never changes what a key does.
> - **HOME-4** Active slot shows letter, VFO/channel and name, band (a channel's zone, HOME-4.3), frequency, mode, S-meter, tones, offset/reverse, power level always (Low shows too); the mode chip says FM, FM-N (NFM) or AM (VFO-20). The tone chip (and the compact cards' tone column) shows both tones in 7 characters: the same both ways as the tone ("T 100.0", "D023N"); sent only as the tone; heard only as "R " and the tone ("R 88.5", "R D023N"); sent with a different heard tone as the sent one marked "*" ("T100.0*", "D754I*"); reverse swaps sent and heard (VFO-7).
>   - The chips sit in fixed slots, each with its own x and width (decided Oct 5, 2026): mode (x 15, 36 px), tone (54, 57), shift (114, 57: "+600k", "SPLIT", "R" in front while reversed) and power pinned to the right edge (176, 50). A value that is off leaves its slot empty; nothing moves.
>   - A split's TX frequency takes the band's place in the card header ("VFO · TX 146.520"). Compact cards' value line uses fixed columns too (mode, tone, shift; on the activity layout mode, tone, power at the right).
>   - The Transmit screen's row is the same: mode, the tone being sent as the red chip, power pinned right.
> - **HOME-4.1** While a channel list scans, the card treats the channel the scan is on as a channel at rest: its name leads (large on the big card, the frequency small under it), and the scan's last hit shows by name ("last Club rptr"). A band scan, or a channel without a name, shows the frequency as before.
> - **HOME-4.2** Where PTT can never transmit as the slot is now (a receive-only build or channel, AM, outside the band plan or the calibration, a split across the band relay), the power chip says "No TX" in amber instead of the level ("RX only" doesn't fit its 50 px), from the same checks the PTT refusal runs; hold 2 there says why ("No TX" and the reason) instead of changing the power. Refusals that pass with time (busy, battery, cooling, keyed elsewhere) keep the level.
> - **HOME-4.3** Channel mode leads with the name: the header says the number short and the channel's zone, "012 · Repeaters" (no "CH"), where a VFO says its band ("VFO · VHF"): band words belong to tuning by frequency, a channel comes from a zone. A channel in no zone keeps the band ("012 · UHF"), as does a scan ("SCAN · Airband") and a slot in the broadcast band ("Broadcast", BCR-21). The header takes the room the state beside it leaves, so "012 · " and a 16-character zone name fit whole beside an idle state or a tag (RX, MON, FM) on the large and compact cards and the single + scope layout; with a longer state, a clarifier or the APRS note it keeps at least 120 px (140 on single + scope) and the name is cut at a character, never wrapped; the large card shows the name in the 26 px name font when it fits (13 characters), else the 22 px one (16 always fit), with the frequency small under it; compact cards show the name at the left in the 22 px font when it fits beside the frequency, else 15 px bold, with the frequency small at the right; single + scope does the same as the large card. A VFO, a scan, or a channel with no name shows its frequency large as before. The Transmit screen's header reads "012 Club repeater"; menus, lists, editors and the terminal keep "CH 012".
> - **HOME-5** Watched slots show letter, frequency or name, and state. While watch is cancelled by the relay (WATCH-11), the cards say "Watch off"; there is no per-slot relay tag.
> - **HOME-6** Receiving: RX chip and live S-meter. Transmitting: red TX.
> - **HOME-7** Redraw only what changed; the meter never makes the frequency flicker.
> - **HOME-8** Holding a digit runs its shortcut at the long-press time, while still held; a popup in the middle of the screen names it for 1.2 s: just the feature's name, with the new value under it for a setting (hold 0: the channel). The hint bar stays. The release does nothing. No page shows during the hold; the list of shortcuts is a reference page at MENU 0 9 1 3.
> - **HOME-9** Toasts replace the hint bar for 3 s and never cover the frequency.
> - **HOME-10** # (short) on home opens the Status page; while a watched slot is receiving, it pauses watch instead (WATCH-6) and the hint bar says "# Pause". Hold # stays key lock.
> - **HOME-11** The slots are always stacked A, B, C, top to bottom; SLOT only changes which one is large, in its own place.
> - **HOME-12** In the watch layout the three cards fill the content area: the large card 124 px tall, the others 67 px, 6 px apart, with 5 px clear below the status bar and above the hint bar. The extra height spaces the rows out; nothing new is shown (decision 98).
> - **HOME-13** Home stays quick while the knob turns (decision 106).
>     - **HOME-13.1** While the knob turns (until 400 ms after its last step), home redraws the active slot's part at once (frequency, header, chips, meter) and holds the heavier parts: the other slots' cards or lines, the activity rows and the scope strip; each of those light redraws takes under 20 ms.
>     - **HOME-13.2** The held parts draw once the knob rests, to the same picture a full redraw gives.
>     - **HOME-13.3** A part not yet on the screen is never held. Every layout.
> - **HOME-14** On the single + scope layout, while a slot plays broadcast and the strip can't run beside it (MODE-5: the active slot is the broadcast slot, another slot in the band, or a slot needing the band relay), the strip is drawn plainly off: a dim frame with no grid, bars or labels, so it never looks like a quiet scope. It comes back as a working strip once the active slot is a normal one again, or no slot plays broadcast (MODE-4).
> - **HOME-15** Quick mute: \* (short) on home mutes the active slot and \* again unmutes it; \* \* within a second turns it off (HOME-15.1), and \* on an off slot turns it back on. A muted slot still receives: its squelch, S-meter and the green LED work as before; only its audio is kept off the speaker, and it never holds the speaker from a watched slot (WATCH-3). On the broadcast slot it mutes the broadcast. The mute stays with its slot (A, B or C) through slot changes until \* again. It is RAM only, never saved: a power cycle clears it.
>   - Shown in the slot's own state word, in amber, on every layout: "Muted"; while it receives, "Muted" with the RX tag beside it (HOME-15.3). Home has no room for a new mark, so the state word carries it; on the broadcast slot "Muted" takes the place of the broadcast's own states (BCR-26). A toast confirms each press ("Slot A muted", "\* unmutes, \*\* off"); there is no hint-bar label.
>   - **HOME-15.1** Off: \* \* within a second (the second \* within 1 s of the one that muted) turns a slot off; a later \* only unmutes, so unmuting never passes through Off; \* on an off slot turns it on. An off slot isn't received or watched: no chip listens to it, the active one too, so its watch turns go to the other slots (WATCH-2.1; e.g. A off beside APRS mode's C on 2 m gives C the VHF chip alone, and its "APRS first" note goes); it is never heard and never scans. The toasts: "Slot A off" with "\* turns it back on", then "Slot A on". The APRS slot (C while APRS mode, KISS or beacons hold it) keeps Normal ↔ Muted, and C is turned on when APRS takes it. A latched monitor (SQL-14) goes off with it. RAM only, as the mute: a power cycle turns every slot on. The readback's card `state="Off"`.
>   - **HOME-15.2** An off slot's card is powered down (mock-up O1): no surface fill (the page shows through), a dashed outline in the dim line colour instead of the border, the slot letter dim, a dim header naming what it is on ("VFO · VHF · 146.520"; a channel's number and name, or its frequency without one; cut to fit) with "Off" at its right, a big dim "OFF" in the middle and "\* turns it back on" under it. As the active slot it keeps the large card's size and the same look, its dashed outline blue, so SLOT still shows where it is.
>   - **HOME-15.3** Muted while receiving, every card keeps "Muted" in amber and shows the green RX tag right of it, as a receiving card does (the large card's outlined tag, the small cards' bold RX), with the green border of any receive (the large card keeps its blue). On the APRS card the priority note ("APRS first", "A·B first", APRS-21) hides while both show; on the single + scope layout the header shows the same. The readback keeps `state="RX muted"`.
>   - **HOME-15.4** An off slot doesn't transmit, scan or latch monitor: PTT (A for the active slot, B for slot B), the side connector's PTT, VOX, the dialer and a remote key-up, SIDE2's scan and SIDE1's monitor are refused with the refusal beep and a toast, "Slot A is off" with "\* turns it back on". No TX refused screen: nothing in the menu fixes it.
>   - On a scanning active slot \* still skips the hit (KEY-18); hold \* is the quick menu (HOME-17); channel-only mode allows it (PIN-5).
> - **HOME-16** Retired (decision 109): hold 0 + knob changed the brightness and hold 0 alone jumped to the home channel at the release. The brightness moved to the quick menu's knob (HOME-17) and hold 0 jumps at the long press again (HOME-8).
> - **HOME-17** Quick menu: hold \* on home (the long press, 700 ms) brings up a small box over home that gives the side keys and the knob a feature each while it is up: PTT A reverse on the active slot (VFO-7), PTT B night red, PF1 (SIDE1) steps GPS through Off, Auto and On (0 6 1), PF2 (SIDE2) Bluetooth on/off (0 9 2 1), the knob the brightness.
>     - **HOME-17.1** The box lists the knob's row first, where the knob sits on top of the radio, then the side keys top to bottom: Knob brightness, PTT A, PTT B, PF1, PF2.
>   - The box (240 × 320 portrait: 176 × 116 px, in the middle of the content area) has one row per key: the key, its feature and that feature's state now ("PTT A Reverse off", "PTT B Night red off", "PF1 GPS on", "PF2 Bluetooth off", "Knob Brightness 7"). Each press acts at once, and only the rows that changed are drawn again. There is no hint-bar label.
>   - PTT B switches to night red, and from night red back to the theme in use before it (dark when that isn't known, as after a power cycle in night red); its rows and the whole screen change colour at once (DISP-18). The knob steps 0 7 4 2's level for the theme in use, 1–10 with no wrap, the keypad light with it (DISP-16, DISP-22), and doesn't tune. Every change applies live and is saved as the same setting changed in the menu is.
>   - It is latched: it stays up until BACK, \* again, any other key, or 5 s with no key or knob input. The key that closes it does nothing else, however long it is held (no long press, no repeat). It also closes when the screen goes dark, when the keys lock (KEY-20) and when another screen comes up.
>   - Safety: while it is up, PTT A and PTT B are its keys and never key the transmitter, in every build. A PTT pressed while it was up never keys while it is still held, even after the box closes (5 s, BACK, the screen going dark): it has to be let go and pressed again. Once the box is closed PTT keys as usual (KEY-7). The side connector's PTT is not one of its keys: it closes the box and transmits as usual, with every transmit check. VOX is held while the box is up (VOX-3) and keys only after it closes. The link's remote `KEY` (LINK-20) does the same.
>   - Not available while the active slot scans: hold \* does nothing there and \* still skips the hit (KEY-18). Locked, hold \* does nothing but the lock toast (KEY-14). Channel-only mode refuses it (PIN-5). On the APRS slot it opens, and PTT A says why reverse can't change (APRS-19; its row shows "-"). Short \* stays quick mute (HOME-15).
> - **HOME-18** A data key-up (an APRS beacon, message, ack or digipeat, a KISS frame) opens no Transmit screen, so the slot's card shows it: a red bold "TX" tag (the large card) or word (the small cards) and a red border for as long as the Radio task reports it keyed (Alex, Oct 25: "aprs tx should turn vfo c red tx box"). It wins over every other state word. The readback's card `state="TX"`.

> **Spec: exclusive modes**
>
> - **MODE-1** The exclusive modes (band scope and home's scope strip, tone search, frequency counter, FM broadcast, HF mode, the crossband repeater) follow from state, never from events. The wanted mode is the nearest mode screen that is up or that BACK returns to (the crossband repeater once started with # on its screen), else home's strip on the single + scope layout once the active frequency has rested (MODE-4) and the active slot lets it run beside a broadcast (MODE-5), else FM broadcast while a slot plays broadcast (BCR-29), else none: normal receive. The broadcast is started and stopped apart from the other modes: it plays in its own mode, or beside the strip (MODE-5), and the strip coming and going never restarts it. While keyed only HF mode (HF-23) and the crossband repeater (XB-14) keep running; the others stop before key-up (SCOPE-12, BCR-16, TX-24).
> - **MODE-2** One reconciler brings the radio to the wanted mode after every key, knob step, screen change and tick: the running mode's stop, then the wanted one's start, in that order, each sent once. Screens never start or stop a mode themselves. A retune (an FM station, an HF frequency, the scope's centre) goes to the Radio task only while its mode runs; otherwise the next start carries it.
> - **MODE-3** A running mode holds a lease: the UI confirms it at least every 0.5 s (any command counts). With no confirmation for 1.5 s and no command waiting, the Radio task stops the mode itself, goes back to normal receive and logs "mode lease ran out". The snapshot counts these stops; the UI then takes the mode as stopped and starts again whatever is still wanted. The strip and a broadcast beside it (MODE-5) share one lease: run out, both are stopped. The lease lives in RAM only: nothing is written to flash.
> - **MODE-4** On the single + scope layout the strip stops at the first change of the active frequency (knob, ▲▼, entry, a slot change), so normal receive follows the knob. It sweeps again 500 ms after the last change, centred on the new frequency.
> - **MODE-5** Home's strip keeps listening on the active slot's own frequency, and runs beside a broadcast (decision 115):
>   - The strip's chip has the active slot's own receive setup (filter, mode, squelch level, tone). Every 8 points (about 80 ms at its 10 ms a point) the sweep goes back to the slot's frequency for seven dwells (70 ms, stock's watch dwell) with the chip's squelch open delay at 0 (SQL-17) and reads the squelch each dwell: a call there is found within about 0.15 s.
>   - A carrier there holds the sweep on that frequency: the slot's tone rules and quick mute (HOME-15) decide the audio, its S-meter and state show it as in normal receive, and a call heard mutes a broadcast as any slot does (BCR-24). The sweep goes on from the point it left 100 ms after the squelch closes (stock's receive end). Squelch 0 (always open) holds it for good. The looks nearly double a pass's time (56 points: about 1.05 s rather than 0.56 s).
>   - While a slot plays broadcast, the strip runs beside it, the broadcast playing on, when the active slot is a normal one: not in the broadcast band, and not needing the band relay the broadcast leaves released (BCR-15). Otherwise the strip is off (HOME-14) and the broadcast plays alone, as it does while the knob turns (MODE-4).
>   - While the strip sweeps or holds, the other slots aren't listened to (watch, scans and Battery Save wait, as with the band scope, SCOPE-13); with a broadcast they are watched again whenever the strip is off. PTT stops the strip and the broadcast before key-up and both come back after (TX-24).
> - **MODE-6** The UI never waits for the Radio task (decision 162). It hands a command over only when the Radio task's queue (8 deep) has room; the rest wait in the UI's own queue, in the order they were made, and go on the next turn (every 10 ms while any wait), so keys, the display, the terminal and link answers on the cable and Bluetooth carry on whatever the Radio task is doing.
>     - **MODE-6.1** Nothing jumps ahead: a key-up's plan and its slot's settings go before it, an unkey after it.
>     - **MODE-6.2** A newer setting replaces an older one of the same kind still waiting (a slot's frequency, one of its settings, the active slot, the watch set, Battery Save, the scope's set-up; repeated "the UI is alive" commands), but only while no other command lies between them: never across a transmit, unkey, power-off, mode, seek or scan command. Transmit settings (plan, tones, DTMF, CW ID, VOX, mic gain, timeout) are never merged.
>     - **MODE-6.3** Full (16 waiting), the oldest "alive" command (activity, lease renewal, sweep hold, key beep) goes first, then the oldest setting; transmit, unkey, power-off and mode commands are the last to go.
>     - **MODE-6.4** At power off and reboot the UI gives the Radio task up to 1 s to take what is waiting and then the power-off command (TX-33), then goes on with the save and the power regardless.
>     - **MODE-6.5** The power-on burst fits the queue: the saved state replaces what the defaults queued before it, so the Radio task always gets the saved active slot, watch set and APRS slot (until Oct 22, 2026 the doubled burst overflowed it, pushed those out, and the Radio task kept A active under a screen showing C: APRS mode on C heard nothing). The queue holds 32 commands since Nov 3, 2026: with APRS mode on and C muted the burst was 17, one over the 16 it held, and the saved active slot was the one pushed out (black: A stayed active underneath, its squelch held the watch hop on it and the speaker played it while the cards said C).
> - **MODE-7** The Radio task takes the next command within about half a second whatever it is doing: anything that lasts longer runs as a state that its tick steps, not as a wait inside a command (decision 162).
>     - **MODE-7.1** An SI4732 seek (HF-31 in HF mode, ◀▶ in FM broadcast, BCR-18) is started by its command and its tune status read every 20 ms by the tick; any HF or broadcast command, a new seek or power off cancels it where it is (FM_TUNE_STATUS with CANCEL); one that finds nothing in 15 s is cancelled there too. A plain SI4732 tune or power-up gives up after 500 ms.
>     - **MODE-7.2** A dialled DTMF sequence (DTMF-1) is stepped by the tick symbol by symbol, so PTT let go or power off ends it at once with the transmission.
>     - **MODE-7.3** The tick runs on time while commands stream in: its next time counts from the last tick, not from the last command (before, commands under 10 ms apart held it off: watch, scans and the crossband repeater stood still).
>     - **MODE-7.4** Still waited out inside a command: the unkey's end tone, CW ID and tail (TONE-8, at most a few seconds with a CW ID), a beep (at most 1 s, SND-11) and the SI4732's crystal settling at its power-up (500 ms).

> **Spec: navigation**
>
> - **NAV-1** Channel mode: knob/▲▼ step channels in the zone; ◀▶ step zones, skipping empty ones.
> - **NAV-2** VFO mode: knob/▲▼ step by the slot's step; ◀▶ step bands, by frequency from low to high, wrapping; every receive band is in the list, and the region decides transmit only.
> - **NAV-3** SIDE2 held: big steps (1 MHz or 10 channels).
> - **NAV-4** Digits open entry, showing the band, whether the typed value is on the step, and whether TX is allowed there.
> - **NAV-5** SLOT cycles the enabled slots, A → B → C.
> - **NAV-6** No key's meaning depends on a setting.

> **Spec: edit in place**
>
> - **EDIT-1** Hold SLOT: single-slot layout, first setting focused, status bar EDIT A, slot tagged EDIT.
> - **EDIT-2** VFO: 9 settings. Channel: zone, name, frequency + 12 settings.
> - **EDIT-3** Arrows move, knob changes; hint bar "◀▲▼▶ Pick · Knob Change".
> - **EDIT-4** Changes apply at once and save within 2 s; "\* Undo" for 5 s.
> - **EDIT-5** Changing zone or number moves the channel; Home sets the one home channel.
> - **EDIT-6** Ends on BACK, SLOT or 8 s idle; PTT keeps changes and transmits.
> - **EDIT-7** Settings that don't apply are greyed and say why when selected.

### Under the hood


### Status

Mock-ups approved (0b). Built in roadmap 2a; done when all HOME, NAV and EDIT rules pass in the simulator and on the radio.


### Settled details

- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - HOME-4: decided Oct 4, 2026.
  - HOME-4.3 (HOME-4a until Oct 28, 2026, renumbered as a sub-rule): decided Oct 5, 2026. Changed Oct 15, 2026 (user, decision 178): a channel's header names its zone, not its band ("012 · UHF" became "012 · Repeaters"); the header widens into the room the state leaves.
  - HOME-4.1: decided Oct 19, 2026 (Alex, daily use; decision 192): people name their channels and care about the name far more than the frequency.
  - HOME-4.2: Oct 20, 2026 (Alex, daily use, Oct 16; decision 197): airband and RX-only channels showed LOW/MID/HIGH though PTT is refused.
  - HOME-17.1: Oct 19, 2026 (Alex, daily use, Oct 15): the knob's row moved from last to first.
  - HOME-5: changed Oct 3, 2026.
  - HOME-8: decided Oct 4, 2026. Changed Oct 12, 2026: hold 0 ran at the release (HOME-16); back at the long press Oct 13, 2026 (decision 109).
  - HOME-11: decided Oct 3, 2026.
  - HOME-13, MODE-1 – MODE-4: decided Oct 12, 2026 (decision 106). The knob lag and the strip restarting on every click were seen on the black radio (UI backlog 5 and 6).
  - HOME-13.1: changed Oct 15, 2026 (user, decision 180): a light redraw's budget is 20 ms (the radio took 16 ms; the test had assumed 10).
  - HOME-14: decided Oct 12, 2026 (user, UI backlog 12): the strip greyed out without a label while broadcast plays; seen on the black radio. Changed Oct 13, 2026 (decision 115): off only while the active slot can't sweep beside the broadcast (MODE-5).
  - MODE-5: decided Oct 13, 2026 (user, decision 115). The strip had no look at the active frequency: while it swept, home heard nothing. Stock's scope (`analysis/scope_stock.md`) has no strip; the look's timing is stock's watch's (`analysis/watch.md` §2). Changed Oct 15, 2026 (user, decision 166): the look was two dwells (20 ms, stock's settle alone) and never heard a carrier on the radio, open delay 0 or not; now seven (70 ms, stock's dwell) with the open delay at 0 (SQL-17).
  - HOME-4: the tone chip's both tones, changed Oct 13, 2026 (bench: it showed only the sent tone, so a slot decoding D023N with none sent showed nothing).
  - HOME-15: decided Oct 12, 2026 (user): quick mute on \*, RAM only, no hint-bar label; shown in the state word because home has no spare room. Neither stock nor nicFW has a per-slot mute. Changed Oct 13, 2026: hold \* is the quick menu (HOME-17).
  - HOME-15.1 – HOME-15.4: Oct 27, 2026 (Alex, decision 314): \* cycles Normal, Muted, Off (tracker j3-9); changed the same day (Alex): \* mutes and unmutes, \* \* within a second turns off, \* on Off turns on; muted while receiving shows "Muted" with the RX tag (it read "RX muted" in amber, which hid that the slot was receiving). Stock and nicFW have no per-slot off; stock's dual watch is turned off as a whole.
  - HOME-16: decided Oct 12, 2026 (user, decision 108): hold 0 + knob changes the brightness; hold 0 alone jumps to the home channel at the release, the one hold digit that acts on release, an exception to the Oct 4 "hold digits run at once" rule (decision 40), so the knob can be turned during the hold without jumping first. A dark screen: the waking 0 does nothing itself, but the knob still works while it is held (the simplest consistent case: the wake rule is about the key's own press, and the knob turn is a separate input). Retired Oct 13, 2026 (decision 109): never flashed; the quick menu (HOME-17) took the brightness.
  - HOME-17: decided Oct 12, 2026 (user, decision 109), built Oct 13, 2026. Latched rather than held like a shift key: easier one-handed, so the 5 s idle close and the PTT rules are its safety. Stock and nicFW have no such menu; both put features on programmable side-key presses, which Ferrite rejected (one fixed key layout).
  - NAV-2: decided Oct 6, 2026.

### Open points

None.

---

