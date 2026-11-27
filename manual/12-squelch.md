## 12. Squelch and monitor

### What it's for

Squelch keeps the speaker quiet until a signal is there. Monitor opens it on demand.

### Using it

- **Set squelch:** hold SIDE1 and turn the knob (or ▲▼); you hear it as you set it. Or MENU 1, with a live signal meter.
- **Monitor:** hold SIDE1 to listen with squelch open. Tap SIDE1 to latch it; tap again to release.
- **Per channel:** the channel's squelch override (hold ABC).
- **Fine control:** MENU 0 9 9 1 sets the thresholds per band.

### Screens

| | |
| --- | --- |
| ![Squelch editor](img/screens/MenuEdit.png) | |
| MENU 1, OK | |

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| MENU 1 | Squelch | 0–9 | 4 |
| 0 9 5 | Squelch | Chip, software | Chip (SQL-18.7) |
| 0 9 9 1 | Advanced squelch, per band | Noise open, noise ceiling, RSSI open, glitch, hysteresis | Table values |
| Channel | Squelch override | Global, 0–9 | Global |

> **Spec: squelch**
>
> - **SQL-1** Squelch uses both noise and signal strength. Each level 0–9 sets noise open, noise ceiling, RSSI open, glitch and hysteresis from a table.
> - **SQL-2** Advanced settings per band replace the table values for that band.
> - **SQL-3** The close threshold sits one hysteresis beyond the open one, so a fading signal doesn't chatter.
> - **SQL-4** Above the noise ceiling the squelch never opens, whatever the signal.
> - **SQL-5** *(retired, decision 269: the software squelch closes at once when the carrier goes; 0 9 5's squelch tail was never built and its number is SQL-18.3's)* The squelch stays open for the tail time after the signal goes.
> - **SQL-6** A channel's squelch override beats the slot's level. Global (the default for a new channel) uses the slot's own level; 0–9 are the channel's own. Stored as 0 = Global, 1–10 = levels 0–9, so every level fits. SIDE1 + knob on a Global channel moves the slot's level and leaves the channel Global.
> - **SQL-7** Changing the level is live: audio opens and closes as you turn.
>     - **SQL-7.1** Setting the level ends the hold's monitor: SIDE1 held past its long press opens monitor (SQL-9.1), and the first step of the level closes it, so the squelch opens and closes with the level as it turns (it stayed open: "Open: you hear it" at any level). A monitor latched with a tap stays on. (A review of Nov 20, 2026.)
>     - **SQL-7.2** A new level goes to the chip holding the slot as its thresholds alone, with no retune: the audio carries on, and the software squelch keeps its state with the new limits (each step retuned the chip and dropped the audio). (A review of Nov 20, 2026.)
> - **SQL-8** Opening or closing the squelch holds the receiver on for 10 s; an open squelch keeps it awake (chapter 33).

> **Spec: monitor**
>
> - **SQL-9** SIDE1 is the monitor key.
>     - **SQL-9.1** SIDE1 held: squelch open while held.
>     - **SQL-9.2** SIDE1 tapped: open until tapped again.
>     - **SQL-9.3** SIDE1 is the monitor key on every screen that doesn't give it a job of its own, menus and Satellites included, and with the keys locked (SQL-11). The screens that keep SIDE1: home's SIDE1 + knob or ▲▼ (squelch) and ◀▶ (clarifier), the squelch screen, the band scope (listen), HF mode, the crossband repeater and the key test; the frequency counter has no audio, so SIDE1 does nothing there. Decision 421.
>     - **SQL-9.4** Monitor opens the audio whatever else holds the receiver: home's scope strip goes back to the monitored slot and stays on it, open, and on the satellite pass page the downlink opens. Before, both kept their own squelch, and monitor worked only once a menu had stopped the strip. Decision 421.
> - **SQL-10** SIDE1 + knob or ▲▼ sets the level from home without opening a menu.
> - **SQL-11** Monitor and squelch work while the keys are locked.
> - **SQL-12** The squelch screen shows the noise floor and the signal.
>     - **SQL-12.1** The squelch screen (SIDE1 + knob or ▲▼) shows the noise floor beside the live signal: the signal while the squelch is closed, smoothed (an eighth of each reading).
>     - **SQL-12.2** With a carrier, how far it is above the floor ("Noise floor -121 dBm, signal +36 dB").
>     - **SQL-12.3** No other meter styles: bars or dBm on the cards (0 7 3 1). dBm shows the level as a number ("-93 dBm", green while the squelch is open) where the bars and their S-reading are; on watch + activity's cards, whose state has no bars, the number takes the S-reading's place beside RX ("RX -93 dBm"). Every home layout follows the setting (ferrite#216).
>     - **SQL-12.4** Home's and the watch's S-meters show the level while the squelch is open or the slot is monitored (SQL-9), and are empty while it is closed, as stock (decision 474). The level under the threshold, the signal or the band's noise, is on the squelch screen (SQL-12.1) and the squelch editor's "Signal now" bar, and with monitor. A slot no chip reads (not active, not watched, not tuned for a scan) shows an empty meter rather than its last level (ferrite#237). The crossband, counter and tone search screens show the level as read, open or closed.
> - **SQL-14** A tapped (latched) monitor shows MON on the slot's card, where RX and idle show, and nowhere in the status bar. Built for the tap; monitor while held comes with the Radio task's squelch (milestone 2).
>     - **SQL-14.1** Making another slot active (SLOT, the link's or terminal's `slot X active`, Low Power Mode giving a broadcast slot's place to A) turns a monitor latched on the slot left off, with a toast ("Monitor off · slot changed"). A latch held the watch on its slot (WATCH-3.2), so the new active slot heard nothing (ferrite#129).
> - **SQL-13** Level 0 is squelch off: audio always heard, shown "0 (open)" in menus.
>     - **SQL-13.1** Level 0 and monitor open the audio, not the carrier: busy lockout (TX-21), the APRS slot's busy check, the green LED, the receive activity that wakes the screen, the Activity history and DTMF decoding go by a carrier as the squelch decided it (each was set off by level 0's always-open or by monitor: PTT refused on an empty channel, the LED always lit). Battery Save's hold and VOX's block still go by the audio. On home's scope strip, level 0 holds the strip on its slot (SQL-13.2). (A review of Nov 20, 2026.)
>     - **SQL-13.2** On home's scope strip (the single + scope layout, MODE-5), level 0 on the strip's slot holds the strip on that slot's frequency, open, as monitor does (SQL-9.4): the strip doesn't sweep while its slot is at 0, and sweeps again from the next level up (once the squelch closes). Not while the slot is muted or off (HOME-15).
> - **SQL-15** The level table is stock's (0x0801E64C, checked in the disassembly Oct 12, 2026): level n opens at the calibration's 0xF0C0[n] and closes at 0xF0D0[n] (REG_78, 0.5 dB steps), each less the band's RSSI offset while the offset is below the open value: ≥ 400 MHz 0xF0E0[(MHz−400)/10, at most 12], 300–400 0xF110[(MHz−350)/5], 130–180 0xF0F0[(MHz−130)/5, at most 9], 200–300 0xF100[(MHz−200)/5] (280–299 read on into 0xF110), 15–100 0xF170[(MHz−15)/5, at most 16]. 108–130 MHz has no offset: open at 0xF0D0[n], close 10 below. Programmed whenever a chip is tuned to a slot, only when the values change. Not copied from stock (decision 222), each taking the nearest calibrated point instead: its out-of-table read at 300–345 MHz (Ferrite uses the 350 MHz entry); 100–108 MHz (the 15–100 table's last entry) and 180–200 MHz (0xF0F0[9], the 175 MHz entry), where stock has no table and leaves the RSSI open threshold at 0 whatever the level; and an erased table entry (0xFF: both radios' 0xF100[13–15], 265–279 MHz, and 0xF170[16], 95–100 MHz), which stock takes as an offset too big to apply, takes the nearest programmed entry below it. Its leftover close byte where no offset applies isn't copied either (Ferrite writes 0).
> - **SQL-16** Noise squelch is stock's, from calibration.
>     - **SQL-16.1** Noise squelch is stock's: REG_4F = n << 8 | (n − hysteresis), n by band class from 0xF210 bytes 5–8 (≥ 400 MHz, everything else, 200–300, 300–400 MHz) and the hysteresis in byte 9.
>     - **SQL-16.2** 26.020–26.110 MHz gets stock's fixed 0x2322.
>     - **SQL-16.3** Stock writes no glitch thresholds here, nor does Ferrite.
>     - **SQL-16.4** Blank calibration: the defaults stock compiles in, receive only (CAL-5).
> - **SQL-17** The squelch's open delay (REG_4E bits 13–11, how long the open conditions must hold before the chip reports open) is stock's 7, the longest, for ordinary receive, keeping its debounce, and 0 while the chip listens to a scan step or priority look (SCAN-20.1) or home's strip looks at the active frequency (MODE-5), so a carrier reads open within the step, and on the APRS slot (C while APRS mode, KISS or beacons hold it: APRS-21.1, APRS-29), so a packet's carrier reads open within C's turn. A scan stopped on a hit, the strip held on a call and the band scope's listen are ordinary receive. Written only when it changes, and again after the chip sleeps.
>     - **SQL-17.1** The open delay is REG_4E[15:12] on the BK4829 (its register table; 0x3815: open delay 3, close delay 8): a scan step or priority look writes 0 there and keeps the close delay in [11:8], ordinary receive stock's 3. The driver wrote bits 13:11, the BK4819's layout, so a scan step's 0 cleared the close delay too. (A review of Nov 20, 2026.)
> - **SQL-18** Software squelch (decision 269; since SQL-18.7 the choice under 0 9 5, the chip's decision the default): on FM the Radio task decides open and closed itself, each 10 ms tick, from the chip's RSSI (REG_67) and noise (REG_65), with the thresholds SQL-15 and SQL-16 give the chip (the chip keeps them, and its own squelch, for the screens that use it). AM keeps the chip's decision.
>     - **SQL-18.1** Closed, it opens when the RSSI is at or over the open threshold and the noise at or under the noise open threshold: on three readings in a row for ordinary receive (30 ms, in place of the chip's open delay, SQL-17; decision 293), on the first for a scan step or a priority look.
>     - **SQL-18.2** Open, it closes the moment the noise reaches the noise ceiling, or 3 over the noise open threshold if the chip's ceiling is closer (decision 293; the carrier has gone: no squelch tail), or when the RSSI stays under the close threshold for three readings in a row (30 ms; a fading signal rides a shorter dip). A retuned chip starts closed.
>     - **SQL-18.3** 0 9 5 Squelch: Chip (the default since SQL-18.7), the chip's own decision as stock, or Software (SQL-18); saved with the settings, the terminal's `set 0 9 5 software` too. Stored at the end of the settings record, apart from 0.9.4's byte: every radio coming from 0.9.4 reads Chip, whatever it had. The Advanced squelch page (0 9 9 1) says which decides. A bench build's cable log has each software change with its noise, RSSI and what the chip said.
>     - **SQL-18.4** The APRS slot keeps the chip's decision (decision 278): it holds through a single noisy reading and has the chip's tail, so a packet's end and its checksum reach the decoder. C is muted most of the time in APRS mode, so the software squelch's quick close bought nothing there, and its one-reading close at the noise ceiling cut packets short.
>     - **SQL-18.5** The software squelch counts time, not readings: each reading counts for the time since the one before (10 ms in watch or scan, 50 ms on a lone slot). It opens after 30 ms of passing readings and at least two of them (a scan step on the first), fades after 30 ms under the close threshold and at least two readings, and closes at the noise ceiling on two readings in a row, not one. At the 10 ms tick that is three readings to open or fade, as before; at 50 ms it opens in 100 ms (was 150), inside Battery Save's 180 ms wake window, and one noisy reading no longer chops a weak signal for 150 ms. (A review of Nov 20, 2026.)
>     - **SQL-18.6** A chip back from sleep, or receiving again after a transmission, starts with its software squelch closed, as a retuned one does (it carried the state from before). (A review of Nov 20, 2026.)
>     - **SQL-18.7** The chip decides by default, as stock (decision 425): its squelch bit (REG_0C bit 1: RSSI, noise and glitch, with its open and close delays), under stock's debounce: receive opens once the bit has read open for 30 ms and at least two readings (stock's three polls at its 10 ms loop; a scan step or priority look on the first), and ends once it has read closed for 100 ms and at least two readings (stock's ten closed polls), so a weak, fluttering signal rides through. AM too. Users found stock's squelch worked where Ferrite's software squelch didn't; on black with the bladeRF (Nov 21, 2026), at the edge of opening the chip held a 1 kHz tone open 2-10 times as long as the software squelch, with fewer drops; strong signals held in both. (Stock comparison of Nov 21, 2026.)
>     - **SQL-18.8** An open squelch's CTCSS or DCS match holds through 100 ms and at least two readings of loss (stock's count of 10), so a missed detection doesn't mute the audio; a closed squelch ends it at once.
>     - **SQL-18.9** The receive set-up writes REG_37 0x9F1F first and the transmit set-up 0x9D1F first, as stock's (Ferrite left the start-up's 0x9D1F for receive, the factory calibration having been made at stock's); then receive off, the frequency and bandwidth, the squelch thresholds (when they changed, SQL-15), the demodulator, the sub-tone and receive on, so the chip never decides on the old thresholds at the new frequency.
>     - **SQL-18.10** A receiving chip retuned with only its frequency changed (a scan step, a watch turn to a slot set up the same, a Doppler step, the clarifier) gets the frequency, its thresholds when they changed, the sub-tone detector, then receive on (0x0200, 0xBFF1): never REG_30 = 0 nor REG_37, so its AF DAC stays on. A turn to another slot mutes first; a step on the same slot keeps its audio. SQL-18.9's full order stays for a chip waking, after a transmit or any other use, or when anything but the frequency changes. 0.9.5's full order on every tune clicked in whatever the shared amplifier carried (console#51, ferrite#70, #79; decision 433). Beside a broadcast a turn to a slot set up otherwise keeps receive on too (BCR-23.2).
> - **SQL-19** The APRS slot's squelch over the chip's decision (SQL-18.4; decision 298). Alex, Oct 27: "the sql seems to ping open a LOT randomly".
>     - **SQL-19.1** Closed, it opens on the chip's open on two 10 ms ticks in a row; a single tick's open is a spike and is ignored.
>     - **SQL-19.2** A retuned chip's opens in its first 30 ms are ignored (on a shared VHF chip C is retuned for each turn).
>     - **SQL-19.3** Open, it follows the chip: the chip's hold through a noisy reading and its tail stay (SQL-18.4).
>     - **SQL-19.4** Counts since power-on, both chips: opens, opens shorter than 50 ms, spikes ignored, opens ignored while settling; on the home readback's own line `aprs_sq opens=N short=N spikes=N settle=N` while C is the APRS slot, and each open's length in a bench build's cable log ("aprs sq open ms").
>     - **SQL-19.5** The APRS slot receives with the chip's receive noise gate (REG_28 bit 8) and AFC off and its 300 Hz high-pass and de-emphasis off (APRS-55, decision 309); the squelch's thresholds, open delay and decisions (SQL-17, SQL-18.4, SQL-19) are as before.
> - **SQL-20** Open beep (decision 402; **not built yet**: specified only, no release has it, so there is no setting to look for): a tone as the squelch opens, so a quiet channel announces a signal.
>     - **SQL-20.1** Set per channel (the channel's options, Console's channel list) and per VFO slot; the choices are the end tones' (TONE-10.2): Off (the default), Beep, Two-tone up, Two-tone down, Chirp, Quindar. No radio-wide setting.
>     - **SQL-20.2** With an open beep set, the slot's audio waits 70 ms after the squelch opens: with the software squelch's 30 ms (SQL-18.1), the signal has held about 100 ms. Shorter opens stay silent. Only the speaker waits: the squelch, the watch, scans and the decoders see the open as before.
>     - **SQL-20.3** The tone plays from the MCU (SND-11's key-beep path, at the key beeps' volume) over the received audio: the audio opens with the tone and isn't muted under it, so nothing after the wait is lost. The Radio task steps it each tick and doesn't wait through it; it stops when the audio does. Skipped if DAC1 is busy with another sound.
>     - **SQL-20.4** It plays each time the speaker opens to the slot: when its squelch opens, when the watch turns the audio to it, and when a scan stops on a signal. Never on the APRS slot, nor for a latched monitor, nor while keyed.
>     - **SQL-20.5** With 0 9 5 at Chip, the 70 ms is timed from the chip's open.
>     - **SQL-20.6** Stored in the channel record's byte 31, bits 5-7 (0 = Off, 1-5 the tones), and for a VFO in its saved settings' flags byte, bits 2-4 (the link's channel records too): no format change; an older writer's 0 reads Off.
>     - **SQL-20.7** Set on the tone picker's second page (MENU 4, ▼ past TX): on a channel below its end tone and tail, on a VFO alone; # is Off. The terminal's `ch` line has `openbeep=off|beep|up|down|chirp|quindar`.
> - **SQL-21** An exclusive mode (HF mode, the satellite screen, the crossband repeater, the scope, the frequency counter, tone search) reads only its own slots: the scope its strip's slot while it listens there, tone search its slot, crossband its two sides, the others none. Every other slot shows as not read for as long as the mode runs: squelch closed, no carrier (so nothing is busy for busy lockout, TX-21, or the APRS slot's clear-channel check), an empty meter (SQL-12.4), and the APRS slot's squelch closed to the decoder, so its capture stops and the core clocks down (PWR-26.9). The watch takes such a slot as closed when it resumes, with no hang time. Before 0.9.8 each kept the state it had when the mode started: C caught mid-packet stayed open, held the core at full clock (about 20 mA more) and failed every beacon as busy (ferrite#132).

### Under the hood


### Status

Squelch editor mock-up approved (0b). Basic squelch in 1e; advanced squelch in milestone 2. Done when all SQL rules pass on the radio on 2 m and 70 cm.


### Settled details

- Level 0 is squelch open: audio always heard, like a permanent monitor; 1–9 are thresholds (decided Oct 6, 2026).
- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - SQL-6: decided Oct 4, 2026.
  - SQL-12: decided Oct 7, 2026; nicFW shows dBm with its floor.
  - SQL-14: decided Oct 6, 2026.
  - SQL-13: decided Oct 6, 2026.
  - SQL-13.2: decision 464 (Nov 25, 2026; ferrite#140, ferrite#44). Before, level 0 was heard on the strip only while a carrier held it there, so home stayed silent and the audio opened once a menu stopped the strip.
  - SQL-15: decision 76; changed Oct 20, 2026 (decision 222): the nearest calibrated point where stock has none (100–108, 180–200 MHz, erased entries).
  - SQL-21: decided Nov 25, 2026 (ferrite#132, found by the code audit of Nov 23, 2026).
  - SQL-17: decided Oct 15, 2026 (user, decision 166); the APRS slot added Oct 15, 2026 (decision 181, APRS-21.1). Stock writes REG_4E once, 0x3815 (open delay 7), in its start-up table (0x08009E94 in 0x08009D44) and never changes it (`analysis/bk4829_reg_access.csv`); its scan and watch get by with 70 ms per stop and three open polls. Ferrite's 50 ms step heard from 25 ms, and with the delay at 7 a channel scan never stopped on a carrier on the radio (Oct 15, 2026); with it at 0 it stopped on 2 m. A deviation from stock, scans and the strip only.

### Open points

- SQL-20.3 rests on the receive audio and the MCU's DAC1 being summed before the volume pot (`analysis/audio_path.md`: inferred, not measured). Check on the radio that the tone and a received signal play together cleanly; if not, the audio opens after the tone.

---

