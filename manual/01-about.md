## 1. About Ferrite

### What it's for

Ferrite is open firmware for the Radtel RT-950 Pro, and only the Pro: the non-Pro RT-950 is not supported. It transmits and receives on every band the radio is built for, keeps what people use every day from stock, and adds decoders and RF-awareness features.

### Using it

| Ferrite is | Ferrite isn't |
| --- | --- |
| Daily-use parity with stock, transmit included: FM voice on every band and power level, offsets, tones, DTMF, APRS, VFO and channels, watch (three slots), scan, GPS, FM broadcast, HF mode, weather alerts, phone programming | Digital voice (M17, DMR, P25…); headers may be monitored later |
| Decoders: POCSAG, SAME, DSC, AIS | User scripting (for now) |
| An open, documented link protocol, used by Ferrite's own web app over cable and Bluetooth | LVGL (unless the drawing layer proves too limiting) |
| Real battery life: the MCU sleeps when there's nothing to do | A way to replay other people's signals |
| Safe for the radio: calibration and bootloader untouchable, transmit fenced in by the firmware | Any language but English; voice prompts |

Hardware: control boards RT950_V01 and RT950_V02. Early V01 boards without Radtel's SI4732 fix are deaf on medium and long wave; the firmware can't detect this.

### Screens

No mock-up yet.

> **Spec: principles**
>
> - **GOAL-1** Transmit is core, built second (milestone 4): receive is proven first.
> - **GOAL-2** Receive never depends on transmit code; a build with transmit compiled out works fully.
> - **GOAL-3** One owner per chip: only the Radio task touches the BK4829s, only the UI task the screen.
> - **GOAL-4** Home answers, from arm's length: what am I listening to, is anything there, am I transmitting.
> - **GOAL-5** Any screen or common setting is at most three presses from home.
> - **GOAL-6** Same key, same meaning on every screen; no key's meaning depends on a setting.
> - **GOAL-7** Anything that changes what a key does (lock, scan) shows in the status bar; every other active state is on the Status page.
> - **GOAL-8** As SAFE-1 and SAFE-3: never write calibration, the bootloader or MCU flash.
> - **GOAL-9** The MCU sleeps whenever there is nothing to do.

> **Spec: non-goals**
>
> - **GOAL-10** No digital voice: the MCU can't hear the mic (PA0 is only a level, bench Oct 13, 2026). Features that need the mic's audio are shelved in `archive/mic-audio-features.md`. The receive-only digital voice monitor stays.
> - **GOAL-11** No CJK fonts, pinyin or translations; no voice prompts. Flash and RAM go to features.
> - **GOAL-12** Never replay other people's signals.

### Under the hood


### Status

Goals settled. Licence: PolyForm Noncommercial 1.0.0, free for any noncommercial use; selling Ferrite needs a commercial licence (decision 228, Oct 21, 2026; it replaced GPL-3.0, chosen Oct 6). This manual: CC BY-NC-SA 4.0 (decision 230).


### Settled details

- Only the RT-950 Pro is supported; the non-Pro RT-950 is not (decided Oct 7, 2026).

### Open points

None.

---

