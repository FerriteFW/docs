## Appendix C. Safety rules that apply everywhere

This appendix is the one home of the safety rules. A rule elsewhere that says the same thing keeps its ID, so tests and the test plan still find it, and reads "As SAFE-n" with a one-line summary: GOAL-8, INST-4, INST-6, BACKUP-6, BACKUP-10, BOOT-1, BOOT-2, BOOT-3, KEY-8, TX-16, TX-19, TX-42, PIN-8, HF-21, UPD-6, UPD-7, CAL-1, LINK-3, LINK-4 and DEC-1.

> **Spec: protecting the radio**
>
> - **SAFE-1** Calibration (0x00F000–0x00FFFF) is read-only: the SPI driver refuses any erase or write whose erase unit overlaps it, and offers only 4 KB sector erase and page program.
> - **SAFE-2** The bootloader update area (0x300000 up) is never written, with no exception, not even to clear a stale header: the storage driver refuses it; a 0xA55A header found there at boot is shown on About, and the installer refuses to install over one (INST-5).
> - **SAFE-3** The firmware never writes MCU flash, the bootloader or the option bytes (EOPB0 included); nor does the installer. The marker sector (0x080F0000) changes only through the stock bootloader: under a Ferrite image that reaches it, or on the way back to stock, which puts the recorded word back or leaves it erased (BACKUP-12, decision 338).
> - **SAFE-4** Install saves and verifies the full 4 MB first (through the hwtest reader); Ferrite then erases every sector except calibration (0x00F000–0x00FFFF) and the update area (0x300000 up) on its first boot, only after the verified backup exists, and records the calibration CRC; a CRC mismatch at boot locks transmit.
> - **SAFE-5** The link has no calibration write (only `CAL_READ`, a read-only copy for backup; no `CAL_WRITE`, ever): no message writes the calibration sector (0x00F000–0x00FFFF) or the update area (0x300000 up), and any request touching them is refused; it can't change TX limits; `STOCK_RESTORE` skips both areas.
> - **SAFE-6** Link writes come from the cable, or from Bluetooth past the radio's PIN while a PIN lock is on (LINK-7, LINK-30); every write is validated for its band. KISS transmit needs only KISS mode on (KISS-7).
> - **SAFE-7** Safe state first, before RAM init after reset, and on any panic or fault: PA5 low as a GPIO (PA drive 0), then RF paths clear, then the relay; audio amp off.
> - **SAFE-8** The independent watchdog is on; a hang ends in a reset into the safe state. It runs from the moment the tasks start, about 6.5 s (4.4 to 8.7 s, the watchdog's own clock varies), fed each time the main loop turns (at least every 10 ms); any reset stops it again, so the bootloader and the updater never meet it (decision 364).
>     - **SAFE-8.1** A fault (a crash: a bad instruction, a bad memory access, a panic) puts the radio in the safe state with the red LED, then restarts it, as a hang does. Three restarts without a minute of running between them stop the radio in the safe state with the red LED until it is turned off, so a fault at start can't loop for ever.
>     - **SAFE-8.2** The start after a fault or a hang says so: a toast ("Radio restarted", "after a fault" or "after a hang"), a cable log line with the fault's address, and the readback's `restart` line (Console). The address survives the restart but not a power cut (the battery out).
> - **SAFE-9** No reset touches calibration, the update area or the SSB patch, and no stock power-on mode exists.
>     - **SAFE-9.1** The reset from 0 9 7 2 (BOOT-14) never touches calibration, the update area or the SSB patch.
>     - **SAFE-9.2** Nor does the reset reached by holding MENU at power-on.
>     - **SAFE-9.3** No other power-on combo exists: none of stock's power-on modes (super mode, all-band test, +0x49/+0x4A).

> **Spec: transmit**
>
> - **SAFE-10** One owner: only the Radio task keys the transmitter; everything else asks it (TX-17).
> - **SAFE-11** One path state machine owns the six path selects, the relay and PA7/PC5; break before make (TX-23 – TX-29). Only the active slot's band or HF mode's receiver decides the relay (SAFE-20 – SAFE-22); watching, scanning and sweeps never move it (WATCH-10, HF-3).
> - **SAFE-12** Where: the band plan holds everywhere; emergency frequencies need a second PTT (TX-1 – TX-12, XB-2, XB-3).
>     - **SAFE-12.1** The band plan holds in every mode: a key-up outside it is refused, whatever starts it.
>     - **SAFE-12.2** Retired (decision 224): the 1.25 m cap held in every mode the same way; there is no cap now (TX-9).
>     - **SAFE-12.3** It holds in crossband (XB-2, XB-3).
>     - **SAFE-12.4** With Extend TX on, transmit still stops at Extend TX's range (TX-2, TX-41): 18–64, 136–174, 200–260 and 400–520 MHz within the calibration; airband, 64–136 MHz, below 18 and above 520 MHz stay refused.
>     - **SAFE-12.5** Nothing is always blocked, but emergency frequencies need a second PTT.
> - **SAFE-13** Blank or invalid calibration, or the wrong MCU: transmit locked, receive works (TX-13 – TX-15).
> - **SAFE-14** Unintended transmit: a PTT held at power-on, VOX, KISS and remote PTT are all guarded.
>     - **SAFE-14.1** A PTT held at power-on is ignored until released: no transmission until every PTT input (PE3, PE2 and PE6) has read released at least once after boot.
>     - **SAFE-14.2** One held longer than 1 s from boot shows "PTT stuck" with its name ("PTT A", "PTT B", "side PTT" for the connector's PE6, joined with " + ") as a popup in the middle of the screen, over any other toast, from home's first draw, kept up while held and 2 s after it is let go (one let go before home first showed is named once for 2 s) (transmit builds).
>     - **SAFE-14.3** And a cable log line naming them ("ptt stuck: PTT A 1", then "ptt stuck: let go 0") (transmit builds).
>     - **SAFE-14.4** A PTT held at power-on is not a key at boot: it never opens the bring-up build's key test or skips the owner card (decision 149).
>     - **SAFE-14.5** VOX, KISS and digipeating are off by default.
>     - **SAFE-14.6** Remote PTT needs a 2 s keepalive (LINK-20).
> - **SAFE-15** Automatic transmissions need a callsign, are ≥ 30 s apart unless the user presses PTT (KISS frames excepted, KISS-2), have a capped length, and never go while the user transmits or the channel is busy.
> - **SAFE-16** Decoders have no path to the transmit command.
> - **SAFE-17** Every transmission is limited in time and duty; crossband is never on at power-up.
>     - **SAFE-17.1** Every transmission has a timeout (TX-30, XB-9).
>     - **SAFE-17.2** Every transmission has the duty limit (TX-31, XB-10).
>     - **SAFE-17.3** Crossband is never on at power-up (XB-1).
> - **SAFE-18** Battery cut-off refuses transmit, and power-off unkeys cleanly first (TX-32, TX-33).
> - **SAFE-19** Nothing keys the transmitter as an alarm or by remote command: no SOS remote alarm, no kill or stun.
> - **SAFE-20** The band relay (PC4, an Omron G6K) is a mechanical wear part, so only a deliberate user action moves it: tuning or switching the active slot, HF mode moving between its receivers (HF-11), or PTT on a slot that needs the other state (WATCH-12). Nothing automatic moves it: watch, scan (priority and smart checks included), background jobs, band scope and sweeps, tone search, the frequency counter, the crossband repeater, decoders, or link, KISS and terminal commands other than tuning the active slot. Anything that would need it is refused or cancelled, saying why (WATCH-11, SCAN-14, TX-37).
> - **SAFE-21** It never moves with RF present: not while keyed, in the unkey wait, or with any TX select on. Before it moves, the receiving chip is muted and its RX select cleared; after, the path state machine waits 10 ms (the G6K datasheet gives 3 ms operate and release) before selecting the new path and unmuting.
> - **SAFE-22** A guard in the path state machine: more than 10 relay switches in a minute is treated as a bug. The relay holds where it is, the event log records "Relay switching too often", and further switches that minute are refused except to the safe state.
> - **SAFE-23** This matches stock: it never moves the relay during transmit, and runs the SI4732 only with it released (`docs/hardware.md` §7.3).
> - **SAFE-24** A bench test (decision 114, TERM-29) may hold both band receive selects on, VHF RX (PB0) and UHF RX (PE12), the one case of two receive selects at once: the receive path moving between VHF and UHF then switches no pin, and Battery Save's sleep leaves both on. Never the HF select and never with the relay energised: refused there, and HF mode and the safe state drop it. Every key-up clears both before any TX select (the crossband repeater's clears the transmitting chip's band select and keeps the receiving one, XB-6); the hold stays asked for and the unkey sets both again. RAM only, off at boot.

### Under the hood


### Settled details

- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - SAFE-9: installing has already erased the rest of stock's data.
  - SAFE-20: decided Oct 6, 2026.
  - SAFE-24: decision 114, Oct 13, 2026. Stock never holds two receive selects on to listen, but its crossband repeater runs one band's receive select beside the other band's keyed PA through the same diplexer (`analysis/crossband_repeat.md` §5, noted Oct 24, 2026), a harsher case than two receive selects.

---

