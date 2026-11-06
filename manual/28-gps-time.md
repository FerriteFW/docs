## 28. GPS, time and waypoints

### What it's for

The GPS gives position, UTC time and speed to the clock, APRS, the Nearby channel view and the waypoint store. Waypoints show distance and a compass arrow to places you've stored.

### Using it

| To | Do |
| --- | --- |
| See the fix | MENU 0 6 2: the fix, satellites and accuracy on one line; latitude and longitude large; grid square, altitude, speed, course, local time and UTC; the nearest waypoint at the foot |
| See the satellites | ◀▶ on the GPS screen: a sky plot (where each satellite is) and a signal bar for each |
| GPS screen options | Hold MENU on the GPS screen: mark here, waypoints, GPS settings |
| Mark where you are | MENU 0 6 7, mark here |
| Go to a waypoint | MENU 0 6 7, pick one: a dial that turns course up while you move, the distance large, bearing and ETA |
| Set the clock by hand | MENU 0 6 6 (with no GPS time) |
| Use a fixed position | MENU 0 6 9 (used when there's no fix) |

The status bar shows a satellite while GPS is on: outline while searching, solid with a fix from the last 3 minutes. With GPS on the module isn't left running: it sleeps between fixes and wakes once a minute, before each timed APRS beacon, and at once when you open a GPS screen; Status (#) shows "Fix · sleep 42 s" while it sleeps. The clock reads `14:32`, `Z` for UTC, `--:--` with no time source. Setup suggests the time zone from the fix.

### Screens

| | |
| --- | --- |
| ![GPS position](img/screens/GpsPosition.png) | ![GPS position, moving](img/screens/GpsPositionMoving.png) |
| Position (MENU 0 6 2) | Moving: speed and course |
| ![GPS satellites](img/screens/GpsSatellites.png) | ![Go to, course up](img/screens/GpsGoTo.png) |
| Satellites (◀▶): sky plot and signals | Go to a waypoint while moving: course up, ETA |

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| 0 6 1 | GPS | Off, auto, on | Auto |
| 0 6 3 | Coordinate format | Decimal, DDM, DMS, Grid square | DDM |
| 0 6 4 | Units | Metric, imperial, nautical | Metric |
| 0 6 5 | Time zone | UTC−12 to +14, with 30 and 45 min offsets | UTC |
| 0 6 6 | Clock | 24 h, 12 h; from GPS on, off; set manually | 24 h, from GPS |
| 0 6 7 | Waypoints | List, mark here; arrival alarm off, 50 m–1 km | Alarm off |
| 0 6 8 | GPS during RX/TX | Always on, off while receiving a signal, off while transmitting, both | Always on |
| 0 6 9 | Fixed position | Latitude, longitude, altitude | None |
| 0 7 5 4 | Arrival tone | Off, on (with Sounds, chapter 32) | On |

> **Spec: GPS**
>
> - **GPS-1** GPS off, auto or on (decision 268).
>     - **GPS-1.1** Off powers the module down (PA8), as stock.
>     - **GPS-1.2** On, the power manager runs it (GPS-26).
>     - **GPS-1.3** The GPS task parses NMEA only while it's powered.
>     - **GPS-1.4** Auto by default (decision 268; it was Off, decision 235: searching costs about 12 mA, some 15 % of standby, power bench Oct 21, 2026). Auto costs nothing until a feature needs a position. A radio keeps the setting it has: one set to Off or On stays so.
>     - **GPS-1.5** Auto (decision 268) powers the module only while something needs a position, and keeps it off (PA8, as Off) the rest of the time. The needs: (a) APRS mode on with position beacons and no fixed position (GPS-3); (b) a GPS screen open (position, satellites, waypoints, go to a waypoint); (c) going to a waypoint, or its arrival alarm armed (a stored waypoint alone is not a need); (d) the clock from GPS (0 6 6): one fix after power-on, then nothing more for the clock. While powered the power manager runs it as On does (GPS-26 – GPS-33: standby between wakes, the wake before a timed beacon, running while moving). When the last need ends the module powers off a minute later (a screen closed and opened again doesn't cycle it). In Low Power Mode GPS is off whatever the setting (PWR-24.4), so a power-on in the mode takes no clock fix, and it isn't taken on leaving. The first fix after the module was off may be a cold start (whether its backup supply keeps the ephemeris with PA8 off is a GPS-31 bench check). The status-bar icon (GPS-6) shows while the module is powered.
> - **GPS-2** Every fix records satellites, HDOP and its age; the last fix is kept with its age while the module sleeps; consumers see the age and never treat a stale fix as current. The position screen shows accuracy as "±N m" (HDOP × 5 m), not the raw HDOP.
> - **GPS-3** With no fix, position users (APRS, Nearby) take the fixed position, or none.
> - **GPS-4** GPS during RX/TX powers the module off for the chosen cases and back on after.
> - **GPS-5** While transmitting, PB10 (USART3 TX) is driven low and restored after, as stock does.
> - **GPS-6** The status-bar icon shows only with GPS on (in Auto, while the module is powered, GPS-1.5): outline searching, solid with a fix from the last 3 minutes (GPS-25), not merely while the module runs.
> - **GPS-14** GPS during RX/TX.
>     - **GPS-14.1** GPS during RX/TX defaults to Always on: the module isn't powered off while receiving and transmitting. Revisit after the bench noise measurement.
>     - **GPS-14.2** The power manager still puts it in standby between fixes then (GPS-26).
> - **GPS-15** The position page (MENU 0 6 2).
>     - **GPS-15.1** A status line with the fix type, satellites used of those in view and the accuracy (GPS-2), the fix's age at the right (amber past 10 s).
>     - **GPS-15.2** Latitude and longitude large in the 0 6 3 format (decimal degrees, degrees and minutes, or degrees, minutes and seconds; with Grid square, the square large and degrees and minutes small under it).
>     - **GPS-15.3** Six tiles: grid square, altitude, speed, course, local time (the radio's clock, as the status bar shows it) and UTC.
>     - **GPS-15.4** The nearest waypoint with its distance, cardinal and a bearing arrow at the foot.
>     - **GPS-15.5** 0 6 3's choices are named Decimal, DDM (degrees and decimal minutes, the default), DMS and Grid square, and every position follows it with the same symbols: the GPS page in full ("45°25.290' N"), a station, a waypoint and the log on one line ("45°25.290'N 75°41.832'W", DMS to the whole second), the position editor's templates. A grid square is always six characters, the subsquare in lower case ("FN03gp").
> - **GPS-16** Altitude, speed and distance follow Units (0 6 4) on every GPS page: metric m, km/h, m and km; imperial ft, mph, ft under 0.1 mi then mi; nautical m, kn, nmi with two decimals under 10.
> - **GPS-17** Course reads "stopped" below 3 km/h: the radio has no magnetic compass, so the course comes from movement and is noise at rest.
> - **GPS-18** The satellites page (◀▶ from the position page): a sky plot, north up, with rings at the horizon, 30° and 60° of elevation, each satellite at its azimuth and elevation (from GSV) with its number, used ones filled (blue GPS, violet BeiDou) and the rest outlined; under it a signal bar for each (dB-Hz, 50 fills).
> - **GPS-19** Go to a waypoint: the dial turns course up while moving at 3 km/h or more (a tick marks ahead, N moves round the ring) and is north up when stopped; the arrow points to the waypoint; the distance large in the chosen units, then the bearing and, while moving, the ETA at the present speed.

> **Spec: GPS power**
>
> - **GPS-26** With GPS on, the module is managed, not left running: it wakes once a minute until a fix, then goes into standby with `$PCAS12,N` (CASIC protocol 2.7.11: VCC kept, so the wake is a hot start; it wakes itself N seconds later), N the seconds to the next planned wake. NMEA still coming 2 s after the command isn't taken for a wake: the cable log says "gps: standby ignored: NMEA still coming" and the plan holds to the standby's end, so a module that won't sleep is sent one standby per planned wake, not one per fix (decision 143). Status's GPS row ("Fix · sleep 42 s") and the terminal's "Radio now" ("GPS fix, standby 42 s") show it; the cable log has a line for each standby, wake and power cycle, each sentence sent to the module as its bytes ("gps: > $PCAS12,60*28<CR><LF> (15 bytes)"), and the 5 s sentence counts through standbys too (0 while asleep).
> - **GPS-27** With APRS mode on and a timed beacon, the module wakes 30 s before each beacon and stays on until it has gone; the minute wakes go on between beacons.
> - **GPS-28** A GPS screen open (position, satellites, waypoints, go to) or the arrival alarm armed keeps the module running. Smart and distance beaconing keep it running while moving (3 km/h or more, SmartBeaconing's slow speed) and hand back to the wakes 3 minutes after the last movement. The clock has no wakes of its own: any fix sets it (GPS-7).
> - **GPS-29** Ephemeris refresh: the first fix after power-on, and then about every 30 minutes a wake, stays on 60 s after its fix, since short hot fixes don't download a full ephemeris.
> - **GPS-30** Without sky: a wake with no fix within 2 minutes goes into standby for 1, 2, 4, 8, then 15 minutes at most before the next; any fix resets it to once a minute. A timed beacon's wake still comes 30 s before it.
> - **GPS-31** A need that comes during standby (a GPS screen opened, a beacon moved sooner) sends a wake byte (CR LF) on USART3; with no NMEA within 3 s, PA8 power-cycles the module (0.5 s off; a cold start unless its backup supply holds the ephemeris). A module that should have woken itself and stays silent 5 s gets the same cycle, once until it is heard again. Which wake works is to confirm on the radio. Note (Oct 13, 2026, decision 147): the ATGM336H (HW=ATGM336H,0006032723090) answers `gps query 1`, so PB10 reaches it, but ignored `$PCAS12,40*2A` (GGA every second on); TERM-36's `gps nmea off` and `gps standby N quiet` test whether it takes CAS12 with its NMEA off, as other AT6558 users found, before this rule's wakes can be confirmed.
> - **GPS-32** Nothing is sent to the module while keyed (PB10 is held low then, GPS-22): a standby, wake byte or power cycle due then waits for the unkey. A wake the module times itself during a transmission just happens (GPS-14).
> - **GPS-33** A beacon never carries a fix older than its interval as current: an automatic beacon then waits up to 2 minutes for a fresh fix (the module's wake comes for it), and if none comes it is skipped with a "Beacon not sent" toast and an event-log entry ("fix too old" or "no position"), the next coming by the schedule. Beacon now without a current fix is refused at once. The fixed position (GPS-3) stands in as itself.
> - **GPS-34** Ferrite sets the module's NMEA output itself, cut to the sentences its parser reads.
>     - **GPS-34.1** Ferrite sets the module's NMEA output itself, so the MCU receives and parses about a third of what the module sends by its own settings: `$PCAS03,1,0,5,5,1,0,0,0*02` (CASIC 2.7.4, fields GGA, GLL, GSA, GSV, RMC, VTG, ZDA, ANT: GGA and RMC every fix, GSA and GSV every 5th, GLL, VTG, ZDA and the antenna TXT off; the fields after ANT, off by default, left as they are), sent once the module is heard after each power-up and power cycle. GSA stays because the fix's 2D/3D and the sky plot's filled (used) satellites come from it.
>     - **GPS-34.2** It is sent again after each wake from standby (its settings live in its RAM).
>     - **GPS-34.3** `$PCAS03,1,0,1,1,1,0,0,0*02` (GSA and GSV every fix too) while the GPS position or satellites page is open, the two that show satellites in view (the waypoint pages don't): sent as those pages open and close while it is awake (asleep, its next wake gets the right one).
>     - **GPS-34.4** Nothing is sent while keyed (GPS-32: the next look sends it) or while the terminal's bench test holds the module (TERM-36).
>     - **GPS-34.5** A GLL, VTG or ZDA still coming 2 s or more after it means the module didn't take it: it is sent again, three times a wake at most (cable log "gps: NMEA set not taken"). Each is in the cable log as its bytes ("gps: > $PCAS03,..."). Never `$PCAS00` (save to the module's flash) or `$PCAS01` (its baud rate).
>     - **GPS-34.6** GGA still comes every second, so the power manager's wakes, standbys and silence checks read as before (GPS-26, GPS-31).
> - **GPS-38** Retired (decision 365): each module power-up sent a CASIC AID-INI with the last fix's position and GPS time, to shorten the search. On black under a skylight it made the first fix slower, not faster (136 and 92 s without it, 190 and 445 s with it), though the message and the time in it were right; the module starts on its own.
> - **GPS-35** The fixed-position editor's fifth row, From GPS, shows the fix ("3D fix", "2D fix" or "No fix"); OK keeps the current fix's position and altitude as the fixed position. Without a real fix (none, or the fixed position standing in) it toasts "No GPS fix" and changes nothing.
> - **GPS-36** "Use as fixed position" in the waypoints' options makes the selected waypoint the fixed position (0 6 9, its altitude unknown), with a toast "Fixed position set" and, with 0 5 5 4 on GPS, "used when there's no fix".

> **Spec: time**
>
> - **GPS-7** With "from GPS" on, a fix sets the clock to UTC; local time adds the time zone.
> - **GPS-8** With no time source the status bar shows the callsign in the clock's place (SBAR-2), `Z` when showing UTC; Status names the clock source.
> - **GPS-9** Retired (decision 92): setup doesn't suggest a time zone from the fix; the clock stays UTC until you set the zone (decision 71), because a guess from longitude is wrong near zone edges and knows nothing of daylight saving.

> **Spec: waypoints**
>
> - **GPS-10** Up to 2,032 waypoints, 32 B each (name 16, position, source: marked, APRS, link, grid), in SPI flash at 0x080000 (16 sectors of 127; decision 333), newest first. Deleting one moves the later ones down (a power cut part way can leave one twice, never lose one).
> - **GPS-11** The waypoint list shows distance and bearing from the current fix; the selected one gets a compass arrow.
> - **GPS-12** The arrival alarm fires once when the fix comes within the set radius: a toast with the waypoint's name and distance, an event log entry, and a tone when Arrival tone (0 7 5 4) is on.
> - **GPS-24** The arrival alarm watches the waypoint being gone to: the one the Go to page shows, kept after leaving the page until another is opened there. Its radius is "Arrival alarm" in the waypoints' options (hold MENU on the list): off, 50, 100, 200, 500 m, 1 km, each OK the next, with a toast naming it; off by default. It fires once and is armed again only after the fix has been more than twice the radius away. The log entry's source is GPS ("Waypoint arrival": the waypoint, "Arrived, N m").
> - **GPS-25** The last fix is kept while the module sleeps or searches again, and is current for 3 minutes after the module last reported it, its age shown (the position page's age turns amber past 10 s, GPS-15): after that the status bar shows searching, and Nearby and APRS take the fixed position (GPS-3). GPS off drops it. Off around signals (GPS-4), the module comes back 2 s after the last signal, so a run of short signals doesn't power-cycle it, and the last fix stays (built with roadmap 5a).
> - **GPS-13** The link reads and writes the waypoints: `READ_MANY` and `WRITE_MANY` of waypoints, by their place in the list, replaced, added or deleted (LINK-55).
> - **GPS-21** A grid square can be typed where a position is taken: the fixed position's fourth row (MENU 0 6 9; OK types it) and "Add a grid square" in the waypoints' options. 4 or 6 characters, capitals and digits with multi-tap as a callsign is typed (\* switches); the position is the square's centre, and a waypoint is named with the square. Anything else is refused and stays to be fixed.
> - **GPS-22** While keyed, PB10 (USART3 TX to the GPS) is driven low and returned to the UART after unkey, as stock does (0x080252D8 / 0x0802530C); the GPS task owns the pin and the Radio task asks for it. As stock's PTT press (0x0801C6D4), the Radio task drives it low itself once a key-up's checks pass, before the key-up; the GPS task's next look keeps it low, or hands it back if the key-up was refused (decision 130).
> - **GPS-23** The clock isn't kept across power-off: it comes from GPS, or from a manual set after each power-on. OK on 0 6 6 types the date and time as 12 digits, YYYYMMDDhhmm, in local time (0 6 2's zone); a date that doesn't exist is refused. It runs from then; with 0 6 6's "from GPS" on, GPS time takes over at the next fix.
> - **GPS-37** The clock keeps running without a fix while the radio is on (GPS-23), and learns its own drift: each time a fix sets it, the difference from GPS time over the time since the last fix gives the crystal's error in ppm, smoothed over several fixes and kept with the user trims (so it survives a restart); between fixes the clock runs corrected by it, so a week without sky stays within about a second (Alex, Oct 31: "we may drift a bit... but we should be able to adjust fairly quickly, that will let the arms work without sat data"). A fix more than 2 s from the corrected clock says nothing about drift when it follows a manual set or a restart, and is used only to set the clock. Changing the core clock (dynamic clocking, PWR-26) loses no time.
> - **GPS-20** # on an APRS station screen saves the station's last position as a waypoint named with its callsign, source APRS, with a toast "CALL saved as a waypoint"; a station with no position is refused with "CALL has no position".

### Under the hood


### Status

Ferrite's NMEA set (GPS-34, decision 158) built Oct 14, 2026, host-tested and in the simulator, not yet run on a radio: bench checks are that the module takes `$PCAS03` with its NMEA running (no "gps: NMEA set not taken") and the cable log's 5 s counts drop.

The GPS power manager (GPS-26 – GPS-33, decision 110) built Oct 13, 2026, host-tested and in the simulator (a fake module with fix delays, standby and an indoor mode), not yet run on a radio. Bench checks: that `$PCAS12,N` puts the module in standby and it wakes itself N s later (the cable log's "gps: standby" and "gps: awake" lines, NMEA stopping and coming back); whether the wake byte ends standby early or the PA8 fallback is what runs ("gps: no NMEA after a wake: power cycled"); time to a fix after standby and after a power cycle; the current through a run of wakes; whether PB10 held low while keyed wakes a sleeping module.

Position entry (A8) built Oct 4, 2026: the fixed position in the 0 6 3 format (Grid square is typed as degrees and minutes), kept in settings with the format (simulator shot `position-entry`). The GPS pages (GPS-15 – GPS-19) are built in the simulator (Oct 7, 2026; shots `gps-position`, `gps-position-moving`, `gps-satellites`, `waypoint-go-moving`); the GPS task's parser keeps each satellite's elevation and azimuth from GSV for the sky plot (5a, below). The rest is built in roadmap 5a; done when fix, time, coordinate formats, fixed position, waypoints, arrival alarm and GPS off during RX/TX work on the radio.


### Settled details

- no. PC14 and PC15 (the 32 kHz crystal pins) are the green LED and a detect input, so there is no RTC crystal; stock and nicFW keep no time across power-off either. The clock comes from GPS, or is set by hand each power-on (GPS-23).
- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - GPS-8: changed Oct 15, 2026 (decision 183): the callsign, not `--:--`, with no time (SBAR-2).
  - GPS-2: changed Oct 3, 2026; the last fix kept with its age while the module sleeps, Oct 13, 2026 (decision 110).
  - GPS-1, GPS-6, GPS-14: changed Oct 13, 2026 for the power manager (decision 110): on means managed; the icon solid for a recent fix, not a running module.
  - GPS-25: changed Oct 13, 2026 (decision 110): current for 3 minutes, not 10 s, so the minute wakes don't flicker the icon or drop the position between fixes.
  - GPS-26 – GPS-33: decided Oct 12, 2026 (user, `research/gps-power.md`), built Oct 13, 2026. Stock keeps the module running whenever GPS is on.
  - GPS-34: decided and built Oct 14, 2026 (user, decision 158). A deliberate deviation from stock: V0.27 sends `$PCAS03,5,0,0,0,0,3,7,60*35` (0x0800CDE0) right after powering the module (0x08016BCC clears PA8, then 0x08016BF0 calls it) and again each time its parser takes a TXT sentence (0x0801C2C8; its type table at 0x0805BC72 is GGA, VTG, ZDA, TXT, so the module's start-up text brings it again), never from a menu. That asks GGA every 5th fix, VTG every 3rd and ZDA every 7th (what stock's parser reads) and turns RMC and GSV off, which Ferrite needs for the date and the sky plot.
  - GPS-36: decision 226 (Oct 21, 2026; from the nicFW comparison).
  - GPS-35: decision 208 (Oct 20, 2026, Alex: "if you get a lock you can commit that lock to the fixed position").
  - GPS-15: decided Oct 7, 2026.
  - GPS-12: decided Oct 6, 2026.
  - GPS-24: decided Oct 7, 2026, built with roadmap 5a.
  - GPS-21: decided Oct 7, 2026; nicFW takes a grid as a target or position.
  - GPS-23: no RTC crystal on this board.
  - GPS-20: decided Oct 7, 2026.

### Open points

- Why stock holds PB10 low while keyed (GPS-22 copies it): for the bench.
- CAS12 standby on the radio (GPS-31): whether a UART byte ends it early, whether it keeps the ephemeris (hot wakes), its current, and whether the module's backup supply (V_BCKP) survives PA8 off: for the bench. If standby loses the ephemeris, standby gives way to power-off and the wakes stretch (`research/gps-power.md`, rule 6).

---

