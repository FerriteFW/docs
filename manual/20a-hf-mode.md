## 20a. HF mode

### What it's for

Everything below 64 MHz, on its own screen: long wave, medium wave and shortwave broadcast AM, USB, LSB and CW on the SI4732 (with the SSB patch), and everything from 18 MHz (17 m to 6 m, CB, the 13 m broadcast band) in FM and AM on BK4829 chip 1 through the band relay, with transmit where your region and Extend TX allow.

### Using it

1. **MENU 0 3 3** (Tools › HF mode). The radio sets the relay for the receiver in use (HF-11), loads the SSB patch into the SI4732 (a progress bar shows; it takes a while) and opens the HF screen.
2. Everything else pauses while you're here: watch, scan, APRS, decoders, background jobs and beacons. The crossband repeater can't run.
3. Tune:

| To | Press |
| --- | --- |
| Tune | Knob or ▲▼, by the step |
| Big step | SIDE2 + knob: 1 MHz |
| Change the step | ◀▶ (◀ bigger, ▶ smaller; the digit at the step is underlined) |
| Change band | SIDE1 (next), hold SIDE1 (the one before) |
| Change mode | SIDE2: AM, USB, LSB, CW, FM (as the frequency allows) |
| Filter width | \* narrower, # wider |
| Type a frequency | Digits (\* = point) |
| Seek | Hold 3 up, hold 1 down |
| AGC | Hold 4 (the next) |
| Recent list | Hold 7 (the last 10 frequencies) |
| Save as a channel | Hold 9 |
| HF options | Hold MENU |
| Transmit (18–64 MHz, where allowed) | PTT |
| Leave | BACK (back where you opened it), hold BACK (home) |

There are no channels or zones in HF mode: each band remembers its own VFO, and # shows the last 10 frequencies you used. Without the SSB patch, USB, LSB and CW are hidden; AM and chip 1 still work. Early V01 boards can't hear medium or long wave: that's a hardware fault, and the firmware can't detect it.

### Screens

| | |
| --- | --- |
| ![HF mode, 40 m USB](img/screens/HfMode.png) | ![HF mode, 49 m AM](img/screens/HfAm.png) |
| 7.074 MHz USB on 40 m (amateur list) | 6.070 MHz AM on 49 m (broadcast list) |

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| 0 3 3 | HF mode | Opens HF mode | — |
| Hold MENU | Step | AM 1, 5, 9, 10 kHz; USB/LSB/CW 10, 50, 100 Hz, 1 kHz; chip 1 as the home steps | 9 kHz (10 kHz in the Americas); 100 Hz |
| Hold MENU | Bandwidth | SI4732 AM: 6, 4, 3, 2 kHz; chip 1 wide, narrow | 6 kHz |
| Hold MENU | AGC | Auto, Fixed 1 (the most gain) to Fixed 10 (the least) | Auto |
| Hold MENU | Recent list | View, clear | Empty |
| 0 9 6 | SSB patch | Installed or not; source | — |

> **Spec: entering and leaving**
>
> - **HF-1** HF mode opens only from MENU 0 3 3. No hold-digit shortcut, no side key, and tuning past the lowest home band never enters it.
> - **HF-2** It refuses to open, saying why, while a chip transmits or the crossband repeater runs.
> - **HF-3** On entry: the relay is set for the receiver in use (HF-11) and the SI4732 powers up for the mode: AM without the patch, USB, LSB or CW with the patch streamed in behind a progress bar (HF-19). The same bar shows when the first USB, LSB or CW after AM loads it.
> - **HF-4** BACK leaves HF mode to the screen it was opened from (hold BACK: home): the SI4732 is muted and powered down, the relay follows the active slot again (WATCH-10), and everything paused resumes.
> - **HF-5** The status bar shows the screen name `HF`; `TW`/`DW` and `SCN` are absent while in HF mode.

> **Spec: what pauses**
>
> - **HF-6** While in HF mode, everything else pauses: watch, scan, APRS receive and beacons, digipeating, decoders, background jobs and SAME weather alerts. The Status page lists them as "Paused: HF mode", and with SAME on the status bar shows the alerts-paused bell (SBAR-18).
> - **HF-7** No automatic transmission runs in HF mode; KISS frames and remote `KEY` are refused with the reason.
> - **HF-8** Leaving resumes each paused feature as it was; nothing paused is changed or forgotten.

> **Spec: receivers and bands**
>
> - **HF-9** HF mode covers everything below 64 MHz: the SI4732 (LW, MW, SW broadcast AM; USB, LSB, CW with the patch) and BK4829 chip 1 through the relay (18–64 MHz: 17 m to 6 m and CB; FM and AM; a home slot there has NFM too, VFO-14).
> - **HF-10** The receiver follows from frequency and mode, as stock and nicFW do below 18 MHz: below 18 MHz the SI4732 (AM, and USB, LSB, CW with the patch); from 18 MHz chip 1 in FM and AM. Chip 1 has no SSB (its baseband route hears both sidebands), so from 18 MHz USB, LSB and CW stay on the SI4732 (HF-10.1). A mode a frequency doesn't offer becomes FM there, and AM below 18 MHz.
>     - **HF-10.1** *(experimental; decision 446)* USB, LSB and CW are offered up to 30 MHz on the SI4732 (17 m, 15 m, 12 m, 10 m), with the relay released for it (HF-11); from 30 MHz they aren't offered. The SI4732's documented range ends at 23 MHz (AN332's tune command; its brief says SW to 26.1 MHz) and the board's input past 18 MHz is untested, so results may vary: going into SSB past 18 MHz shows "Experimental" / "please report", and the step line names the receiver "SI4732 exp" there (the readback's `rx` "SI4732 EXP"). Receive only (HF-24). Reports of what works, band by band, are welcome on GitHub or Discord.
> - **HF-11** The relay follows the receiver in use, as stock does: energised while chip 1 is in use (18–64 MHz, FM or AM), released while the SI4732 is (below 18 MHz). Stock always releases it for the SI4732 (0x080114BC). It switches only when the receiver changes (tuning across 18 MHz), never while a chip is keyed or in the unkey wait; the receiver being left is muted first and the new one unmuted after the relay settles (it used to stay energised for all of HF mode).
> - **HF-12** Keys (decision 349, after nicFW's tuner keys): knob/▲▼ tune by the step; ◀▶ change the step (◀ a bigger one, ▶ a smaller), and the frequency's digit at that step is underlined; SIDE2 the next mode the frequency allows (a row of the modes shows for 1.5 s, the one picked lit); SIDE2 + knob 1 MHz; SIDE1 the next band in the list the mode picks (HF-32), hold SIDE1 the band before; \* a narrower filter, # a wider one (stopping at either end); digits frequency entry (\* point, then \* or OK enters, VFO-24); hold 3 / hold 1 seek up / down (HF-31); hold 4 the next AGC; hold 7 the recent list; hold 9 saves a channel (HF-26); hold MENU HF options (MENU-25), 0 there the full menu. Hold # stays key lock.
> - **HF-13** ABC and V/M (tapped or held) do nothing in HF mode; a toast says why.
> - **HF-14** Hold MENU opens HF options: step, bandwidth, AGC, LNA, fine tune (BFO), recent list.
> - **HF-15** The screen (decision 349), top to bottom: the mode as a coloured badge, the filter and AGC as chips, the band and receiver (SI4732 or chip 1) at the right; the frequency, its tuning digit underlined; the step, and the signal as S units (S1 to S9, then dB over: S9 is -73 dBm) with the SNR on the SI4732; the band strip, where the frequency sits in its band (an amateur band in CW, data and phone parts, a broadcast band whole, with its edges); the S-meter with its S-unit scale; the last two recent frequencies (or the frequency being typed); then the keys as a grid of eight (SIDE2 Mode, SIDE1 Band, \* # Filter, 0-9 Freq, hold 3 Seek (hold 1 seeks down), hold 4 AGC, hold 7 Recent, hold 9 Save), so none is hidden. The BFO offset shows in USB, LSB and CW once fine tune is built (HF-35); until then \* and # are the filter in every mode.
>     - **HF-15.1** On the SI4732 the level is its reading (dBµV at the chip) less an estimated 20 dB for the board's front end (an LNA before the chip's AM input), as dBm at the antenna: the chip reads 13-33 dBµV of indoor noise on the whip, which a receiver measured at the antenna shows as about S2-S5 (Alex, Nov 3: S6-S8 on noise was wrong; no real station heard yet to calibrate against, so an estimate). Chip 1 (from 18 MHz) gives dBm itself.
> - **HF-16** SI4732 audio follows BCR-6 and BCR-7. PA7/PC5 are 1/1 for the SI4732's AM input (to confirm on the bench), set only by the path state machine.

> **Spec: SSB patch**
>
> - **HF-17** Ferrite never ships, publishes or commits the patch. Each owner imports it from their own stock `.BTF`. (Was BCR-8.)
> - **HF-18** Import it with the flasher (`--ssb-from`: the patch is bundled after the image, and the first boot copies it to SPI flash and verifies its SHA-256; later boots find it installed and write nothing), or over the link with `SSB_WRITE` (the cable, or Bluetooth past the PIN while a PIN lock is on: LINK-8). Only the storage task writes it, to 0x008000 (layout 3, decision 333; 0x06B000 in layout 2). (Was BCR-9.)
> - **HF-19** As stock (decision 351): the SI4732 runs AM without the patch, and USB, LSB and CW with it: powered up with the patch flag (`POWER_UP 01 31 05`), 550 ms for the crystal, then the patch's 8-byte records streamed from SPI flash (a few seconds), then SSB_MODE (the filter's bandwidth, AVC on, AFC off), stock's AVC max gain and soft mute off. A change between USB, LSB and CW keeps the patch; a change to AM powers the chip up again without it, and back to a sideband loads it again. Stock waits 3 s at each such switch; Ferrite doesn't. (Was BCR-10.) The patch goes at a 3 µs I2C half period (about 150 kHz): at 1 µs the clock's low time was under the SI4732's 1.3 µs minimum (ferrite#88; decision 433).
>     - **HF-19.1** In USB, LSB and CW the chip tunes to the whole kHz and the rest goes on the BFO (SSB_BFO, Hz), so a step under 1 kHz moves only the BFO; CW is received on USB 700 Hz below the frequency shown, so a carrier on it is a 700 Hz tone. The filter's SSB bandwidths are 3, 2.2, 1.2 and 0.5 kHz (SSB_MODE's AUDIOBW). The BFO's sign (the chip hearing tune + BFO) is to confirm on a real signal.
> - **HF-20** With no verified patch, USB, LSB and CW are hidden and About says the patch isn't installed. AM and chip 1 still work. (Was BCR-11.)
> - **HF-21** As SAFE-9: a settings reset never erases the SSB patch. (Was BCR-12.)

> **Spec: transmit**
>
> - **HF-22** HF transmit (18–64 MHz, chip 1, FM or a home slot's NFM; AM is receive only) works in HF mode and from a home slot on those frequencies, under the same chapter 15 rules (TX-4).
> - **HF-23** In HF mode, any PTT (A, B, C or the side connector) transmits on the HF frequency, on chip 1 only, in FM (AM is receive only), where the region and Extend TX allow, with every chapter 15 check. It doesn't go home first (an exception to KEY-7).
>     - **HF-23.1** After any key-up in HF mode (PTT on 10 m or 6 m FM, or an automatic transmission) the HF receiver is set up again on the Radio task's next tick: its receive route, its tune and the speaker. The key-up leaves the transmit path's receive set-up and the speaker off, and the screen doesn't ask for HF mode again, so the receiver stayed silent until a retune (ferrite#130).
> - **HF-24** On an SI4732 frequency or mode (below 18 MHz, or USB, LSB, CW), PTT refuses: "Receive only here".
> - **HF-25** Before key-up the SI4732 is muted and its input switched away (TX-24); transmit is only possible on chip 1, so the relay is already energised (HF-11) and doesn't move.

> **Spec: memory**
>
> - **HF-26** HF mode's memories are channels (CHAN-26): hold 9 saves one (KEY-23), and recalling one opens HF mode on it.
> - **HF-27** Each HF band remembers its own VFO: frequency, mode, step, bandwidth, fine tune.
> - **HF-28** The recent list holds the last 10 frequencies used (frequency and mode), newest first, without duplicates. A frequency counts as used after 10 s on it or a transmission. OK on an entry tunes it.
>     - **HF-28.1** # clears the recent list only after the shared confirm ("Clear the recent list?", MENU-23), from the list's own page and from HF mode's recent row; an empty list has nothing to ask.
> - **HF-29** The HF VFOs and the recent list live in RAM while in HF mode and are written to their own SPI sector (0x084000) on leaving and at power-off, never while tuning.
> - **HF-30** HF transmit starts on Low (TX-36).

> **Spec: seek**
>
> - **HF-32** SIDE1 walks
> - **HF-33** Battery Save in HF mode is as in FM broadcast (BCR-19): the SI4732 stays awake while it plays and the BK4829 receivers you aren't using keep their sleep cycle.
> - **HF-35** The SI4732's AM settings are sent to it, at power-up and when they change (decision 292): the bandwidth (AM_CHANNEL_FILTER: 6, 4, 3 or 2 kHz), the AGC (Auto, or AM_AGC_OVERRIDE with a fixed index, Fixed 1 = index 0, the most gain, to Fixed 10 = 37, the least), stock's AVC max gain 0x7800 and soft mute off. Its seek steps by the band's channel spacing: 9 kHz on LW, MW 10 kHz in the US and Canada and 9 kHz elsewhere, 5 kHz on shortwave. LNA and a fine-tune (BFO) setting aren't offered yet: HF-19.1's 10 Hz steps tune SSB finely.
> - **HF-34** A band's step the first time it is tuned: 5 kHz on shortwave broadcast, 9 kHz on LW, MW 10 kHz in the US and Canada and 9 kHz elsewhere, 100 Hz on amateur bands in SSB or CW; after that the band keeps its own (HF-27). HF mode starts on 31 m at 5 kHz.
> - **HF-31** Hold 3 seeks up and hold 1 seeks down, as nicFW's tuner (LP-3, LP-1), with the SI4732's own seek: in AM below 18 MHz only (the SSB patch has no seek, and chip 1 isn't the SI4732); elsewhere a toast says so. It searches HF mode's SI4732 range (150 kHz to 18 MHz) and stops at its edge rather than wrapping round. HF mode keeps the frequency it stops on; a seek that finds nothing in 15 s is cancelled where it got to. The radio keeps working while it seeks (MODE-7.1): a retune, HF off or a new seek cancels it.

### Under the hood


### Status

No mock-up. Receive is roadmap 2e (Listen); SSB with patch import in 3e; transmit in milestone 4 (4a, measured in 4e). The firmware's Radio task takes HF mode (Oct 7, 2026, not yet run on a radio): the SI4732 below 18 MHz, chip 1 through the relay from 18 MHz (decision 322), both through the path machine with the HF receiver cause, and hold 3 / hold 1 seek (HF-31); SSB waits for the patch import. Done when LW, MW and SW AM, USB and LSB with the patch, and 10 m FM on chip 1 all receive on the radio; leaving resumes everything; and the recent list survives a power cycle.


### Settled details

- SIDE2 does nothing in HF mode, and there is no band scan; seek is hold 3 / hold 1 (HF-31).
- overload is left to the chip's AGC, as stock: AVC max gain 0x7800 (0x3103) and soft mute off (0x3302 = 0), written since decision 292 (before, the chip's defaults ran); a fixed AGC (HF-35) is the user's attenuation. No attenuator switching. AM noise on 690 kHz indoors read 2-2,635 at PA2 (black, Oct 25, 2026, volume 56): AM runs hotter there than FM; LINK-13.7's stream of HF audio clips on loud AM until a level is set for it.
- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - HF-10: decided Oct 7, 2026; stock uses the BK4829 there.
  - HF-11: changed Oct 6, 2026.
  - HF-22: changed Oct 3, 2026. Nov 24, 2026 (ferrite#84): a home slot's NFM there named.
  - HF-13, HF-26: changed Oct 14, 2026 (user, decision 159): hold 9 saves (hold V/M did); hold V/M joins V/M's toast, since the zone list means nothing in HF mode (KEY-23).
  - HF-32: decided Oct 7, 2026; nicFW's tuner has one LW/MW/SW list, stock a fixed band list.
  - HF-33: decided Oct 7, 2026. Checked Oct 12, 2026: HF mode puts every BK4829 it doesn't use to sleep (watch and scan pause, HF-8), so none needs the cycle; the sleep step never touches the SI4732 (BCR-19).
  - HF-31: decided Oct 7, 2026. Changed Oct 15, 2026 (decision 164): the seek band is HF mode's SI4732 range and the seek stops at its edge; the chip's own AM seek band (520-1710 kHz, never set) and its wrap sent a seek up from 9.4 MHz to 1.71 MHz on the radio. Oct 15, 2026 (decision 165): the screen gave up on a seek at 15 s from the key, just before the Radio task cancelled it at 15 s from its start and reported where it got to, so the screen kept the old frequency while the receiver sat elsewhere, and the next seek took that stale report as its landing (down from 9.4 MHz "landed" on 10.94 MHz); the screen now waits 17 s and takes a landing only when the receiver's report moves off where it was before the seek.

### Open points

None.

---

