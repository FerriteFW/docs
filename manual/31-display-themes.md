## 31. Display, themes and the look

### What it's for

How every screen looks: frame, fonts, colours, backlight and LEDs. Looks may change; what a key does never does.

### Using it

| To | Go to |
| --- | --- |
| Change theme: dark, daylight (high contrast for sun), night red, cyberpunk | MENU 0 7 1 |
| Change home layout (chapter 6) | MENU 0 7 2 |
| S-meter style, power-on message, boot screen | MENU 0 7 3 |
| Set backlight timeout, brightness, light on transmit, what wakes the screen, the keypad light | MENU 0 7 4 |
| Set the LEDs (and the battery heartbeat) | MENU 0 7 6 |

### Screens

| | | |
| --- | --- | --- |
| ![Home, daylight](img/screens/HomeADay.png) | ![Quick settings, daylight](img/screens/MenuQuickDay.png) | ![Transmit, daylight](img/screens/TransmitDay.png) |
| Home, daylight | Quick settings, daylight | Transmit, daylight |
| ![Home, night red](img/screens/HomeNight.png) | ![Transmit, night red](img/screens/TransmitNight.png) | ![Scope, night red](img/screens/ScopeNight.png) |
| Home, night red | Transmit, night red | Scope, night red |
| ![Home, cyberpunk](img/screens/HomeCyber.png) | | |
| Home, cyberpunk | | |

### Settings

| Menu | Setting | Values | Default |
| --- | --- | --- | --- |
| 0 7 1 | Theme | Dark, daylight, night red, cyberpunk | Dark |
| 0 7 2 | Layout | Watch, single + scope, watch + activity | Watch |
| 0 7 3 1 | S-meter | Bars, dBm | Bars |
| 0 7 3 2 | Power-on text | Off, callsign, 16-character text | Callsign |
| 0 7 3 3 | Boot screen | Logo, owner card | Logo |
| 0 7 4 1 | Backlight timeout | 5, 10, 15, 30 s; 1, 2, 5, 10 min; always on | 1 min |
| 0 7 4 2 | Brightness | 1–10; night red keeps its own level | 7 (night red 3) |
| 0 7 4 3 | Backlight on transmit | Off, on | On |
| 0 7 4 4 | Wake on | Keys; keys and RX; keys, RX and TX | Keys and RX |
| 0 7 4 5 | Key light | Off, with the screen, on key press, always | With the screen |
| 0 7 6 | LEDs | Off; RX and TX; RX, TX, heartbeat (DISP-21) | RX, TX, heartbeat |

> **Spec: frame**
>
> - **DISP-1** Portrait 240 × 320, always (MADCTL 0xC0); never drawn or described as 320 × 240.
> - **DISP-2** Every screen: status bar rows 0–19, content 20–299, hint bar 300–319; 4 px grid, 8 px side margins.
> - **DISP-3** The hint bar says what \*, # and MENU do on this screen.
> - **DISP-4** Redraw only changed rectangles, through a 240 × 40 strip buffer and ST7789 window writes.
> - **DISP-5** Waterfalls use the panel's hardware scroll: one new 240 px row per line, no history in MCU RAM.

> **Spec: look**
>
> - **DISP-6** Text: JetBrains Mono, regular and bold, 12 and 15 px; the menus' rows (MENU 0) at 14 px regular in 25 px rows, every name and value whole (decision 372). Frequency digits: Ferrite Mono Tight, 46 px (active slot) and 26 px (watched), one digit width so frequencies never shift. Barlow Semi Condensed only for the FERRITE wordmark.
> - **DISP-7** Fonts are 4-bit anti-aliased, compiled into MCU flash, English only; nothing depends on stock's font data.
> - **DISP-8** No text under 12 px; text contrast at least 4.5:1 in dark, daylight and cyberpunk. Night red draws all text at full red on black (DISP-18); dark adaptation comes first.
> - **DISP-9** Colours come only from named tokens: background, surface, text, secondary text, accent, receive, transmit, warning, info, slot A, B, C. A theme is one token table; views never use literal RGB.
> - **DISP-10** Colour never carries meaning alone: transmit is red and says TX; every colour state also has a shape.
> - **DISP-11** Colour by exception: amber needs attention, red is critical.
> - **DISP-12** Icons fit a 16 × 16 px box, one colour, drawn from their state's token.
> - **DISP-13** No decorative animation; only live values move (meters, scan position, clock).
> - **DISP-14** Theme and layout never change a key's meaning.
> - **DISP-18** Themes (0 7 1: dark, daylight, night red, cyberpunk) change colours where they enter the drawing primitives (fill, text, masks), once per call. Dark is the token table as drawn; daylight swaps each token for the daylight boards' colour (a colour that isn't a token, such as the scope's waterfall, stays as drawn); cyberpunk swaps each for the owner's cyberpunk palette (ground #0A0414, surface #120826, lines #3A2466, text #F2E9FF, secondary #B9A6D9, dim #6C5A8E; cyan #00F0FF for the accent, slot A, the active card's frequency, key names and the clock; magenta #FF2BD6 for receive, the meter, slot B, warnings and the status and hint bars' rules; yellow #FFE600 for slot C and the battery; colour only, no glows, the corners as in the other themes). Night red is red or black only: grounds, surfaces, card backgrounds and dim fills black; text, digits, lines, outlines and meters full red; a filled highlight (a selected row, the active slot's letter badge, a tag such as RX) solid red with black text on it; the active card marked by a 2 px outline; an empty meter segment or a bar's track a red outline, black inside. No dim red anywhere except the scope's spectrum and waterfall gradient, which keeps red levels at each colour's own brightness. Text is blended from the themed colours. A change redraws the whole screen at once, the boot screen and owner card included; the VT100 terminal is unaffected. The quick menu's PTT B switches to night red and back to the theme in use before it (HOME-17).
> - **DISP-19** Corners suit a pixel screen: 1 px on slot badges, chips, tags and small keys; 2 px on fields and medium boxes; 3 px on cards and full-width boxes. Only dots, pills, rings and icons are fully round (the radii were halved, as 3–6 px looked soft at 240 x 320).
> - **DISP-20** Text in a box is centred on its drawn pixels, not its advance widths (the fonts store whole cells). A box holding one line of 9 px capitals has an odd height (13, 15, 17, 23, 25, 33 px) so they sit evenly; slot badges are 13 x 13. `cargo sim` renders checked by measuring every outlined box.

> **Spec: backlight and LEDs**
>
> - **DISP-15** When the backlight goes off, and what wakes it.
>     - **DISP-15.1** Backlight goes off after the timeout (never with "always on"). Keys and the knob always wake it and start the timeout again. A key or knob step on the radio that wakes it does nothing else; one from the link (LINK-19) wakes it and acts (decision 162). The timeout (0 7 4 1) defaults to 1 min (decided Oct 12, 2026: 15 s felt short on the radio).
>     - **DISP-15.2** A key press wakes it either way, PTT included, and a remote PTT (`KEY`, LINK-20.1) is a PTT press: it lights a dark screen whatever 0 7 4 4 says (decision 175).
>     - **DISP-15.3** A slot receiving wakes it and holds it lit while it lasts with "keys and RX" (the default) or "keys, RX and TX" (0 7 4 4), not with "keys".
>     - **DISP-15.4** A transmission wakes it and holds it lit while it lasts only with "keys, RX and TX".
>     - **DISP-15.5** Broadcast FM isn't receiving here: it never wakes the screen or lights the LED.
>     - **DISP-15.6** Auto power off counts receiving and transmitting whatever 0 7 4 4 says.
>     - **DISP-15.7** The APRS slot receiving (APRS mode's C, and a slot deferring to it, APRS-21.2) never wakes the screen or holds it lit, whatever 0 7 4 4 says: on a busy APRS channel packets come every few seconds and would keep the backlight on (decision 255). A message to us (APRS-6) wakes it as receive would, with "keys and RX" or "keys, RX and TX". Auto power off still counts it (DISP-15.6); the receive LED is unchanged.
> - **DISP-16** Brightness 1–10 (0 7 4 2).
>     - **DISP-16.1** Brightness 1–10 (0 7 4 2, default 7) dims the backlight, and the keypad light with it (DISP-22), by PWM (DISP-23): the steps on a geometric curve (each about 1.41 times the last): 4.5, 6.5, 9, 12.5, 18, 25, 35.5, 50, 71 and 100 % duty. Dark is 0.
>     - **DISP-16.2** 10 is full on, 1 the dimmest still readable indoors, and the steps look even.
>     - **DISP-16.3** On home, the quick menu's knob changes the same level (HOME-17).
> - **DISP-17** The LEDs show transmit and receive, per 0 7 6.
>     - **DISP-17.1** Red LED while transmitting.
>     - **DISP-17.2** Green while receiving.
>     - **DISP-17.3** Per 0 7 6: with it Off, neither lights.
> - **DISP-21** Heartbeat (0 7 6's third value, the default): while the screen is dark, the LEDs flash in the battery's colour (SBAR-9.1's: green above 80 %, yellow down to 31 %, red at 30 % and below or at the low warning): one short flash every 5 s; while a message to you or an alert is unread (INBOX-3.1), red, green, red instead, one after another, every 2 s (DISP-21.1). Yellow assumes the two LEDs blend (bench).
>     - **DISP-21.1** The unread pattern lights one LED at a time: red, green, red, 120 ms each with 120 ms between (red and green together read as a dim blur, not yellow: Alex, Oct 22, 2026).
>     - **DISP-21.2** A heartbeat flash lasts 120 ms, full on (the LEDs have no dimming): 80 ms looked dim (Alex, Oct 22, 2026).
> - **DISP-30** Link transfers (decision 332): while a link client (Console) reads or writes records over the cable or Bluetooth (channels, zones, range presets and their skips, settings, the quick messages, waypoints and DTMF memories, APRS heard and messages, the event log, the way back to stock: `READ`, `WRITE`, `DELETE`, `BEGIN`, `USED`, `READ_MANY`, `WRITE_MANY`, `LOG_READ`, `HEARD`, `MSGS`, `STOCK_RESTORE`, and a `STREAM` of any of them), the green LED flashes, 120 ms on and 120 ms off, lit screen or dark, and goes on for 1 s after the last such frame. The screen readback and Live View (`UI`, a `STREAM` of it), keys, commands, events and audio don't count, nor a request refused for want of `AUTH` (LINK-30). Transmit's red and receive's steady green win over it; it wins over the heartbeat; with 0 7 6 Off nothing lights (DISP-17.3). A firmware update is the bootloader's own (UPD) and unchanged.
> - **DISP-22** The keypad light (PB3) has its own setting, 0 7 4 5: off, with the screen (lit while the screen is), on key press (5 s after any key or knob step, the one that wakes the screen too, while the screen is lit), or always. Lit, it shines at the screen's brightness: the same duty as the screen's current level (night red's in night red), also while the screen is dark ("always"), so one level dims both (DISP-16, DISP-23). Off is duty 0.
>     - **DISP-22.1** The keypad light runs on the screen's curve scaled to a 50 % top: half the screen's duty at every level (2.25 % at 1, 25 % at 7, 50 % at 10), to save power (Alex, Oct 22, 2026; a launch default to review).
> - **DISP-24** A list or table with more rows than fit shows a scroll cue at its right edge: a 3 px track (LINE) beside the rows, x 236–238 right of the values, and a thumb (SUB) sized to the page and placed at the first shown row's share, at least 12 px, with 1 px corners (DISP-19). It shows only while there are rows above or below the page, on every scrolling table (the Status page, settings lists) and list (channels, zones, APRS heard and messages, the event log, waypoints, range presets and skips, Recent, quick messages).
> - **DISP-23** Brightness is PWM at 25 kHz (above flicker and hearing), the screen's and the keypad light's from one level table. The screen's is on PC6 from TMR8 channel 1, PC6's own timer function (no remap). The keypad light's is on PB3 from TMR2 channel 2, PB3's only timer function, on TMR2's partial remap (IOMUX_REMAP TMR2_MUX = 01, written with JTAG kept off); only channel 2's output is enabled, so PA15 (TMR2 channel 1 on that remap) stays the GPIO output it is. The audio capture's ADC trigger is therefore TMR4 channel 4 (ADC1 OCTESEL = 0101), not stock's TMR2 channel 2; its pin PB9 stays the Bluetooth power GPIO. Ferrite's TMR3 is the Embassy time driver. Night red has its own level: 0 7 4 2 sets the level of the theme in use, so night red's (default 3) is kept apart from the others' (default 7).
> - **DISP-26** Backlight on transmit (0 7 4 3, default on): on, a lit screen stays lit for the whole transmission, however long, and the timeout starts again at unkey; off, the backlight and a keypad light following it are dark while keyed and come back at unkey, the timeout where it was. Whether a transmission lights a dark screen is 0 7 4 4's (DISP-15).
> - **DISP-27** While the screen is dark (the backlight's timeout, or dark while keyed, DISP-26) the panel sleeps: display off, then the ST7789's sleep in, and nothing is drawn. Waking, it leaves sleep, waits the panel's 120 ms, turns the display on and redraws the whole screen before the backlight comes back; sleep in and sleep out are at least 120 ms apart. Measured Oct 21, 2026: the panel costs about 7 mA awake (power bench, `docs/dev/power.html`).
> - **DISP-25** No blank-then-draw on live updates: a region that changes while its screen stays up (a frequency, a meter, a list row, a card, a box) goes from its old picture to its new one with no background or partial layer shown between. Each part redraws in place over what it covers, or the region is drawn off the screen in bands a few rows tall and each band sent once. Only a change of screen, page or theme (DISP-18) paints the whole area afresh (with no clear first, DISP-29). Every live update also keeps to its screen's budget of pixels written.
> - **DISP-28** A step through a list repaints only the rows that changed (two, unless it scrolls) and its position line, and reads what the list shows only when the step or the data changed: compose's address book and quick messages as the channel list (until Oct 22, 2026 they rebuilt from flash and repainted their whole box on every step: "slower then grandma at the buffer line", Alex).
> - **DISP-29** Drawing does each piece of work once (decision 267): (1) a region drawn off the screen in bands (DISP-25) runs its drawing once, recorded (fills, rounded boxes, text, masks and the regions inside it, with their arguments), and each band replays the recording; a drawing too big to record runs once per band as before. (2) A new screen (one opened, a page or theme change, the panel woken, DISP-27) isn't cleared first: its drawing is recorded, the background goes only where nothing opaque of it paints, then the drawing goes over it, regions inside it in bands, so each pixel of the content area is written once (twice only under outlines and rounded corners); the few screens too big to record clear first as before. (3) A frame where nothing on the screen changed sends nothing to the panel. (4) After ABC the new large card is drawn first, then the others top to bottom. The pictures are the ones clearing first and drawing per band give; a bench build's `lcd paint old` (TERM-40) brings that way back to compare by eye.

### Under the hood


### Status

Dark theme, fonts and logo approved (0a, 0b); daylight boards drawn, awaiting approval (0c). Daylight and night red are built and switch live in both simulators (Oct 4, 2026); 7a finishes them on real glass. Display and backlight in 1c. Not built yet: DISP-5's hardware scroll for waterfalls (software scroll today; the scope's Status). Done when every DISP rule passes in the simulator and on real glass.


### Settled details

- A key press that wakes a dark screen only wakes it; PTT and the volume knob act at once (decided Oct 6, 2026; PTT is refused only by the key lock's "All", KEY-14.3). A remote key from the link wakes it and acts (decision 162, Oct 14, 2026).
- LEDs: red while transmitting, green while a slot receives, green flashing while Console reads or writes records (DISP-30). While the screen is dark a heartbeat flashes in the battery's colour (green above 80 %, yellow down to 31 %, red at 30 % and below): one short flash every 5 s, or red, green, red every 2 s while a message or alert is unread. A setting turns the heartbeat off (decided Oct 6, 2026; 0 7 6, DISP-21); yellow assumes the two LEDs blend (bench).
- Rule history and comparisons with stock and nicFW (kept here so the rules state behaviour only):
  - DISP-18: decided Oct 4, 2026. Changed Oct 13, 2026 (decision 109): night red on the quick menu's PTT B. Changed Oct 15, 2026 (user, decision 186): night red strict, red or black only (it turned every colour into red at its own brightness, so surfaces and cards were dark-red fills), as the owner's strict mock-up. Changed Oct 15, 2026 (user, decision 188): the cyberpunk theme.
  - DISP-8: changed Oct 15, 2026 (decisions 186, 188): night red's secondary text is full red too; cyberpunk meets 4.5:1.
  - DISP-19: decided Oct 6, 2026.
  - DISP-20: decided Oct 6, 2026.
  - DISP-21: decided Oct 6, 2026.
  - DISP-22: decided Oct 6, 2026.
  - DISP-24: decided Oct 8, 2026, decision 91.
  - DISP-23: decision 76. Changed Oct 12, 2026: TMR8 channel 1 instead of TMR3 (Ferrite's time driver), 25 kHz; night red's own level is 0 7 4 2 while night red is on (no separate item).
  - DISP-15.2: the remote PTT spelled out Oct 15, 2026 (decision 175): a bench test took a remote key-up for a transmission no key started (DISP-15.4).
  - DISP-15, DISP-16, DISP-22, DISP-26: built Oct 12, 2026 (brightness, wake screen on, backlight on transmit; "on key press" now lights for the waking key too). The shown values of 0 7 4 4 and 0 7 6 shortened to fit the menu and the terminal's `set` (RX, TX).
  - DISP-16, DISP-22, DISP-23: changed Oct 12, 2026, after the first radio test: level 1 was too dark, so the old level 2 (4.5 %) is the new floor and levels 2–10 follow a geometric curve (was 2, 4.5, 8, 12.5, 18, 26, 36, 50, 70, 100 %); the keypad light, on/off until then, is dimmed with the screen by PWM on PB3 (TMR2 channel 2, partial remap), and the audio capture's trigger moved from TMR2 channel 2 to TMR4 channel 4 to free TMR2.
  - DISP-16: changed Oct 12, 2026 (user, decision 108): hold 0 + knob on home stepped it too (HOME-16). Changed Oct 13, 2026 (decision 109): the quick menu's knob instead (HOME-17).
  - DISP-30: decided Oct 31, 2026, decision 332 (Alex: a transfer should be visibly running).
  - DISP-29: decided Oct 23, 2026, decision 267: black's cable log had a ABC redraw at 187 ms (131 KB, about 40 ms of it the bus: the rest the card drawing, run once per 8-row band from the slow flash) and every screen open at 263-281 KB for a 153 KB screen (a clear, then the content over it).
  - DISP-25: decided Oct 12, 2026: blanking a region before drawing it flickered on the radio's slow display bus (the scope, home's cards). Changed Oct 13, 2026 (decision 109): a theme change counts as a new page (the quick menu changes it on home).

### Open points

- The token values live in `ferrite-ui` (`gfx.rs` for dark, `theme.rs` for daylight); daylight still needs approval on real glass.

---

