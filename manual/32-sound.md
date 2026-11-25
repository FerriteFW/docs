## 32. Sound

### What it's for

Beeps and tones that confirm what the radio did, and what reaches the speaker. There are no voice prompts.

### Using it

- **Volume:** the knob on top (it is also the power switch). It's analog.
- **Beeps:** MENU 0 7 5: key beep, beep volume, alert tones, arrival tone (at a waypoint, GPS-12). The end tone (roger beep) is under Transmit, 0 8 4, and the DTMF sidetone under DTMF, 0 8 5 4.
- **Speaker-mic:** plugs into the side connector. Grounding its mute pin silences the internal speaker and mic; the Status page's Speaker mic row says Connected while it's in.
- **Never** use an adapter that grounds a speaker output (Kenwood-style): the bridge amp burns out.

### Screens

No mock-up yet.

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| 0 7 5 1 | Key beep | Off, on | On |
| 0 7 5 2 | Beep volume | Low, Mid, High | Mid |
| 0 7 5 3 | Alert tones | Off, on | On |
| 0 7 5 4 | Arrival tone | Off, on (reaching a waypoint, GPS-12) | On |
| 0 7 5 5 | Message sound (APRS-6.1) | Off, Ding, Mail, Packet, Droid, Pager | Packet |
| 0 7 5 6 | Message volume (APRS-6.2) | Low, mid, high, max | Max |

> **Spec: sound**
>
> - **SND-1** No voice prompts or recorded speech; beeps and the screen carry all feedback.
> - **SND-2** Volume is the analog knob; the firmware has no volume control. The receive audio level into it is stock's fixed REG_48 0xB2BF (Gain2 -4.5 dB, AF DAC 15), written with every receive setup; the chip's start-up 0xB3FF is 8 dB hotter and distorted on the radio (decision 102).
> - **SND-3** Key beep on each key press when on, at the beep volume: Low, Mid or High (0 7 5 2), DAC1 triangle levels 5, 7 and 9 (SND-11; decision 101).
> - **SND-4** A refused transmit beeps and shows the reason: a PTT's, a remote key-up's (LINK-20.3) and the Radio task's own refusals alike.
> - **SND-5** The end tone (roger beep) is a transmit setting now: 0 8 4 and per channel (TONE-8 to TONE-12).
> - **SND-6** An alert (SAME, DSC distress) sounds until acknowledged, when alert tones are on.
> - **SND-7** One mixer in the DSP task decides what reaches the speaker; unused sources are muted.
> - **SND-8** Decoders keep working with the speaker muted.
> - **SND-9** The amp (PE4) is off when nothing plays, and in the safe state.
> - **SND-10** Side connector mute grounded: internal speaker and mic off.
> - **SND-11** Key beeps, UI beeps and alert tones come from DAC1 (PA4) into the speaker amp, as stock's key beeps do (its voice-prompt engine): DAC on, 30 ms, amp on; amp off, 30 ms, DAC off. The chips keep receiving; the one passing audio is muted for the beep (REG_47) and unmuted after. Never while transmitting. Tones that go on air stay on the BK4829 (TONE-12).
> - **SND-12** The speaker mic is found as stock finds it, and takes over the speaker and the mic.
>     - **SND-12.1** The speaker mic is found as stock finds it, on PC15 (input with pull-up, low = connected): at boot two readings 50 ms apart, both low; then a reading every 10 ms, and four in a row against the state change it (40 ms; one reading back at the state starts the count again).
>     - **SND-12.2** Connected: PE1 high, the speaker switched to the side connector: only the speaker mic plays.
>     - **SND-12.3** Connected: the mic switched to the side connector too: the speaker mic's own mic is the one that transmits (but for the radio's own PTT, SND-12.7).
>     - **SND-12.4** Connected: the shared audio stage (PB8) on and held on, so nothing that ends a sound or keys the transmitter turns it off.
>     - **SND-12.5** When it is removed: PE1 low; PB8 goes off with the next sound that ends.
>     - **SND-12.6** The Status page shows Speaker mic: Connected or None.
>     - **SND-12.7** The PTT pressed picks the mic (decision 430; stock doesn't: it takes the speaker mic whenever one is plugged in). With a speaker mic plugged in, its own PTT (the side connector's, PE6) transmits on its mic; the radio's own PTT (PTT A or B) transmits on the radio's mic, PE1 low and PB8 off for the key-up (PB8 on silences the radio's mic, and the speaker mic holds it on, SND-12); a key-up with no PTT pressed (VOX, the link, a data burst) keeps stock's choice, the speaker mic. PE1 follows the detect again at the unkey, and PB8 is held on again.
> - **SND-13** While audio is playing (the speaker on for a slot heard, the broadcast or HF mode), key beeps and the refusal beep are skipped. The alert tone (SND-6) still sounds, clean: the radio audio (the BK4829s and the SI4732, broadcast or HF) is muted under each tone and comes back after it, and the amp stays on. With nothing playing, beeps are as SND-11.
> - **SND-14** The cable's transmit pin (PC10, UART4 TX, the side connector's pin 11) is a GPIO output held high from reset, as stock holds it outside programming mode: Radtel speaker mics take their mic bias from it. While a speaker mic is connected (SND-12, or PC15 low while that is still being decided) it stays so and nothing is sent on the cable (no cable log, terminal or link answers; what waits is dropped), in every build; the UART still receives. Without one the pin is the UART's, as now (TX-43 still holds it while keyed). Never driven low. Decision 146.
>     - **SND-14.1** Some speaker mics are quiet on this radio, and the firmware can only add gain: the radio's own mic bias on the connector's mic pin (pin 2) is weak, about 70–80 mV, while Radtel's speaker mics that take their bias from pin 11 get a steady 3.3 V (SND-14). On black with a Radtel speaker mic (Nov 24, 2026), pin 11 stayed high through every key-up, yet speech at Mic gain 12 peaked near 1 kHz of deviation and barely rose above the hiss: that mic takes too little bias. More Mic gain (10–12, VOX-15.3) helps and adds hiss with it; the real fix is a mic powered from pin 11, or the known mod (5.1 kΩ from pin 11 to the mic). (ferrite#180.)

### Under the hood


### Status

No mock-up. Speaker on squelch in 1e; roger beep in 4b. The speaker-mic detect (SND-12) is built Oct 13, 2026 (decision 116), not yet run on the radio. Key beeps (0 7 5 1), the beep volume (0 7 5 2) and alert tones (0 7 5 3) are wired since Oct 8, 2026 (decision 96): the app sends each beep and the Radio task plays it on the BK4829 at the volume's tone gain; before that the beep path existed but nothing asked for key or alert beeps. Done when every SND rule passes on the radio.


### Settled details

- Beep volume 1–5 sets beeps relative to voice; both go through the speaker path, so the knob scales both (decided Oct 6, 2026).
- MDC1200 transmit is dropped: no MDC ID, no MDC roger ID; MDC1200 is decode only (decision 74); PTT ID was dropped too (decision 214).
- the side connector's mute is PC15, the debounced active-low detect input stock reads (low: PE1 and PB8 set, `analysis/pin_audit.md`); Ferrite reads it the same way and switches PE1 as stock (SND-12, decision 116). Bench-confirm what PE1 switches.
  - SND-14: decision 146, Oct 13, 2026 (bench: the speaker mic keyed Ferrite but sent no audio; stock's PC10 is OUT-PP high, `analysis/speaker_mic_tx.md`).
  - SND-12: decision 116, Oct 13, 2026. Stock V0.27: boot check 0x0801BE54, poll 0x08010290 in one of the main loop's ten 1 ms slots (0x0800CFBC, dispatched from the SysTick flag), so every 10 ms; its count at 0x200001E5 is cleared by an agreeing reading, and the fourth disagreeing one changes flag 0x2000A3B4[0x4B]. Ferrite's input task reads it with the keys, every 10 ms; the Radio task, which owns the audio pins, switches PE1 and holds PB8.
- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - SND-11: decided Oct 7, 2026; changed Oct 12, 2026 (decision 100): stock's key beeps are DAC1 clips, not the BK4829 generator.
  - SND-4: built Oct 15, 2026 (decision 164): until then no transmit refusal beeped (the refused screen's comment said the Radio task beeped; it didn't); the UI test caught it on a remote key-up (PE4 never on). The refused screen's readback counts the refusal beeps (`beeps=`), as the 80 ms beep is over before a `gpio` sample over the link.

### Open points

None.

---

