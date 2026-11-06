## 17. DTMF

### What it's for

Sends DTMF digits: by hand or from stored memories. Decoding is chapter 27.

### Using it

- **Dialer:** 0 8 5 1, type the digits and send.
- **Memories:** 0 8 5 2, 16 entries of up to 16 digits.

### Screens

No mock-up yet.

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| 0 8 5 1 | Dialer | Type and send | — |
| 0 8 5 2 | Memories | 16 × 16 digits, each with a 10-character name (# names it) | Empty |
| 0 8 5 3 | Speed | 50–200 ms, each tone and each gap | 100 ms |
| 0 8 5 4 | DTMF sidetone | Off, on (hear the digits sent, at beep volume) | On |
| 0 8 5 5 | First digit delay | 0–1000 ms after key-up, so a repeater opens | 300 ms |

> **Spec: DTMF**
>
> - **DTMF-1** Dialer and memories transmit through the full chapter 15 sequence and checks.
> - **DTMF-2** Digits come from the BK4829's DTMF generator; the mic is muted while they are sent.
> - **DTMF-3** Each digit is on for the speed (0 8 5 3), then off for the same time. A sequence starts the first digit delay (0 8 5 5) after key-up, so a repeater has opened; digits sent live while PTT is held (DTMF-7) don't wait.
> - **DTMF-7** While keyed, the digits, \* and # send DTMF live for as long as each is held, from any screen; the dialer's typed digits go out with Send. The UI sends them, the Radio task makes the tones (milestone 4).
> - **DTMF-11** While keyed, MENU, ▲, ▼ and BACK send A, B, C and D live, as nicFW puts A–D on its four non-digit keys.
> - **DTMF-12** Each DTMF memory has a name of up to 10 characters (# in the list; "Link on", "IRLP 3500"), shown in the list and the dialer's header; clearing a memory clears its name. Names are 16 records of 12 B after the memories (0x041F00). The memories and their names are read and written over the link (LINK-56).
> - **DTMF-13** The dialer's Send keys like PTT (the same checks, not on an emergency frequency), hands the digits to the Radio task, which waits the first digit delay and sends each at the speed (DTMF-3), then unkeys through the UI; no end tone or CW ID follows (TONE-11). 0 8 5 3 steps 50–200 ms by 10, 0 8 5 5 0–1000 ms by 50.
> - **DTMF-8** DTMF sidetone (0 8 5 4, on by default): the digits being sent are heard on the speaker at the beep volume (0 7 5 2).

### Under the hood


### Status

Dialer and memories built Oct 4, 2026 (A14, A15; simulator shots `dtmf-dialer`, `dtmf-memories`); Send transmits since Oct 7, 2026 (DTMF-13). Hold 1–4 types A–D. Roadmap 4d for the tones themselves.


### Settled details

- The dialer does both (decided Oct 6, 2026): digits typed on its screen go out with Send (the radio keys, sends, unkeys); digits pressed while holding PTT go out live, on any screen.
- DTMF sidetone is on, at beep volume, with a setting to turn it off (decided Oct 6, 2026; 0 8 5 4, DTMF-8). (A–D: hold 1–4 in the dialer, decided Oct 4, 2026.)
- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - DTMF-4, DTMF-5, DTMF-6: dropped with PTT ID (decision 214, Oct 20, 2026): the big ham makers (Icom, Yaesu, Kenwood) don't offer it, it's a land-mobile feature, and a DTMF burst at every key-up is unwelcome on many repeaters. DTMF dialling and memories stay; decoding others' PTT IDs (chapter 27) stays.
  - DTMF-3: decided Oct 7, 2026.
  - DTMF-7: decided Oct 6, 2026.
  - DTMF-11: decided Oct 7, 2026.
  - DTMF-12: decided Oct 7, 2026; nicFW has 99 named presets; 16 named ones stay.
  - DTMF-13: decision 87.
  - DTMF-8: decided Oct 6, 2026.

### Open points

None.

---

