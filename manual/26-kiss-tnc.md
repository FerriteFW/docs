## 26. KISS TNC

### What it's for

Lets an APRS or packet app on a computer or phone use the radio as its modem, receive and transmit, over the cable or Bluetooth.

### Using it

1. MENU 0 5 8: the port, **Cable** or **Bluetooth** (Bluetooth by default). Then MENU 0 5 3: **KISS**. That port now speaks raw KISS bytes, which is what apps expect; with KISS off it speaks the Ferrite link protocol (chapter 29).
2. For Bluetooth, turn it on (MENU 0 9 2 1) and connect from the app.
3. Received frames go to the app; frames from the app are transmitted on the APRS frequency. Turning KISS on is your consent for apps to transmit packets: KISS has no session, so no PIN is asked, but every transmit check still applies.

**Which apps work.** Most APRS apps are written for the Mobilinkd TNC and its Bluetooth KISS service (`datasheets/protocols/BLE-KISS-API.md`): aprs.fi on iPhone and Android, RadioMail, PocketPacket and the Bluetooth builds of APRSdroid look only for that service, and the classic APRSdroid uses classic Bluetooth (SPP). The radio's stock Bluetooth module offers neither, only a plain serial service, so those apps won't find it over Bluetooth until the module runs our own firmware or is replaced. What works now:
- **The cable:** APRSdroid over USB, Xastir, YAAC, or any program that takes a serial KISS TNC.
- **iPhone through a bridge:** the cable into a small computer (a Raspberry Pi) running kiss-tnc-bridge, which offers the radio to aprs.fi and the other iOS apps with the standard service.
- **Bluetooth:** Ferrite's web app (in Bluefy on iPhone) and the few apps that take a plain BLE serial port (radiochat-aprs, an ATAK bridge).

### Screens

No mock-up yet.

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| 0 5 3 | APRS mode | KISS turns it on (Off, Tracker, On, KISS) | Off |
| 0 5 8 | KISS port | Cable, Bluetooth | Bluetooth |
| 0 9 2 1 | Bluetooth | Off, on | Off |

> **Spec: KISS**
>
> - **KISS-1** Off by default.
> - **KISS-2** Frames from the app are automatic transmissions: callsign set, length cap, never on a busy channel, timeout and duty limit; they are exempt from the 30 s spacing (APRS-9), and the app sets TX delay, persist and slot time with KISS commands (defaults 300 ms, 63, 100 ms; no menu items).
> - **KISS-3** Only the Radio task keys; a KISS frame is a request that can be refused.
> - **KISS-4** Every frame received on the APRS frequency is sent to the app.
> - **KISS-5** Over Bluetooth, KISS uses the plain serial characteristic (FFE0/FFE1), transmit included.
> - **KISS-6** With KISS on, the chosen port (cable or Bluetooth) carries raw KISS bytes, not link frames; with it off, that port speaks the Ferrite link protocol.
>     - **KISS-6.1** KISS is turned on and off as 0 5 3's KISS (decision 440); 0 5 8 is only its port, Cable or Bluetooth (Bluetooth by default), kept while KISS is off. Changing 0 5 8 with KISS on moves KISS to that port. A record from before keeps KISS on the port it was on.
> - **KISS-7** Turning KISS on is the consent for apps to transmit packets; KISS has no session, so the link's PIN (LINK-30) isn't asked. The normal transmit checks apply (KISS-2).
> - **KISS-8** The link protocol has no `KISS` message: packets go only through KISS mode on its own port (KISS-6), so the web app can't send or receive them alongside programming on one connection. The link on the other port still runs beside it (the cable for Console, Bluetooth for a KISS app, or the other way round).
> - **KISS-9** While KISS is on (cable or Bluetooth), slot C is the APRS slot, as with APRS mode (APRS-15, APRS-19): it tunes to the APRS frequency (0 5 4) and is locked there ("Slot C held by KISS"), it has receive priority on its chip (APRS-21.1), and KISS frames go out on it. KISS off gives C back (unless APRS mode holds it).
> - **KISS-10** KISS on means the app does APRS: while it is on, the radio sends nothing of its own. APRS mode and automatic beacons are suspended (their settings kept, back as they were when KISS goes off), 0 5 3 and 0 5 6 1 are greyed with "KISS on: the app sends", and Beacon now and sending a message from the radio are refused with the same words. The radio still decodes (KISS-4): the heard list, the inbox and the message sound work as ever. Two stations' acks, beacons and query answers from one radio and its app are never sent.
> - **KISS-11** KISS follows the KISS TNC spec (`datasheets/protocols/KISS.txt`, 1987) as a single-port, half-duplex TNC. Port 0 only: frames for other ports are ignored. Commands: 0 data (15 bytes, the shortest AX.25 frame, up to the length cap), 1 TXDELAY (applied to the host's frames), 2 P and 3 SlotTime (p-persistence as the spec's section 6), 4 TXtail (kept, not used), 5 full duplex (kept, but never skips the channel check: KISS-2, the radio is half duplex), 6 SetHardware (ignored). Return (0xFF) is ignored: KISS is the radio's own setting, not a mode the host leaves. A byte after FESC other than TFEND or TFESC is dropped and the frame goes on, as the spec says.
> - **KISS-12** Mobilinkd's KISS extensions (SetHardware, command 6: `datasheets/protocols/Mobilinkd_KISS_config_protocol.md`) and the other hardware commands apps send (the Benshi and B.B. Link set and restore frequency, 0xEA and 0xEB) are ignored, and the radio never sends a command-6 frame of its own. Never acted on, whatever comes later: a test-tone or PTT command (Mobilinkd's 0x07, 0x08, 0x09: they key the transmitter), a frequency set from the host (slot C stays locked, KISS-9), a save to flash. Answering read-only queries (firmware version, battery) is not done: the apps that send them, Mobilinkd's configuration apps, can't find the radio over Bluetooth anyway.
> - **KISS-13** A client's frame waits for a clear moment at most 5 s (APRS-10's window), then is dropped quietly (the client resends as it sees fit), so it never waits for ever or holds back the frames after it; KISS turned off (or Low Power Mode) drops a frame still waiting. Decision 284.

### Under the hood


### Status

No mock-up. Built in 5d, within the milestone 5 gate; module chip and pads probed in 1a. Done-when not set beyond that gate.


### Settled details

- KISS parameters (TX delay, persist, slot time) are set by the app's KISS commands, defaults 300 ms, 63 and 100 ms; no menu items (decided Oct 6, 2026).
- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - KISS-9: decided Oct 15, 2026 (decision 173): a frame queued with APRS mode off waited on C's own VFO forever. Built Oct 15, 2026: C follows KISS from every path that turns it on or off (menu, `set`, a settings write), with a toast; APRS-19's lock said how KISS is turned off. Changed Oct 15, 2026 (decision 181): the lock names only what holds C ("Slot C held by KISS"), and KISS gives C receive priority (APRS-21.1).
  - KISS-2: decided Oct 6, 2026.

### Open points

- BLE module firmware: chip unconfirmed; if it can't be flashed, iOS APRS apps need a module swap (decide before milestone 5).

---

