## 38. Packet station: mailbox and TNC

### What it's for

Makes the radio a small packet node: other stations connect over 1200-baud AX.25 to leave and read mail, and a laptop on the terminal can connect to other stations and BBSes.

### Using it

- **Mailbox:** turn it on (its own slot listens on the mailbox frequency). Callers connect to your callsign with SSID (for example `C VA3ABC-1`) and use `L` list, `R n` read, `S call` send, `K n` kill, `B` bulletins, `Q` quit. New mail shows in the inbox.
- **Your mail:** read and write it in the terminal (chapter 37), or read it on the radio: the Status page's Mailbox row (#, then the last row) opens the mailbox screen.
- **TNC terminal:** in the terminal's TNC page, `C call` connects through the radio, `D` disconnects; what you type is sent, what arrives is shown.

### Screens

No mock-up yet.

### Settings

**Not built:** the mailbox's settings are out of the menu until it is (decision 245); they were 0 5 8 2 – 0 5 8 5 (mailbox, its SSID and frequency, bulletins). The KISS TNC is MENU 0 5 8 (chapter 26).

> **Spec: mailbox**
>
> - **MBX-1** Off by default; needs a callsign; answers only on its own SSID.
> - **MBX-2** AX.25 connected mode at 1200 baud (AFSK, as APRS), one connection at a time, window of 4 frames.
> - **MBX-3** Commands: L, R n, S call, K n, B, Q, H (help). Personal messages are readable only by the sender, the addressee and you; bulletins by anyone.
> - **MBX-4** Messages live in their own SPI region (64 KB, about 100 messages of up to 512 B), CRC-checked records; when full, new messages are refused, never silently overwritten.
> - **MBX-5** Every reply is an automatic transmission: callsign set, never on a busy channel, refused on emergency frequencies (TX-35), duty and heat limits apply.
> - **MBX-6** Power defaults to Low.
> - **MBX-7** Answering is allowed only where the region table marks automatic operation as permitted on that frequency.
> - **MBX-8** New personal mail sets the inbox and shows a toast.

> **Spec: TNC terminal**
>
> - **MBX-9** From the terminal, `C call` opens a connection through the radio and `D` closes it; the user's keystrokes are the operator's transmissions (not automatic).
> - **MBX-10** The mailbox and the TNC terminal never hold two connections at once.

### Under the hood


### Status

Not scheduled yet: after the terminal (chapter 37) and APRS (milestone 5). Packet is 1200 baud. 9600 can be sent on the bench (the TX filter bypass and an equaliser, Oct 27, 2026) but not received: the receive path can't carry it (research/tx-response/audio-limits-oct27.html), so 9600 packet isn't offered.


### Open points

- The region table needs an "automatic operation permitted" field per band segment (rules differ by country; to be researched, not guessed).
- Forwarding to a full BBS or Winlink: a later phase.

---

