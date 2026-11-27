## 11. Quick settings and the menu

### What it's for

MENU opens the active slot's nine settings. MENU 0 opens everything else. Every item has a number path you can type straight through.

### Using it

**Quick settings** (MENU on home), always these nine:

| # | Item | # | Item |
| --- | --- | --- | --- |
| 1 | Squelch | 6 | Step (VFO only) |
| 2 | TX power | 7 | Watch |
| 3 | Mode | 8 | Channel (save, or edit) |
| 4 | Tones | 9 | Battery Save |
| 5 | Offset | 0 | More |

**More** (MENU 0, or hold MENU on home): a Recent row, then nine groups. MENU 0 0 opens the Status page. A group's last row, **Advanced**, holds the settings whose defaults are right for nearly everyone and that can take the radio away from its expected behaviour (MENU-32).

**Why the 0:** MENU's own digits 1–9 are the quick settings, so the 0 is quick settings' way into More and keeps the two numberings apart. Paths in this manual are written from MENU, for example MENU 0 7 3 3 (Boot screen), which works typed from any screen. On home, **hold MENU** opens advanced settings directly, so the short form is hold MENU, 7 3 3 (decided Oct 3, 2026: keep the two tiers as they are).

| Path | Group | Items |
| --- | --- | --- |
| 0 1 | Watch and scan | Watch, resume, priority check, range presets, skip list, Advanced (pause time, direction, scan inputs, return to) |
| 0 2 | Channels | Browse, add repeater, zones, channel display, Local zone, FM broadcast (its settings: step, AGC, radio monitor, sleep timer; decision 354) |
| 0 3 | Tools | Band scope, frequency counter, HF mode, crossband repeater, tone search (satellites after v1, ch 28a) |
| 0 4 | Decoders and alerts | Event log, POCSAG, DTMF decode, popups, weather alerts |
| 0 5 | APRS | Heard, messages, APRS mode, frequency, my station, beacon, digipeat, KISS TNC, Advanced (path, TX delay, TX level, FX.25, mute speaker) |
| 0 6 | GPS and time | GPS, position, coordinate format, units, time zone, clock, waypoints, GPS during RX/TX, fixed position |
| 0 7 | Display, sound, power | Theme, home layout, display, backlight, sounds, LEDs, Battery Save, auto power off, menu timeout |
| 0 8 | Transmit | Timeout, VOX, mic gain, end tone, DTMF, callsign and ID, busy lockout default, Advanced (subtone level, tail elimination, Extend TX, Dry TX) |
| 0 9 | System | Keys and lock, connections, PIN and lock, region, squelch tail, SSB patch, setup and reset, about, Advanced (advanced squelch, discriminator, calibration and trims, debug console, cable log, terminal colour) |

Every value is in Appendix A.

**On every settings screen:** ▲▼ move; the knob (or ◀▶) changes the value live; OK opens a bigger editor; # resets to default; \* undoes for 5 s; BACK goes back one level; PTT keeps the change and goes home.

**Other screens** have their own options: **hold MENU** (a short press is the screen's OK; 0 there opens the full menu; MENU-25):

| Screen | Hold MENU offers |
| --- | --- |
| Band scope | The scope settings, 0 3 1 (bars, step, sweep speed, trigger, waterfall) |
| FM broadcast | Step, AGC, radio monitor, presets |
| HF mode | Step, bandwidth, AGC, LNA, fine tune (BFO), recent list |
| APRS heard, the APRS card | Beacon now (APRS-17), messages, clear the heard list, APRS settings |
| APRS messages | Write a message, quick messages (TEXT-7), APRS settings |
| Channel lists | Show hidden (CHAN-24) |
| Event log | Mark all read, clear the log, decoder settings |
| GPS position, waypoints | Mark here, waypoints or GPS position, GPS settings |

**The APRS slot's quick page:** **hold ABC** on the APRS slot opens its most-used APRS settings as a grid, the way hold ABC on any other slot opens the slot's settings (EDIT-1): arrows pick, the knob changes, OK opens the bigger editor, # resets, BACK or ABC leaves. The help box names each setting's menu path (MENU-34):

APRS mode, beacon, power, frequency, path, digipeat, beacon text ("Bcn text", the comment, typed in T9 by default, TEXT-10), its text rate (APRS-50.1) and symbol: the same page whatever holds C (APRS mode or KISS).

**Task flows** for rare jobs, inside the tree: add a repeater, set up weather alerts, add a Bluetooth device, setup.

### Screens

| | | |
| --- | --- | --- |
| ![Quick settings](img/screens/MenuQuick.png) | ![More](img/screens/MenuTop.png) | ![A group](img/screens/MenuGroup.png) |
| MENU | MENU 0 | MENU 0 5 |
| ![Editing a value](img/screens/MenuEdit.png) | ![Quick settings, daylight](img/screens/MenuQuickDay.png) | |
| MENU 1, OK | MENU, daylight theme | |

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| 0 7 9 | Menu timeout | Off, 10, 20, 30, 45, 60 s | 30 s |

> **Spec: structure**
>
> - **MENU-1** MENU on home opens quick settings: nine fixed rows for the active slot, in the order above; 0 opens advanced. On the APRS slot it opens the APRS page instead (APRS-17.3), where 0 opens advanced too.
> - **MENU-2** MENU 0 (or hold MENU on home) opens More, the full menu: a Recent row and nine groups. MENU 0 0 opens Status.
> - **MENU-3** At most 9 items per list, each list on one screen; a group may have a third level, nothing deeper.
> - **MENU-4** Groups are named by what you're doing, never by chip or module.
> - **MENU-5** Digits always pick. A path typed at full speed lands where it would typed slowly.
> - **MENU-6** A number means one thing everywhere in a release, whatever the mode, slot or screen; numbers may change between releases.
>     - **MENU-6.1** Until 1.0.0, menu numbers move freely: a dropped item's number doesn't stay empty, and the rest close up (0.8.x is the limited alpha, 0.9.x the first public release). From 1.0.0, existing numbers stay put until 2.0; a 2.0 alpha or dev build may reorganise them again (and 2.0's notes list the moves). A new item may take a free number at any time; reorganising existing ones may not.
> - **MENU-7** One English name per item, shared by menu, status bar, manual and web app, from one table.
> - **MENU-8** Recent shows the last 3 settings changed, in a fixed place; lists never reorder (it was 5).
> - **MENU-9** No profiles.
> - **MENU-10** Task flows live inside the tree and end on the normal settings page.
> - **MENU-11** Squelch, power, volume, scan and monitor are never only in a menu.

> **Spec: rows and editing**
>
> - **MENU-12** Every row shows its number, full name and value; a dot marks a non-default value.
>     - **MENU-12.1** A group's row shows a live value: its first setting's (0 3 1 Scope, 0 4 5 SAME, 0 7 3 Display, 0 7 4, 0 7 5 Sounds, 0 8 2), 0 8 5 DTMF its tone speed, 0 1 5 the skip count ("Empty" when none); never the menu table's fixed text. (ferrite#135)
> - **MENU-13** Quick rows say whether the value belongs to this channel or the VFO.
> - **MENU-14** An item that doesn't apply stays visible and greyed; selecting it says why (e.g. "VFO only").
> - **MENU-15** A one-line help for the highlighted item sits at the foot, with its path.
> - **MENU-16** ▲▼ move; the knob changes the highlighted value live, with no edit step; ◀▶ change it one step. Every hint bar names the knob.
> - **MENU-17** OK opens items that need room (tone list, squelch with its meter); inside, knob or ◀▶ change, digits type, \* is the point.
> - **MENU-18** # resets the highlighted value to its default.
> - **MENU-19** A change takes effect as soon as it is made; only the destructive actions of MENU-23 wait for a confirm.
> - **MENU-20** BACK leaves an edit and restores the old value; OK keeps it; PTT keeps it and goes home.
> - **MENU-21** Changes save within 2.5 s (2 s after the last change, looked for every 500 ms: PWR-26.14), power-cut safe. No save step, no pending state.
> - **MENU-22** After a change, the hint bar offers "\* Undo" for 5 s.
> - **MENU-23** Only destructive actions confirm (delete channel or zone, reset), naming what goes.

> **Spec: moving around**
>
> - **MENU-24** BACK goes back one level (KEY-5) and keeps your place there, whichever way you came (quick settings, MENU 0, the Status page); hold BACK goes home; each group remembers its last item while you are in the menu: back in it from MENU 0 (or its parent group) it opens there; going home forgets, so the next visit starts on row 1, as the number paths do. A group opened to a setting (a Status page row, a shortcut) opens on that setting.
> - **MENU-25** Hold MENU on any other screen opens that screen's own options, one page style everywhere (numbered rows, 0 the full menu); a screen without options says "No options here". As in the menus (MENU-5), a digit picks its row, and a row that opens a screen opens it; a row that does something (send, clear, toggle) waits for OK.
> - **MENU-26** A highlighted signal with a frequency (scope peak, decoder log) offers "Go" to tune it. APRS stations have no Go: they share one frequency, and OK opens the station instead.
> - **MENU-27** Dropped (Oct 4, 2026): the help box under every list already shows the item's number path (MENU-15), so no separate tip screen (D5).
> - **MENU-28** An idle menu returns home after the menu timeout (0 7 9: Off, 10, 20, 30, 45 or 60 s; 30 s by default). Off keeps menus up until left. Other screens keep their own timeouts (EDIT-6).
> - **MENU-29** The menu never interrupts the radio: audio, squelch, scan, watch and decoders keep running.
> - **MENU-30** While transmitting, MENU does nothing.
> - **MENU-31** A setting that holds a frequency (0 5 4 the APRS frequency, 0 4 2 3 the pager frequency, a range preset's start and end) opens one shared frequency entry box on OK (or its digit): home's entry (digits, \* the point, OK or a whole frequency keeps it, BACK deletes, then leaves), headed with the setting, showing its value now and what it takes. A frequency outside the setting's range is refused with a toast saying why, the digits kept to fix: APRS 64-300 MHz on 5 kHz steps, pagers 136-520 MHz, range edges 18-1300 MHz with the start under the end and never across 18 or 64 MHz (SCAN-14). The knob still steps the value on its row. The terminal's `set` takes the same settings in MHz with the same checks (TERM-12).
> - **MENU-32** Each settings group whose settings include ones that can take the radio away from its expected behaviour ends with an **Advanced** row: those settings, one list, with defaults that are right for nearly everyone. The rest of the group is what owners change. A group with none has no Advanced row. The full menu itself (MENU 0, hold MENU) is **More**.
> - **MENU-33** A row stays out of the menu until its feature is built: no row says only "setting comes next". Background job (WATCH-13 – WATCH-15), Scan target (SCAN-2) and the Nearby sort (CHAN-15) left the menu with decision 256, until they are judged worth building; the rows after them closed up (MENU-6.1).
> - **MENU-34** Hold ABC on the APRS slot opens its quick page: nine APRS settings as a 3 x 3 grid (APRS mode, beacon, power, frequency, path, digipeat, "Bcn text" the beacon comment, text rate, symbol), as hold ABC on another slot opens the slot's (EDIT-1). It is the same page whatever holds C: APRS mode or KISS. Each cell is a menu setting by its path, with the menu's values, steps, greying and reset: the arrows pick (stopping at the grid's edges), a digit picks a cell (MENU-5), the knob changes the value at once (MENU-16, MENU-19, with "\* Undo", MENU-22), OK opens what the menu row opens (MENU-17, MENU-31), # resets (MENU-18), BACK or ABC returns home. A value too long for its cell is cut at a word break, and the help box shows it whole while the cell is picked; otherwise the help box has the setting's help line, or why it is greyed (MENU-14), with its path. Idle, it goes home after the menu timeout (MENU-28). Other screens have no quick page. Alex, Nov 12, 2026 (decision 378).

### Under the hood


### Status

Mock-ups approved (0b). Quick settings in 2a; advanced settings, type-ahead and editing in 2b. Done when all MENU rules pass in the simulator.


### Settled details

- No breadcrumb header: menus keep the mock-ups' design, the screen name in the status bar and the number path in the help line (decided Oct 7, 2026; the old plan's rule 7 wanted "Menu › 5 APRS › 2 Messages").
- The help line is always on; there is no setting (decided Oct 6, 2026).
- MENU 0 stays a numbered list, as the mock-ups; no icon grid (decided Oct 7, 2026).
- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - MENU-8: decided Oct 6, 2026.
  - MENU-26: decided Oct 6, 2026.
  - MENU-31: decided Oct 15, 2026 (user, decision 182): 0 5 4 could only be stepped 5 kHz at a time by the knob, and the terminal couldn't set it. (MENU-27, dropped Oct 4, keeps its number.)
  - MENU-33: decided Oct 22, 2026 (user, decision 256, from the user guide review): "hide for now, we need to eval if these features are needed... or just noise/extra junk". Resume 0 1 4 → 0 1 2, priority check 0 1 5 → 0 1 3, range presets 0 1 6 → 0 1 4, skip list 0 1 7 → 0 1 5, Advanced 0 1 8 → 0 1 6, channel display 0 2 5 → 0 2 4.
  - MENU-25: changed Oct 22, 2026 (decision 257): a digit on an options page opens a row that opens a screen, so reading a message from the APRS slot is OK 1 (it only moved the highlight).
  - MENU-6.1: changed Oct 22, 2026 (user, decision 259): numbers move freely until 1.0.0, not the first public release (0.9); after that only a 2.0 alpha or dev build reorganises them, and new items may take free numbers at any time.
  - MENU-1: changed Oct 15, 2026 (decision 181): on the APRS slot, MENU opens the APRS page (APRS-17.3), its quick-settings rows being fixed there.
  - MENU-24: changed Oct 14, 2026 (decision 153): the last item is kept for the visit to the menu, and a link to a setting opens on it.

### Open points

- Validation with owners (card sort, tree test) is not done.

---

