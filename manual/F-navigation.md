## Appendix F. Navigation

Every screen, how you get to it and where its keys lead, one table per chapter. The rows are generated from the firmware's code (`docs/tools/navgraph.py --tables`), so they stay true as the screens change; How they are made: the developer guide, Navigation tables.

<!-- nav:counts -->
84 screens in 30 chapter tables: 80 built, 0 placeholders, 4 with a hook but no event source, 0 with no way in, 0 missing.
<!-- /nav:counts -->

**Keys.** MENU and OK are one key: a short press is the screen's OK (on home: MENU, quick settings); held, it is hold MENU, the screen's options. *digit* is any of 0–9; *hold 1* is a digit held on home (the shortcut runs at the long press). MENU 0 x y z is a path in the advanced menu (the tree at the end). "OK on Channel" is OK with that row selected; *back* is the screen it was opened from.

**On every screen**, not repeated in the rows: BACK goes back one level (a row says so only where it differs); hold BACK goes home, except on *modal* screens (PIN entry, the reset at power on, a link write, power off, empty battery); PTT goes home and transmits, PTT up goes back (HF mode transmits in place); hold # locks and unlocks the keys; hold MENU opens the options where the row lists them, elsewhere "No options here"; menus and lists go home after 30 s idle, edit in place after 8 s.

**Status** after a name: none = built and reachable; *placeholder* = opens the "coming" screen; *hook, no event source yet*; *no way in yet*; *missing*.

<!-- nav:tables -->
#### Chapter 9 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-a1"></a>**A1** Frequency entry (VFO) | Home: digit (VFO) · MENU digit / OK · [Channel editor](#nav-a4): OK on Frequency · [Save VFO as channel](#nav-a9): OK on Frequency · [Add repeater](#nav-a10): OK on Frequency · [Range preset editor](#nav-a11): OK · [Band scope](#nav-b10): digit · [Value editor](#nav-a5): OK | digit / * / OK → [HF mode](#nav-b12) · OK (VFO) → Home · OK (a channel's or repeater's frequency) → back · idle 30 s → Home |
| <a id="nav-a9"></a>**A9** Save VFO as channel | Home: hold 9 (VFO) · [HF mode](#nav-b12): hold 9 · [Quick settings](#nav-d1): OK on Channel (VFO) · [Scan](#nav-b9): any key if self.list | OK on Name → [Text entry](#nav-a7) · OK on Frequency → [Frequency entry (VFO)](#nav-a1) · OK → back · idle 30 s → Home |

#### Chapter 6 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-a2"></a>**A2** Channel number entry | Home: digit (channel) | digit / * / OK → [HF mode](#nav-b12) · digit / * / OK → Home · # · * · OK · digit → back |
| <a id="nav-a3"></a>**A3** Edit in place, VFO | Home: hold SLOT (VFO) | OK on a cell → [Value editor](#nav-a5) · OK on Tone → [Tone picker](#nav-a6) · idle 8 s → Home |
| <a id="nav-a4"></a>**A4** Channel editor | Home: hold SLOT (channel) · [Channel row actions](#nav-c10): OK on Edit · [Quick settings](#nav-d1): OK on Channel (channel) · [Add repeater](#nav-a10): OK at the end · [Transmit refused](#nav-b7): OK (receive-only channel) | OK on Name → [Text entry](#nav-a7) · OK on Frequency → [Frequency entry (VFO)](#nav-a1) · OK on a field → [Value editor](#nav-a5) · OK on Tone → [Tone picker](#nav-a6) · idle 8 s → Home |
| <a id="nav-b1"></a>**B1** Home (watch layout) | [Shortcut map](#nav-b4): OK · [Channel number entry](#nav-a2): digit / * / OK · [Frequency entry (VFO)](#nav-a1): OK (VFO) · [PIN entry](#nav-a17): OK · [Frequency counter](#nav-b15): OK (tune there) · [Scan](#nav-b9): any key if self.list / SIDE2 · [Band scope](#nav-b10): OK (tune to the marker) · [Squelch (SIDE1 held)](#nav-b21): SIDE1 released · [Transmit refused](#nav-b7): PTT again · [Emergency frequency](#nav-b8): 5 s without PTT · [Zones](#nav-c11): OK on a zone · [Boot: a check failed](#nav-d12): any key · [Boot: self-test](#nav-d11): checks passed · [Boot: owner card](#nav-d13): 4 s, or any key · [Setup 8, Summary](#nav-a27): OK / # finish · hold BACK (any screen) | MENU / hold → [Screen options (hold MENU)](#nav-d4) · SIDE1 + ▲▼ or knob → [Squelch (SIDE1 held)](#nav-b21) · hold SLOT (channel) → [Channel editor](#nav-a4) · hold SLOT (VFO) → [Edit in place, VFO](#nav-a3) · hold V/M → [Zones](#nav-c11) · # → [Status page](#nav-d6) · MENU → [Quick settings](#nav-d1) · hold MENU → [More](#nav-d2) · SIDE2 → [Scan](#nav-b9) · hold SIDE2 alone (KEY-22) → [Frequency counter](#nav-b15) · digit (VFO) → [Frequency entry (VFO)](#nav-a1) · digit (channel) → [Channel number entry](#nav-a2) · hold 1 → [Band scope](#nav-b10) · hold 3 / hold 8 → [Value editor](#nav-a5) · hold 5 → [Tone picker](#nav-a6) · hold 9 (VFO) → [Save VFO as channel](#nav-a9) · hold 9 (channel) → [Confirm (shared)](#nav-a18) · home: nothing above it |
| <a id="nav-b2"></a>**B2** Home, single + scope | MENU 0 7 2 = single + scope (home's layout) | home: nothing above it |
| <a id="nav-b3"></a>**B3** Home, watch + activity | MENU 0 7 2 = watch + activity (home's layout) | home: nothing above it |

#### Chapter 11 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-a5"></a>**A5** Value editor | Home: hold 3 / hold 8 · [More](#nav-d2): OK on Recent · [Channel editor](#nav-a4): OK on a field · [Edit in place, VFO](#nav-a3): OK on a cell · [Quick settings](#nav-d1): OK on a row · [Transmit refused](#nav-b7): OK (RelayMismatch) / OK (AmRxOnly) | OK → [Frequency entry (VFO)](#nav-a1) · OK → back · idle 30 s → Home |
| <a id="nav-a18"></a>**A18** Confirm (shared) | Home: hold 9 (channel) · [Channel row actions](#nav-c10): OK on Delete · [Quick settings](#nav-d1): OK on Tones · [Range presets](#nav-c12): \* (delete) · [Zones](#nav-c11): \* (delete) | # · OK → back |
| <a id="nav-d1"></a>**D1** Quick settings | Home: MENU · [Status page](#nav-d6): OK on Watch / OK on Battery Save | ◀▶ / OK / knob on 0 8 8 4 → [Extend TX warning](#nav-a19) · ◀▶ / OK / knob on 0 9 3 / 0 9 3 1 → [PIN entry](#nav-a17) · 0 / OK on More → [More](#nav-d2) · digit / OK → [Channel browser: views](#nav-c8) · OK on Tones → [Confirm (shared)](#nav-a18) · OK on Channel (channel) → [Channel editor](#nav-a4) · OK on Channel (VFO) → [Save VFO as channel](#nav-a9) · OK on a row → [Value editor](#nav-a5) · OK on Tone → [Tone picker](#nav-a6) · idle 30 s → Home |
| <a id="nav-d2"></a>**D2** More | Home: hold MENU · [Screen options (hold MENU)](#nav-d4): 0 (full menu) · [Quick settings](#nav-d1): 0 / OK on More | OK on Recent → [Value editor](#nav-a5) · OK on Recent (a tone) → [Tone picker](#nav-a6) · 0 → [Status page](#nav-d6) · 1–9 / OK on a group → [Settings group / list](#nav-d3) · idle 30 s → Home |
| <a id="nav-d3"></a>**D3** Settings group / list | MENU 0 1–9 (advanced settings: a digit) · [More](#nav-d2): 1–9 / OK on a group · [Screen options (hold MENU)](#nav-d4): OK on Decoder settings / OK on APRS settings / OK on GPS settings · [Transmit refused](#nav-b7): OK (out of band) → MENU 0 9 4 / OK (out of band) → MENU 0 8 8 / OK (busy) → MENU 0 8 7 · [Zones](#nav-c11): SLOT · [Status page](#nav-d6): OK on Transmit / OK on Extend TX → MENU 0 8 / OK on Region → MENU 0 9 / OK on Broadcast → MENU 0 2 6 / OK on Clock → MENU 0 6 / OK on Bluetooth → MENU 0 9 2 / OK on VOX → MENU 0 8 2 / OK on Weather alerts → MENU 0 4 5 | digit · OK → the item: a value edited here, a list (›) or a screen (the MENU 0 tree) · digit / OK on 0 7 3 2 / digit / OK on 0 4 2 3 / digit / OK on 0 6 6 / digit / OK on 0 5 9 2 → [Text entry](#nav-a7) · digit / OK on 0 5 5 3 → [APRS message compose](#nav-a16) · digit / OK → [Frequency entry (VFO)](#nav-a1) · idle 30 s → Home |
| <a id="nav-d4"></a>**D4** Screen options (hold MENU) | Home: MENU / hold · [APRS heard](#nav-c3): hold MENU · [Channel browser: views](#nav-c8): hold MENU · [Waypoints](#nav-c14): hold MENU · [Go to waypoint](#nav-c15): hold MENU · [GPS position](#nav-c16): hold MENU · [GPS satellites](#nav-c17): hold MENU · [Event log (inbox)](#nav-c1): hold MENU · [Band scope](#nav-b10): hold MENU · [APRS station](#nav-c4): hold MENU · [Event detail](#nav-c2): hold MENU · [APRS message](#nav-c6): hold MENU · [HF mode](#nav-b12): hold MENU | 0 (full menu) → [More](#nav-d2) · OK on Recent → [HF recent](#nav-c18) · OK / OK on Write a message → [APRS message compose](#nav-a16) · OK / OK on Grid → [Text entry](#nav-a7) · OK → [APRS station](#nav-c4) · OK on MsgDelete / OK on Messages → [APRS messages](#nav-c5) · OK on Decoder settings / OK on APRS settings / OK on GPS settings → [Settings group / list](#nav-d3) · OK on Waypoints → [Waypoints](#nav-c14) · OK on Heard → [APRS heard](#nav-c3) · OK on Event log → [Event log (inbox)](#nav-c1) · OK on GPS position → [GPS position](#nav-c16) · OK → back · idle 30 s → Home |

#### Chapter 16 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-a6"></a>**A6** Tone picker | Home: hold 5 · [More](#nav-d2): OK on Recent (a tone) · [Channel editor](#nav-a4): OK on Tone · [Edit in place, VFO](#nav-a3): OK on Tone · [Quick settings](#nav-d1): OK on Tone | OK → back · idle 30 s → Home |

#### Chapter 7 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-a7"></a>**A7** Text entry | MENU digit / OK [0 7 3 2] · MENU digit / OK [0 4 2 3] · MENU digit / OK [0 6 6] · MENU digit / OK [0 5 9 2] · [Channel row actions](#nav-c10): OK on Rename · [Channel editor](#nav-a4): OK on Name · [Screen options (hold MENU)](#nav-d4): OK / OK on Grid · [Save VFO as channel](#nav-a9): OK on Name · [Add repeater](#nav-a10): OK on Name · [Range preset editor](#nav-a11): OK on Name · [Zone editor](#nav-a12): OK on Name | OK → back · idle 30 s → Home |
| <a id="nav-b4"></a>**B4** Shortcut map | MENU 0 9 1 3 | OK → Home |
| <a id="nav-d9"></a>**D9** Key test | MENU 0 9 1 2 | BACK and PTT are keys under test; only hold BACK leaves |

#### Chapter 28 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-a8"></a>**A8** Position entry | MENU 0 6 9 / 0 5 5 5 | BACK |
| <a id="nav-c14"></a>**C14** Waypoints | MENU 0 6 7 · [Screen options (hold MENU)](#nav-d4): OK on Waypoints | hold MENU → [Screen options (hold MENU)](#nav-d4) · OK → [Go to waypoint](#nav-c15) |
| <a id="nav-c15"></a>**C15** Go to waypoint | [Waypoints](#nav-c14): OK | hold MENU → [Screen options (hold MENU)](#nav-d4) |
| <a id="nav-c16"></a>**C16** GPS position | MENU 0 6 2 · [GPS satellites](#nav-c17): ◀▶ / OK · [Screen options (hold MENU)](#nav-d4): OK on GPS position · [Status page](#nav-d6): OK on GPS | hold MENU → [Screen options (hold MENU)](#nav-d4) · ◀▶ / OK → [GPS satellites](#nav-c17) |
| <a id="nav-c17"></a>**C17** GPS satellites | [GPS position](#nav-c16): ◀▶ / OK | hold MENU → [Screen options (hold MENU)](#nav-d4) · ◀▶ / OK → [GPS position](#nav-c16) |

#### Chapter 10 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-a10"></a>**A10** Add repeater | MENU 0 2 2 | OK on Name → [Text entry](#nav-a7) · OK on Frequency → [Frequency entry (VFO)](#nav-a1) · OK at the end → [Channel editor](#nav-a4) · OK → back |
| <a id="nav-a12"></a>**A12** Zone editor | [Zones](#nav-c11): SLOT on a zone | OK on Name → [Text entry](#nav-a7) · BACK / SLOT → [Zones](#nav-c11) |
| <a id="nav-c8"></a>**C8** Channel browser: views | MENU 0 2 1 · [Quick settings](#nav-d1): digit / OK · [Zones](#nav-c11): OK on Nearby | hold MENU → [Screen options (hold MENU)](#nav-d4) · OK on a view → [Channel list](#nav-c9) · OK → back · idle 30 s → Home |
| <a id="nav-c9"></a>**C9** Channel list | [Channel browser: views](#nav-c8): OK on a view | OK on a channel → [Channel row actions](#nav-c10) |
| <a id="nav-c10"></a>**C10** Channel row actions | [Channel list](#nav-c9): OK on a channel | OK on Edit → [Channel editor](#nav-a4) · OK on Rename → [Text entry](#nav-a7) · OK on Delete → [Confirm (shared)](#nav-a18) |
| <a id="nav-c11"></a>**C11** Zones | Home: hold V/M · MENU 0 2 3 · [Zone editor](#nav-a12): BACK / SLOT | OK on Nearby → [Channel browser: views](#nav-c8) · OK on a zone → Home · SLOT → [Settings group / list](#nav-d3) · \* (delete) → [Confirm (shared)](#nav-a18) · SLOT on a zone → [Zone editor](#nav-a12) · idle 30 s → Home |

#### Chapter 14 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-a11"></a>**A11** Range preset editor | [Range presets](#nav-c12): OK on a preset / # new | OK on Name → [Text entry](#nav-a7) · OK → [Frequency entry (VFO)](#nav-a1) |
| <a id="nav-b9"></a>**B9** Scan | Home: SIDE2 | any key if self.list / SIDE2 → Home · any key if self.list → [Save VFO as channel](#nav-a9) |
| <a id="nav-c12"></a>**C12** Range presets | MENU 0 1 4 | \* (delete) → [Confirm (shared)](#nav-a18) · OK on a preset / # new → [Range preset editor](#nav-a11) · idle 30 s → Home |
| <a id="nav-c13"></a>**C13** Skip list | MENU 0 1 5 | BACK |

#### Chapter 23 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-a13"></a>**A13** Location codes | MENU 0 4 5 2 | BACK |
| <a id="nav-b17"></a>**B17** Alert | an alert arrives: SAME header decoded (any screen) | OK once silenced / hold MENU → [Event log (inbox)](#nav-c1) |

#### Chapter 17 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-a14"></a>**A14** DTMF dialer | MENU 0 8 5 1 · [DTMF memories](#nav-a15): OK (a memory in the dialer) | BACK |
| <a id="nav-a15"></a>**A15** DTMF memories | MENU 0 8 5 2 | OK (a memory in the dialer) → [DTMF dialer](#nav-a14) |

#### Chapter 25 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-a16"></a>**A16** APRS message compose | MENU digit / OK [0 5 5 3] · [APRS station](#nav-c4): OK · [APRS message](#nav-c6): OK · [APRS messages](#nav-c5): # · [Screen options (hold MENU)](#nav-d4): OK / OK on Write a message | OK → back |
| <a id="nav-c3"></a>**C3** APRS heard | MENU 0 5 1 · [Screen options (hold MENU)](#nav-d4): OK on Heard | hold MENU → [Screen options (hold MENU)](#nav-d4) · OK → [APRS station](#nav-c4) |
| <a id="nav-c4"></a>**C4** APRS station | [APRS heard](#nav-c3): OK · [Screen options (hold MENU)](#nav-d4): OK | OK → [APRS message compose](#nav-a16) · hold MENU → [Screen options (hold MENU)](#nav-d4) |
| <a id="nav-c5"></a>**C5** APRS messages | MENU 0 5 2 · [Screen options (hold MENU)](#nav-d4): OK on MsgDelete / OK on Messages | OK → [APRS message](#nav-c6) · # → [APRS message compose](#nav-a16) |
| <a id="nav-c6"></a>**C6** APRS message | [APRS messages](#nav-c5): OK | OK → [APRS message compose](#nav-a16) · hold MENU → [Screen options (hold MENU)](#nav-d4) |

#### Chapter 34 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-a17"></a>**A17** PIN entry | MENU 0 9 3 3 (Change PIN) / ◀▶ on 0 9 3 1 (PIN lock: on with no PIN, or off) · [Quick settings](#nav-d1): ◀▶ / OK / knob on 0 9 3 / 0 9 3 1 · [Boot: self-test](#nav-d11): a PIN is set · hold # while locked, PIN to unlock (any screen) | OK → Home · *modal* at power on and at unlock: hold BACK ignored; BACK deletes a digit |

#### Chapter 4 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-a19"></a>**A19** Extend TX warning | MENU 0 8 8 4 (turning Extend TX on) · [Quick settings](#nav-d1): ◀▶ / OK / knob on 0 8 8 4 | OK → back |
| <a id="nav-a20"></a>**A20** Setup 1, Welcome | MENU 0 9 7 1 · [Boot: self-test](#nav-d11): first boot · [Reset](#nav-d14): OK, then hold # 3 s | OK → [Setup 2, Callsign](#nav-a21) · # skip the rest → [Setup 8, Summary](#nav-a27) · BACK: back (first page) |
| <a id="nav-a21"></a>**A21** Setup 2, Callsign | MENU 0 8 7 1 · [Transmit refused](#nav-b7): OK (no callsign) · [Setup 1, Welcome](#nav-a20): OK | OK → [Setup 3, Region, then Extend TX](#nav-a22) · BACK: the page before |
| <a id="nav-a22"></a>**A22** Setup 3, Region, then Extend TX | [Setup 2, Callsign](#nav-a21): OK | OK → [Setup 4, Owner card](#nav-a23) · BACK: the page before |
| <a id="nav-a23"></a>**A23** Setup 4, Owner card | [Setup 3, Region, then Extend TX](#nav-a22): OK | OK → [Setup 5, Time](#nav-a24) · BACK: the page before |
| <a id="nav-a24"></a>**A24** Setup 5, Time | [Setup 4, Owner card](#nav-a23): OK | OK → [Setup 6, Look](#nav-a25) · BACK: the page before |
| <a id="nav-a25"></a>**A25** Setup 6, Look | [Setup 5, Time](#nav-a24): OK | OK → [Setup 7, Battery Save](#nav-a26) · BACK: the page before |
| <a id="nav-a26"></a>**A26** Setup 7, Battery Save | [Setup 6, Look](#nav-a25): OK | OK → [Setup 8, Summary](#nav-a27) · BACK: the page before |
| <a id="nav-a27"></a>**A27** Setup 8, Summary | [Setup 7, Battery Save](#nav-a26): OK · [Setup 1, Welcome](#nav-a20): # skip the rest | OK / # finish → Home · BACK: the page before |

#### Chapter 24 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-b5"></a>**B5** Toast (overlay) | a message, decode or refusal (any screen) | an overlay for 3 s; keys go to the screen under it |
| <a id="nav-c1"></a>**C1** Event log (inbox) | MENU 0 4 1 · [Alert](#nav-b17): OK once silenced / hold MENU · [Screen options (hold MENU)](#nav-d4): OK on Event log · [Status page](#nav-d6): OK on Inbox | hold MENU → [Screen options (hold MENU)](#nav-d4) · OK → [Event detail](#nav-c2) |

#### Chapter 15 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-b6"></a>**B6** Transmit | PTT on any screen · [HF mode](#nav-b12): PTT (stays in HF mode) · [Transmit refused](#nav-b7): PTT again · [Emergency frequency](#nav-b8): PTT again | PTT up / TX timeout → back |
| <a id="nav-b7"></a>**B7** Transmit refused | PTT refused, any screen · [HF mode](#nav-b12): PTT, refused · [Emergency frequency](#nav-b8): PTT again | PTT again → [Transmit](#nav-b6) · PTT again → Home · PTT again → [Emergency frequency](#nav-b8) · OK (no callsign) → [Setup 2, Callsign](#nav-a21) · OK (out of band) → MENU 0 9 4 · OK (out of band) → MENU 0 8 8 · OK (busy) → MENU 0 8 7 · OK (not calibrated) → [Calibration (view only)](#nav-d8) · OK (receive-only channel) → [Channel editor](#nav-a4) · OK (battery) → [Status page](#nav-d6) · OK (TX locked) → [About (+ checks page)](#nav-d7) · OK (RelayMismatch) / OK (AmRxOnly) → [Value editor](#nav-a5) · OK → back |
| <a id="nav-b8"></a>**B8** Emergency frequency | PTT on 121.5, 243.0 or 406.0–406.1 MHz, any screen · [Transmit refused](#nav-b7): PTT again | PTT again → [Transmit refused](#nav-b7) · PTT again → [Transmit](#nav-b6) · 5 s without PTT → Home |

#### Chapter 21 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-b10"></a>**B10** Band scope | Home: hold 1 · MENU 0 3 1 6 | hold MENU → [Screen options (hold MENU)](#nav-d4) · OK (tune to the marker) → Home · digit → [Frequency entry (VFO)](#nav-a1) |

#### Chapter 20a (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-b12"></a>**B12** HF mode | MENU 0 3 3 · [Frequency entry (VFO)](#nav-a1): digit / * / OK · [Channel number entry](#nav-a2): digit / * / OK · [HF mode: SSB patch loading](#nav-b13): patch loaded | # → [HF recent](#nav-c18) · hold 9 → [Save VFO as channel](#nav-a9) · PTT, refused → [Transmit refused](#nav-b7) · PTT (stays in HF mode) → [Transmit](#nav-b6) · hold MENU → [Screen options (hold MENU)](#nav-d4) |
| <a id="nav-b13"></a>**B13** HF mode: SSB patch loading | MENU 0 3 3 (while the SSB patch loads) | patch loaded → [HF mode](#nav-b12) |
| <a id="nav-c18"></a>**C18** HF recent | [Screen options (hold MENU)](#nav-d4): OK on Recent · [HF mode](#nav-b12): # | OK → back · idle 30 s → Home |

#### Chapter 22 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-b14"></a>**B14** Tone search | MENU 0 3 5 | # · OK → back |
| <a id="nav-b15"></a>**B15** Frequency counter | Home: hold SIDE2 alone (KEY-22) · MENU 0 3 2 | OK (tune there) → Home |

#### Chapter 19 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-b18"></a>**B18** Crossband start | MENU 0 3 4 · [Crossband ready](#nav-b19): any key (stops) · [Crossband running](#nav-b20): any key (stops) | # start → [Crossband ready](#nav-b19) |
| <a id="nav-b19"></a>**B19** Crossband ready | [Crossband start](#nav-b18): # start · [Crossband running](#nav-b20): pass ends | a pass starts → [Crossband running](#nav-b20) · any key (stops) → [Crossband start](#nav-b18) |
| <a id="nav-b20"></a>**B20** Crossband running | [Crossband ready](#nav-b19): a pass starts | pass ends → [Crossband ready](#nav-b19) · any key (stops) → [Crossband start](#nav-b18) |

#### Chapter 12 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-b21"></a>**B21** Squelch (SIDE1 held) | Home: SIDE1 + ▲▼ or knob | SIDE1 released → Home |
| <a id="nav-d10"></a>**D10** Advanced squelch | MENU 0 9 9 1 | BACK |

#### Chapter 27 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-c2"></a>**C2** Event detail | [Event log (inbox)](#nav-c1): OK | hold MENU → [Screen options (hold MENU)](#nav-d4) |

#### Chapter 8 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-d6"></a>**D6** Status page | Home: # · [More](#nav-d2): 0 · [Transmit refused](#nav-b7): OK (battery) | OK on Transmit / OK on Extend TX → MENU 0 8 · OK on Region → MENU 0 9 · OK on Broadcast → MENU 0 2 6 · OK on Clock → MENU 0 6 · OK on Bluetooth → MENU 0 9 2 · OK on VOX → MENU 0 8 2 · OK on Weather alerts → MENU 0 4 5 · OK on Inbox → [Event log (inbox)](#nav-c1) · OK on Watch / OK on Battery Save → [Quick settings](#nav-d1) · OK on GPS → [GPS position](#nav-c16) · OK on Mailbox → [Mailbox](#nav-d24) · idle 30 s → Home |

#### Chapter 36 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-d7"></a>**D7** About (+ checks page) | MENU 0 9 8 · [Transmit refused](#nav-b7): OK (TX locked) | BACK |

#### Chapter 35 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-d8"></a>**D8** Calibration (view only) | MENU 0 9 9 2 · [Transmit refused](#nav-b7): OK (not calibrated) | BACK |

#### Chapter 5 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-d11"></a>**D11** Boot: self-test | power on | a check failed → [Boot: a check failed](#nav-d12) · first boot → [Setup 1, Welcome](#nav-a20) · a PIN is set → [PIN entry](#nav-a17) · checks passed → Home · boot screen = owner card (0 7 3 3) → [Boot: owner card](#nav-d13) · no keys |
| <a id="nav-d12"></a>**D12** Boot: a check failed | [Boot: self-test](#nav-d11): a check failed · [Boot: owner card](#nav-d13): a check failed | any key → Home |
| <a id="nav-d13"></a>**D13** Boot: owner card | [Boot: self-test](#nav-d11): boot screen = owner card (0 7 3 3) | a check failed → [Boot: a check failed](#nav-d12) · 4 s, or any key → Home |
| <a id="nav-d14"></a>**D14** Reset | MENU held at power on · MENU 0 9 7 2 | OK, then hold # 3 s → [Setup 1, Welcome](#nav-a20) · *modal* at power on: hold BACK ignored |
| <a id="nav-d22"></a>**D22** Power off | event: volume knob off | *modal*: no keys |

#### Chapter 3 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-d15"></a>**D15** SSB patch confirm | event: unknown SSB patch at boot | OK → back |
| <a id="nav-d16"></a>**D16** SSB patch status | MENU 0 9 6 | BACK |

#### Chapter 29 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-d17"></a>**D17** Link status | MENU 0 9 2 2 | BACK |
| <a id="nav-d21"></a>**D21** Link write progress | event: write session | *modal*: only BACK (cancel) |

#### Chapter 33 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-d23"></a>**D23** Empty battery | event: empty battery | *modal*: no keys |

#### Chapter 38 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-d24"></a>**D24** Mailbox | [Status page](#nav-d6): OK on Mailbox | BACK |

#### Chapter 30 (not in the manual)

| Screen | Get here | Go from here |
| --- | --- | --- |
| <a id="nav-d25"></a>**D25** Finish the update | another layout's data on the chip (or Console's first raw write) | BACK |
<!-- /nav:tables -->

**Not reachable yet:**

<!-- nav:unreachable -->
- **Placeholders** (the way in works, the "coming" screen opens): .
- **Built, hook, no event source yet**: D15 SSB patch confirm: App hook `ssb_patch_found`; the patch check at boot doesn't call it yet (sim F10); D21 Link write progress: App hook `link_write_progress`; the Link task doesn't exist yet (sim after F11); D22 Power off: App hook `power_off`; the volume switch isn't read yet (sim F8); D23 Empty battery: App hook `battery_empty`; the battery monitor doesn't call it yet (sim F9).
<!-- /nav:unreachable -->

Not in the tables yet (hand-kept until `docs/tools/navgraph.py` reads IDs with a letter suffix): **A16a** Quick messages, reached from APRS messages (C5): hold MENU, OK on Quick messages; OK edits one, # puts the factory text back (manual TEXT-7). Weather radio (B16) is still in the code, but the manual dropped its screen on Oct 6, 2026: the WX channels are a zone (WX-1).

**MENU 0, the advanced menu.** ▸ opens a screen, › a third-level list; the rest are values changed in the list.

![MENU 0 tree: every group and item of the advanced menu with its number](img/nav/menu0.svg)

