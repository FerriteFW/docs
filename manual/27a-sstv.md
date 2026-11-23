## 27a. SSTV pictures

### What it's for

Receives slow-scan television pictures (the ISS's SSTV events, the SSTV nets) and sends them: a picture from Console, one you received, or the built-in test card with your callsign.

### Using it

1. MENU 0 3 7. The screen name is **SSTV**. It listens on the active slot; the other slots pause while it's open.
2. A picture starts by itself when its header (VIS) is heard, and draws line by line. It's saved when it ends; the newest two are kept.
3. **◀▶** step through the saved pictures, the test card and the pictures to send. **OK** on one of them sends it.
4. **#** starts a mode by hand, for a sender whose header was missed: Robot 36, Martin M1, Scottie S1, PD90, PD120.
5. Sending: the knob picks the mode, **OK** sends: the active slot transmits the picture (36 s for Robot 36, 1.5 to 2 minutes for the others). **BACK** stops it.

### Screens

| | |
|---|---|
| SSTV | The picture (scaled to 240 wide), its mode, line and time; below, what ◀▶ and OK do. |
| Send | The picture, the mode (knob), its length and the slot's frequency and power; OK sends. |

### Settings

None: the mode a picture is sent in is picked each time (Robot 36 first).

> **Spec: SSTV**
>
> - **SSTV-1** MENU 0 3 7 opens the SSTV screen. It listens on the active slot; while it's open the watch pauses (the active slot alone is heard) and comes back when it closes; a running scan stops where it is. It doesn't open while transmitting or while the crossband repeater runs, as the satellite screen (SAT-1). Closing it while a picture comes in ends that picture, saved and marked incomplete (SSTV-2.4).
> - **SSTV-2** Receive: Robot 36, Martin M1, Scottie S1, PD90 and PD120.
>     - **SSTV-2.1** A picture starts on its VIS header (the code and its parity checked); a header heard during a picture that's going well is ignored.
>     - **SSTV-2.2** The sender's clock error (slant) is corrected from the sync pulses: a straight line fitted to their times sets the line period, within 1.5 % of the mode's.
>     - **SSTV-2.3** Every picture is 320 wide and at most 256 lines: PD120's 640 x 496 is averaged to 320 x 248.
>     - **SSTV-2.4** A picture ends after its last line, or when 12 lines in a row have no sync (the signal went); it's saved either way, marked incomplete in the second case.
>     - **SSTV-2.5** # starts a mode by hand (no VIS): the picture starts at the next sync heard.
>     - **SSTV-2.6** A picture holds the active slot's squelch open (its monitor) from its header until it ends, so a weak or fading signal doesn't cut it; a monitor the user had latched (SQL-9.2) is left alone.
> - **SSTV-3** The screen shows the picture scaled to 240 wide (240 x 192 for 256 lines; a received one as its lines arrive), and below it what the picture is (mode, frequency, incomplete) or the line coming in, and the slot listened on. It opens on the newest picture received, else the test card.
> - **SSTV-3.1** The UI readback (LINK-19) has an `sstv` line: the picture shown (`view`: its slot, or `card`), what's in that slot (`slot`: `rx`, `send` or `empty`) with its mode, lines (`open` while it's coming in) and `complete`; the page (`main` or `send`, with the Send page's mode); while a picture comes in its mode, slot and lines so far (`rx`, `rx_slot`, `rx_lines`); while one goes out its mode and frame (`tx`, `frame`); a mode started by hand (`forced`); and `held=1` while a picture holds the squelch open.
> - **SSTV-3.2** When a picture ends the screen keeps showing it, whole, with no blank in between: until its header is finished (its lines are written after its last rows) the lines it ended with are used.
> - **SSTV-4** Storage (decisions 403, 404): four picture slots in the SPI flash from 0x15D000, past the stock bootloader's fonts, 0x29000 bytes (41 sectors) each.
>     - **SSTV-4.1** Slot 0 holds the picture to send (written by Console); slots 1 to 3 take received pictures in turn: the two newest are kept, and the third is always erased ready for the next, so a picture's first lines are never lost to an erase (decision 432).
>     - **SSTV-4.2** A slot's first sector is its header (below); its pixels start at the slot plus 0x1000: 320 x 256, row by row, RGB565 little-endian (640 bytes a row).
>     - **SSTV-4.3** The header, 64 bytes: magic `SSTV` (4), format 1 (u8), kind (u8: 1 received, 2 to send), the VIS code (u8; 0 for a picture not received), flags (u8: bit 0 clear = complete), width (u16, 320), lines (u16; 0xFFFF while it's being received), UTC seconds (u32; 0 unknown), frequency (u32, 10 Hz units; 0 none), name (16 bytes ASCII, 0-padded), a sequence number (u32: the received slots' order), the rest 0xFF. All little-endian.
>     - **SSTV-4.4** A received picture's header is written when it starts, with lines 0xFFFF and flags 0xFF; its lines and flags are programmed when it ends (NOR: bits only cleared). A slot without the magic is empty.
>     - **SSTV-4.5** Console writes a picture to send by erasing the slot's 41 sectors, programming the pixels, then the header last (`DATA_WRITE`, LINK-60: the cable only).
> - **SSTV-5** Send: OK on a picture (a received one, one to send, or the test card) opens Send. A send waits up to 5 s for the store's queued work (an erase as the screen opens) so the picture's rows can be read as it goes.
>     - **SSTV-5.1** The modes Robot 36, Martin M1, Scottie S1 and PD90 (PD120 isn't sent: its 496 lines would be our 248 doubled). A mode longer than the transmit timeout (TX-30) is refused with its length.
>     - **SSTV-5.2** It's a data transmission on the active slot, at the slot's power: the automatic transmission's checks (TX-35) and the band's rules apply, the audio from DAC1 into the microphone input (as APRS), at the deviation APRS uses.
>     - **SSTV-5.3** Robot 36 sends lines 8 to 247 of a 256-line picture (its 240 from the middle); a picture shorter than the mode repeats its last line.
>     - **SSTV-5.4** BACK stops the picture and unkeys; so do the transmit timeout and the battery under load (the key-up ends, the picture stops).
>     - **SSTV-5.5** While a picture goes out, the screen shows it at half size (160 x 128, centred) and, below: "Sending" and the mode, with the slot and its power; the TX frequency in large digits; a progress bar; and the line and the time left, in full text colour (Alex, Nov 22, 2026: the line was too dim, and the frequency matters most while sending).
> - **SSTV-6** The test card: the colour bars, a grey ramp, the callsign large (or "NO CALL") and "Ferrite"; drawn as it's sent, never stored.
> - **SSTV-7** Receive below 18 MHz isn't possible: the broadcast receiver (SI4732) that HF mode uses there isn't wired to the decoders' input (`analysis/audio_path.md`). 18-30 MHz SSB goes through the transceiver and is heard.

### Under the hood

The codec is `ferrite/digimodes/usstv` (no_std, f32): a quadrature discriminator at 24 kHz, pixels averaged into 320 bins as they arrive (the decoder about 6 KB of RAM, in the decoder slot), and a phase-continuous encoder playing 48 kHz from DAC1. Its round-trip tests run every mode clean, noisy, with a 300 ppm clock error and forced.

### Status

Codec, storage, screen and sending built and tested on the host and in the simulator (Nov 15, 2026); Console's SSTV page built (its `sstv` branch). Not yet tried on a radio. Done when a picture from the ISS or another radio decodes on the radio, and one the radio sends decodes in MMSSTV or QSSTV.


### Settled details

- Decided Nov 15, 2026 (Alex: "i want rx for sstv and tx for sstv of a image from spi flash, OR via console or pocket"; decision 403).
- Colour for Robot and PD is BT.601 studio swing, as MMSSTV and QSSTV use.

### Open points

- Pocket: the same pictures over Bluetooth needs `DATA_WRITE` beyond the cable (LINK-60), for the picture slots only.
- Sending a received picture with the sender's callsign on it: a matter for the person sending; the radio doesn't add text over a picture.
