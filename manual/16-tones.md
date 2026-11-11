## 16. Tones, tone burst and tail elimination

### What it's for

Sends the CTCSS or DCS tone a repeater or group needs, the tone burst that opens older repeaters, and an end-of-transmission signal so the other squelch closes without a noise burst.

### Using it

- **Tones:** MENU 4, or hold SLOT and pick the tone cell. RX and TX are set separately, each as a mode (Off, CTCSS, DCS-N, DCS-I: ◀▶) and a value (the knob); cross modes are just different pairs. Hold 5 opens the tone picker; MENU 0 3 5 finds the tone on the air (chapter 22).
- **Tone burst:** PTT + SIDE2 sends 1750 Hz.
- **Tail elimination:** in the Transmit group, 0 8 8: mode (receive-side muting sits beside transmit, in the same setting) and phase; a channel can turn it off or on for itself (TONE-7).
- **End tone (roger beep):** 0 8 4, beside tail elimination; a channel's End tone overrides it, as its Tail elimination does. Both are set on the tone picker's second page: OK on a channel's Tone cell, then ▼ past the TX tone (TONE-17). A short tone sent as you let go of PTT, before the carrier drops, so the other side hears that you've finished. OK on a value plays it on the speaker without transmitting.

### Screens

No mock-up yet.

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| MENU 4 | Tones (RX, TX) | Off, CTCSS (50 tones), DCS (104 codes, normal or inverted) | Off |
| 0 8 4 | End tone (roger) | Off, beep, two-tone up, two-tone down, chirp, Quindar | Off |
| 0 8 8 1 | Subtone level | Low, Normal, High: the CTCSS/DCS level around the calibration's (TONE-16) | Normal |
| 0 8 8 2 | Tail removal | Off, receive, transmit, both | Off |
| 0 8 8 3 | Phase | 55 Hz, 120°, 180°, 240° | 55 Hz |
| Channel | Tail elimination | Global, off, on (the radio's 0 8 8 mode and phase) | Global |
| Channel | End tone | Global, off, beep, two-tone up, two-tone down, chirp, Quindar | Global |

> **Spec: tones**
>
> - **TONE-1** CTCSS and DCS come from the BK4829's generator at the calibration's deviation.
>     - **TONE-1.1** CTCSS and DCS come from the BK4829's generator.
>     - **TONE-1.2** Their deviation comes from calibration (0xF210 byte 1 CTCSS, byte 2 DCS: REG_51 bits 6:0, written at every key-up, as stock 0x0800A488 and 0x0800D3E0).
>     - **TONE-1.3** Each within 7 bits: a byte over 0x7F locks transmit (TX-14).
> - **TONE-2** RX and TX tones are independent; every CHIRP cross mode is one pair.
>     - **TONE-2.1** In the tone picker each of RX and TX is a mode (Off, CTCSS, DCS-N, DCS-I) and a value in it. ▲▼ pick RX or TX, ◀▶ change the mode, and only the knob (or typed digits, TONE-15) changes the value, wrapping within the mode; on Off the knob does nothing. A mode doesn't remember a value: a new one starts at its first (67.0 Hz, D023), except that DCS-N and DCS-I swap keeping the code. The screen shows the four modes as chips over the mode's values; the hint bar names ◀▶ Mode. Quick settings, the cards and the channel editor's cells stay one field ("T 88.5", "D023N"); the terminal's `slot` takes either form (TERM-35.2); CHIRP stays one field.
> - **TONE-3** A tone search result is applied as the RX tone; it asks before setting TX.
> - **TONE-4** PTT + SIDE2 sends the burst as a transmission, with every chapter 15 check.

> **Spec: tails**
>
> - **TONE-5** Tail elimination on transmit: at unkey, the 55 Hz tone or the CTCSS phase shift, sent while still keyed (TX-26). On a DCS channel it sends the DCS turn-off code (134.4 Hz) instead; the phase setting is for CTCSS only.
> - **TONE-6** Tail elimination on receive: mute on the same events from the other station.
> - **TONE-7** A channel's Tail elimination is Global (the radio's, 0 8 8), Off or On (sent on this channel at the radio's phase, 0 8 8 3).
> - **TONE-8** The end tone (roger beep, "audio tail") goes out after PTT is released, while still keyed, before the PA drops. Order at unkey (TX-26): end tone → CW ID when due → tail elimination (55 Hz or phase) → PA drive 0. The mic is muted while it plays.
> - **TONE-10** End tones (decision 141): short, at the tones' deviation, with a silent lead-in, before TX-47's 400 ms carrier hold.
>     - **TONE-10.1** The end tone is chosen in 0 8 4; a channel's End tone overrides it, VFOs use 0 8 8 3.
>     - **TONE-10.2** The choices, each short:
>         - **Beep:** 1000 Hz, 150 ms.
>         - **Two-tone up:** 800 Hz then 1200 Hz, 100 ms each.
>         - **Two-tone down:** 1200 Hz then 800 Hz, 100 ms each.
>         - **Chirp:** three rising 60 ms tones, 1000, 1250, 1500 Hz.
>         - **Quindar:** 2475 Hz, 250 ms (the Apollo end-of-transmission tone).
>     - **TONE-10.3** Each at the tones' deviation (TONE-19), below voice peak.
>     - **TONE-10.4** The sequence (end tone, and CW ID after it) starts with the chip in tone transmit and the generator silent for 200 ms, so the first step goes out at full level: the BK4829's first tone after entering tone transmit swells (time constant about 80 ms, 90 % at about 190 ms; tones after it are steady). Stock's roger beep (0x0800FFEC: 1000 Hz then 850 Hz, 80 ms each) has no lead-in; this one is Ferrite's.
>     - **TONE-10.5** It plays before TX-47's 400 ms carrier hold.
> - **TONE-11** It follows voice transmissions only: none after APRS, KISS or packet frames, a tone burst on its own, DTMF dialling, or the crossband repeater (XB keeps its own rules). The timeout (TX-30) counts it; at a timeout or a battery cut-off unkey it is skipped.
> - **TONE-12** Tones that go on air (sidetones, tone burst, DTMF, end tone, CW ID) come from the BK4829's generator (REG_70/71), timed by the Radio task; only local beeps use DAC1 (SND-11).
> - **TONE-19** Tones sent on air use stock V0.29's generator gains, at Ferrite's deviation (decision 141).
>     - **TONE-19.1** A single tone sent on air (tone burst, end tone, CW ID) is tone 1 at stock V0.29's gain 0x17 (REG_70 0x9700, 0x0801F33C); a DTMF pair is 0x45 each (0xC5C5), as both stock versions.
>     - **TONE-19.2** The generator's deviation is set by REG_40 (the TX deviation), not by its REG_70 gain.
>     - **TONE-19.3** While any of these tones play REG_40's low 12 bits are 0x43C (the top four kept), and stock's 0x50A goes back when they end (back to the microphone, or the end of the end tone or CW ID).
>     - **TONE-19.4** Through the voice set-up's pre-emphasis the deviation rises with frequency; at 0x43C, wide FM, about 1.1 kHz at 800 Hz, 1.45 kHz at 1000 Hz, 2.3 kHz at 1500 Hz and 2.56 kHz at Quindar's 2475 Hz (the highest end tone, aimed at about 2.5 kHz); NFM halves it.
>     - **TONE-19.5** Stock leaves 0x50A for its tones (1000 Hz 2.43 kHz, 2475 Hz 4.30 kHz); this is Ferrite's.
> - **TONE-20** DCS polarity as stock's, sent and received (decisions 140, 142).
>     - **TONE-20.1** A DCS code goes out as stock sends it (0x0800D3CC): the normal codeword, with REG_51 bit 13 ("transmit negative code") set for a normal code (REG_51 0xA000 with the calibration's byte 2): with bit 13 clear the chip sends the code inverted, so a normal code needs it set.
>     - **TONE-20.2** An inverted code goes out with bit 13 clear (REG_51 0x8000), the same normal codeword.
>     - **TONE-20.3** Receive is set up the same way, as stock's (0x0801E4C8 to 0x0800D3CC): REG_51 0xA000 (normal) or 0x8000 (inverted) and the normal codeword for both.
>     - **TONE-20.4** The squelch opens only on the channel's polarity, as stock's 0x0801EAC4: a normal code on REG_0C bit 14 ("positive code received"), an inverted one on bit 15 ("negative code received"). A D023N channel stays shut to D023I.
>     - **TONE-20.5** The tone hint's scan (TSRCH-12) reads the scan detectors, which can't tell a code from the other polarity's code that sends the same bits (D023I is D047N on air), so a DCS hint names both: the one with the slot's own code number first, else the normal one ("Heard D023I/D047N" on a D023N slot).
> - **TONE-15** Typed tones need not be standard: the picker keeps the 50 CTCSS tones and 104 DCS codes first, and digits type any CTCSS from 60.0 to 260.0 Hz or, on a DCS code, any code D000–D777. The tone word holds them as it is; the card and lists show them as any tone; the terminal, the link and imports take them. nicFW takes 0.1–300 Hz and any DCS.
> - **TONE-17** A channel's end tone and tail elimination share record byte 31 (end tone bits 0–2: Global, off, beep, two-tone up, two-tone down, chirp, Quindar; tail bits 3–4: Global, off, on); a record from before them, or a value out of range, reads Global. On a channel the tone picker (A6) has a second page with the two, under the RX and TX tones; # sets Global, \* undoes. The terminal writes them as `endtone=` and `tail=`, the link as the channel record's last byte.
> - **TONE-18** Tail elimination plays inside the 400 ms carrier hold every unkey has (TX-47), as stock (0x08024DCC): with no sub-tone the 55 Hz tone (stock's REG_51 0x9000 or the calibration's 0xF210 byte 1, and REG_07 0x0471, 0x0801D078; the Subtone level doesn't change it), on CTCSS the phase shift 0 8 8 3 picks (55 Hz there sends the tone), on DCS the 134.4 Hz turn-off code (REG_52 bit 15, bits 14:13 the phase or 0). On receive (0 8 8 2 receive or both, or a channel's On), a tone channel already goes quiet when the tone stops; a channel with no tone listens for the 55 Hz tail and mutes on it.
> - **TONE-16** Subtone level (0 8 8 1): Low, Normal (the calibration's level) or High, for a repeater that opens unreliably. High adds stock's step to the calibration's byte (0x0F CTCSS, 0x14 DCS: 0x0800A490, 0x0800D3EC), Low takes the same off (Ferrite's own), and the result stops at 0x7F where stock's mask wraps it. Three steps keep it near spec; nicFW's 0–127 is easy to set out of spec. Overall TX deviation stays the calibration's.
> - **TONE-13** The tone burst (PTT + SIDE2) lasts as long as SIDE2 is held while keyed; the UI sends it, the Radio task sounds it (milestone 4).
>     - **TONE-13.1** The burst is 1750 Hz, not a setting.
> - **TONE-9** Tail elimination lives in the Transmit group (0 8 8), receive-side muting beside it; it is not a squelch option.

### Under the hood


### Status

No mock-up. Roadmap 4b; deviation measured in 4e.


### Settled details

- The tone burst lasts as long as its key is held, keying the radio while held (decided Oct 6, 2026).
- "Repeater tail delay" is dropped: it had no defined meaning, and tail elimination covers the squelch tail (decided Oct 6, 2026).
- On a DCS channel, tail elimination sends the DCS turn-off code (134.4 Hz); the phase setting is for CTCSS only (decided Oct 6, 2026).
- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - TONE-2.1: decision 205 (Oct 20, 2026): the picker had been one list of about 260 stops (off, CTCSS, DCS-N, DCS-I) on the knob and ◀▶.
  - TONE-5: decided Oct 6, 2026.
  - TONE-13.1: decision 198 (Oct 20, 2026): the 1000/1450/2100 Hz choices dropped; the row had been greyed at 1750 Hz.
  - TONE-7: decision 86.
  - TONE-15: decided Oct 7, 2026.
  - TONE-17: decision 86.
  - TONE-18: decision 87.
  - TONE-16: decided Oct 7, 2026.
  - TONE-13: decided Oct 6, 2026.
  - TONE-19: decision 121 (V0.27's 0x3C, chosen by decision 85, is about 8 dB hotter); REG_40 for tones, decision 141.
  - TONE-10: the silent lead-in, decision 141.
  - TONE-20: decision 140; receive, decision 142 (Ferrite's D023N opened to a stock radio's D023I on Oct 13, 2026).
  - TONE-20.5: changed Oct 15, 2026 (decision 169): the hint named only the normal form, so a D023I sent to a D023N slot read "Heard D047N" (the receiving session).

### Open points

- Compander: check whether the BK4829 has the BK4819's hardware compander; if it does, a per-channel on/off (from the old settings table's open questions).

---

