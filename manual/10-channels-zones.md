## 10. Channels, zones and the home channel

### What it's for

Up to 4,000 stored channels in up to 512 zones of 256 channels each. Each channel sits in one zone (a folder) or none. One of them is the home channel you always come back to.

### Using it

**On home, channel mode** (V/M): knob or ▲▼ step channels in the zone, in number order; ◀▶ step zones; SIDE2 + knob steps 10; digits type a number (entry shows its name, or "empty").

**Edit a channel:** hold SLOT. Zone, name and frequency at the top; below, mode, RX tone, tone, offset, power, squelch, busy lock, scan (in scans, Skip or Priority, CHAN-24), APRS, RX only, number and Home; Hidden is the list's Hide. Changing zone or number moves the channel. The terminal's editor and `ch` change the same fields by the same rules (CHAN-32).

**Home channel:** set the Home cell on a channel (it clears the old one). Hold 0 jumps to it from VFO or any zone.

**Channel browser** (MENU 0 2 1): pick a zone or a view; row actions are edit, rename, move, renumber, copy to slot, skip, delete (asks first).

| View | Holds |
| --- | --- |
| A zone | Its channels, by number |
| All | Every channel, zoned or not |
| Per band | 2 m, 70 cm, air, marine, broadcast (76–108 MHz: the saved FM stations, BCR-31) |
| Recent | The last 10 channels tuned to, transmitted on or heard, newest first (CHAN-25) |
| Nearby | Channels with a position, nearest first (needs a GPS fix) |

**Local** (MENU 0 2 5, on at 50 km): a zone the radio makes for itself from where you are: every channel with a position within the range, nearest first. It sits after your zones, so ◀▶ on home reach it after the last one, the zones page lists it last, and SIDE2 scans it like any zone. It follows you: as you move a kilometre or so it is worked out again, and a channel near the edge stays until it is 10 % past the range, so it doesn't come and go. Nothing is stored and nothing is written. Without a GPS fix or the fixed position (MENU 0 6 9) it is still there but empty, and says "no position". Off takes it away. For a 10 W handheld, 30 km is a typical reach and more from high ground; 50 km keeps the repeaters you might reach from a hill.

**Zones** (MENU 0 2 3): one line per zone: its name, its chips and how many channels it holds (an empty zone is dimmed). The chips: **● A** on the zone the active slot's channel is in (the active slot's letter only), **SCAN** when the zone is in "scan all", **HID** when it is hidden from ◀▶ on home. Under the list, a preview of the selected zone: its name and state (scan on, or the bands it spans: 2m · 70cm), its first four channels as name, distance and frequency, and a footer (+2 more, its priority channel, or scan off). OK puts the active slot on the zone and goes home: on the channel it last used there, else the zone's first channel, and ◀▶ on home go on from there. SLOT edits the zone (rename, scan options, priority 1 and 2), # makes a new one, \* deletes one after asking (its channels are kept, in no zone).

Location shows only where it exists. With a GPS fix, or the fixed position (MENU 0 6 9) standing in, and channels that have a position (set with the terminal's `ch 12 pos=`, or in Ferrite Console, which reads, edits and writes them over the link, LINK-53, and keeps them from its imports: a RepeaterBook CSV's latitude and longitude, the library's airports and licensed sites), a **Nearby** row heads the list with the nearest one's direction and distance (NE 2.3km), and a previewed channel with a position shows how far it is, compass letters first: 2.3km, 23.4km, 123km, then far (miles with 0 6 4 Imperial). ▲ from the first zone selects Nearby; its preview lists the four nearest, and OK opens the browser's Nearby view. Without a position the page shows nothing about location. Nothing changes by itself: the page never moves a slot or picks a zone for you.

**Add repeater** (MENU 0 2 2): frequency, shift, tone, name, then the channel's edit screen.

### Screens

| | |
| --- | --- |
| ![Editing a channel in place](img/screens/HomeEditCh.png) | ![Home, channel mode](img/screens/HomeA.png) |
| Hold SLOT, channel | Home |
| ![The zones page with a position: Nearby, chips, places in the preview](img/screens/Zones.png) | ![The zones page without a position](img/screens/ZonesPlain.png) |
| Zones, with a position (B active on Repeaters) | Zones, no fix and no fixed position |

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| MENU 8 | Channel | VFO: save as a channel. Channel: edit | — |
| 0 2 4 | Channel display | Name, number, frequency | Name |
| 0 2 5 | Local zone | Off, 10, 20, 30, 50, 80 km | 50 km |
| 0 9 3 2 | Channel-only mode | Off, on (hides VFO and editing) | Off |

Per channel (hold SLOT or MENU 8):

| Field | Values | Default |
| --- | --- | --- |
| Mode | FM, NFM, AM, WFM (BCR-33) | FM |
| Name | 16 characters | Empty |
| Zone | Any of 512 with room (256 channels each, CHAN-35), or none | The zone being browsed |
| Home | Yes, no | No |
| Skip | On, off | Off |
| Busy lockout | Off, on | Off |
| RX only, reverse, talkaround, APRS | On, off | Off |
| Hidden | On, off (left out of channel lists unless "show hidden" is on; CHAN-24) | Off |
| Priority | On, off (checked during any scan; CHAN-24) | Off |
| Tail elimination | Global, off, on | Global |
| End tone | Global, off, beep, two-tone up, two-tone down, chirp, Quindar | Global |
| Squelch override | Global, 0–9 | Global |
| Position and radius | Latitude, longitude, radius | None |
| Service type | Repeater, simplex, APRS, air, marine, weather, PMR/FRS, utility, public safety, satellite, broadcast, data, 4 user types | None |

> **Spec: storage**
>
> - **CHAN-1** 4,000 channels × 64 B at SPI 0x010000, 63 a sector (layout 3, decision 333); a record whose RX frequency reads 0xFFFFFFFF is empty.
> - **CHAN-2** Record: RX freq 4 (10 Hz), TX freq 4 (absolute, 0 = RX; flag bit 10 marks a split, whose TX is its own frequency rather than RX plus a shift), mode 1, bandwidth 1, power 1 (0 = default), step 1 (0 = band default), RX tone 2, TX tone 2, flags 2, zone low byte 1 (byte 18), squelch override 1, latitude 4, longitude 4 (1e-7°), radius 2 (100 m, 0 = 30 km), service 1, end tone and tail 1 (byte 31: end tone bits 0–2, tail bits 3–4, 0 Global), name 16, options 1 (bits 0–1 spare, PTT ID's until decision 214; bits 2–4 end tone: 0 Global, 1 off, 2–6 beep, two-tone up, two-tone down, chirp, Quindar, 7 reserved; rest reserved), reserved 11, version 1 (2: decision 333; a record of another version reads as empty), zone high byte 1 (byte 61: the zone is 2 bytes, 0xFFFF none; version 1 had one byte at 18, 255 none, and 0xFF here), CRC-16. A zone past the last there can be (512 and up, but 0xFFFF) reads as empty too.
> - **CHAN-23** Mode byte: 0 FM, 1 NFM, 2 AM; values 3 and up are reserved.
> - **CHAN-3** Tone word: CTCSS in 0.1 Hz; bit 15 DCS, bit 14 inverted; 0 = none.
> - **CHAN-4** Flags: skip, busy lock, RX-only, talkaround, APRS, hidden, has position, priority (CHAN-24).
> - **CHAN-5** Name: 16 characters, all shown on home (HOME-4.3) and in lists.
> - **CHAN-31** A name holds only A–Z, a–z, 0–9, space and the symbols `- . / _ # + & ( ) ' !`. Text entry's symbols page for a channel name has only those (other text, such as a zone's name, keeps the full page, KEY-12). Everything else that brings a name in maps any other character to `-` rather than refusing it: the terminal's editor, `ch ... name`, `load`, the link's channel writes (as `load`; bytes outside printable ASCII are still refused there as before, LINK-5), and a stored name as it is read. Zone and preset names keep printable ASCII.
> - **CHAN-6** 512 zones × 32 B at 0x050000 (127 per sector; decision 333): name 16, flags (in "scan all", shown in ◀▶, sort by distance), resume, dwell, a reserved byte (written 0), priority 1 and 2, the channel count (2: CHAN-36; 0xFFFF in a record from before it), reserved 4 and CRC. Zone numbers are 2 bytes everywhere (the channel record, the link, the terminal): 0 to 511 are zones, 0xFFFF is "no zone" and 0xFFFE Local (CHAN-34), never stored.
> - **CHAN-7** Each channel has a fixed place in flash (channel n: sector n / 63, slot n % 63); RAM keeps no zone per channel (decision 333: at 4,000 channels that would be 4 to 8 KB), only the member lists of the slots' zones (CHAN-36).
> - **CHAN-8** No zone index in flash: the slots' member lists and the zones' counts are kept right by every write (CHAN-36).
> - **CHAN-9** Channel records are read from flash on demand; there is no channel list in RAM.
> - **CHAN-35** A zone holds at most 256 channels (decision 333); "no zone" has no limit. The 257th is refused whichever way it comes: the save form says "Not saved: zone full (256)", the browser's Move "Zone full" / "256 channels at most", the terminal's `ch` "zone: full (256 channels at most)" and its list's Move stops there ("Zone full (256 channels): moved N of M"), the link's channel writes answer `invalid` with the same reason (LINK-22), and the store refuses it too. The editors' zone field (the channel editor, the terminal's editor, the save form's Zone) steps over a full zone. A channel already in the zone is edited and renumbered as before. Ferrite Console's import splits a longer list over zones.
> - **CHAN-36** The slots' zones are kept as member lists (decision 333): the channel numbers of each slot's zone in number order, three lists of up to 256 (a list shared when two slots are on one zone), 1.5 KB in all. A list is built by one pass over the channel records when a slot takes a zone no list holds (each record looked at by its zone and squelch bytes, read whole only when it may be in the zone: about 22 ms on the bus for a full zone among 4,000), and every channel write keeps it right after that. Stepping, positions and a slot's channel scan (SCAN-25) use it. Every other view (All, per band, Nearby, Local, another zone, no zone, search) pages through flash from where its last page ended. Each zone's channel count is in its zone record (CHAN-6): a write changes it in RAM for a few zones and the records are rewritten once channel writes have been quiet for 2 s (and at power off), a sector at a time, so a link writing thousands of channels doesn't rewrite the zone sector for each; the boot counts every zone in one pass (no table kept) and puts a wrong count right.

> **Spec: zones and views**
>
> - **CHAN-10** Each channel is in exactly one zone or none; order within a zone is channel number.
> - **CHAN-11** ◀▶ on home skip zones with no channels and zones not marked "shown in ◀▶".
> - **CHAN-12** Deleting a zone asks first; its channels move to no zone and stay in All.
>     - **CHAN-12.1** A slot on the deleted zone, and its copy of the channel, go to no zone too, whether the zone was deleted on the radio or from Ferrite Console (the link's `DELETE`), so a later edit of that channel doesn't write the old zone back. Decision 284.
> - **CHAN-13** Deleting a channel happens only in the browser; it asks first and names the channel.
> - **CHAN-14** All, per band (2 m, 70 cm, air, marine, broadcast), Recent and Nearby are computed, never stored.
> - **CHAN-15** Nearby lists channels with a position by distance from the GPS fix; it is empty without one.
> - **CHAN-16** Channel-only mode hides VFO mode and all channel editing.
> - **CHAN-24** Hidden leaves a channel out of the channel lists unless "show hidden" is on in the list's options (hold MENU; kept); a hidden channel is still reachable by number and still scanned. Skip and Priority exclude each other: one choice, in scans, Skip or Priority (the editor's Scan cell, the terminal's Scan row; `ch`'s `skip` and `priority` each replace the other, and a record with both reads as Priority). Priority has a channel checked during scans only (not while just receiving) at the priority interval (0 1 3), besides the zone's priority 1 and 2 (SCAN-12). Both are set in the channel editor and the terminal's `ch`.
> - **CHAN-27** The zones page (MENU 0 2 3, C11) is a compact list, one 21 px line per zone (its name, chips, its channel count at the right; an empty zone dimmed), seven lines above a preview of the selected zone: its name in capitals and its state at the right ("scan on", else the bands its channels span, "2m · 70cm", "empty"), its first four listed channels in number order (CHAN-10, CHAN-24), each as name, place and frequency in fixed columns (the frequency right-aligned, the place in a column as wide as the widest place, the name in the rest, clipped, never wrapped; no channel numbers, no shift signs), then a footer: "+N more", then the first priority channel while the zone is in scan, marked with a star ("★ NAME", so "+1 more · ★ Club repeater" fits whole; a 16-character name fits too), else "scan off". The preview's header is a filled band (the theme's LINE fill, its top edge a 2 px DIM rule, the zone's name in bold TEXT): the list on the page ground above it and the channels on the surface under it read as three parts in every theme. OK on a zone puts the active slot on it and goes home: the slot goes to channel mode on the channel it last used in that zone (a slot keeps its zone and place while on its VFO), else on the zone's first listed channel in number order (CHAN-10; hidden ones only with "show hidden", CHAN-24; HF channels passed, CHAN-26), and home's ◀▶ and knob go on from there (NAV-1); a toast names the slot and the zone ("Slot A", "Repeaters"). A slot already on that channel is left as it is; otherwise the retune ends a scan on the slot, as ◀▶ on home do. OK on an empty zone says "No channels" / "in this zone" (one with only HF or hidden channels: "No channels" / "HF or hidden only") and stays. The APRS slot refuses with APRS-19's message (KISS-9's while KISS holds it) and the page stays. Channel-only mode allows it (zone browsing, PIN-5). SLOT opens the zone's editor (A12; SLOT again or BACK returns to the list), # makes a zone, \* deletes one (CHAN-12). The hint bar: OK Use, SLOT Edit, # New (KEY-9's three; \* still deletes). A move redraws the two lines that changed and the preview, which is one pass over the zone's channels. The channel browser's zone list (C8) draws its zones with the same lines.
> - **CHAN-28** A place is compass letters then a distance: the absolute bearing from the position to the channel as one of eight points (N, NE, E, SE, S, SW, W, NW, each the 45° centred on it), and the distance in at most three digits, never wrapping: under 10 "2.3km", under 100 "23.4km", under 1000 "123km" (no decimal), then "far". In 0 6 4's units: Imperial in miles ("2.3mi"), Nautical in nautical miles ("2.3nm"), the same way. "NE 2.3km", "N 123km", "W far".
> - **CHAN-29** Location shows only where it exists: with a position (a GPS fix, or the fixed position standing in, GPS-3) and at least one listed channel with a position, a Nearby row is pinned at the top of the zones page with only the nearest one's place (no counts), and a previewed channel shows its place only when it has a position. Otherwise the page shows nothing about location. ▲▼ and the knob go through the Nearby row (▲ on the first zone selects it; the list wraps at both ends); on it the preview lists the four nearest ("nearest first", "+N more") and OK opens the browser's Nearby view (CHAN-15). The nearest is found again when the position has moved about 100 m or the channels changed. Location only informs: no zone, slot or channel changes because of where the radio is.
> - **CHAN-30** A zone's chips: "● A" (the active slot's letter, in its colour) only on the zone the active slot's channel is in, never for the other slots' zones or a slot on its VFO; SCAN for a zone in "scan all"; HID for a zone hidden from ◀▶ (CHAN-11).
> - **CHAN-34** Local (decision 326): with MENU 0 2 5 not Off (Off, 10, 20, 30, 50, 80 km; 50 km by default), a zone called Local holds every stored channel with a position (CHAN-2) within that range of the position (the GPS fix, or the fixed position standing in, GPS-3), nearest first by (distance, number), at most 48 (the nearest).
>     - **CHAN-34.1** Its place: after the stored zones, as the browser's computed views follow the zones (CHAN-14): ◀▶ on home reach it after the last zone with channels (and ◀ from the first), on its nearest channel a slot can sit on (CHAN-26), and the knob and ▲▼ step it nearest first (NAV-1); the zones page lists it last ("Local", its channel count, the active slot's chip; no SCAN or HID: it has no zone settings), its preview "within 50 km", its four nearest with their places (CHAN-28) and "nearest first"; OK puts the active slot on it as on any zone (CHAN-27, the toast "Slot A" / "Local"); SLOT opens its setting (0 2 5); \* does nothing. A card on it names Local where it names the zone (HOME-4.3). The browser's picker doesn't list it (its Nearby view is the full list by distance, CHAN-15).
>     - **CHAN-34.2** Scans: SIDE2 on a slot on Local scans its channels (with the zones added with digits, SCAN-3), Skip and HF passed as in any zone, with the radio's resume rule and no priority channels of its own.
>     - **CHAN-34.3** When it is found again: when the position has moved 0.009° (about 1 km) in latitude or longitude from where it was found, the channels changed, or the range did; never per fix or per draw. One pass over the channels, a record read each, as the Nearby row's. A channel joins within the range and leaves only past the range plus 10 %, so one at the edge stays put while the fix wanders. A slot on Local keeps its channel when the list changes, at its new place; if it has left the list, the knob goes on from where it was.
>     - **CHAN-34.4** No position: Local is still a zone, empty: its row dimmed with 0, its preview "no position" and "Needs a GPS fix, or set 0 6 9"; OK and SIDE2 on it say "Local" / "no position" (none in range: "no channels in range") and change nothing; a slot on it keeps its channel. ◀▶ on home pass it while it is empty, as any empty zone.
>     - **CHAN-34.5** Nothing is stored: its members are channel numbers in RAM (112 bytes), no flash is written for it. Turning 0 2 5 Off takes the zone away; a slot on it goes to its channel's own zone on the same channel (nothing retunes, as CHAN-29: location never changes a slot by itself).
> - **CHAN-25** Recent: a channel joins when a slot is tuned to it, when you transmit on it, or when a slot on it opens squelch; the last 10, newest first, each once (a channel already there moves to the top). Kept in RAM (22 B, in the store), not saved: it starts empty at power-on (CHAN-14).

> **Spec: home channel**
>
> - **CHAN-17** One home channel per radio, stored in settings as a channel number (2 B).
> - **CHAN-18** Setting Home on a channel clears it on the old one; renumbering carries it; deleting the channel clears it.
> - **CHAN-19** Hold 0 puts the active slot on the home channel in channel mode, from VFO or any zone.
> - **CHAN-20** With none set, hold 0 shows "No home channel: hold SLOT to set" (set it with hold SLOT on a channel).
> - **CHAN-21** The home channel is separate from zone priority channels.
> - **CHAN-22** A channel holds 0.15–64 MHz (an HF channel, CHAN-26) or what the chips receive, 64–630 and 756–1300 MHz (VFO-21). A transmit frequency apart from RX (an offset or split) stays within 64–1000 MHz; a simplex channel above 1000 MHz is receive only (VFO-21). The editors' knob keeps RX on its side of 64 MHz and steps over 630–756 MHz.
> - **CHAN-32** A channel's fields have one set of rules, the same in the radio's channel editor, the terminal's editor, `ch`, `load` and the link's channel writes: the zone's choices, the frequency steps by band (VFO-18), typed frequencies and their limits (CHAN-22, CHAN-26, TX-37), Offset and Split (Offset's 4th choice is Split on the TX it had, VFO-16), power refused on an RX-only channel (greyed with "this channel is RX only" wherever it shows, EDIT-7), Skip and Priority as one choice (in scans, Skip or Priority, CHAN-24), Home, the name (CHAN-31) and # (a channel's squelch default is Global, SQL-6). Each place keeps its own layout and words; a refusal names the field (the editors "Power: ...", `ch` its key, `power: ...`).
> - **CHAN-33** Channel display (0 2 4) is how a channel shows on home's cards and lines: its name (the default; a channel without one shows its frequency), its number ("CH 012"), or its frequency, large as a VFO's. One setting for all three slots.
> - **CHAN-26** HF channels (below 64 MHz) keep HF mode's frequency and mode (AM; USB, LSB, CW below 18 MHz; FM from 18 MHz), simplex, in zones like any channel; HF mode's step, bandwidth and AGC stay its own.
>   - **Saving:** hold 9 in HF mode saves one (the save form, then back to HF mode).
>   - **Recalling:** by number, from the browser or as the home channel, one opens HF mode on its frequency and mode (without the SSB patch, USB, LSB and CW come up as AM); a home slot never sits on one: ▲▼ and ◀▶ on home go past them, and so does V/M's first channel.
>   - **Scans:** no slot scan stops on one: a scan never moves the relay (SAFE-20) and the SI4732 is HF mode's.
>   - The record is unchanged: its mode byte already holds 0–5. nicFW keeps its tuner memories in its channel slots; Ferrite does the same with its channels (decided Oct 7, 2026).

### Under the hood


### Status

Edit-in-place mock-ups approved (0b). Storage built in 1d (Oct 4, 2026), simplified the same day to a fixed map: channel records, zones and range presets at fixed addresses, tested with 2,500 simulated power cuts during changes and recovery and 300 queued writes read mid-way; both simulators read and write through it. Browser, zones and views in 2c (Nearby once GPS lands in 5a). Done when all CHAN rules pass in host tests and the simulator, including simulated power loss.


### Settled details

- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - CHAN-2: decision 86.
  - CHAN-23: USB, LSB, CW and SSB fine tune were dropped Oct 3, 2026: SSB/CW is HF mode only.
  - CHAN-5: decided Oct 7, 2026.
  - CHAN-31: decision 221, Oct 20, 2026 (flash: the two name fonts are cut to the set). Stock's name entry appears to take all of printable ASCII (abc/ABC/123 modes and a `!`–`~` character table in V0.27's initialised data).
  - CHAN-6: smart scan until decision 72.
  - CHAN-8: decided Oct 4, 2026.
  - CHAN-24: decided Oct 7, 2026; decided Oct 6, 2026. Changed Oct 20, 2026 (decision 223): Skip and Priority exclude each other everywhere (only the radio's editor kept them apart; the terminal's editor and `ch` let both be on).
  - CHAN-22: changed Oct 20, 2026 (decision 223): a simplex channel above 1000 MHz is kept (receive only), as the radio's editor and the save form already made them (`ch` and `load` refused it, so a dump of one didn't load); the radio's editor's knob stopped at 1000 MHz and stepped into 630–756 MHz.
  - CHAN-32: decision 223, Oct 20, 2026.
  - CHAN-25: decided Oct 7, 2026.
  - CHAN-14: changed Oct 22, 2026 (decision 258): a Broadcast band view, the saved FM stations, in place of FM presets (BCR-31). Channel display moved from 0 2 5 to 0 2 4 (decision 256).
  - CHAN-34: decision 326, Oct 30, 2026 (Alex: "something that has to be ENABLED", then "i think it is on by default, and go with 50k by default"): a zone worked out from where the radio is. 50 km covers what a 10 W handheld reaches from high ground (30 km is typical on flat land). Last after the stored zones so their numbers and places stay as they are.
  - CHAN-27 to CHAN-30: decided Oct 14, 2026 (user, decision 155): the zones page as a compact list over a preview, chosen from four mock-ups (option B, location only where it exists). The browser's Nearby view stays the full list by distance (CHAN-15); the Nearby sort setting (then 0 2 4) was never built and left the menu with decision 256 (MENU-33).
  - CHAN-27: changed Oct 14, 2026 (user, decision 157): the footer marks the priority channel with a star instead of "priority:", so the name fits rather than scrolling.
  - CHAN-1, CHAN-2, CHAN-6 to CHAN-8, CHAN-35, CHAN-36: decision 333, Oct 31, 2026 (Alex: "lets up the channels to 4k channels. zones to 512", "lets cap channels per zone at 256. nice and easy"): layout 3. A zone number per channel in RAM would have cost 4 to 8 KB at 4,000 channels; the slots' member lists cost 1.5 KB, and the scan bitmaps went with them (SCAN-25). Built Nov 1, 2026.
  - CHAN-27: changed Oct 15, 2026 (user, decision 178): OK puts the active slot on the zone and goes home (it opened the zone's editor, which is now SLOT; the page had no way to pick a zone, only ◀▶ on home did); the preview's header became a filled band, as the list, the header and the channels ran together.

### Open points

None.


---

