# The Ferrite Manual

Firmware for the Radtel RT-950 Pro · draft, Oct 2, 2026

Spec, design doc and manual in one: each chapter is one feature, how it's used, and the rules the firmware must follow. A user manual will be derived from it later.

Chapters: **What it's for · Using it · Screens · Settings · Spec** (numbered rules such as `HOME-4`, written against by code and tests; a rule that held several claims is split into sub-rules such as `TX-30.1` under it, each checked one way, decision 160) **· Under the hood · Status · Open points.**

---

## Contents


**Part 1 · Getting started**

- [1. About Ferrite](#1-about-ferrite)
- [2. Before you start: backups and the way back to stock](#2-before-you-start-backups-and-the-way-back-to-stock)
- [3. Installing Ferrite](#3-installing-ferrite)
- [4. First-run setup](#4-first-run-setup)
- [5. Power on and the self-test](#5-power-on-and-the-self-test)

**Part 2 · Everyday use**

- [6. The home screen and the slots](#6-the-home-screen-and-the-slots)
- [7. Keys and the key lock](#7-keys-and-the-key-lock)
- [8. The status bar and the Status page](#8-the-status-bar-and-the-status-page)
- [9. VFO and frequency entry](#9-vfo-and-frequency-entry)
- [10. Channels, zones and the home channel](#10-channels-zones-and-the-home-channel)
- [11. Quick settings and the menu](#11-quick-settings-and-the-menu)
- [12. Squelch and monitor](#12-squelch-and-monitor)
- [13. Watching several slots](#13-watching-several-slots)
- [14. Scanning](#14-scanning)

**Part 3 · Transmitting**

- [15. Transmitting: where, how much power, and the checks](#15-transmitting-where-how-much-power-and-the-checks)
- [16. Tones, tone burst and tail elimination](#16-tones-tone-burst-and-tail-elimination)
- [17. DTMF](#17-dtmf)
- [18. VOX, mic gain, reverse and CW ID](#18-vox-mic-gain-reverse-and-cw-id)
- [19. Crossband repeater](#19-crossband-repeater)

**Part 4 · Listening tools**

- [20. FM broadcast receiver](#20-fm-broadcast-receiver)
- [20a. HF mode](#20a-hf-mode)
- [21. Band scope](#21-band-scope)
- [22. Tone search and frequency counter](#22-tone-search-and-frequency-counter)
- [23. Weather radio and alerts](#23-weather-radio-and-alerts)

**Part 5 · Data and decoders**

- [24. Notifications, the inbox and the event log](#24-notifications-the-inbox-and-the-event-log)
- [25. APRS](#25-aprs)
- [26. KISS TNC](#26-kiss-tnc)
- [27. Decoders: pagers, DSC, AIS](#27-decoders-pagers-dsc-ais)
- [27a. SSTV pictures](#27a-sstv-pictures)

**Part 6 · Location**

- [28. GPS, time and waypoints](#28-gps-time-and-waypoints)
- [28a. Satellites](#28a-satellites)

**Part 7 · Connections**

- [29. Bluetooth, the cable and the web app](#29-bluetooth-the-cable-and-the-web-app)
- [30. Updating the firmware](#30-updating-the-firmware)

**Part 8 · System**

- [31. Display, themes and the look](#31-display-themes-and-the-look)
- [32. Sound](#32-sound)
- [33. Power and Battery Save](#33-power-and-battery-save)
- [34. PIN, lock and recovery](#34-pin-lock-and-recovery)
- [35. Calibration and trims](#35-calibration-and-trims)
- [36. About and the self-test](#36-about-and-the-self-test)

**Part 9 · Packet and the terminal**

- [37. The terminal and mini CPS](#37-the-terminal-and-mini-cps)
- [38. Packet station: mailbox and TNC](#38-packet-station-mailbox-and-tnc)

**Appendices**

- [Appendix A. Every setting, by menu number](#appendix-a-every-setting-by-menu-number)
- [Appendix B. The key card](#appendix-b-the-key-card)
- [Appendix C. Safety rules that apply everywhere](#appendix-c-safety-rules-that-apply-everywhere)
- [Appendix D. Glossary](#appendix-d-glossary)
- [Appendix F. Navigation](#appendix-f-navigation)
- [Appendix G. Link protocol v1](#appendix-g-link-protocol-v1)
- [Appendix H. Rule index](#appendix-h-rule-index)
- [Appendix I. Retired rule IDs](#appendix-i-retired-rule-ids)

---

