## 27b. ACARS messages

**On trial.** A receive-only display of the data messages aircraft and ground stations send on the airband. While the screen is open the radio listens on the ACARS frequency in AM and decodes the bursts itself. It stays in Ferrite only if its flash cost earns its place.

### What it's for

Seeing the short data messages airliners exchange with their airlines on VHF: positions, out/off/on/in times, weather, crew messages. Each one names the flight and the aircraft, so you see who's around.

### Using it

1. MENU 0 3 8. The screen name is **ACARS**. The header says the frequency and how many messages there are.
2. **▲▼** or the knob move through the messages, newest first. **OK** opens one.
3. **◀▶** pick the ACARS frequency: 131.550 (the default), 131.725, 130.025, 129.125, 130.450, 131.450, 136.900. The header says "listening" once the radio is on it, "receiving" while a signal is there, and "not listening" before.
4. **\*** shows only the messages with text, hiding link tests, acknowledgements and data reports (rows that say "Aircraft data report · 512 chars" or similar); **\*** again shows them all. Your choice is kept.
5. **#** shows slot B in a strip above the list, one row fewer, and hides it again. While ACARS listens, slots A, B and C aren't received: the radio's VHF receiver is on ACARS and the other one rests.
6. On a message: **▲▼** or the knob scroll its text, **◀▶** go to the newer and older message, **BACK** returns to the list.

### Screens

| | |
|---|---|
| ACARS | The messages, two lines each: the kind (TEXT, OOOI, ACK, TEST ...), the flight (or the aircraft when there's no flight), the time heard; the airline and the aircraft (or what the message is), the label. |
| ACARS with the strip | The same with slot B's frequency, mode and state in a line above it. |
| ACARS message | The flight large, the airline and aircraft, the label and its meaning; Airline, From, Message, Heard and Check rows; the text. |

### Settings

The frequency, picked with ◀▶ on the screen (kept with the settings).

> **Spec: ACARS**
>
> - **ACARS-1** MENU 0 3 8 (Tools) opens the ACARS screen on its list, the newest message selected; BACK leaves it. On trial (decision 454): receive only; while it's open the radio listens for ACARS (ACARS-11).
> - **ACARS-2** Frames: what the radio reads from each burst, and how it keeps them.
>     - **ACARS-2.1** A frame is the bytes after SOH: mode (1), registration (7, dot-padded), technical acknowledgement (1, NAK for none), label (2), block ID (1), then STX and the text (220 characters at most), or straight to the end; the end is ETX (the last block) or ETB (more follow), then the CRC (2, low byte first) and DEL. Bytes that don't have that shape aren't a frame and are dropped; no bytes make the radio fail.
>     - **ACARS-2.2** Each character is 7-bit ASCII with odd parity: the bytes with even parity are counted; the CRC is CRC-16/KERMIT (0x1021 reflected, initial 0) over the mode to the ETX or ETB as received. A frame with a bad CRC is kept and shown, marked "CRC bad" in red, and never joined to others.
>     - **ACARS-2.3** A block heard again with the same CRC within 60 s (the aircraft sending it again) is kept once.
>     - **ACARS-2.4** Blocks ending in ETB are joined with the blocks that follow: on a downlink by the aircraft, the flight and the message number but its last letter; on an uplink by the aircraft, the label and the mode. Up to 440 characters (two blocks); more is cut and marked "text cut". A message whose next block hasn't come within 30 s, or whose block letter skipped one, is kept as it is, marked "blocks missing". Two messages at most are joined at once; a third finishes the older.
>     - **ACARS-2.5** A block ID that's a digit is a downlink (from the aircraft): its text starts with the message number (4, M01A) and the flight (6, AC0123: the airline's two-letter code and the number). A letter is an uplink (from a ground station), with neither.
> - **ACARS-3** ◀▶ on the list step through 131.550, 131.725, 130.025, 129.125, 130.450, 131.450 and 136.900 MHz, wrapping; 131.550 is the default. The choice is a setting, stored at the end of the settings record (an older record reads 131.550). The list's header shows it, AM, and what the radio does: "listening" on that frequency, "receiving" while its squelch is open, "not listening" until the radio is on it (just after a change, in Low Power Mode, or with no VHF receiver). The header redraws as soon as that changes. Decision 465.
> - **ACARS-4** The list: newest first, a compact two-line row a message (APRS Traffic's, APRS-59: ten to a page, nine under slot B's strip). Line one: the label's kind as a tag, the flight (the registration when there's none) and the clock time it came (its age without a clock). Line two: the start of the message's text when it has some (the airline and the registration are on its page, ACARS-7); without text, the airline's name (else its code) and the registration, or for a message without a flight what its label means, after "from ground" on an uplink; the label at the right. A bad CRC puts "CRC bad" first, in red. ▲▼ and the knob move, OK opens; with no messages it says "No messages yet". Decision 465.
>     - **ACARS-4.1** Repeats: a message without text, its CRC good, whose aircraft's newest row is the same kind (the same label, direction and flight, no text either: link tests, acknowledgements, general responses) isn't a new row: that row counts it ("3x Q0" at the right), takes its time and moves to the top. A message with text, or another kind, in between starts a new row. As APRS's Traffic list does for beacons. Decision 465.
>     - **ACARS-4.2** \* on the list shows only the messages with text, and again all of them. The header then counts those shown ("4 with text"), ▲▼ and ◀▶ on a message skip the hidden ones, and with none to show it says "No messages with text". The choice is a setting (an older record shows all). Decision 465.
>     - **ACARS-4.3** Data reports: messages meant for a machine, not people. An H1 whose text starts with `#` and a three-character sub-label (after "- " too) is one: #DFB "Aircraft data report" (the aircraft's data unit: engine, takeoff and trip reports), #CFB "Fault report", #M1B and #M2B "Flight computer message", any other "data (#T1B)". So is every message labelled B6 (ADS-C report), AA or BA (FANS CPDLC) or MA (MIAM data). Its row's second line is the kind and the text's size ("Aircraft data report · 512 chars") instead of the text; its page puts the kind in the label's chip and keeps the raw text to scroll. \* (ACARS-4.2) hides it with the messages without text. The first block decides for joined blocks. Decision 467.
> - **ACARS-5** # shows slot B in a strip above the list: its frequency, mode and state; the list has one row fewer. # again hides it. While ACARS listens (ACARS-11) B isn't received, so its state reads off; B on the UHF chip beside ACARS is a later step.
> - **ACARS-6** The airline table: in the SPI flash at 0x0C0000 (32 KB), written by Console (from data.ferritefw.dev's list; not built yet). A 16-byte header (magic `FAIR`, version 1, count, CRC-32 of the rows, 4 reserved) and 29-byte rows sorted by IATA code: IATA (2), ICAO (3), name (24, NUL-padded). It's checked once each time the screen opens; a flight's airline is found by a binary search. With no table, or a damaged one, the flight's code shows instead.
> - **ACARS-7** A message's page: the flight large (red with a bad CRC), the airline and registration, a chip with the label and its meaning; then Airline (name and ICAO code, or the code "not in the table"), From (aircraft or ground, and the block), Message (the number and the blocks joined), Heard (the clock time or age, the frequency, and how many times for a repeat, ACARS-4.1), Check (CRC ok or bad, blocks missing or text cut, parity errors, the mode, the acknowledgement); then the text, wrapped at words and at its own line ends. ▲▼ and the knob scroll the text a line at a time, stopping at its end; ◀▶ go to the newer and older message, each from its top; BACK returns to the list.
> - **ACARS-8** Messages are kept in RAM only, about 3 KB: the last 16, their text sharing 1.5 KB, the oldest dropped first; they're gone at power off. The simulator starts with ten made-up messages (one uplink, one with a bad CRC, one of two blocks), and a bench build's terminal has `acars feed [N]` (the first N sample frames heard now), `acars clear` and `acars` (the counts).
> - **ACARS-9** The UI readback (LINK-19) has an `acars` line: the page (`list` or `message`), the messages (`n`), the selection, the frequency, the strip, the airline table's rows once checked; `text` (1 while only messages with text are listed, ACARS-4.2); `radio` (1 while the radio listens on the frequency shown, ACARS-11); on a message also its flight, registration, label, direction (`up`), CRC, blocks whether it is a data report (`data`, ACARS-4.3) and the text's first line shown.
> - **ACARS-10** Labels: about thirty common ones are named (H1 message to or from the crew, _d general response, Q0 link test, 5Z airline designated, SA media advisory, 80 OOOI and position, the Q-labels' out, off, on and in reports, the clearance and CPDLC labels ...); another numbered label reads "Airline defined", any other "Unknown label".
> - **ACARS-11** While the ACARS screen is open (MODE-1's ACARS mode, held by MODE-3's lease), the VHF receiver listens on the frequency picked in narrow AM, its audio always to the decoder (a burst's start never waits for the squelch), the speaker off unless the monitor is latched; the UHF receiver rests, and watch, scans, Battery Save's sleeps and the other decoders wait, as in satellite mode. BACK, PTT or any screen that isn't ACARS's ends it and everything resumes. Not in Low Power Mode (PWR-24.4). The decoder is Ferrite's own (decision 459): 2400 bit/s MSK from the receive audio, the bit clock pulled hard to the first edges after the pre-key's steady tone, each bit read from the carrier's phase at the bit's edge, four front ends side by side; the sync is `*` SYN SYN then SOH, either polarity; each burst is listed once, a copy with a good CRC chosen over one without.
>     - **ACARS-11.1** A bench build's terminal has `acars tune FREQ`: the ACARS screen listens there instead (RAM only, for the bench's signal generator on 446.475; never a transmission on the airband), and `acars tune off`.
>     - **ACARS-11.2** A burst cut short (a fade, a collision) doesn't cost the next one: while a front end reads a message's body it still watches for a new burst, and a sync that comes within 40 bits of a pre-key (at least 32 equal bits in a row, of the sync's polarity) drops the body and reads the new message. A body can't hold such a run (7 bits and odd parity allow at most 14 equal bits in a row), so a message is never dropped for a sync inside its own text.

### Under the hood

The parser, the joining and the RAM log are `ferrite-core`'s `acars` (no heap, host-tested and fuzzed); the airline table's reader is `airlines`, and `tools/mkairlines.py` packs the CSV. The receiver is `ferrite-core`'s `acarsrx`, run by the DSP task on the decoders' 24 kHz audio while the screen has the decoder slot (as SSTV's screen does); the Radio task's ACARS mode tunes the VHF chip. The BK4829's own FSK modem can't take ACARS: it needs an alternating preamble ACARS never sends (bench, Nov 25, 2026, ferrite#192).

### Status

Screens, parser and airline table built and tested on the host and in the simulator (Nov 24, 2026). The radio decodes ACARS (Nov 25, 2026): on the bench, from a bladeRF on 446.475 through the whole path (`acars tune`), 113 of 114 bursts at about −64 dBm and every one at −76; real traffic on 131.550 not yet heard (black, indoors, two minutes). Done when the radio lists real traffic on 131.550.
