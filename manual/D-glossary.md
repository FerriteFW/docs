## Appendix D. Glossary

| Term | Meaning |
| --- | --- |
| Active slot | The slot shown large on home; it takes the keys and its PTT is the default. |
| AIS | Ship position reports on marine VHF; decoded, never sent. |
| APC | The PA drive voltage (DAC2, PA5), read from the calibration curves. |
| APRS | Packet position and message network on 144.390 MHz (US; the frequency follows the region). |
| APRS mode | MENU 0 5 3: slot C becomes the APRS slot, watched and decoding; with C active, PTT A opens a message. |
| Automatic view | A computed channel list: All, per band, Recent, Nearby. Never stored. |
| Background job | A zone scan or decoder that a watched slot runs instead of one frequency. |
| Band scope | A muted sweep on the active slot's chip showing signal bars across a span, with a waterfall row (chapter 21: hold 1 on home; settings at MENU 0 3 1). |
| Battery Save | Duty-cycles the BK4829 receivers to sleep; levels 1–3 use stock's timings. The main power lever. |
| Beacon | An automatic APRS position report: manual, timed, by distance or smart (APRS-24). |
| BK4829 | The two Beken transceiver chips: one VHF, one UHF and 18–64 MHz. Two receive at once at most. |
| Busy lockout | Refuse TX while the channel is busy (carrier). |
| Calibration sector | SPI flash 0x00F000–0x00FFFF: factory PA curves, TX windows, trims. Read only, never written. |
| Calibration windows | The TX ranges in the calibration sector: equipment limits, not legal ones. |
| Channel | A stored frequency set (64 bytes); 1,000 of them, each in one zone or none. |
| Channel-only mode | Hides the VFO and editing (MENU 0 9 3 2). |
| Clarifier | A receive-only offset of ±2.5 kHz on the active slot for an off-frequency signal: SIDE1 + ◀▶ (VFO-22). |
| CTCSS, DCS | Sub-audible tone and digital code squelch. |
| CW ID | Your callsign sent in Morse at unkey, radio-wide (0 8 6 2) or by the crossband repeater (XB-12); off by default. |
| Digipeater | Relays APRS packets addressed to an alias it answers to (WIDE1-1, your callsign); off by default (APRS-26). |
| DSC | Digital Selective Calling on marine VHF; decoded, distress raises an alert. |
| DTMF | Keypad tones sent and decoded in audio. |
| Duty limit | A heat budget across transmissions, weighted by power level, that refuses transmit when spent (TX-38); separate from the per-transmission timeout. |
| Emergency frequency | A frequency where the first PTT warns and a second one transmits (TX rules); nothing is always blocked. |
| End tone | A roger beep or Quindar tone at unkey: radio-wide (0 8 4) or per channel (TONE-17). |
| Event log | Flash ring of every decode and alert (for APRS: messages to you and send failures; stations heard go to the heard list): MENU 0 4 1, and Ferrite Console's Event Log. Not the inbox. |
| Extend TX | Off by default. Widens transmit from the region's amateur bands to the calibration windows. |
| Fast pass | A range scan's quick signal-strength-only step, 15 ms; only a step over the noise floor gets the full squelch check (SCAN-21). |
| Fixed position | A typed position used when there is no GPS fix (GPS rules). |
| Frequency counter | Finds a nearby transmitter's frequency with the BK4829's frequency-scan function, 64–1300 MHz (TSRCH-10); MENU 0 3 2 or hold SIDE2. |
| Heard list | The APRS stations heard, newest first, 50 at most (APRS-3); kept across a restart in its own flash region (APRS-4). |
| Heartbeat | With the screen dark, an LED flash every 5 s in the battery's colour; red, green, red every 2 s while something is unread (decision 63, DISP-21.1). |
| Help line | The line under a list that names the highlighted item and its number path (MENU-15). |
| HF mode | Its own screen for everything below 64 MHz: SI4732 (AM, USB, LSB, CW) and chip 1 (18–64 MHz). MENU 0 3 3; everything else pauses while in it. |
| Hint bar | Bottom 20 px: what \*, # and MENU do here. |
| Hit list | The last 16 frequencies a range scan stopped on, with counts; OK tunes, hold 9 saves (SCAN-23). |
| Home channel | The one channel hold 0 jumps to; set with the Home cell in slot edit. |
| Inbox | APRS messages to you; the status-bar envelope counts the unread ones, red for an alert. Decodes go to the event log. |
| Key lock | Hold # locks the keys; monitor, squelch and volume still work, and PTT too unless the lock covers it (hold #, then \*: chapter 7). |
| KISS | Serial TNC protocol; lets PC and phone apps send and receive APRS through the radio. |
| Monitor | Opens the squelch while SIDE1 is held, or latched by a tap; MON on the slot's card. |
| Nearby | Channels with a position, sorted by distance from the GPS fix. |
| Nuisance skip | A frequency skipped for this scan only; held in RAM. |
| Number path | The digits that reach a setting from MENU 0, e.g. 0 8 6 2 (MENU-15). |
| Owner card | Your name and contact details, optionally shown at power-on (MENU 0 7 3 3). |
| Path machine | The one piece of code that owns the RF path selects, the band relay and PA7/PC5, break before make (SAFE-11). |
| Path pins | GPIOs that select the RX and TX RF paths. All cleared before one is set; never RX and TX together. |
| POCSAG | Pager protocol, decoded at 512, 1200 or 2400 baud. |
| Popups | 0 4 4: whether decoder hits show a toast; they always go to the event log. |
| Priority channel | A channel checked during scans: a zone's priority 1 and 2, or one with the Priority flag (CHAN-24, SCAN rules). |
| Quick message | One of nine stored APRS message texts for fast replies. |
| Quick settings | MENU on home: the active slot's most-used settings. |
| Range preset | A named VFO range for scanning: start, end, step, mode, up to 48 skips. |
| Recent list | Recent: the last 10 channels tuned to, transmitted on or heard (CHAN-25); in HF mode, its last 10 frequencies, kept in place of channels. |
| Region | Chosen in setup (MENU 0 9 4); sets the amateur TX bands and some defaults. |
| Relay rule | The band relay follows the active slot (in HF mode, the receiver in use: HF-11); watch turns off while the watched slots need different relay states, and scans needing the other state are refused. |
| Reverse | Listen on a repeater's input: hold \* on home, then PTT A (the quick menu); the tones swap with the frequencies (VFO-7). |
| Safe state | All path pins clear, PA drive 0 V, audio amp off. First code after reset and on any fault. |
| SAME | Weather-alert header codes on US and Canadian weather radio; filtered by FIPS (US) or CLC (Canada) location codes. Decoded by the BK4829 in hardware. |
| Scroll cue | The slim track on the right of a list that shows there is more above or below (DISP-24). |
| SI4732 | The broadcast receiver chip: FM broadcast (chapter 20); AM, shortwave, SSB in HF mode (chapter 20a). |
| Slot | One of three receivers, A, B, C, each on a VFO or channel. PTT A keys the active one, PTT B slot B. |
| Split | A channel or VFO whose transmit frequency is its own, not receive plus a shift. |
| SSB patch | SI4732 firmware patch, copied from the owner's stock firmware; never shipped. |
| Status page | MENU 0 0: every active state in words. |
| Tail elimination | Hides the squelch tail with a 55 Hz burst or a CTCSS phase shift at unkey. |
| Talkaround | Transmit on the receive frequency of a repeater channel, skipping the shift. |
| Toast | A 3 s message over the hint bar. |
| Tone burst | A short 1750 Hz (default) tone to open a repeater: PTT + SIDE2. |
| Update area | SPI flash from 0x300000, used by the bootloader. Never written. |
| VFO | Free tuning; one per slot, remembered per band. |
| View | A channel list to browse: a zone, or an automatic view. |
| Watch | Receiving on more than one slot: off, A+B, A+B+C. |
| Watched slot | A slot that is not active; heard only while the active slot is quiet. |
| Zone | A folder of channels; doubles as a scan set. 254 at most (CHAN-6). |
| Zone map | One byte per channel number in RAM, the channel's zone, read at boot; zone lists come from it. |
| Zone set | The zones marked "in scan all": scanned together as one list (SCAN rules). |

---

