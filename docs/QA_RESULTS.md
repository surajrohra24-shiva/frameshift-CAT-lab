# QA results — FrameShift v12

**Date:** 27 October 2026  
**Scope:** Answer-key enumeration, source integrity, accessible controls, TITA live-region behavior, explicit recap action, theme preference synchronization, and scripted Chromium interaction checks.

## v12 checks

- DILR permutation tests enumerate Low / Medium / High answer keys: Q1 E / E / G; Q2 A / A / C.
- JavaScript syntax check passes; HTML has no duplicate IDs.
- TITA filtering and Check Answer state remain immediate; only the `aria-live` message and `aria-invalid` update are debounced by 600 ms. Blur flushes validation immediately. Unsupported answer letters remain blocked.
- `showResults()` no longer opens the feedback modal automatically. The results heading receives focus, and **View Personalised Recap** opens the modal on explicit activation.
- Theme initialization prefers an explicitly selected theme; otherwise it follows `prefers-color-scheme` and responds to OS changes. Manual toggles persist a choice marker. Legacy theme values are not blindly trusted because earlier versions persisted auto-detected OS modes as if they were manual choices.
- Session snapshots do not reapply the prior theme as a manual override.
- Existing focus trap, active-time clock pause, chart-table accessibility, CSV/XLSX `.gitignore` and local-only session behavior remain in place.
- Python DILR tests (4 tests) and Node source-integrity assertions passed after the v12 changes.
- Scripted Chromium smoke tests passed using `page.set_content` because navigation to local files is blocked by the test environment: (1) system theme follows OS changes before a manual override, and the manual choice is respected afterward; (2) TITA validation message remains quiet while typing, appears after the debounce, clears promptly on blur, and button state is immediate; (3) the complete six-task route reaches results without opening the modal automatically, the results heading receives focus, the recap button opens the modal, and closing it restores focus to the button.
- Theme migration tests passed for empty preferences, a legacy theme conflicting with the current OS, a legacy value matching the OS (continues to follow OS), and an explicit manual override.

## Known limitations / manual checks

- A physical screen-reader audit has not been completed; debounce timing reduces repetitive announcements but needs assistive-technology testing.
- A scripted media-emulation test verified OS-theme changes and explicit overrides. Still manually verify a real operating-system appearance change in the downloaded file.
- The scripted six-task flow verified the recap modal is not shown automatically, the results heading is focused after finishing, and the recap button opens the modal. Confirm these paths manually with a keyboard and screen reader.
- Check a multi-minute hidden-tab timer pause and refresh/resume using the downloaded file in the target browser; earlier timer simulation passed, but this v12 run focused on the requested three changes.
- The Coach is a local rule-based demo, not live AI or a human mentor. Difficulty tiers are prototype-defined, not officially CAT-calibrated. Personalised recommendations are heuristic, not a validated diagnosis or score predictor. No real-user study establishes learning transfer, score improvement, adoption or retention.
- The survey is small and self-selected (15 submitted; 14 valid for most core questions). Keep raw responses and exports outside the repository.
