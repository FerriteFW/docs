## 7. Keys and the key lock

### What it's for

One fixed key map, the same on every screen and every Ferrite radio. No key can be reassigned, and no setting changes what a key does.

![Ferrite keys on the RT-950 Pro](img/keys-diagram.png)

### Using it

| Key | Press | Hold, or combination |
| --- | --- | --- |
| MENU/OK | Home: quick settings. Lists: open the item, or keep an edit | Home: More (the full menu) |
| BACK | Back one level, to the screen you came from (on home: nothing), or cancel an edit (the old value returns) | Home, from anywhere (not on the PIN at power on, a link write or power off) |
| ▲▼ | Home: step frequency or channel. Lists: move | Repeat |
| ◀▶ | Home: zone (channel mode) or band (VFO mode). Everywhere else: the same as the knob, unless the screen says otherwise (KEY-19) | Repeat |
| Knob | Home: tune or step channels. Settings: change the highlighted value | Home, quick menu up: brightness (HOME-17) |
| ABC | Next slot, A → B → C. Zones page: edit the zone (CHAN-27) | Edit the active slot in place |
| V/M | VFO ↔ channel | Zones (the zone list), in VFO and channel mode alike (KEY-23) |
| SIDE1 (PF1) | Tap: monitor latched until tapped again | Monitor while held. Hold + knob or ▲▼: squelch; hold + ◀▶: clarifier |
| SIDE2 (PF2) | Scan start/stop | Held alone: frequency counter, opened as it comes up (KEY-22). Hold + knob or ▲▼: big steps (1 MHz, 10 channels) |
| \* | Home: the active slot Normal, Muted, Off in turn (HOME-15, HOME-15.1). Decimal point in entry. Scanning: skip this hit. Elsewhere the hint bar's action | Home: the quick menu (HOME-17) |
| # | Home: the quick help, or pause watch while a watched slot is receiving. Elsewhere: the hint bar's action | Key lock on/off |
| 0–9 | Frequency, channel or menu number | Shortcut (below) |
| PTT A | Transmit on the active slot from any screen (returns home first; exceptions in KEY-7). Quick menu up: reverse, never transmits | PTT + SIDE2: tone burst |
| PTT B | Transmit on slot B from any screen (returns home first). Quick menu up: night red, never transmits | PTT + SIDE2: tone burst |

**Long-press digits on home.** The shortcut runs at the long press and a popup in the middle names it ("TX power" with "Mid" under it, "Band scope"); letting go does nothing. MENU 0 9 1 3 lists them with their current values. 2–8 match stock's factory defaults; 0, 1 and 9 are Ferrite's:

| Key | Shortcut | Key | Shortcut |
| --- | --- | --- | --- |
| 0 | Home channel | 5 | Tones (the tone picker) |
| 1 | Band scope | 6 | Step: the next one (VFO only) |
| 2 | TX power: low, mid, high | 7 | Shift: the options, simplex, +, −, Split (the value editor) |
| 3 | Squelch (the value editor) | 8 | Offset: its amount, typed in MHz (VFO-26) |
| 4 | Watch on/off | 9 | Copy: a VFO to a channel (the save form); a channel to the VFO ("Copy to VFO?", OK copies) |

**Hold \* on home: the quick menu** (HOME-17). A small box over home; while it is up PTT A is reverse, PTT B night red, PF1 GPS on/off, PF2 Bluetooth on/off and the knob the brightness, each acting at once with its new state shown. BACK, \* or any other key closes it, as do 5 s without a key. PTT A and PTT B never transmit while it is up.

FM broadcast (tune a slot into the broadcast band: BCR-21; its settings MENU 0 2 6), weather (its channels' zone, chapter 23), tone search (MENU 0 3 5), APRS heard (MENU 0 5 1), mode and Battery Save (MENU) have no digit.

HF mode has no key or shortcut: open it from MENU 0 3 3 (chapter 20a).

**Key lock:** hold #. The keypad locks at once and a popup says "Keypad locked" with "\* all · 0 all but PTT" for 3 s: press \* or 0 then to lock more, or just let go. A padlock shows in the status bar.
- **Keypad** (hold # and let go): the front keys and the tuning knob. PTT, SIDE1 (monitor, squelch) and SIDE2 (scan, the counter) still work.
- **All but PTT** (hold #, then 0): every key and the knob, the side keys too. PTT still works.
- **All** (hold #, then \*): PTT too; the padlock is red.

The volume knob and hold # (to unlock) always work. **Auto lock** (MENU 0 9 1 1: off, 30 s, 1, 2 or 5 min) locks the keypad by itself after that long without a key (KEY-20).

**Text entry** (names, callsign, messages): multi-tap on the digits; \* is a space and # cycles upper case, lower case, symbols, as the keys are marked (\_ and ^); BACK deletes.

**Predictive text** (message text only: APRS messages): one press per letter, and the radio offers the words those keys spell, from a small built-in dictionary of message and ham words.
- Keys: the digits type, the knob (or ▲▼) picks among the words offered, and # takes the word and adds a space.
- Shortening: a word with a shorter form offers it next ("received" then "QSL"), since an APRS message holds 67 characters.
- Starting a message: an empty one shows the quick messages ("73", "On my way", "Call me"…); OK on one puts it in to send or add to.
- Spelling a word itself: # goes round T9 (predictive), abc, ABC, 123 and back to T9; the screen says which ("Typing: T9").

**Side connector:** its PTT transmits on the active slot; its mute input silences the internal speaker and mic while grounded.

The radio has no top button, and the knob has no push.

### Screens

No mock-up yet.

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| 0 9 1 1 | Auto lock | Off, 30 s, 1, 2, 5 min (KEY-20) | Off |
| 0 9 1 2 | Key test | Shows each key's code, name and press type; hold BACK leaves | — |
| 0 9 1 3 | Shortcuts | The ten hold-digit shortcuts and what each does now | — |

> **Spec: key map**
>
> - **KEY-1** One fixed map; no user assignment; a key's meaning never depends on a setting.
> - **KEY-2** One table maps the 20 matrix codes, direct keys, PTTs, side keys and encoder to logical keys; all other code uses logical keys only.
> - **KEY-3** Short press fires on release, under 700 ms. Long press fires while held, at 700 ms; the release after it does nothing (digits on home too: HOME-8). There is no gap between the two (stock is about 500 ms, nicFW about 1 s).
> - **KEY-4** ▲▼◀▶ and the knob repeat at 10 per second after 400 ms held.
> - **KEY-5** One BACK rule everywhere: a short BACK goes back one level, to the screen this one was opened from (on home it does nothing); on an edit or a screen's own step (typed digits, a sub-page) it takes that step back first. Hold BACK goes home from any screen, except the modal ones that must not be left: the PIN at power on, a link write in progress and power off. The key test shows a short BACK like any key and is left with hold BACK.
> - **KEY-6** Keys typed ahead are buffered and never dropped while a screen draws.
> - **KEY-7** Which PTT keys which slot.
>     - **KEY-7.1** PTT A transmits on the active slot.
>     - **KEY-7.2** PTT B transmits on slot B.
>     - **KEY-7.3** From any screen, a PTT goes home first.
>     - **KEY-7.4** The side-connector PTT transmits on the active slot.
>     - **KEY-7.5** There is no PTT C: slot C transmits from PTT A when it is the active slot.
>     - **KEY-7.6** The exceptions: HF mode transmits in place (HF-23), the band scope transmits on the signal it monitors (SCOPE-12), a PTT that would key the APRS slot opens a message (APRS-18), and while home's quick menu is up PTT A and PTT B are its keys and never transmit (HOME-17).
> - **KEY-8** As SAFE-14: a PTT held at power-on is ignored until released.
> - **KEY-9** The hint bar names what \*, # and MENU do on the current screen: at most three key + label pairs (four don't fit 240 px), the screen's own keys before the universal BACK.
> - **KEY-10** Every long press is also reachable from a visible screen or list.
> - **KEY-11** The ten long-press digits are fixed as in the table above. 7 and 8 work the same on a VFO and a channel (decision 418); 6 on a channel changes nothing and says "VFO only".
> - **KEY-21** The shortcut list (MENU 0 9 1 3) runs its rows: ▲▼, the knob or a digit pick one, OK runs it from home as holding that digit would (with its popup), and the help line names the digit to hold ("Hold 5").
> - **KEY-23** Hold V/M on home opens the zone list (C11, as MENU 0 2 3) in VFO and channel mode alike; OK there puts the active slot on a zone and comes back home (CHAN-27). Hold 9 is copy, one of the few keys whose meaning follows the mode, the same idea both ways: on a VFO it opens the save form (VFO-9); on a channel it asks "Copy to VFO?" (the channel named; OK copies, BACK cancels) and OK does VFO-23. Where hold V/M saved before, hold 9 saves: HF mode (HF-26) and the scan hit list (SCAN-23); hold V/M there opens nothing (HF mode says why, HF-13). Channel-only mode refuses hold 9 and still opens the zone list (PIN-5).
> - **KEY-24** The channel knob steps the same way on every screen: one way is up (the next channel, a higher frequency, value or level, the next item in a list), the other down. Its direction is the encoder read A before B, as the first builds had it (decision 369, reversing decision 196).
> - **KEY-25** A key is never held up by the screen's work or the radio's updates: the UI task takes a key or the knob before anything else waiting for it (the Radio task's snapshot, the tick), and the time a press is held is its own: a hold is a hold and an arrow moves one row however busy the screen (decision 341; black, Nov 1, 2026: on the satellite pages the downlink's level changed every 10 ms tick and kept the keys waiting, so a press and its release arrived together, a held MENU read as OK and the arrows lagged and jumped).
> - **KEY-26** What every key does on every screen (each key tapped and held, the side keys, PTT A and the knob: where it leads, what it asks the radio, any message) is a reviewed record in the simulator's tests; a change shows up there and is accepted on purpose. Decision 424.
> - **KEY-22** SIDE2 (PF2) held alone opens the frequency counter (MENU 0 3 2) when it comes up. Held as a modifier (+ knob or ▲▼ for big steps, or with PTT as the tone burst) it never does, however long it is held. Not in channel-only mode (PIN-5).
> - **KEY-12** Text entry: multi-tap digits; \* (marked _ on the key) is the space; # (marked ^) cycles case and symbols; BACK deletes. 0 also has the space before its digit, and 1 the marks before its (TEXT-2.1). There is no cursor: typing and BACK work at the end of the text, and the knob and ◀▶ do nothing there. Message text also has predictive entry (TEXT-1 to TEXT-11). A channel name's symbols page has only the name set's symbols (CHAN-31).
> - **KEY-17** # on home: the quick help, or pause watch while a watched slot is receiving (HOME-10).
> - **KEY-18** \* while scanning skips the current hit for this scan (SCAN-11), on the scan screen and on home while the active slot scans, where hold \* does nothing (no quick menu); on home otherwise \* mutes and unmutes the active slot, \* \* within a second turns it off and \* on an off slot turns it on (HOME-15, HOME-15.1) and hold \* is the quick menu (HOME-17). On the scan screen ▲▼ set the direction and leave a hit (SCAN-16), and # skips a hit for every scan (SCAN-17). No other key pauses or skips.
> - **KEY-19** ◀ and ▶ (short press and repeat) do exactly what the knob does, ◀ = one click back, ▶ = one forward: in menus and quick settings they change the highlighted value, in a value editor they step it, in a list they move.
>   - Screens that give ◀▶ a job of their own: home (band or zone), scope (marker; the knob moves the centre), HF mode (band), FM broadcast (seek), the crossband start screen (move between cells), the edit grids (move between cells; the knob changes the cell), More's Recent row (pick one), the event log list (filter by source), GPS (position ↔ satellites), About (About, the Help pages and the self-test, HELP-1), PIN entry (◀ deletes), setup's text pages (◀ deletes), channel renumbering and range-preset edges (steps of 10 / 1 MHz), and the key test.
>   - Anywhere else on those screens, ◀▶ are the knob (decided Oct 4, 2026).

> **Spec: predictive text**
>
> - **TEXT-1** Two ways to type: multi-tap (KEY-12) everywhere, and predictive for message text only (APRS compose and replies, and any later messenger). Names, callsigns, channel and zone names, frequencies and numbers stay multi-tap: they aren't dictionary words.
> - **TEXT-2** Predictive keys: 2–9 type one letter each (the phone layout: 2 abc … 9 wxyz); a strip above the hint bar shows the words those keys spell, best first, the chosen one highlighted; the knob or ▲▼ moves through every match, not only those shown; \* (or 0) takes the highlighted word and adds a space; BACK takes back the last key press (or, between words, deletes a character); the case is automatic: a capital starts the message and follows . ? !, Q-codes and shorthand in capitals (CAPS words: ABC in multi-tap); 1 cycles punctuation (TEXT-2.1) after a word; hold a digit types the digit itself (73, 146.52, 2m); # takes the word in progress and goes on to multi-tap (TEXT-10).
>   - **TEXT-2.1** The marks are . , ? ! ' / - @ : in that order, round again after the colon; 1 types the first anywhere (after a word, a space or on an empty message) and each 1 straight after changes it to the next. While a mark is being picked the strip shows all nine with the one in the text highlighted. Multi-tap's 1 has the same marks, then the digit 1 (KEY-12). \* (or 0) is the space.
> - **TEXT-3** Keys that spell no dictionary word show as their digits with "no word: # to spell it"; nothing is guessed. Words are spelled in multi-tap and the message goes on in predictive.
> - **TEXT-4** Short forms: when the highlighted word has one in the short-form table (received → QSL, thanks → TNX, weather → WX, location → QTH, see you later → CUL…), it is offered right after it in the strip, always. Q-codes and shorthand are shown and sent in capitals (QSL, TNX, WX, 73). A phrase's short form (thank you → TU, see you later → CUL, good night → GN) is offered after its last word when the words before it were just typed, and takes their place: "see you" then later offers CUL, and # leaves "CUL".
> - **TEXT-5** The compose screen counts characters against the 67 APRS allows ("34/67"); a key that would pass it is refused with a short beep (the BK4829's tone generator, SND-11, by `RadioCmd::Beep`) and "67 characters: the APRS limit". In multi-tap, tapping the last letter's key again within the second changes that letter and isn't refused (KEY-12): only a key that would add one is.
> - **TEXT-6** Quick messages: an empty message shows the quick-message list in place of the strip; the knob or ▲▼ picks one and OK puts it in the message (nothing is sent until OK on Send). Typing a digit starts the message instead and hides the list.
>   - **TEXT-6.1** The quick messages are optional: \* ("Write" in the hint bar, with "\* or a letter: write your own" under the strip) puts the list away for an empty message box; any key that types (a letter key, 1, a held digit) puts it away too. It stays away while compose is open, even when the text is deleted again; on an empty message the knob brings it back (▲▼ go to the recipient, as on any message) ("Knob: the quick messages again"). BACK on the list still goes to the recipient.
> - **TEXT-7** Nine quick messages of up to 67 characters, editable on the radio (Messages, MENU 0 5 2: hold MENU, Quick messages), over the link for the web app (LINK-54) and in the terminal (`quick 3 "On my way"`, TERM-12); kept with the APRS settings (SPI 0x055000–0x057FFF, layout 3), not in the radio-wide settings. The list shows each as yours or factory; OK edits one (predictive or multi-tap, as for messages), # puts the factory text back, and a message left empty stays empty. Factory set: 73; QSL, thanks; On my way; Call me; Where are you?; QRT for now; Yes; No; Are you on the repeater? (`ferrite/assets/words/quick.txt`).
> - **TEXT-8** The dictionary is small on purpose: about 570 words (core message words, amateur-radio vocabulary, and words people type in real APRS messages; SCOWL's word list as the English check), about 3 KB packed, built by `tools/mkwords.py` from `ferrite/assets/words/`. The words are an SPI part (`words-en.bin`, 64 KB slot at 0x0B0000) installed with every update (decision 345), read through a 64-byte window per lookup: no copy in RAM; without the part no words are offered. The short forms (TEXT-4) and the factory quick messages (TEXT-7) stay in the firmware image's slow flash, so they work without it. The slot leaves room for a bigger dictionary.
> - **TEXT-9** No learned words: the dictionary changes only with the firmware. The order of `core.txt` decides ties between words with the same keys (good/home, on/no).
> - **TEXT-10** Predictive (T9) is the default for message text. # (marked ^) goes round T9, abc, ABC, 123 and back to T9, the screen saying which ("Typing: T9") and the hint bar naming the next; keys that spell nothing go when # leaves T9 (decision 374, Daria). A message to a service goes round abc, ABC, 123 only (APRS-39). Whether T9 was last chosen is kept for the next message, in the settings record with no menu number (Appendix A, "Kept without a menu number").
> - **TEXT-12** ◀▶ move a cursor in a name (text entry) and in an APRS message; typing, spaces, marks, words and BACK work at the cursor, and what is after it stays. A word being predicted goes in before the cursor moves. ▲▼ and the knob stay on the word suggestions and the quick list. At the start, BACK deletes nothing and doesn't leave.
> - **TEXT-11** The strip shows three candidates at a time at 12 px, a short form counting as one right after its word, and where the highlighted one is ("2/5"); longer lists page with the knob. The hint bar names the keys in use: "Knob Word", "\* Space", "# abc".
>   - **TEXT-11.1** With no word in progress the hint bar is "OK Send", "1 Mark", "# abc", and the line under the strip names the rest ("\* space   hold a digit: digit"); on the quick list it is "Knob Pick", "OK Insert", "\* Write". Multi-tap's line lists its marks ("1 . , ? ! ' / - @ :   \* space") and its hint bar has # with the mode it goes to ("# ABC", "# 123", "# T9").
> - **TEXT-13** Message text holds printable ASCII only: compose's keys (letters, digits, the space and TEXT-2.1's marks) type nothing else, and never APRS's | ~ { (the link's `SEND` refuses those too, chapter 25).

> **Spec: key lock**
>
> - **KEY-13** Hold # toggles the lock; a padlock shows in the status bar while locked. Hold # locks at once in Keypad mode (KEY-14.1), and a popup in the middle of the screen says "Keypad locked" with "\* all · 0 all but PTT" for 3 s. In those 3 s \* makes it All (KEY-14.3) and 0 All but PTT (KEY-14.2), and the popup confirms it ("All keys locked" with "PTT too" or "PTT works"); the key does nothing else (no mute, no home channel). Letting go and pressing neither leaves Keypad; after the 3 s \* and 0 are locked keys like any other (KEY-14.4). Hold # while locked unlocks, from any mode ("Keys unlocked"). The Status page's Key lock row says Off or the mode; the UI readback's `bar` line adds `lockmode=keypad`, `allbutptt` or `all` after `lock=1`.
> - **KEY-20** Auto key lock: after no key or knob input for the set time (off, 30 s, 1, 2 or 5 min; default off; MENU 0 9 1 1, Auto lock) the keys lock in Keypad mode (KEY-14.1), with no popup and no choice (\* and 0 are locked keys at once), the padlock shows, and hold # (with the PIN, when the PIN covers unlocking) unlocks.
> - **KEY-14** Locked, the mode chosen at the lock (KEY-13: Keypad, All but PTT or All; decisions 302, 304) decides what still works. In every mode the volume knob and hold # (KEY-13, KEY-16) work.
>     - **KEY-14.1** Keypad: the front keys and the tuning knob are locked. PTT, SIDE1 (monitor, and SIDE1 + knob or ▲▼ the squelch, SQL-11; not SIDE1 + ◀▶, the clarifier) and SIDE2 (scan, SCAN-1; held alone, the frequency counter, KEY-22; not SIDE2 + knob or ▲▼, the big steps) work.
>     - **KEY-14.2** All but PTT: every key and the tuning knob are locked, the side keys too (no monitor, squelch, scan or counter). PTT works.
>     - **KEY-14.3** All: PTT is locked too: it doesn't key and shows the locked toast (TX-18). The status bar's padlock is red.
>     - **KEY-14.4** A locked key (hold \* too: no quick menu, HOME-17) or tuning knob step shows the toast "Locked — hold # to unlock" and does nothing else; a side key held through it gives nothing at its release (no scan, no monitor). Remote keys obey the lock as the radio's do (LINK-19).
>     - **KEY-14.5** The mode isn't a setting: there is no menu item for it (decision 304 dropped 0 9 1 2 Lock covers; the key test and the shortcut list moved up to 0 9 1 2 and 0 9 1 3). The lock isn't stored either: the radio comes up unlocked at power on. The settings byte that held Lock covers stays in the record, unused, so the record's length is unchanged; what an older record left there has no effect.
> - **KEY-15** Auto lock (0 9 1 1) is KEY-20.
> - **KEY-16** With a PIN set to "at power on and unlock", unlocking asks for it (chapter 34).

### Under the hood


### Status

No mock-up. Key identity from the key test (roadmap 1a, 1c); lock in 2g. Done when every key shows in the key test and all KEY rules pass in the simulator and on the radio.


### Settled details

- The knob has no push switch (confirmed Oct 7, 2026, decision 75); the plan's encoder-push coarse-step toggle is dropped. Coarse steps stay on SIDE2 + knob.
- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - KEY-3: decided Oct 7, 2026. Changed Oct 12, 2026: hold 0 on home acted at its release (HOME-16, decision 108); undone Oct 13, 2026 (decision 109).
  - KEY-7: decision 77; nicFW's PTT keys the active VFO, and stock's PF1 can be set to PTT C. Changed Oct 13, 2026 (decision 109): the quick menu's PTT keys (HOME-17).
  - KEY-21: decided Oct 7, 2026; nicFW's Function menu does the same for its assignable functions; ours stays the fixed ten.
  - KEY-22: decided Oct 7, 2026, decision 77; Stock's PF1 long is the spectrum; nicFW puts its fast scanner on an assignable hold.
  - KEY-23: decided Oct 14, 2026 (user, decision 159). Hold V/M saved a VFO (VFO-9) and copied a channel (VFO-23), and hold 9 opened the zones. A deviation from stock: stock's factory hold 9 is ZONE SELECT (decision 39) and its hold V/M is APRS (the stock manual; the decompile's code-2 action is still undecoded); nicFW's V/M hold is assignable with no documented default, and its "Chan 2 VFO" a function.
  - KEY-23: changed Oct 15, 2026 (decision 178): OK on the zone list now picks the zone for the active slot (CHAN-27).
  - KEY-24: Oct 19, 2026 (Alex, daily use; decision 196): every knob was backwards, probably since the first build: the encoder's direction was never checked (hardware.md's open item 9). Fixed at the decoder (PB5 read as A), so every screen follows. Reversed Nov 9, 2026 (Alex: "turns the wrong way ... I was wrong"; decision 369): A before B again, as the first builds.
  - KEY-12: Nov 9, 2026 (an alpha tester, Alex; decision 367): \* and # swapped to match the key markings, \* (\_) the space and # (^) the case; the owner card had no way to type a space.
  - TEXT-1: decided Oct 6, 2026.
  - TEXT-4: built Oct 7, 2026.
  - TEXT-8: changed Oct 6, 2026.
  - TEXT-9: decided Oct 6, 2026.
  - TEXT-12: decided Oct 7, 2026; nicFW's T9 editor moves its cursor with ▲▼.
  - TEXT-2.1, TEXT-6.1, TEXT-11.1, TEXT-13: Oct 27, 2026 (Alex, daily use; decision 301): punctuation was there (1) but nowhere in the hint bar, and @ : were missing; the quick list had no way out but typing.
  - KEY-20: decided Oct 6, 2026; nicFW's Auto Lock.
  - KEY-14: changed Oct 14, 2026 (decision 153): SIDE1's squelch named (SQL-11) and the clarifier left out.
  - KEY-14: changed Oct 27, 2026 (Alex, daily use; decision 302): Lock covers has three modes (Keypad, All but PTT, All) in place of "keys" and "keys and PTT"; Keypad lets SIDE2 through as well as SIDE1. nicFW's lock leaves only PTT (its manual), as All but PTT does here.
  - KEY-13, KEY-14, KEY-14.5, KEY-20: changed Oct 27, 2026 (Alex, daily use; decision 304): the mode is chosen as the keys lock (hold #, then \* or 0 within 3 s) instead of in 0 9 1 2, which is gone; auto lock always locks the keypad. Stock and nicFW have one lock mode each, set in the menu.
  - KEY-18: changed Oct 12, 2026 (HOME-15): \* on home is quick mute, and skips there too while the active slot scans. Changed Oct 13, 2026 (decision 109): hold \* on home is the quick menu, not while scanning. Changed Oct 27, 2026 (decision 314): \* mutes and unmutes, \* \* within a second turns the slot off; skipping while scanning unchanged.

### Open points

None.

---

