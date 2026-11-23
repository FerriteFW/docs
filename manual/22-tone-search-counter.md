## 22. Tone search and frequency counter

### What it's for

**Tone search** finds the CTCSS tone or DCS code in use on the active slot. The **frequency counter** finds the frequency of a strong transmitter nearby.

### Using it

**Tone search:** MENU 0 3 5.

1. The search listens on the active slot. It shows "searching" with the elapsed time until it finds a tone.
2. **OK** applies what it found. On a VFO it sets the RX tone (and asks before setting TX too). On a channel it's loaded for now but not saved to the channel.
3. **BACK** cancels and leaves the tones as they were.

**Tone hint:** when a station comes in on a slot but your tone keeps it silent, the radio checks which tone it's sending and shows it on the slot's card: "Heard 88.5". Open quick settings (MENU) and press **OK** on Tones to use it; the radio asks before changing the TX tone too. On a channel, # in that question saves it to the channel.

**Frequency counter:** MENU 0 3 2.

1. Key the other transmitter close to the radio.
2. The counter shows its frequency and level and keeps a list of recent hits.
3. **OK** copies the frequency to the VFO.

### Screens

No mock-up yet.

> **Spec: tone search**
>
> - **TSRCH-1** MENU 0 3 5 searches on the active slot's frequency.
> - **TSRCH-2** The screen shows slot, frequency and signal. It also shows the result (CTCSS in Hz, or DCS code and polarity) or "searching" with the elapsed time, plus the last hits once two different tones have been heard (one would repeat the result).
> - **TSRCH-3** Detection uses the BK4829's scan detectors: REG_68 for CTCSS (read at the BK4829's own scale, about 20.38 counts per Hz: the BK4819's 20.64888 read 88.5 as 87.3), REG_69/6A for DCS. The searched slot's chip alone listens, on the slot's frequency with its audio muted (an exclusive mode: watch and scans pause, MODE-3's lease holds it); a reading counts when the next one agrees with the carrier there, and the result stays after the carrier until a different tone is found.
>     - **TSRCH-3.1** A CTCSS reading is the mean of the last four with the carrier before it is snapped to a tone (TSRCH-13); no carrier or no reading starts the four again. The detector wanders about ±1.4 % carrier to carrier, more than the 1.5 % between 250.3 and 254.1 Hz.
> - **TSRCH-4** OK sets the RX tone. The TX tone changes only after a second confirm.
> - **TSRCH-5** BACK leaves the slot's tones unchanged.
> - **TSRCH-9** On a channel, OK loads the found tone into the slot without saving the channel record; it lasts until you leave the channel; # saves it into the channel record.

> **Spec: tone hint**
>
> - **TSRCH-12** A slot held on a signal (the active slot, or a watched slot the watch holds for its audio) whose carrier has kept the noise squelch open for 0.5 s while its CTCSS or DCS tone squelch keeps the audio shut gets its tone measured: the Radio task switches that chip's sub-tone detectors to scan (TSRCH-3) for up to 1.2 s, then puts the slot's own tone detector back. The audio stays muted throughout, as it already was.
> - **TSRCH-13** What was heard shows on the slot's card in place of its state, in amber: "Heard 88.5" or "Heard D023I/D047N" (CTCSS snapped to the nearest standard tone, since the reading wanders about ±1.4 % carrier to carrier; a reading in the middle fifth between two tones, more than 2/5 of their gap from the nearer, shows nothing; DCS with its polarity, so a reversed code shows, and the code of the other polarity that sends the same bits, TONE-20.5), in all three home layouts. It never moves focus, switches slots or opens a screen. A tone that equals the slot's own shows nothing.
> - **TSRCH-14** The hint clears 30 s after the carrier was last heard, at once when the slot's frequency or receive tone changes, and when the tone squelch opens.
> - **TSRCH-15** One measurement per carrier: the next waits until the carrier drops and comes back. A carrier has dropped once the squelch has stayed shut 1 s: the slot's own retune (a new receive tone tunes the chip again) shuts it for a moment under the same carrier. None while transmitting, on a scanning slot, with monitor latched, on a slot with no receive tone, on the APRS slot, or in HF mode, FM broadcast or another exclusive mode. Watch and scan timing don't change.
> - **TSRCH-16** With a hint, quick settings' Tones row (MENU 4) shows the heard tone ("heard 88.5"; the slot's own beside it until 0.8.2, decision 372) and its help line says "OK uses the heard tone". OK sets the heard tone as the RX tone, then asks "Set the TX tone too?" (OK sets TX, BACK leaves it), as tone search does (TSRCH-4). On a channel the tones load into the slot without saving the record; # in the question saves the channel (TSRCH-9). Without a hint, OK on the row opens the tone editor as before.

> **Spec: frequency counter**
>
> - **TSRCH-6** MENU 0 3 2 opens the counter. It shows the strongest nearby transmitter's frequency and level, a hold, and the last hits.
> - **TSRCH-7** OK copies the frequency to the active slot's VFO; a slot on a channel switches to VFO mode, as the scope's OK does.
> - **TSRCH-10** The frequency counter's range.
>     - **TSRCH-10.1** The counter covers 64–1300 MHz with both BK4829s, each in its own range: chip 0 below 300 MHz, chip 1 from 300 MHz (its 630–756 MHz gap excepted).
>     - **TSRCH-10.2** It never moves the band relay (SAFE-20), so 18–64 MHz is not counted.
>     - **TSRCH-10.3** Both chips count at once, with both band receive paths on (SAFE-24): a strong, close carrier on one band can't keep the other band's chip from counting. A chip's reading counts only when it is in that chip's range and agrees with its reading before; the strongest reading of the last 2 s shows. If both paths can't be on (a slot has the band relay energised), the chips take turns, and a chip keeps its turn only while it has readings that count. Closing the counter turns the second path off again. Decision 420.
> - **TSRCH-11** # holds: the reading freezes on screen while the counter keeps listening; OK then copies the frozen frequency (TSRCH-7), and # again releases it.
> - **TSRCH-8** The counter only receives. It never keys the transmitter.

### Under the hood


### Status

No mock-ups. Tone search is in 2d and the counter in 2e. The tone hint (TSRCH-12 to TSRCH-16) is built on the PC; bench-confirm on the BK4829: how long the scan detectors take to settle (the BK4819 needs a few hundred ms; the probe waits up to 1.2 s), that switching between the slot's detector and the scan is silent, and that REG_68 reads a CTCSS tone with REG_51 in its DCS scan setting (`subtone_scan_on`: REG_51 = 51, CTC1 0x0AD7, as the BK4819 drivers' tone scan).


### Settled details

- The counter copies into the active slot's VFO; a slot on a channel switches to VFO mode, as the scope's Go does (decided Oct 6, 2026).
- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - TSRCH-2: changed Oct 3, 2026.
  - TSRCH-9: decided Oct 3, 2026; decided Oct 6, 2026; decided Oct 7, 2026.
  - TSRCH-7: decided Oct 6, 2026.
  - TSRCH-10: decided Oct 7, 2026; nicFW has a fast scanner on LP-7; stock's counter covers the VHF/UHF chips.
  - TSRCH-11: decided Oct 7, 2026.
  - TSRCH-3, TSRCH-13: the REG_68 scale and the 1 % snap, Oct 15, 2026 (decision 177): the clear radio's 88.5 read "T 87.3".
  - TSRCH-13: changed Oct 15, 2026 (decision 179): the nearest standard tone, refused only midway between two, replaced the 1 Hz / 1 % window: 88.5 read "T 89.6" after decision 177's scale and "T 87.3" before it, so the reading wanders and no window fits; a tone off the table is no longer shown to 0.1 Hz.
  - TSRCH-3: built Oct 15, 2026 (decision 168); until then the Radio task dropped the screen's command, so the search said "Searching" forever on the radio (the receiving session), while the simulator faked a result.
  - TSRCH-15: changed Oct 15, 2026 (decision 170): a drop is the squelch shut 1 s; the two-radio run measured a second time after a new receive tone, the retune's moment of shut squelch read as a drop.
  - TSRCH-12 to TSRCH-16: decided Oct 9, 2026 (decision 99). Neither stock nor nicFW has it: both offer only a tone scan you start by hand.

### Open points

None.

---

