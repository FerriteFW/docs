## 9. VFO and frequency entry

### What it's for

Tune any frequency the radio can receive, by stepping or by typing it.

### Using it

1. V/M puts the active slot in VFO mode. Each slot has its own VFO, remembered per band. Home VFOs tune 18 MHz and up in FM, NFM, AM or NAM (narrow AM, the airband's default), or WFM for broadcast FM anywhere 64–108 MHz (chapter 20); below 18 MHz, and USB, LSB and CW, are in HF mode (chapter 20a).
2. Knob or ▲▼ step by the slot's step; SIDE2 + knob steps 1 MHz; ◀▶ change band.
3. Type a frequency: digits, with \* as the point; OK enters it, or \* again once a digit follows the point (146 \* 52 \*), so one hand does it all. What you type is tuned exactly, never snapped to the step; entry shows the band, whether the value is on the step, and whether transmit is allowed there (VFO-12).
4. Hold ABC to edit the VFO: mode, RX tone, tone, offset, power, step, squelch, busy lock, reverse.
5. Hold 9 (or MENU 8) to save it as a channel; on a channel, hold 9 copies it to the VFO. For reverse, hold \* (the quick menu), then PTT A.

### Screens

| | |
| --- | --- |
| ![Editing a VFO in place](img/screens/HomeEdit.png) | ![Quick settings on a VFO](img/screens/MenuQuick.png) |
| Hold ABC, VFO | MENU, VFO |

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| MENU 2 | TX power | Low, mid, high | Low |
| MENU 3 | Mode | FM (wide), NFM (narrow), AM, NAM (narrow AM, for 8.33 kHz channels); the mode is the bandwidth (VFO-20) | By region: FM in the Americas, Australia and New Zealand, NFM elsewhere; NAM on the airband (SETUP-7, VFO-4.2) |
| MENU 4 | Tones | RX and TX each: off, CTCSS (50), DCS (104, normal or inverted) | Off |
| MENU 5 | Offset | Simplex, +, −, split (a TX frequency of its own); amount in kHz | 600 kHz on 2 m, 5 MHz on 70 cm |
| MENU 6 | Step | 10, 50, 100, 500 Hz; 1, 2.5, 5, 6.25, 8.33, 10, 12.5, 25, 50, 100 kHz | By region: 5 kHz on 2 m and 1.25 m in the US and Canada, else 12.5 kHz on VHF/UHF (VFO-18) |

> **Spec: VFO**
>
> - **VFO-1** One VFO per slot: frequency, mode (which is the bandwidth too, VFO-20), step, RX and TX tones, offset, power; remembered per band.
> - **VFO-2** The band comes from the frequency, via a fixed table: range, chip, RF path and relay, PA, default mode and step, TX allowed.
> - **VFO-3** Chip 0 serves VHF and 200–300 MHz; chip 1 serves 300 MHz and up, plus 18–64 MHz through the relay.
> - **VFO-4** Home VFOs and channels: FM, NFM, AM, NAM on either BK4829, and WFM on the SI4732 (a broadcast slot on 64–108 MHz, BCR-33). FM is 25 kHz and NFM 12.5 kHz (stock's and nicFW's Wide and Narrow); WFM is broadcast FM, as Icom, Yaesu, Kenwood and CHIRP name it. The Mode setting's help line says so: "FM, NFM, AM, NAM (8.33 kHz). WFM: broadcast RX." (decisions 417, 447). USB, LSB and CW exist only in HF mode, on the SI4732 (HF-10); the BK4829's SSB isn't used.
>     - **VFO-4.1** The Mode editor (MENU 3) shows each mode with its width: "FM · 25 kHz", "NFM · 12.5 kHz", "WFM · broadcast", "NAM · 8.33 kHz"; AM shows alone. The heading's default stays the name. Decision 417.
>     - **VFO-4.2** NAM is AM through the narrow receive filter (REG_43 0x4008, the one NFM uses; AM keeps stock's wide 0x3028), for 8.33 kHz airband channels: on the bench the wide filter passed a neighbour 8.33 kHz to one side at full strength, NAM rejects it on both sides and leaves the wanted AM signal within 1 dB, and it keeps ±5 kHz offset carriers on 25 kHz channels. Receive only, as AM (TX-20). The airband (108-137 MHz) defaults to NAM in every region; HF bands keep AM. Choosing the 8.33 kHz step (MENU 6) on an AM slot turns it to NAM. Stored as mode 7 (CHAN-23); CHIRP calls it NAM too. Channels and VFOs already in AM stay AM. Decision 447.
> - **VFO-5** Knob/▲▼ step by the slot's step; SIDE2 held, 1 MHz; ◀▶ step bands (NAV-2, NAV-3).
> - **VFO-6** RX and TX tones are set separately; that covers every cross-tone mode.
> - **VFO-7** The quick menu's PTT A (hold \* on home, then PTT A: HOME-17) toggles reverse (listen on the input): it stays until toggled again, the shift chip shows R, and the tones swap with the frequencies, so you hear the users' tone on the input and send the repeater's on the output (the Radio task swaps them with the Reverse parameter).
> - **VFO-8** Step is a VFO setting: on a channel it is greyed with "VFO only".
> - **VFO-9** Hold 9 on a VFO saves it as a channel (KEY-23; on a channel hold 9 is VFO-23). On 18–64 MHz it saves an HF channel (CHAN-22, CHAN-26). The save screen offers the first free channel number after the slot's last channel (wrapping) and the zone being browsed (none if none), both changeable before OK.
> - **VFO-10** Channel-only mode (0 9 3 2) hides VFO mode.
> - **VFO-16** Split, MENU 5's 4th choice, transmits on a frequency of its own (RX UHF and TX VHF, odd splits).
>   - **Choosing it:** turning onto it (knob or ◀▶, in the slot editor, MENU 5 or the channel editor) makes today's TX the split's and stays put, with a toast "Split: OK sets the TX frequency"; turning on leaves it like any other value.
>   - **Setting the TX:** OK on Split, in the value editor or the quick list (MENU 5), opens frequency entry for the TX frequency, prefilled; OK there sets it, BACK keeps the split's old TX (decided Oct 5, 2026: choosing it used to jump straight into entry, which took the knob away).
>   - **Other shifts and keys:** + and − keep the slot's amount: the band's (VFO-26), or one typed with hold 8. In VFO mode, retuning RX doesn't move a split's TX. Reverse swaps RX and TX in a split too. Hold 7 opens the four choices, Split among them.
>   - **Display:** home shows "SPLIT" in the shift slot and the TX frequency in the card header, "VFO · TX 146.520" (HOME-4; compact cards show "TX 146.520" in their shift column); the Transmit screen shows the real TX large and RX on its line (decided Oct 4, 2026).
>   - **Refused:** a split or shift whose TX needs the band relay in the other state from RX (one side below 64 MHz, TX-37) is refused when it's set: a toast says why, frequency entry stays open, and the old shift or split TX stays.
> - **VFO-26** The offset's amount: each band's default follows the region, and hold 8 types any amount. Decision 418.
>   - **VFO-26.1** Defaults: 600 kHz on 2 m, 1.6 MHz on 1.25 m and 5 MHz on 70 cm; in Europe (IARU Region 1) 70 cm takes 7.6 MHz. The usual direction (Add repeater, # on its Shift row) is down on 2 m below 147 MHz and on 70 cm in Europe, else up.
>   - **VFO-26.2** Hold 8 opens an entry for the amount in MHz (10 kHz to 100 MHz), empty, with the slot's offset now and the TX frequency the typed amount gives. OK keeps it in the direction the slot has (from simplex or split, the band's usual one); it follows RX as RX is tuned, unlike a split. Out of range, or refused by TX-37 or a channel's rules: a toast, and the entry stays.
>   - **VFO-26.3** Hold 7 opens the shift's four choices (simplex, +, −, Split) and stays until OK or BACK. + and − keep the slot's amount; from simplex or split, or on a new band, the band's.
>   - **VFO-26.4** On a channel, hold 7 and 8 do the same, through the channel's rules, and save it (EDIT-4).
>   - **VFO-26.5** In hold 8's entry ▲ makes the offset +, ▼ makes it −; a Shift row shows which, and the TX row follows at once. Without either it goes in the slot's direction (VFO-26.2). Decision 418.
>   - **VFO-26.6** Hold 7's editor shows, under each choice, where it transmits ("TX 147.120"; for Split, the split's TX). Decision 418.
> - **VFO-19** # does nothing in frequency entry: OK keeps a typed frequency, or it goes in by itself once complete (VFO-17); \* types the point, and after a digit past the point enters the frequency as OK does (VFO-24).
> - **VFO-20** The mode is the bandwidth: FM is wide, NFM narrow, AM keeps the wide filter and NAM takes the narrow one (VFO-4.2); there is no separate bandwidth setting. Quick settings row 3 is Mode; the edit grid's second cell is RX tone. A record or saved state from before with FM and its narrow flag set reads as NFM, and the record's narrow byte follows the mode. The terminal still reads `bw=` in older dumps (FM and NFM follow it) and no longer writes it.
> - **VFO-17** Typed frequencies go in without OK once they are whole: from three decimals on, as soon as the value sits on the step's grid, and always at five decimals. With a 5 kHz step 146.940 goes in at the last 0; with the 8.33 kHz step, three decimals within 50 Hz of a channel are that channel (118.008 is 118.00833, VFO-18.1); with 12.5 kHz 145.500 goes in at once, while 145.512 waits and a 5 makes it 145.5125. A leading 0 is a MHz digit, so 0 7 8 0 0 0 is 78.000 MHz. OK takes a shorter or off-grid entry at once, exactly as typed. While typing, MHz and three decimals are big and the 10 Hz digits small, as on the card, so nothing changes size.
> - **VFO-18** A band's default step follows the region: 2 m and 1.25 m take **5 kHz** in the US and Canada, where channels sit on 15 and 20 kHz spacing (146.520, 146.940, 147.225 aren't on a 12.5 or 25 kHz grid); elsewhere 2 m keeps 12.5 kHz (IARU Region 1). It applies when a VFO enters the band, at start-up, and when the region is set (setup, 0 9 4); a step the user picked is kept, and stored channels are never moved. Hold 6 / MENU 6 picks any step.
>     - **VFO-18.1** The 8.33 kHz step moves on the 8.33 kHz channel grid: each 25 kHz block at +0, +8.333 and +16.667 kHz, to the chips' 10 Hz (833 and 1667 above the block), so three steps are exactly 25 kHz and steps never drift (a flat 8.330 kHz drifted 100 Hz in 30 steps, ferrite#189). A step from a frequency off the grid goes from the channel nearest it. Decision 447.

> **Spec: frequency entry**
>
> - **VFO-11** A digit on home in VFO mode opens frequency entry; \* is the decimal point (and, once a digit follows it, OK: VFO-24).
> - **VFO-12** What's typed is what's tuned, to 10 Hz, never snapped to the step, as serious HTs do; the knob then steps from there. Entry shows the digits typed, the band, the step and whether the value is on it ("12.5 kHz, off it"), and whether transmit is allowed there or why not.
> - **VFO-13** Frequencies are kept in 10 Hz units and formatted by a fixed-point formatter, never `core::fmt`.
> - **VFO-14** Home VFOs tune 18 MHz and up; the home band list includes the HF bands 18–64 MHz (12 m, 10 m, CB, 6 m), in FM, NFM and AM (chip 1 through the relay, as on any band; USB, LSB and CW are HF mode's, HF-10.1). Entry below 18 MHz says "< 18 MHz: HF mode, MENU 0 3 3" (one line). A VFO in the broadcast FM band plays broadcast FM on the SI4732 (BCR-21).
> - **VFO-15** A home slot on 18–64 MHz needs the relay; the relay follows the active slot only (WATCH-10).
> - **VFO-21** Home VFOs and channels receive 18–630 and 756–1300 MHz, both ends included, nicFW's range (the BK4829 datasheet says 18–580 and 760–1160 MHz; the PLL is reported to lock wider). Above 1000 MHz is receive only: no transmit plan, Extend TX included, reaches it.
>   - **Entry:** four digits are three MHz digits and a decimal, the point coming by itself (1 2 1 5 is 121.5, 1 3 0 0 is 130.0, 1 0 5 0 is 105.0), so airband types as it always has. 1000–1300 MHz goes in only by a second \* on 100–130, which takes the point away for a fourth MHz digit: 1 2 9 \* \* 6 OK is 1296 MHz, 1 3 0 \* \* 0 OK is 1300, and \* after the fourth digit types the point (1 2 9 \* \* 6 \* 2 \* is 1296.2, VFO-24). The hint bar shows each step: after the first \* on 100–130 (shown "129.") it reads "\* again: 4-digit MHz"; after the second (shown "129") it names the fourth digit's range for the typed prefix, "0-9 1290-1299 MHz" ("0 1300 MHz" on 130); elsewhere the hints are as usual.
>   - **Refused:** a frequency no chip can receive is refused when committed: the entry stays open with the digits as typed, its warning line and a toast say "Can't tune: 18-630, 756-1300 MHz", and nothing is tuned (decided Oct 7, 2026; widened the same day, decision 72).
>   - To confirm on the bench: PLL lock and rough sensitivity at 1.2 GHz through the UHF front end; if it won't lock, the top comes back down.
> - **VFO-24** In frequency entry, \* after the point with at least one digit typed after it enters the frequency exactly as OK does, for one hand: 146 \* 52 \* tunes 146.520. Wherever OK does something else it does the same (split's TX frequency: \* sets it; the channel editor, Add repeater and the scope's centre: \* hands it back; HF mode's own typing: \* tunes it), and a refusal is the same (the entry stays with its digits). \* \* back to back keeps its meaning: the point, then on 100–130 a fourth MHz digit (1 2 9 \* \* 6 is 1296 MHz, VFO-21); with the point already typed and nothing after it, \* does nothing (never a second point). The hint bar shows "\*/OK Go" once \* would enter. Channel entry has no point: \* does nothing there.
> - **VFO-25** Choosing a region (setup, 0 9 4) moves a slot still on its factory frequency, when the region refuses to transmit there, to one in band in every region: A from 146.520 to 145.500, B from 443.475 to 433.500. A frequency the user tuned is never moved, and the US, Canada and Australia keep the factory ones.
> - **VFO-22** Clarifier: SIDE1 + ◀▶ on home move the active slot's receive frequency in 100 Hz steps, up to ±2.5 kHz, for an off-frequency AM or FM signal (SIDE1 + ▲▼ is the squelch: SIDE1 holds the receive side). It never moves the transmit frequency, isn't saved, and any retune clears it (the Radio task drops it on a new frequency). The card shows "CLR +0.3" beside the state; a toast names each step. As nicFW's per-VFO clarifier.
> - **VFO-23** Hold 9 on a channel asks "Copy to VFO?" (KEY-23); OK copies it to the slot's VFO: frequency, shift or split, tones, mode, power, step and busy lock (a channel's Global squelch becomes the VFO's level); the slot is on its VFO and V/M goes back to the channel, which is untouched. Toast "Copied to VFO". nicFW's "Chan 2 VFO".

### Under the hood


### Status

Mock-ups approved (0b). Built in 2a. Done when all VFO rules pass in the simulator and 2 m and 70 cm tune on the radio.


### Settled details

- ◀▶ on home steps through the bands by frequency, low to high, wrapping (12 m, 10 m, CB, 6 m, air, 2 m, 1.25 m, 70 cm …); every receive band is listed, and the region decides transmit only (decided Oct 6, 2026).
- Hold 9 saves at the first free channel number after the slot's last channel (wrapping), in the zone being browsed (no zone if none), both pre-filled on the save screen and changeable before OK (decided Oct 6, 2026).
- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - VFO-4: changed Oct 3, 2026.
  - VFO-7: decided Oct 6, 2026. Changed Oct 13, 2026 (user, decision 109): on the quick menu's PTT A, not hold \* itself.
  - VFO-7: Nov 22, 2026 (a Discord report, ferrite#102): reverse swapped only the transmit side; the receiver is now tuned to the input too, and retuned when reverse, the shift or split changes.
  - VFO-9: decided Oct 6, 2026. Changed Oct 14, 2026 (decision 153): it refused on 18–64 MHz, from before HF channels (CHAN-26). Changed Oct 14, 2026 (user, decision 159): hold 9, not hold V/M (KEY-23).
  - VFO-20: decided Oct 6, 2026.
  - VFO-14: changed Nov 24, 2026 (a Discord report, ferrite#84): NFM on 18–64 MHz too. The VFO already took it; the rule said FM and AM only, and a CB channel refused NFM, so its Mode was stuck on FM.
  - VFO-17: decided Oct 5, 2026.
  - VFO-18: decided Oct 5, 2026.
  - VFO-12: decided Oct 5, 2026.
  - VFO-22: decided Oct 7, 2026.
  - VFO-23: decided Oct 7, 2026. Changed Oct 14, 2026 (user, decision 159): hold 9 with a confirm, not hold V/M at once (KEY-23).
  - VFO-24: decided Oct 13, 2026 (user, decision 118); VFO-19 and VFO-11 changed with it (\* was only the point).
  - VFO-26: Nov 18, 2026 (Alex, decision 418): a user in Germany needed 7.6 MHz on 70 cm, and hold 7 "showed a popup then closed it": it cycled the shift with a 1.2 s popup and no list.
  - VFO-25: decided Nov 17, 2026 (decision 409). Users who chose the UK in setup found every key-up refused: the factory frequencies are US ones, out of the UK's 2 m (144-146) and 70 cm (430-440).
  - VFO-21: changed Oct 14, 2026 (decision 153): the ends included (630.000 and 1300.000 were refused), and 1000–1300 MHz typed as digits. Changed again Oct 14, 2026 (user, decision 154): four digits are airband again (1 2 1 5 is 121.5); \* \* on 100–130 is the only way to type 1000–1300 MHz, with hints for both steps.

### Open points

None.

---

