## 13. Watching several slots

### What it's for

Listen on two or three slots at once, and answer on whichever is heard.

### Using it

1. MENU 7 (or hold 4): watch off, A+B, or A+B+C.
2. The active slot is large and heard first. A watched slot is heard when the active one is quiet.
3. A watched slot that opens is highlighted (RX on its card) and plays while the active slot is quiet. The active slot never changes by itself: only you change it (SLOT, or a PTT that keys its own slot).
4. To answer: PTT B keys slot B whichever slot is active; PTT A keys the active slot (KEY-7). To answer slot C, press SLOT to make it active, then PTT A.
5. A home slot on 18–64 MHz needs the band relay. If the watched slots need different relay states, watch turns itself off: a toast says "Watch off: HF needs the relay", `TW`/`DW` disappears, and the Status page says why. It comes back by itself once they all need the same state.
6. **Pause:** while a watched slot is receiving, # on home pauses watch for the pause time (MENU 0 1 6 1, 1 min); the hint bar shows "# Pause".
7. Watching pauses while any slot transmits and stays paused for 30 s after unkey, so replies on your channel are not missed (WATCH-16). With Battery Save on, watched receivers sleep and wake on its cycle, so a watched slot may miss the first fraction of a second.

### Screens

| | |
| --- | --- |
| ![Home, watch layout](img/screens/HomeA.png) | ![Home, watch + activity](img/screens/HomeC.png) |
| Watch | Watch + activity |

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| MENU 7, 0 1 1 | Watch | Off, A+B, A+B+C | A+B |
| 0 1 6 1 | Pause time | 30 s, 1 min, 5 min | 1 min |

> **Spec: watch**
>
> - **WATCH-1** One slot is active; the others in the watch set are watched.
> - **WATCH-2** Two BK4829s, one awake at a time, as stock: slots on the same chip take turns on it, and slots on different chips take turns through the receive path, the chip not listened to asleep meanwhile. With APRS mode on, slot C's chip stays awake beside the other (APRS-16), and C has priority on its chip (APRS-21.1).
>     - **WATCH-2.1** A slot turned off with \* (HOME-15.1) takes no turns, the active one too: it leaves the watch set and no chip listens to it, so its turns go to the other slots (A, B and C on 2 m with B off: A and C alternate; A off beside APRS mode's C: C has the chip alone). It is never heard.
> - **WATCH-3** Whose audio is heard when several slots receive.
>     - **WATCH-3.1** The active slot's audio has priority.
>     - **WATCH-3.2** A watched slot is heard only while the active slot's squelch is closed or the active slot is muted. A latched monitor (SQL-14) holds the active slot's squelch open, so while it is latched the watch stays on the active slot: no watched slot is listened to or heard (as stock's squelch 0, which never hops).
>     - **WATCH-3.3** A muted slot (quick mute, HOME-15) is never heard and takes no priority; it still listens.
>     - **WATCH-3.4** A muted slot keeps a chip it shares only for its dwell, so it blocks no other slot.
> - **WATCH-4** A watched slot that opens squelch is highlighted.
> - **WATCH-5** The active slot changes only when you change it. A watched slot that is heard is highlighted and plays (WATCH-3, WATCH-4), but never becomes the active slot, on home or any other screen. Stock's watch moves to the slot that opened and goes home 100 ms after it closes; nicFW's MultiWatch switches to it unless Keep VFO is on. Ferrite deliberately doesn't: a slot that changes under you is disruptive, and PTT B (KEY-7) answers slot B without switching.
> - **WATCH-6** While a watched slot is receiving, # on home pauses watch for the pause time (0 1 6 1, default 1 min), so a busy slot can't keep taking the speaker; the hint bar shows "# Pause".
> - **WATCH-7** Hold 4 turns watch off, and on again as the set it was before (A+B or A+B+C; A+B if it was never on).
> - **WATCH-8** Under Battery Save, watched chips follow Battery Save's own sleep/wake cycle; a watched slot may miss the first fraction of a second. Watch default stays A+B.
> - **WATCH-9** Watch pauses while the crossband repeater runs (XB-13).
> - **WATCH-16** Watched slots pause while any slot transmits. After the unkey, watch stays paused until the active slot has been quiet for 30 s or a key is pressed, so the reply on your frequency isn't missed; a longer # pause (WATCH-6) is left as it is.
>     - **WATCH-16.1** The APRS slot (APRS mode, KISS or beacons holding C) keeps listening through that pause and through a # pause: on its own chip, or taking its turns beside the active slot on a shared one (as 0 5 9 7 says). Its card never reads "paused". Only while keyed does the active slot have a chip alone. Before this, every voice transmission left APRS deaf for at least 30 s (Alex, Oct 27: "deaf for 30s?!?! that cant be right"; decision 297).
>     - **WATCH-16.2** While the watch leaves the APRS slot out (another slot transmitting, a relay cancel, WATCH-11), its card says "paused" in amber, so nobody expects packets meanwhile (Alex, Oct 27: "we should also show that the APRS rx is paused"). The readback's card `state="paused"`.

> **Spec: relay rule**
>
> - **WATCH-10** The relay (PC4) follows the active slot's band: set for 18–64 MHz, clear otherwise. Watching and scanning never switch it; in HF mode it follows the receiver in use (HF-11).
> - **WATCH-11** Watch and the band relay: when the watched slots disagree on the relay, watch stops and says why.
>     - **WATCH-11.1** When the slots in the watch set need different relay states, watch is cancelled: no `TW`/`DW`. Watch resumes by itself when they all need the same state again. There is no per-slot relay tag.
>     - **WATCH-11.2** A toast says so: "Watch off: HF needs the relay".
>     - **WATCH-11.3** The Status page's Watch row says why (SBAR-17).
> - **WATCH-12** The relay changes only when the active slot or its band changes; never at key-up (TX-37: a transmission that needs the other state is refused, decision 128), never while transmitting or in the unkey wait.

> **Spec: background jobs** (not built; the setting, once 0 1 2, is out of the menu until jobs are judged worth building: MENU-33, decision 256)
>
> - **WATCH-13** Only a watched slot on its own chip can run a job.
> - **WATCH-14** A job is a zone scan or a decoder; hits go to the event log and the inbox.
> - **WATCH-15** A slot running a job carries a job tag on home and appears on the Status page under Jobs.

> **Spec: timings** (defaults, to confirm on the bench)
>
> - **WATCH-17** Slots sharing a chip take turns: 150 ms on the active slot, 70 ms on each watched one (stock hops about every 70 ms), 100 ms on APRS mode's C (APRS-21.1). A slot whose squelch opens keeps the chip while it is open and for 2 s after it closes. A chip given the receive path back (or a new slot) reads its squelch shut until it has woken, tuned and passed its open delay: a closing read within 60 ms of that (to confirm on the bench) doesn't close a slot that was open, so a muted slot receiving reads RX muted through the hop (HOME-15).
>     - **WATCH-17.1** *(bench builds only, TERM-38; decision 262)* The Radio task times the turns the chips actually take: a turn runs from the chip's retune to a slot until it is retuned to another slot or sleeps (a new frequency on the same slot continues it). Each slot's whole turns and their total ms since boot show with `bk turns`; `bk turns reset` shows them, then zeroes them (a turn in progress still counts whole when it ends). RAM only. The mean of a run's counts is a turn's true length, which reading a register over the link (about 160 ms a read) can't give.
>     - **WATCH-17.2** With a priority slot (APRS mode's or KISS's C, APRS-21.1) on one chip, the active slot on the other chip gets 70 ms turns of the receive path, as a watched slot does, and turns on either chip count only while that chip has the path, so A and B each get a whole look in turn with C's between (decision 279). C is never deaf longer than 70 ms, inside even a short packet's flags. That other chip stays tuned between turns (APRS-16), so the shorter turn costs no retune. An active slot sharing C's chip keeps its 150 ms: each turn there starts with a retune.
>     - **WATCH-17.3** "Shared VHF" (0 5 9 7): who wins a chip the priority slot (APRS mode's or KISS's C) shares with A or B, and the receive path between chips (decision 295). **APRS first** (the default): C takes 400 ms turns and every other slot a 100 ms look, C's turn after each look on a shared chip (A, C, B, C): with A and B both on 2 m, C listens about 72 % of the time and is never deaf longer than about 140 ms (modelled), so a packet is caught early in its flags; a call on A or B is still caught in its look and then keeps the chip as any open slot does (C misses packets while it runs, as before). **A·B first** (named Voice first until decision 313; the terminal takes "A.B first"): WATCH-17.2's turns (the active slot 150 ms, watched 70, C 100); with A and B both on 2 m C listens about 18 % of the time, deaf up to about 260 ms, and misses many packets. C's card says which beside its state ("APRS first" grey or "A·B first" amber, APRS-17.1, APRS-21) while A or B shares its chip.

### Under the hood


### Status

Home mock-ups approved (0b). Watch in 2d; background jobs in 6f. Done when three-slot watch and the relay cancel-and-resume pass on the radio.


### Settled details

- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - WATCH-13 – WATCH-15: the Background job row (0 1 2) left the menu Oct 22, 2026 (user, decision 256, MENU-33) until jobs are judged worth building; the pause time moved from 0 1 8 1 to 0 1 6 1.
  - WATCH-5: decision 81, replacing Follow.
  - WATCH-8: as stock dual watch does.
  - WATCH-16: decided Oct 7, 2026, as nicFW's MultiWatch does.
  - WATCH-17.1: added Oct 22, 2026 (decision 262), for the bench to time WATCH-17's turns.
  - WATCH-11: changed Oct 3, 2026.
  - WATCH-2.1: Oct 27, 2026 (Alex, decision 314).
  - WATCH-7: changed Oct 14, 2026 (decision 153): back on as the set it was (it always came back as A+B).
  - WATCH-3: changed Oct 12, 2026: a muted slot (HOME-15) takes no priority, the active one too.
  - WATCH-3.2, WATCH-17: changed Oct 15, 2026 (decision 167): a latched monitor holds the watch on the active slot (until then the hop went on under it: the monitored audio chopped with each turn to the other chip, and by ear a watched B seemed to take the speaker); a closing read just after a chip gets the path back no longer closes an open slot (a muted A receiving read Muted once in four reads). WATCH-17: APRS mode's C's 100 ms turn added Oct 15, 2026 (decision 181).
  - WATCH-2: changed Oct 13, 2026 (decision 111): one chip awake at a time, as stock, instead of both chips listening on their slots at once; APRS mode keeps C's chip awake. Oct 15, 2026 (decision 181): C's priority in APRS mode (APRS-21.1).

### Open points

- How long each slot gets when two share a chip: WATCH-17's defaults, to confirm on the bench (does a carrier open the squelch inside 70 ms, with and without a tone?).

---

