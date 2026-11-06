# The Ferrite Manual (index)

The manual is the spec for the Ferrite firmware for the Radtel RT-950 Pro. The book lives in per-chapter files in `docs/manual/`; this page is only the index. To change the spec, edit the chapter file.

- Find a rule: grep its prefix in [manual/RULES.md](manual/RULES.md) (e.g. `APRS -> 25-aprs.md`), then read only that chapter.
- Build: `.venv/bin/python docs/tools/mkmanual.py` (from the workspace root) concatenates the chapter files in order into `docs/manual.html` and rewrites the generated Appendices H and I and `manual/RULES.md`. `ferrite/tools/testplan.py` reads the same files.
- Front matter and the contents list: [00-front.md](manual/00-front.md). Chapter files sort in book order (`20-` before `20a-`; appendices `A-` to `I-` last).

| Chapter | File |
| --- | --- |
| 1. About Ferrite | [01-about.md](manual/01-about.md) |
| 2. Before you start: backups and the way back to stock | [02-backups.md](manual/02-backups.md) |
| 3. Installing Ferrite | [03-installing.md](manual/03-installing.md) |
| 4. First-run setup | [04-first-run.md](manual/04-first-run.md) |
| 5. Power on and the self-test | [05-power-on-selftest.md](manual/05-power-on-selftest.md) |
| 6. The home screen and the slots | [06-home-screen-slots.md](manual/06-home-screen-slots.md) |
| 7. Keys and the key lock | [07-keys-lock.md](manual/07-keys-lock.md) |
| 8. The status bar and the Status page | [08-status-bar.md](manual/08-status-bar.md) |
| 9. VFO and frequency entry | [09-vfo.md](manual/09-vfo.md) |
| 10. Channels, zones and the home channel | [10-channels-zones.md](manual/10-channels-zones.md) |
| 11. Quick settings and the menu | [11-quick-settings-menu.md](manual/11-quick-settings-menu.md) |
| 12. Squelch and monitor | [12-squelch.md](manual/12-squelch.md) |
| 13. Watching several slots | [13-multi-slot.md](manual/13-multi-slot.md) |
| 14. Scanning | [14-scanning.md](manual/14-scanning.md) |
| 15. Transmitting: where, how much power, and the checks | [15-transmitting.md](manual/15-transmitting.md) |
| 16. Tones, tone burst and tail elimination | [16-tones.md](manual/16-tones.md) |
| 17. DTMF | [17-dtmf.md](manual/17-dtmf.md) |
| 18. VOX, mic gain, reverse and CW ID | [18-vox-mic.md](manual/18-vox-mic.md) |
| 19. Crossband repeater | [19-crossband.md](manual/19-crossband.md) |
| 20. FM broadcast receiver | [20-fm-broadcast.md](manual/20-fm-broadcast.md) |
| 20a. HF mode | [20a-hf-mode.md](manual/20a-hf-mode.md) |
| 21. Band scope | [21-scope.md](manual/21-scope.md) |
| 22. Tone search and frequency counter | [22-tone-search-counter.md](manual/22-tone-search-counter.md) |
| 23. Weather radio and alerts | [23-weather-alerts.md](manual/23-weather-alerts.md) |
| 24. Notifications, the inbox and the event log | [24-inbox.md](manual/24-inbox.md) |
| 25. APRS | [25-aprs.md](manual/25-aprs.md) |
| 26. KISS TNC | [26-kiss-tnc.md](manual/26-kiss-tnc.md) |
| 27. Decoders: pagers, DSC, AIS | [27-decoders.md](manual/27-decoders.md) |
| 28. GPS, time and waypoints | [28-gps-time.md](manual/28-gps-time.md) |
| 28a. Satellites | [28a-satellites.md](manual/28a-satellites.md) |
| 29. Bluetooth, the cable and the web app | [29-bluetooth-link.md](manual/29-bluetooth-link.md) |
| 30. Updating the firmware | [30-updating.md](manual/30-updating.md) |
| 31. Display, themes and the look | [31-display-themes.md](manual/31-display-themes.md) |
| 32. Sound | [32-sound.md](manual/32-sound.md) |
| 33. Power and Battery Save | [33-power-battery.md](manual/33-power-battery.md) |
| 34. PIN, lock and recovery | [34-pin-recovery.md](manual/34-pin-recovery.md) |
| 35. Calibration and trims | [35-calibration.md](manual/35-calibration.md) |
| 36. About and the self-test | [36-about-selftest.md](manual/36-about-selftest.md) |
| 37. The terminal and mini CPS | [37-terminal-cps.md](manual/37-terminal-cps.md) |
| 38. Packet station: mailbox and TNC | [38-packet-station.md](manual/38-packet-station.md) |
| Appendix A. Every setting, by menu number | [A-settings.md](manual/A-settings.md) |
| Appendix B. The key card | [B-key-card.md](manual/B-key-card.md) |
| Appendix C. Safety rules that apply everywhere | [C-safety.md](manual/C-safety.md) |
| Appendix D. Glossary | [D-glossary.md](manual/D-glossary.md) |
| Appendix F. Navigation | [F-navigation.md](manual/F-navigation.md) |
| Appendix G. Link protocol v1 | [G-link-protocol.md](manual/G-link-protocol.md) |
| Appendix H. Rule index | [H-rule-index.md](manual/H-rule-index.md) |
| Appendix I. Retired rule IDs | [I-retired-ids.md](manual/I-retired-ids.md) |
