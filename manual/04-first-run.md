## 4. First-run setup

### What it's for

Asks the few things a new owner needs, one per page, so the radio is usable at once.

### Using it

Runs on first power-on and again from MENU 0 9 7 1. Every page has a default: OK-OK-OK gives a working radio. **OK** next, **BACK** previous, **#** skips the rest.

| Page | Asks | Default |
| --- | --- | --- |
| 1 Welcome | — | — |
| 2 Callsign | Callsign; may be left empty. Digits type, * switches letters/digits | Empty |
| 3 Region | Region (all eight on one screen), then Extend TX (off, or on after its warning) | None: you pick one (SETUP-3) · off |
| 4 Owner card | Name and contact; optional. Edited later in the web app only | Empty |
| 5 Time | Time zone, clock format (set from GPS or not), units | UTC, 24 h from GPS, metric |
| 6 Look | Home layout (three previews), theme | Watch, dark |
| 7 Battery Save | Level, with its trade-off in one line | 1 |
| 8 Summary | Your choices and the transmit state | — |

There's no arming step: after setup, transmit works on your region's amateur bands. The radio starts with no channels.

### Screens

| | | |
| --- | --- | --- |
| ![Setup, welcome](img/screens/SetupWelcome.png) | ![Setup, callsign](img/screens/SetupCall.png) | ![Setup, region](img/screens/SetupRegion.png) |
| Page 1, welcome | Page 2, callsign | Page 3, region and Extend TX |
| ![Setup, owner card](img/screens/SetupOwner.png) | ![Setup, time](img/screens/SetupTime.png) | ![Setup, look](img/screens/SetupLook.png) |
| Page 4, owner card | Page 5, time zone, clock, units | Page 6, home layout and theme |
| ![Setup, Battery Save](img/screens/SetupBattery.png) | ![Setup, summary](img/screens/SetupSummary.png) | |
| Page 7, Battery Save | Page 8, summary | |

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| 0 8 6 1 | Callsign | Text | Empty |
| 0 9 4 | Region | US, Canada, UK, Europe, Australia, New Zealand, Japan, Other | None until chosen in setup |
| 0 8 8 4 | Extend TX | Off, on (warning shown once) | Off |
| 0 6 5 | Time zone | UTC−12 to +14, with 30 and 45 min offsets | UTC |
| 0 6 6 | Clock | 24 h, 12 h; from GPS on/off; manual | 24 h, from GPS |
| 0 6 4 | Units | Metric, imperial, nautical | Metric |
| 0 7 2 | Home layout | Watch, single + scope, watch + activity | Watch |
| 0 7 1 | Theme | Dark, daylight, night red, cyberpunk | Dark |
| 0 7 7 1 | Battery Save | Off, 1, 2, 3 | 1 |
| 0 9 7 1 | Run setup again | — | — |

> **Spec: flow**
>
> - **SETUP-1** Run on first boot (no layout header) and from MENU 0 9 7 1.
> - **SETUP-2** Eight pages in the order above; one question per page.
> - **SETUP-3** Every page has a default and OK on it gives a working radio, except the region: all eight regions show on one screen and none is chosen until OK on one, since the region decides where you may transmit.
> - **SETUP-4** OK next, BACK previous, # skips the rest with defaults kept.
> - **SETUP-5** Each answer writes its menu setting; changing it later in the menu is the same setting.

> **Spec: transmit in setup**
>
> - **SETUP-6** No arming step and no licence confirmation.
> - **SETUP-7** Region sets the amateur transmit bands and defaults: a new VFO or channel's mode is wide FM in the Americas, AU and NZ and NFM in the UK, Europe, Japan and Other; weather radio and SAME in the US and Canada only (hidden elsewhere, WX-3).
> - **SETUP-8** Extend TX is off by default; turning it on shows its warning first: may be illegal where you are, can interfere with services people rely on, you're responsible for every transmission.
> - **SETUP-9** An empty callsign is allowed; automatic transmissions stay refused until one is set.
> - **SETUP-10** The summary shows the transmit state, that there are no channels yet, and how to add them.
> - **SETUP-11** The owner card is entered on the radio only on setup page 4; after that it is edited in the web app only (no radio menu item).
> - **SETUP-12** The callsign is stored and shown in capitals; letters typed in lower case become capitals as you type.
> - **SETUP-13** The callsign takes up to 10 characters and CW ID sends it whole, but an AX.25 address holds 6: with a longer one the callsign page says "over 6 characters: no APRS" under the box (amber), and APRS beacons and messages are refused ("Beacon not sent: callsign over 6"); KISS frames carry the client's own addresses and still go. Decision 174.
>     - **SETUP-13.1** The refusal comes when you send, never later: Send in compose ("Callsign over 6", "no APRS"), Beacon now ("callsign over 6") and the link's message send refuse at once rather than queue something the APRS task can't frame (until Oct 22, 2026 they said "queued" and nothing went).

### Under the hood


### Status

Mock-ups for pages 2, 3 and 8 approved (0b). The store is built (roadmap 1d, Oct 4, 2026) and tested on the PC with thousands of simulated power cuts; both simulators keep their flash, start setup on a blank one, and keep settings through the power switch. Done on the radio when setup runs on first boot and settings survive power cycles and pulled batteries (after 1c).


### Settled details

- Setup pre-selects no region: you pick one, and nothing transmits until you do (decided Oct 6, 2026; a wrong guess is worse than one tap).
- Time zone: UTC until you set it, in setup or at 0 6 5 (decided Oct 7, 2026). GPS gives UTC only, with no daylight saving, so no zone is guessed.
- Setup lists all eight regions on one screen (US, Canada, UK, Europe, Australia, New Zealand, Japan, Other), no submenu (decided Oct 6, 2026); the region mock-up is redrawn from the UI (Oct 7, 2026).
- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - SETUP-3: decided Oct 6, 2026.
  - SETUP-7: decided Oct 7, 2026.
  - SETUP-12: decided Oct 3, 2026.
  - SETUP-13: decided Oct 15, 2026 (decision 174): VE7TEST went out on APRS as VE7TES.

### Open points

None.

---

