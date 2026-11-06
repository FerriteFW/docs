## 24. Notifications, the inbox and the event log

### What it's for

What the radio decoded or received while you weren't looking. Three things, each with one name everywhere (the radio, Ferrite Console, the guides; decision 280): the **inbox** is APRS messages to you (APRS → 1 Messages, the envelope's count); the **event log** is every decode and alert (MENU 0 4 1; Console's Event Log); **Heard** is the APRS stations (APRS-3). Alerts (SAME, DSC distress) take over the screen; everything else is a toast and a count.

### Using it

- **Toast:** a decode or a new APRS message shows one line over the hint bar for 3 s (DTMF heard shows on the slot's card instead, DEC-6.1).
- **Inbox icon:** an envelope in the status bar with the count of unread messages to you (INBOX-3.1); red while an alert waits. Separate counts are on the Status page (MENU 0 0).
- **Event log:** MENU 0 4 1, or from the unread mark. Newest first, unread counts per source; ◀▶ filter by source, hold MENU marks all read or clears. OK opens an event's detail; "Go" tunes to it.
- **Alert:** full screen, flashing border, tone until acknowledged. **OK** silences, **hold MENU** opens the log, **BACK** returns to where you were. One that arrives while you transmit waits for the unkey.

### Screens

| | | |
| --- | --- | --- |
| ![A toast over home](img/screens/Toast.png) | ![A weather alert](img/screens/Alert.png) | |
| A message arrives | SAME warning | |

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| 0 4 1 | Event log | View, filter, clear | — |
| 0 4 4 | Popups | Off, on (a 3 s toast for each decode) | On |
| 0 7 5 3 | Alert tones | Off, on | On |
| 0 7 5 5 | Message sound | Off, Ding, Mail, Packet, Droid, Pager | Packet |

> **Spec: notifications**
>
> - **INBOX-1** A toast is one line for 3 s over the hint bar and never covers the frequency.
> - **INBOX-2** Only alerts (SAME warning, DSC distress) take the full screen.
> - **INBOX-3** The inbox icon shows only while something is unread; one count; red while an alert is unacknowledged.
>     - **INBOX-3.1** The count is the unread messages to you (APRS-32), not the log's entries: decodes, arrivals and alerts go to the event log, which keeps its own unread count (0 4 1's "N new"); an unread alert still turns the icon red. Reading a message lowers the count; the log's "Mark all read" doesn't touch it. Decision 238.
>     - **INBOX-3.2** "Clear the log" leaves no "N new"; the messages' "Mark all read" takes each message's log entry out of the log's count with it (INBOX-7.1), as reading one message does. Decision 284.
> - **INBOX-4** An alert sounds its tone until OK; OK silences, hold MENU opens the log, BACK returns to the screen it came over.
> - **INBOX-5** Notifications never interrupt receive, scan, watch or decoders, and never key the transmitter.
> - **INBOX-12** An alert that arrives while you transmit waits for the unkey, then takes the screen over any other; menus and editors keep their state underneath. While the crossband repeater runs it is a banner instead (XB-19).

> **Spec: event log**
>
> - **INBOX-6** Every decode and alert is appended to the event log ring in SPI flash (APRS: messages to you and what failed to send; the stations heard go to the heard list, APRS-3, APRS-4, not the log): time, source, frequency, slot, an ID, a position, a name (20) and text (64), 128 B a record, 992 records.
>     - **INBOX-6.1** Each record (and each APRS message, APRS-11) also says whether its time was real when stored: stamped while the clock was UTC (from GPS), or not. An age is shown only when it is real: a UTC record while the clock is UTC again, or any record from this power-on. Anything else (stored before a restart without GPS time, every record from before this rule, or a UTC record before GPS time is back) has no age: the radio shows "earlier" and "--:--" for the time ("Before restart" on a detail page), the link sends `ago` 0xFFFFFFFF, and Ferrite Console shows "Before restart" with the CSV's time left blank. Never a guessed date. Decision 281.
> - **INBOX-7** Each record keeps its own read mark (a byte programmed from 0xFF to 0, so marking read never erases); the inbox count at power on is the unread records kept, and goes up with each new one.
>     - **INBOX-7.1** Reading an unread message from someone (Messages, APRS-32) marks its log entry read too, and the inbox count goes down with it: the newest unread APRS entry with its sender and text, among the last 64 (until Oct 22, 2026 only the log's own read did, so read messages still counted).
> - **INBOX-8** When the ring wraps, the oldest go a sector at a time (31 records).
> - **INBOX-13** A power cut during a write loses at most the record being written (and, when it was entering a used sector, that sector's 31 oldest, as the write would have); mount blanks a torn record so nothing after it is lost.
> - **INBOX-9** The log lists newest first, with unread counts per source, and filters by source.
> - **INBOX-10** A highlighted event has "Go" on the hint bar to tune it.
> - **INBOX-11** The web app reads the log from a sequence number (`LOG_READ`, LINK-42) and gets new events live (`SUBSCRIBE`'s event log, LINK-57).

### Under the hood


### Status

Toast and alert mock-ups drawn, awaiting approval (0c). Toast and confirm in 2b; event log, unread counts and detail screens in 6a. Done when every INBOX rule passes in the simulator.


### Settled details

- The inbox icon opens the event log: one inbox for everything (APRS messages, pagers, alerts), newest first, filtered by source; APRS messages are also listed under MENU 0 5 2 (decided Oct 6, 2026).
- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - INBOX-12: decided Oct 6, 2026.
  - INBOX-13: decided Oct 7, 2026.

### Open points

None.

---

