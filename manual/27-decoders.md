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
| 0 4 2 | POCSAG | Pages (the pages heard, DEC-22); Decode (off, on: Pager mode on slot C, DEC-20); frequency (6.25 kHz steps); capcode filter (one capcode, typed with OK; # clears it); Speed (1200, 2400: DEC-23) | Off, 439.9875 MHz, none, 1200 |
| 0 4 3 | DTMF decode | Off, on (the digits heard, on the slot's card) | On |
| 0 4 4 | Popups | Off, on | On |

> **Spec: decoders**
>
> - **DEC-1** As SAFE-16: decoders have no path to the transmit command.
> - **DEC-2** Each decoder takes its audio as the 2f baseband check decides: filter-bypass (discriminator) audio for POCSAG and AIS, normal audio for SAME and DSC.
> - **DEC-3** A decoder needing discriminator audio switches its slot into it while it runs and mutes that slot's speaker.
> - **DEC-4** POCSAG decodes at 0 4 2 5's speed, 1200 (ham paging's, DAPNET) or 2400, either polarity, on slot C in Pager mode (DEC-20; the BK4829's own modem, DEC-23); the capcode filter (one capcode, or none) drops the rest; OK on 0 4 2 4 types it (digits, up to 2,097,151, the 21-bit address), # clears it. A page's text is read as numeric digits for function 0 and as 7-bit text otherwise, unless that comes out mostly unprintable.
> - **DEC-5** DSC distress raises an alert; other DSC calls are logged.
> - **DEC-6** DTMF decode (0 4 3, on by default; off in Low Power Mode, PWR-24) runs the BK4829's own DTMF detector on each chip that receives for a slot. Not on the chip SAME listens with (DEC-19: the two share the tone register and the interrupt flags), not while transmitting (the tone generator's register), armed again after each retune, wake and transmission. Each detector switches only its own interrupt bits, so they can share a chip.
>     - **DEC-6.1** The digits heard take the slot card's state word, in green: "DTMF 101#" (a PTT ID, a dialled sequence), the newest 12. A digit 3 s or more after the last starts a new string; once the carrier has gone the string stays 5 s, then the card shows its state again. No toast and no event log record (Alex, Oct 23, 2026: "we would see it on the screen... is sort of okay for now").
>     - **DEC-6.2** A digit counts only while that slot's squelch is open: the detector finds digits in noise, so a closed squelch drops what it reports (decision 278).
>     - **DEC-6.3** Off on every chip while the APRS slot is held (APRS mode, KISS or beacons: APRS-21.1): the packet tones would read as digits on C, and nothing listens for DTMF then (decision 278).
> - **DEC-7** Every hit goes to the event log and counts in the inbox; a toast only if Popups (0 4 4) is on. Alerts (SAME, DSC distress) are not decodes here: they keep their screen or banner (INBOX-2, XB-19).
> - **DEC-8** A running decoder keeps its receiver out of Battery Save sleep.
> - **DEC-9** Decoders keep running in menus and with the speaker muted.
> - **DEC-18** The DSP task runs one decoder at a time on the one audio capture (PA2): APRS's AFSK when APRS mode or KISS wants it, else none. The pager doesn't use it: POCSAG is received by C's chip's own FSK modem (DEC-23). Background jobs on watched slots (6f) will share it more finely.
> - **DEC-19** SAME headers are decoded by the BK4829's own FSK receiver in its NOAA SAME mode, on the chip of any slot tuned to a weather channel (162.400-162.550 MHz) while SAME alerts are on (WX-3); the MCU only puts the FIFO's words together into the header's text. The first burst that parses raises the alert (WX-11: Battery Save may sleep through the others); the same text again within 5 minutes is the same alert.
> - **DEC-20** Pager mode (decision 452) is 0 5 3's fifth value (APRS-29.3), and Decode (0 4 2 2) is the same switch seen from the pager's side: turning Decode on sets 0 5 3 to Pager, turning it off puts back the APRS mode Pager replaced (Off, Tracker, On or KISS; Off after a restart). Slot C is the pager slot as it is the APRS slot in APRS mode (APRS-15, APRS-21.1): tuned to 0 4 2's frequency, FM, never off, not scanning, kept awake with receive priority; nothing is decoded for APRS and nothing is sent. Turning it on says so: "Pager on" over "C on 439.9875, APRS off" (or ", KISS off" or ", Tracker off"; just the frequency when 0 5 3 was Off). Decode's help line says it takes slot C from APRS. Low Power Mode holds nothing on C (PWR-24), as for APRS.
>     - **DEC-20.1** C's card in Pager mode is the APRS card's (APRS-17) with a pager header, "Pager" bold in C's colour, the frequency, and the pages heard since this power-on on the right ("3 pages", "No pages yet"); its line is the newest page this power-on, capcode and age ("1234570 · 7 s"; "Listening for pages" before one), and on the large card its text after a colon, then "2 new pages" in violet while pages are unread, and the capcode filter at the bottom ("Every capcode", "Capcode 1234567"); no power (nothing is sent). Beside the state, 0 5 9 7's "APRS first" reads "Pager first". This is where to see the decoder runs.
>     - **DEC-20.2** The readback's card line (TERM-37) says `holder=pager` and `pages=N`.
> - **DEC-21** With C the active slot in Pager mode, OK (MENU) or hold MENU on home opens the pager list on its first row, as the APRS card opens the APRS list (APRS-17.3), and one more OK runs it; the hint bar says "OK Pages". The list, in one fixed order: 1 Pages, 2 Event log, 3 Capcode filter, 4 Pager settings (0 4 2); 0 the full menu. A PTT that would key C (PTT A or the side connector's, with C the active slot) opens Pages from any screen and never transmits there (an exception to KEY-7, as APRS-18; DEC-1).
> - **DEC-22** Pages: the pages in the event log, newest first, each its capcode, age and text (decision 452: read from the log, never stored twice). They are also in Messages (0 5 2), among the APRS messages by age, marked with the pager icon and their capcode for a sender; OK opens one (no reply). A page has one read mark, the log's (INBOX-7): reading it in Pages, Messages or the event log takes it off the inbox count. Messages' "Mark all read" marks the pages read too; "Delete all messages" leaves them (they are the log's: its "Clear the log" removes them). 0 4 2 1 "Pages" shows the unread count ("1 new"). The list's header counts them with the messages.
> - **DEC-23** POCSAG is received by the BK4829's own FSK modem on the chip that has slot C (decision 453), never through the audio capture: the board's coupling capacitors cut the low end of the FM demodulator's output, so long runs of one bit came out wrong (on the air, Nov 24, 2026: 512 baud nothing, 1200 one codeword wrong in each page, 2400 nothing). The modem runs FSK 1.2K or 2.4K (0 4 2 5, Speed; 512 is not one of its modes, and ham paging is 1200) with POCSAG's sync codeword as its 4-byte sync word and 16 preamble bytes asked for (with 8, about half the first syncs stalled the frame), the chip's CRC off, and one frame running on across up to 30 batches, each behind its own sync codeword, checked in software. The first missing sync ends the transmission: the page in progress is reported and the modem set up again. Between transmissions the receive FIFO is kept empty. Each batch's polarity comes from its idle codewords (an inverted codeword is a codeword too); the modem's words carry the first byte off the air in their low half. An all-zero word, what a stalled FIFO reads back, is never a page. The words are read as they fall due (16 bits a word at the speed), not on the FIFO's almost-full flag, which the modem doesn't always raise.

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

