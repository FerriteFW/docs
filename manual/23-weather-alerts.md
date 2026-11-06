## 23. Weather radio and alerts

### What it's for

Listens to the weather channels and raises a full-screen alert when a SAME warning for your area arrives.

### Using it

1. Weather radio is ordinary channels: the WX channels (162.400–162.550 MHz) come as a seeded zone, so you listen to them like any zone (◀▶ on home, or the channel browser). There is no weather screen (decided Oct 6, 2026).
2. To set up alerts, use MENU 0 4 5: turn SAME on, enter up to 8 location codes (FIPS in the US, CLC in Canada; with none, every alert shows), set the alert tone, and pick the channel.
3. When an alert arrives, it fills the screen with a flashing border and a tone. **OK** silences the tone, **hold MENU** opens the event log, and **BACK** returns to the screen it came over (hold BACK: home). The inbox icon turns red until you read the alert.

Weather radio and SAME exist only in the US and Canada regions, where they're on by default; in other regions they're hidden.

How SAME decoding works is in chapter 27.

### Screens

| |
| --- |
| ![Weather alert](img/screens/Alert.png) |
| A SAME warning |

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| 0 4 5 1 | SAME | Off, on (US and Canada only; hidden elsewhere) | On |
| 0 4 5 2 | Location codes | Up to 8: FIPS (US), CLC (Canada) | None |
| 0 9 4 | Region | US, Canada, …, Other | None until chosen in setup |

The old Open weather radio item is gone with the weather screen: the WX channels are a zone (WX-1). Weather alerts moved from Tools (0 3 3) to Decoders and alerts (0 4 5) on Oct 7, 2026.

> **Spec: weather radio**
>
> - **WX-1** Weather radio is channels, not a screen: in the US and Canada regions the WX channels (162.400–162.550 MHz) are a seeded zone, listened to like any other; SAME alerts run separately (WX-4) (the old Open weather radio item and its screen are gone). The seed: the seven WX channels as a "Weather" zone on channels 991–997, made at setup when the region is US or Canada (a normal zone you can delete; your own numbering below is untouched); SAME listens on whichever slot is tuned to one of them (WX-2).
> - **WX-2** Weather channels are 162.400–162.550 MHz. SAME listens on whichever slot is tuned to one (DEC-19); there is no channel setting (the Auto-only row left the menu, decision 276).
> - **WX-3** Weather radio and SAME exist only in the US and Canada regions, on by default there; in every other region their menu items are hidden.

> **Spec: alerts**
>
> - **WX-4** A SAME warning that matches a location code, or any warning when no codes are set, opens the Alert screen over any screen.
> - **WX-5** The Alert screen shows the event, the areas, the issue and expiry times (with minutes left), the originator, and the slot and frequency it was heard on.
> - **WX-6** The border flashes and the tone sounds (if on) until OK is pressed, as every alert does (INBOX-4).
> - **WX-7** The Alert screen's keys are the shared ones (INBOX-4): OK silences, hold MENU opens the event log, and BACK returns to the screen the alert came over (KEY-5). The alert stays in the event log (INBOX-6).
> - **WX-8** The inbox icon is red while an unread alert waits (INBOX-3).
> - **WX-9** Alerts are the only events that take over the screen; other decodes show a toast (INBOX-2, INBOX-1).
> - **WX-11** Battery Save is not paused for SAME: the receiver keeps its sleep cycle and catches one of the three header bursts (to confirm on the bench that a header decodes from sleep at each level).
> - **WX-10** Location codes: up to 8, FIPS (US) or Canada's CLC codes; a warning matches when any of its areas is in the list.

### Under the hood


### Status

Alert mock-up drawn Oct 2, 2026, awaiting review (0c). Location codes (A13) built Oct 4, 2026: 8 six-digit codes in settings, edited on the radio (simulator shot `location-codes`). SAME alerts and the Alert screen are in 6b: built Oct 8, 2026 on the BK4829's own SAME receiver (DEC-19, chapter 27), each alert also logged; not yet run on a radio. Done when SAME passes on recorded audio and one live signal.


### Settled details

- One alert-tone switch: Sounds › Alert tones (0 7 5 3) covers SAME and DSC alerts; SAME's own switch is gone and the weather channel moved to 0 4 5 3 (decided Oct 7, 2026); that row, Auto only, left the menu Oct 23, 2026 (decision 276).
- The Alert screen is shared with DSC distress alerts: chapter 24 owns the shared rules (INBOX-1 to INBOX-4, INBOX-12); WX-6 to WX-9 point to them (Oct 8, 2026).
- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - WX-1: decided Oct 6, 2026; decision 73; decided Oct 7, 2026.
  - WX-11: decided Oct 7, 2026.

### Open points

None.

---

