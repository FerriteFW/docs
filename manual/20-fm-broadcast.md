## 20. FM broadcast receiver

### What it's for

FM broadcast on the SI4732, with RDS, on any home slot tuned into the broadcast band (decision 352: there is no separate FM screen). AM, shortwave, long wave and SSB are in HF mode (chapter 20a).

### Using it

**On a home slot.** Tune any slot (A, B or C) into the broadcast FM band, 87.5–108.0 MHz (76–95 MHz with region Japan), by VFO, typed frequency or a stored channel: it plays broadcast FM on the SI4732 by itself, no menu. Tune it out and it's a two-way slot again. For broadcast below 87.5 MHz (64–108), set the slot's mode to **WFM** (MENU 3).

1. Its card shows the frequency, STEREO, the SNR, the station's RDS radio text (the whole 64 characters once it has arrived; the station name only when it sends no text) and the signal. When the station sends its programme type, the header names it in place of Broadcast ("VFO · Jazz").
2. **▲▼ or the knob** tune by the FM step (0 2 6 1, 100 kHz), **◀▶** seek the next station. **MENU** shows FM's settings instead of the slot's: step, AGC, radio monitor, sleep timer, and **5 Saved stations**.
3. Your other slots keep watching. When one of them is heard it takes the speaker and the broadcast goes quiet ("muted" on the card); the broadcast comes back 2 s after that slot's audio ends.
4. One slot plays broadcast at a time: tune a second slot into the band and the broadcast moves to it. The first then says "FM on B" and stays silent until you tune it out.
5. A slot on 18–64 MHz isn't heard while broadcast plays ("Watch off: relay"): the band relay stays released for FM. PTT on another slot stops the broadcast before transmitting and starts it again after.

**Saved stations are channels.** Tune a slot to the station and hold 9 to save it, like any channel, in any zone. MENU 5 on a broadcast slot lists them (the channel browser's Broadcast view, also in its views: every channel on 76–108 MHz); OK on one plays it on that slot. From the browser with no broadcast slot, it tunes the active slot there.

**Sleep timer.** With 0 2 6 4 set, the broadcast slot is quick-muted once the time is up ("Sleep timer: broadcast muted"); \* on it plays it again. A mute isn't saved, so it plays after a restart too.

### Screens

No mock-up yet.

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| 0 2 6 | FM broadcast | Its settings (below) | — |
| 0 2 6 1 | Step | 50, 100, 200 kHz | 100 kHz |
| 0 2 6 2 | AGC | Auto, Fixed 1 (the most gain) to Fixed 10 (the least) | Auto |
| 0 2 6 3 | Radio monitor | Off, on | On |
| 0 2 6 4 | Sleep timer | Off, 15–120 min | Off |

0 2 6 1 – 0 2 6 4 are also quick settings' rows on a broadcast slot (MENU on its card), with 5 Saved stations.

> **Spec: receiver**
>
> - **BCR-1** FM broadcast plays on a slot tuned into the band (BCR-21), on the SI4732 only and never a BK4829. MENU 0 2 6 (Channels) is its settings group (decision 352, Nov 3, 2026: the FM screen that 0 3 1 opened is retired; the slot is the receiver; decision 354, Nov 4: the settings moved from Tools to Channels).
> - **BCR-2** The broadcast slot's card shows what the station sends (BCR-26).
>     - **BCR-2.1** FM shows signal and SNR.
>     - **BCR-2.2** FM shows the RDS text (BCR-26).
>     - **BCR-2.3** FM shows the stereo pilot.
> - **BCR-3** FM's settings: 1 step, 2 AGC, 3 radio monitor, 4 sleep timer (0 2 6 1 – 0 2 6 4), also quick settings' rows on a broadcast slot (BCR-28).
> - **BCR-4** With radio monitor on (the default), the slots keep watching, and a slot that opens squelch interrupts the broadcast (BCR-24). Off, they still receive (the LED, the decoders, APRS) but are kept quiet while the broadcast plays, so none takes the speaker from it; their quick mutes and cards stay as they are. Tuned out of the band, or monitor on again, they are heard again (decision 352: before, the setting only changed the FM screen's text).
> - **BCR-5** The sleep timer quick-mutes the broadcast slot (HOME-15) once its time is up, counted from when the slot took the broadcast, with the toast "Sleep timer: broadcast muted"; the slot stays the broadcast slot and \* plays it again (decision 352: it ended the FM screen's broadcast before).
> - **BCR-6** The SI4732 is muted (hard mute) whenever it isn't the source being heard. No pin selects between audio sources.
> - **BCR-7** SI4732 volume is fixed at 56; the knob is the analog volume. *Deviation from stock*, which fixes it at 63 (decision 290): the SI4732's audio reaches PA2, the receive audio the DSP task captures (LINK-13.7), ahead of the knob, and at 63 it clipped there (black, Oct 25, 2026: 61 still clipped now and then, 59 at the edge, 57 clean); 56 leaves a step of margin. Broadcast's and HF's loudest level on the speaker is about 7 dB lower than stock's; the knob makes up for it.
> - **BCR-17** FM tunes the region's broadcast band only (BCR-21; the FM screen's 64–108 MHz went with it, decision 352).
> - **BCR-18** (Retired with the FM screen, decision 352: the broadcast slot's keys are BCR-25.)
> - **BCR-19** While broadcast plays (a broadcast slot), Battery Save keeps the BK4829 sleep cycle for the slots being watched (decision 73); its sleep and wake steps never touch the SI4732, its audio path or the speaker, so the broadcast plays on. With no slot needing a BK4829, both sleep for as long as the broadcast plays. While the broadcast plays, the sleep step sleeps only the BK4829s and leaves the band's receive path select (VHF RX PB0 or UHF RX PE12) on, so no select switches at Battery Save's rate (decision 113).
> - **BCR-20** The SI4732 input path follows stock: PA7 = PC5 = 0 for FM broadcast, 1/1 for AM, SW, SSB and CW (the LNA path), and PA7 = 1, PC5 = 0 when the BK4829 radio has the antenna after the SI4732 has been used; boot and the safe state drive both low, as stock's master init, and they stay low until the SI4732 is first used (stock sets 1/0 only on leaving broadcast).
> - **BCR-30** The RDS radio text is passed whole (64 characters) and shown once complete: every segment up to its end marker, or all 16 when the station sends none. An A/B change keeps the last text until the new one is complete; a new station starts with none.

> **Spec: broadcast slot**
>
> - **BCR-21** A slot whose frequency (VFO or channel) is in the broadcast FM band, 87.5–108.0 MHz (76–95 MHz with region Japan), ends included, is a broadcast slot: it plays broadcast FM on the SI4732 by itself, with no menu, and no BK4829 listens to it. Tuned out of the band it is a BK4829 slot again. The APRS slot never is (APRS-19). AM broadcast stays in HF mode.
> - **BCR-22** One slot plays broadcast at a time: the one that last came into the band (the active one first, if several came at once). Another slot in the band shows "FM on B" (the slot that has it), with no audio and no receiver, until it is tuned out. When the broadcast slot leaves the band, a slot still in it takes the broadcast.
> - **BCR-23** The broadcast slot is always on, whatever Watch says. The other slots watch as usual, except those needing the band relay (18–64 MHz), which aren't listened to while broadcast plays and show "Watch off: relay" (BCR-15).
> - **BCR-24** Audio: any amateur slot heard takes the speaker and mutes the broadcast at once. The broadcast returns 2 s after that slot's audio ends (its squelch tail); a new signal meanwhile starts the wait again.
> - **BCR-25** On the broadcast slot's card the knob and ▲▼ tune a VFO by the FM step (0 2 6 1) and ◀▶ seek; the station found is taken into the VFO. On a channel they step channels and zones as on any slot. A saved station picked from quick settings' 5 (BCR-31) plays in it.
> - **BCR-26** The broadcast card on home.
>     - **BCR-26.1** The broadcast card shows the frequency, the SNR and the signal, green while it plays.
>     - **BCR-26.2** It shows STEREO when the pilot is heard.
>     - **BCR-26.3** It shows the RDS text: the radio text whole (three lines on the large card, as much as fits on a small one); the station name only when there is no radio text; "No RDS" otherwise.
>     - **BCR-26.4** The state reads FM (playing) or off (another mode screen, or keyed).
>     - **BCR-26.5** It reads muted while a slot heard has the speaker.
>     - **BCR-26.6** The other two home layouts show the RDS text in place of the slot's settings.
>     - **BCR-26.7** Single + scope shows the signal in dBuV with the SNR and STEREO in a row under the frequency, the RDS text under them, and its S-meter shows the SI4732's signal on FM's own scale (0–70 dBuV, labelled 0–60) in place of the S scale, green while it plays.
>     - **BCR-26.8** While the slot plays a station that sends a programme type (RDS PTY), its name takes the place of "Broadcast" in the slot's header ("VFO · Classic rock", "012 · Jazz"). The names follow the region: the North American RBDS list in the US and Canada, the European RDS list elsewhere. "Broadcast" again when the station sends none (type 0) or the slot stops playing.
> - **BCR-27** One FM state: the broadcast slot's station is the broadcast; the Status page's Broadcast row says "FM 100.5 on A" (its OK opens 0 2 6).
> - **BCR-28** Quick settings (MENU) on a slot in the broadcast band are FM's: 1 step, 2 AGC, 3 radio monitor, 4 sleep timer, 0 More.
> - **BCR-29** The broadcast slot runs as the exclusive mode FM broadcast (MODE-1).
>     - **BCR-29.1** A mode screen (band scope, tone search, counter, HF mode, crossband) stops it while it is up.
>     - **BCR-29.2** With the broadcast slot active it takes the place of home's scope strip (HOME-14); with a normal slot active the strip sweeps beside it (MODE-5).
>     - **BCR-29.3** PTT stops it before key-up and starts it again after (TX-24).
>     - **BCR-29.4** The sleep timer mutes the broadcast slot (BCR-5); tuned out of the band it ends.
> - **BCR-32** The SI4732's FM settings are sent to it, at power-up and when they change (decision 292): de-emphasis 75 us in the US and Canada and 50 us elsewhere; the channel filter automatic (the Si4732 forces it wide otherwise); the seek band 87.5–108.0 MHz (76–95 MHz with region Japan) at the FM step (0 2 6 1); the AGC (0 2 6 2) Auto, or FM_AGC_OVERRIDE with a fixed index (Fixed 1 = index 0, the most gain, to Fixed 10 = 26, the least).
> - **BCR-33** WFM is a slot mode beside FM, NFM and AM (decision 353, as nicFW's tuner channels): a slot in WFM is a broadcast slot anywhere the SI4732's FM covers, 64–108 MHz, so the low band (OIRT 65.8–74, Japan below 87.5) plays without taking 64–87.5 from narrow-FM listening; in FM, NFM or AM a slot there is a two-way slot as before. Its tuning range is 64–108 MHz; outside it a WFM slot receives as wide FM on the BK4829; it never transmits ("receive only here"). Its mode number is 6 (after HF's USB, LSB and CW).
> - **BCR-31** Saved stations are channels; there are no FM presets (decision 258).
>     - **BCR-31.1** A station is saved like any channel: hold 9 on a VFO tuned to it (KEY-23), into any zone.
>     - **BCR-31.2** Quick settings' 5 on a broadcast slot opens the channel browser's Broadcast view: every channel on 76–108 MHz (the broadcast band of every region, BCR-21), in number order, whatever its zone. With none it says "No stations saved" and how to save one.
>     - **BCR-31.3** OK on a station there plays it on the broadcast slot (its VFO, BCR-25), or with none tunes the active slot's VFO there, which makes it the broadcast slot (not the APRS slot: "APRS slot: pick A or B"); then back where it was picked from.
>     - **BCR-31.4** The Broadcast view is also in the browser's views (MENU 0 2 1), after Marine (CHAN-14).

> **Spec: SSB patch**
>
> - **BCR-8** (Moved to ch 20a, HF-17.)
> - **BCR-9** (Moved to ch 20a, HF-18.)
> - **BCR-10** (Moved to ch 20a, HF-19.)
> - **BCR-11** (Moved to ch 20a, HF-20.)
> - **BCR-12** (Moved to ch 20a, HF-21.)

> **Spec: input path and safety**
>
> - **BCR-13** PA6 (SI4732 reset) is held low from boot. Before power-up, the driver pulses it low for at least 10 ms, then releases it.
> - **BCR-14** PA7/PC5 are set only by the Radio task's path state machine. FM is 0/0, matching stock (to confirm on the bench); AM/SW/SSB is HF mode's (HF-16).
> - **BCR-15** The band relay (PC4) is released in FM broadcast, as in stock. A slot needing the relay (18–64 MHz) isn't watched while broadcast plays, and its card says "Watch off: relay". The relay never switches while either chip transmits.
> - **BCR-16** PTT first leaves FM broadcast: the SI4732 is muted and its input switched away before key-up.

### Under the hood


### Status

No mock-up. FM is in 1e. FM with RDS and radio monitor are in 2e; the presets gave way to saved channels (BCR-31, decision 258, Oct 22, 2026). The broadcast slot (BCR-21 – BCR-29) and the whole radio text (BCR-30) are built and tested in the simulators (Oct 12, 2026); on the radio still to try. Driver done and tested on the PC, not yet run on a radio. The sleep timer (0 2 6 4, BCR-5) is wired since Oct 8, 2026 (decision 96): the broadcast ends and home shows once its time is up.


### Settled details

- With radio monitor on, the broadcast comes back 2 s after the slot that interrupted it closes (decided Oct 6, 2026; BCR-24, built Oct 12, 2026).
- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - BCR-2: Changed Oct 3, 2026: AM, SW, LW and SSB moved to HF mode, ch 20a.
  - BCR-18: the code as built, Oct 6, 2026.
  - BCR-19: decision 73, Oct 7, 2026.
  - BCR-20: decision 76; "until the SI4732 is first used" spelled out Oct 15, 2026 (a bench test expected 1/0 straight after boot).
  - BCR-1, BCR-3, BCR-18: changed Oct 12, 2026 (decision 107): MENU 0 3 1 opens the screen (was 0 3 1 6); its settings moved into its options.
  - BCR-19: decision 73 restored Oct 12, 2026 (user): the change to "receivers stay awake" made with decision 107 was reverted after the radio showed chip 0 awake through a broadcast at Battery Save 1. Code: the sleep step must leave the SI4732 audio alone (next batch). Built Oct 12, 2026: broadcast no longer keeps the BK4829s awake; the sleep step clears only a BK4829 receive select and leaves the speaker as the broadcast has it.
  - BCR-21 – BCR-30: decision 107, Oct 12, 2026 (UI backlog 9 – 11).
  - BCR-19: changed Oct 13, 2026 (decision 113): the receive select stays on through the sleep while a broadcast plays. On the black radio the broadcast clicked at Battery Save's rate; the BK4829 sleep and wake writes over the cable were silent, the select switching was not. Stock clears the select in sleep (`rf_path(band, 0)`, `analysis/battery_save.md`); Ferrite still does without a broadcast.
  - BCR-3, BCR-18, BCR-25, BCR-28, BCR-31: changed Oct 22, 2026 (decision 258): the 20 FM presets (once 0 3 1 1, a screen of their own) had no way to be stored on the radio; saved stations are channels, and OK on the FM screen opens them. The options renumbered (step 0 2 6 1, AGC 0 2 6 2, radio monitor 0 2 6 3, sleep timer 0 2 6 4).
  - BCR-26, BCR-29: changed Oct 13, 2026 (decision 115): single + scope shows the broadcast slot's signal, SNR and stereo pilot, its S-meter on the SI4732's signal (UI backlog 12's follow-up, seen on the black radio: no SNR, S-meter at S1); the strip sweeps beside a broadcast another slot plays (MODE-5).
  - BCR-1, BCR-3, BCR-27: changed Nov 4, 2026 (decision 354): the settings moved from Tools (0 3 1) to Channels (0 2 6).

### Open points

- Stock seeks 65–108 MHz; Ferrite tunes from 64 MHz (BCR-17). Check the SI4732 hears 64–65 MHz on this board.

---

