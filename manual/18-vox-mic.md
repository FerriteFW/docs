## 18. VOX, mic gain, reverse and CW ID

### What it's for

Hands-free transmit, the mic level, listening on a repeater's input, and sending your callsign in Morse.

### Using it

- **VOX:** 0 8 2. Speak to transmit on the active slot; it unkeys once you have been quiet for the tail time (2 s by default).
- **Mic gain:** 0 8 3.
- **Reverse:** hold \* on home, then PTT A (the quick menu, HOME-17): the active slot listens on its input and transmits on its output. A channel can also store Reverse, or Talkaround (transmit on the RX frequency).
- **CW ID:** set your callsign (0 8 6 1), then CW ID (0 8 6 2).

### Screens

No mock-up yet.

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| 0 8 2 1 | VOX | Off, on | Off |
| 0 8 2 2 | VOX level | 1–9 | 5 |
| 0 8 2 3 | VOX tail | 0.5–3 s | 2 s |
| 0 8 3 | Mic gain | 1–9 | 5 |
| 0 8 6 1 | Callsign | Text | Empty |
| 0 8 6 2 | CW ID | Off, every 10 min, on unkey | Off |
| Channel | Reverse | On, off | Off |
| Channel | Talkaround | On, off | Off |

> **Spec: VOX and mic**
>
> - **VOX-1** VOX is off by default; when on, it shows on the Status page.
> - **VOX-2** VOX compares the mic level on PA0 with the level's threshold, with hysteresis; the BK4829's VOX is unused.
> - **VOX-3** VOX keys only from home, and only when nothing else is sounding.
>     - **VOX-3.1** VOX keys only from home: any other screen (a menu or settings list, MENU and its groups, an editor, frequency or text entry, a hold-digit popup, the quick menu, a prompt or refusal, an alert, setup, the link's screens) holds it, the detector reset, as stock holds VOX on any UI mode but its main screen; its own Transmit screen counts as home while it holds the key. So MENU 0 8 2 can always be reached to turn VOX off.
>     - **VOX-3.2** Nor does it key while any audio plays (a slot heard, the broadcast, a beep) or any slot's squelch is open.
>     - **VOX-3.3** Nor within 5 s of boot.
>     - **VOX-3.4** Nor while an accessory change is debounced.
>     - **VOX-3.5** It samples again only 1.5 s after the last of these ends, as stock (0x08025994: its hold of 15 x 100 ms).
>     - **VOX-3.6** The PA0 tap reads nothing while the audio stage (PB8) is on and decays over seconds after a sound (bench, Oct 13, 2026).
> - **VOX-4** A VOX transmission runs the full chapter 15 sequence, checks and timeout.
> - **VOX-5** VOX unkeys once the level stays below threshold for the tail time (0 8 2 3, 2 s by default, as nicFW's VOX Tail).
> - **VOX-13** VOX keys the active slot, as nicFW's VOX keys the active VFO. Levels are off or 1–9, 1 the most sensitive (keys on the quietest voice) and 9 the least, as VOX-14.1 numbers them (nicFW has 1–15, stock 10 steps).
> - **VOX-14** VOX levels are stock's thresholds (decision 131).
>     - **VOX-14.1** VOX thresholds are stock's (0x0802F73C), compared, as stock does, with bits 11-4 of the 12-bit PA0 reading (0x0801645C): numbered as stock's menu: level 1 = 21 (keys easiest) up to level 9 = 101, in steps of 10, with stock's 8-count hysteresis.
>     - **VOX-14.2** So a higher level needs a louder voice, as a higher volume number does (the feel bench-confirmed).
>     - **VOX-14.3** The setting's help line says so.
> - **VOX-15** Mic gain 1–9 (0 8 3) sets REG_7D[5:0], the BK4829's mic sensitivity (0.5 dB a step, 0x00–0x3F), to 0x24 + (gain − 5) × 2: 5, the default, is stock's default 0x24 (0x0801DD90, its Mic Gain setting 0; the chip starts at 0x12, 9 dB lower), 1 is 0x1C and 9 is 0x2C (stock's setting 1 is 0x2D). The rest of REG_7D stays as the start-up left it, so the default key-up holds stock's 0xE924. The calibration's 0xF210 byte 0 (stock's setting 2) isn't used (decision 126).
> - **VOX-6** Mic gain sets REG_7D at every voice key-up, the crossband repeater's too. A data key-up (APRS) sets stock V0.29's 0x34 for the burst (0x0801F01C) instead; the next key-up sets the mic gain again. The mic isn't muted during a burst, as stock.

> **Spec: reverse and talkaround**
>
> - **VOX-7** The quick menu's PTT A (hold \* on home, then PTT A: HOME-17) toggles reverse on the active slot: RX and TX frequencies swap, and the tones with them (VFO-7); home shows it.
> - **VOX-8** Talkaround transmits on the RX frequency.
> - **VOX-9** The TX checks use the frequency after reverse and talkaround (TX-6).

> **Spec: CW ID**
>
> - **VOX-10** CW ID needs a callsign; without one it is greyed and says why.
>     - **VOX-10.1** The terminal's `set 0 8 6 2` and the link's `CMD` say the same ("CW ID: set a callsign first") when asked for anything but Off with no callsign.
> - **VOX-11** The ID goes out while still keyed, before the PA drops (TX-26).
> - **VOX-12** "Every 10 min" sends the ID at the next unkey once 10 min have passed since the last one; CW ID never keys the radio by itself. 20 wpm, 700 Hz.
> - **VOX-16** 0 8 6 2 is Off, every 10 min or on unkey (every unkey); with no callsign it stays Off and says why (VOX-10). The callsign and the choice go to the Radio task whenever either changes.

### Under the hood


### Status

No mock-up. Roadmap 4c. VOX is wired (Oct 8, 2026, decision 96): 0 8 2's settings go to the Radio task, which compares PA0 with stock's thresholds and reports speech; the UI keys the active slot from it with every PTT check (`tx` build). VOX-3's accessory-change debounce is the speaker-mic detect's (SND-12, decision 116): VOX stays off from boot until its boot check is done and while a change is being counted; the mic level on PA0 while receiving is a bench check.


### Settled details

- Reverse swaps the tones too, keeping a split RX/TX tone pair correct (decided Oct 6, 2026). Hold \* toggled the slot's Reverse, as nicFW and Yaesu do: it stays (R in the shift chip) until toggled again (decided Oct 6, 2026; Icom's hold-to-check was the alternative). Since Oct 13, 2026 the toggle is the quick menu's PTT A (hold \*, then PTT A; decision 109): the user rarely uses reverse.
- CW ID sends at the next unkey once 10 min have passed since the last ID and never keys the radio by itself; 20 wpm and 700 Hz by default (decided Oct 6, 2026).
- CW ID's tone comes from the BK4829 tone generator, as beeps and end tones do (SND-11, TONE-12; decision 85).
- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - VOX-13: decided Oct 7, 2026; its "1 the least sensitive" corrected Oct 15, 2026 to match VOX-14.1 and the radio (level 1 keyed on the quietest reading).
  - VOX-14: decision 76.
  - VOX-15: decision 76.
  - VOX-12: decided Oct 6, 2026. Oct 15, 2026 (decision 164): a callsign changed on setup's callsign page (0 8 6 1) reached CW ID only after a restart (found by XB-12's test); the UI now sends the callsign to the Radio task whenever the setting changes, by any path.
  - VOX-16: decision 87.
  - VOX-3: home only, decision 145 (Oct 13, 2026: VOX keyed in a menu on the bench, so it couldn't be reached to turn it off).
  - VOX-7: changed Oct 13, 2026 (decision 109): on the quick menu's PTT A (HOME-17).

### Open points

None.


---

