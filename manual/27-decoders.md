## 27. Decoders: pagers, DSC, AIS

### What it's for

Decodes signals the radio would otherwise only hiss at: POCSAG pagers, SAME weather alerts, marine DSC and AIS, DTMF and selcall. Receive only.

### Using it

- Turn a decoder on under MENU 0 4. Each hit goes to the event log (chapter 24) and, with popups on, a toast; DTMF shows on the slot's card instead (DEC-6.1).
- Background jobs (a decoder on a watched slot, so the active slot stays free) are specced but not built; their setting is out of the menu until they are judged worth building (MENU-33).
- **Event detail** (OK on an event): POCSAG capcode, baud, function, text; SAME event, areas, issued, expiry, originator; DSC type, MMSI, position, time; AIS MMSI, name, position, course and speed, distance and bearing; DTMF sequence, time, slot.
- SAME and DSC distress raise a full-screen alert (chapter 24). SAME setup is in chapter 23.

### Screens

No mock-up yet for the event log or event detail. The alert is in chapter 24.

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| 0 4 2 | POCSAG | Decode (off, on); frequency (6.25 kHz steps); capcode filter (one capcode, typed with OK; # clears it). 512, 1200 and 2400 baud are decoded at once | Off, 439.9875 MHz, none |
| 0 4 3 | DTMF decode | Off, on (the digits heard, on the slot's card) | On |
| 0 4 4 | Popups | Off, on | On |

> **Spec: decoders**
>
> - **DEC-1** As SAFE-16: decoders have no path to the transmit command.
> - **DEC-2** Each decoder takes its audio as the 2f baseband check decides: filter-bypass (discriminator) audio for POCSAG and AIS, normal audio for SAME and DSC.
> - **DEC-3** A decoder needing discriminator audio switches its slot into it while it runs and mutes that slot's speaker.
> - **DEC-4** POCSAG decodes 512, 1200 and 2400 baud at once and either polarity, on a slot tuned to 0 4 2's frequency while Decode is on; the capcode filter (one capcode, or none) drops the rest; OK on 0 4 2 3 types it (digits, up to 2,097,151, the 21-bit address), # clears it. A page's text is read as numeric digits for function 0 and as 7-bit text otherwise, unless that comes out mostly unprintable.
> - **DEC-5** DSC distress raises an alert; other DSC calls are logged.
> - **DEC-6** DTMF decode (0 4 3, on by default; off in Low Power Mode, PWR-24) runs the BK4829's own DTMF detector on each chip that receives for a slot. Not on the chip SAME listens with (DEC-19: the two share the tone register and the interrupt flags), not while transmitting (the tone generator's register), armed again after each retune, wake and transmission. Each detector switches only its own interrupt bits, so they can share a chip.
>     - **DEC-6.1** The digits heard take the slot card's state word, in green: "DTMF 101#" (a PTT ID, a dialled sequence), the newest 12. A digit 3 s or more after the last starts a new string; once the carrier has gone the string stays 5 s, then the card shows its state again. No toast and no event log record (Alex, Oct 23, 2026: "we would see it on the screen... is sort of okay for now").
>     - **DEC-6.2** A digit counts only while that slot's squelch is open: the detector finds digits in noise, so a closed squelch drops what it reports (decision 278).
>     - **DEC-6.3** Off on every chip while the APRS slot is held (APRS mode, KISS or beacons: APRS-21.1): the packet tones would read as digits on C, and nothing listens for DTMF then (decision 278).
> - **DEC-7** Every hit goes to the event log and counts in the inbox; a toast only if Popups (0 4 4) is on. Alerts (SAME, DSC distress) are not decodes here: they keep their screen or banner (INBOX-2, XB-19).
> - **DEC-8** A running decoder keeps its receiver out of Battery Save sleep.
> - **DEC-9** Decoders keep running in menus and with the speaker muted.
> - **DEC-18** The DSP task runs one decoder at a time on the one audio capture (PA2): APRS's AFSK when APRS mode or KISS wants it, else the pager decoder when it is wanted (DEC-4), else none. Background jobs on watched slots (6f) will share it more finely.
> - **DEC-19** SAME headers are decoded by the BK4829's own FSK receiver in its NOAA SAME mode, on the chip of any slot tuned to a weather channel (162.400-162.550 MHz) while SAME alerts are on (WX-3); the MCU only puts the FIFO's words together into the header's text. The first burst that parses raises the alert (WX-11: Battery Save may sleep through the others); the same text again within 5 minutes is the same alert.

> **Spec: AIS** (DEC-10 to DEC-12 were the sensor reader and jamming alarm, dropped by decision 75; the numbers are not reused)
>
> - **DEC-16** AIS listens on both channels, 161.975 MHz (A) and 162.025 MHz (B), its slot alternating between them.
> - **DEC-17** The range filter (off, 5, 10, 25, 50 nm; default 25) leaves out vessels farther than it from your position; with no GPS fix there is no filter and every vessel is listed.

> **Spec: background jobs**
>
> - **DEC-13** A job runs only on a watched slot on its own chip.
> - **DEC-14** Jobs run only while watch runs: when the relay cancels watch (WATCH-11), or in HF mode (HF-6), jobs pause too.
> - **DEC-15** A job shows as a tag on its slot and on the Status page, never in the status bar.

### Under the hood


### Status

DSC, AIS and selcall/MDC1200 left the menu Oct 23, 2026 (decision 274) until they are built: AIS needs the receive bandwidth measured first (a transmit-capable SDR on the bench, ui-backlog); the BK4829's 5-tone detector and FFSK modem may make selcall and MDC1200 cheap. Their rules stay as the spec for then. No mock-ups. Baseband check in 2f; event log 6a; SAME and POCSAG 6b (built Oct 8, 2026, not yet run on a radio: see Under the hood); DSC, DTMF and selcall 6c; AIS 6e; background jobs 6f. Done when each decoder passes on recorded audio and one live signal.


### Settled details

- One decoder at a time for now (`udigimodes` shares one memory block; decided Oct 7, 2026). POCSAG and other decoders in the background alongside APRS are a later feature (roadmap, Later): about 8 KB of RAM each and CPU time to measure.
- Selcall is MDC1200 only; 5-tone and two-tone paging only if asked (decision 73; nicFW decodes DTMF only).
- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - DEC-13 – DEC-15: the Background job row (0 1 2) left the menu Oct 22, 2026 (user, decision 256, MENU-33) until jobs are judged worth building.
  - DEC-18: decided Oct 8, 2026, decision 89.
  - DEC-19: decision 89.
  - DEC-14: changed Oct 3, 2026.

### Open points

- If EARO → PA2 is AC-coupled with a high corner, POCSAG 2400 and AIS may be out of reach (roadmap 2f, the baseband check).

---

