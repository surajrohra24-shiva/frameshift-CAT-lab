# QA results — FrameShift v13

**Date:** 27 October 2026  
**Scope:** Screen-heading focus on route changes, calculator/Coach focus traps, TITA validation-timeout cleanup, core question logic, and end-to-end browser flow.

## Automated checks

- Four DILR permutation tests pass across Low / Medium / High question variants.
- JavaScript syntax and source-integrity tests pass.
- Screen transitions focus the new screen heading (intro, task screens and results).
- Calculator and Coach dialog focus remains within the active dialog under Tab and Shift+Tab; closing returns focus to the launcher.
- TITA validation remains debounced during typing; submission clears any pending timer and synchronizes the final `aria-invalid`/message state. Playwright reproduced a layout shift when a prior error cleared on blur before pointer click; the validation line now reserves enough vertical space, and the regression test confirms the Check answer button position remains stable.
- The complete High-difficulty practice route reaches results in scripted Chromium testing. The test covers Q1 invalid-to-valid TITA entry, timer cleanup, answer feedback, heading focus, mixed practice, Q2 submission, results, modal focus cycling, and calculator/Coach drawer focus traps.
- The personalised recap does not open automatically; explicit activation opens it and the modal traps focus.
- Git ignore rules continue to exclude CSV/XLSX exports and local research files.

## Test run

Commands run successfully: `python -m unittest discover -s tests -v` (4 tests), `node tests/test_source_integrity.cjs`, and `python tests/test_v13_browser.py` (scripted Chromium via Playwright). The loopback server is blocked in this environment, so the test injects the complete HTML into a real Chromium page with `page.set_content`; it exercises actual DOM events and focus behavior but is not a deployed-site test.

## Manual checks still recommended

- Physically test with NVDA on Windows or VoiceOver on macOS/iOS, including announcement verbosity for TITA validation and heading changes.
- Use Chrome's DevTools Accessibility tree and Lighthouse, then run axe DevTools on the deployed page.
- Keyboard-test the drawers and feedback modal without using the mouse; this complements, but does not replace, automated checks.
- Manually test mobile layout at common viewport widths and the system light/dark preference in an actual browser environment.
- Do not describe this as a full accessibility certification or as proof that FrameShift improves learning. The prototype and 14-response usable survey are exploratory only.
