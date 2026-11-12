## 34. PIN, lock and recovery

### What it's for

Keeps casual hands off the radio, and gets it back when settings go wrong. Not security: anyone can reflash it.

### Using it

- **PIN:** MENU 0 9 3 1 sets when it's asked (at power on, or at unlock too); MENU 0 9 3 3 changes the PIN, 4–6 digits typed twice. Choosing a lock with no PIN set asks for one first.
- **Channel-only mode:** MENU 0 9 3 2 hides VFO and editing.
- **Key lock:** hold # (chapter 7).
- **Reset:** hold MENU while switching on, or MENU 0 9 7 2. One reset clears everything Ferrite stored except calibration and the SSB patch: a screen lists what goes, then OK, then hold # for 3 s (BOOT-14).
- **Setup again:** MENU 0 9 7 1 (chapter 4).
- **Bootloader:** the bottom two side buttons held at power on; Ferrite leaves this alone (chapter 30).

### Screens

No mock-up yet.

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| 0 9 3 1 | PIN lock | Off, at power on, at power on and unlock | Off |
| 0 9 3 2 | Channel-only mode | Off, on | Off |
| 0 9 3 3 | Change PIN | 4–6 digits: the old PIN first, then the new one twice | — |
| 0 9 7 1 | Run setup again | — | — |
| 0 9 7 2 | Reset | Everything except calibration and the SSB patch (BOOT-14) | — |

> **Spec: PIN**
>
> - **PIN-1** With a PIN set, ask for it at power on, and at unlock when chosen, before anything else is usable.
> - **PIN-2** Digits are masked; the screen shows attempts left and the settings-reset hint.
> - **PIN-3** Three wrong entries: wait 30 s, always 30 s; a power cycle resets the count.
> - **PIN-4** A settings reset clears the PIN.
> - **PIN-10** 0 9 3 1 PIN lock and 0 9 3 3 Change PIN are two items. Choosing a lock mode with no PIN set opens PIN entry first; turning the lock off asks for the PIN; Change PIN asks for the old PIN when there is one, then the new one twice (a mismatch starts the new one again). Wrong PINs count toward PIN-3 here too.

> **Spec: channel-only**
>
> - **PIN-5** Channel-only mode hides V/M, frequency entry, MENU 0 and channel editing; ABC, zone browsing, volume, squelch, quick mute (\*, HOME-15) and PTT still work; leaving it is hold #, which asks for the PIN when one is set; in channel-only mode hold # only leaves, so the key lock isn't available there. Hold-digit shortcuts that change a value (0, 2–8, and 9's copy, KEY-23) are refused with "Channel-only: hold # to leave"; 1 (the scope) works, and so does hold V/M (the zone list). Hold \* (the quick menu, HOME-17) is refused the same way.

> **Spec: recovery**
>
> - **PIN-6** Hold MENU at power on: the reset of BOOT-14, before the PIN is asked. The PIN screen gives no hint of it (Alex, Oct 15, 2026): the way out is in this manual only.
> - **PIN-7** The confirm says what will be cleared and what is kept; OK confirms, BACK cancels.
> - **PIN-8** As SAFE-9: no reset touches calibration, the update area or the SSB patch.
> - **PIN-9** The bootloader's power-on combo is never intercepted.

### Under the hood


### Status

No mock-up. Built in 2g (PIN, key lock, channel-only mode). Done when every PIN rule passes in the simulator and a reset is proven on the radio.


### Settled details

- The reset clears everything Ferrite stored except calibration and the SSB patch: settings, channels, zones, presets, the home channel, messages, the event log, waypoints and trims. It asks with deliberate extra steps: a screen listing what goes, then OK, then hold # for 3 s (decided Oct 6, 2026).
- Channel-only mode hides V/M, frequency entry, MENU 0 and channel editing; ABC, zone browsing, volume, squelch and PTT work; leaving it is hold #, which asks for the PIN when one is set; in channel-only mode hold # only leaves, so the key lock isn't available there (decided Oct 6–7, 2026).
- The wait after wrong PINs stays 30 s and a power cycle resets the count (decided Oct 6, 2026).
- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - PIN-3: decided Oct 6, 2026.
  - PIN-10: decided Oct 4, 2026.
  - PIN-5: decided Oct 6–7, 2026; decided Oct 7, 2026. Changed Oct 13, 2026 (decision 109): hold \* is the quick menu, still refused. Changed Oct 14, 2026 (decision 159): hold 9 is copy, refused; the zone list moved to hold V/M, which still opens it.

### Open points

None.

---

