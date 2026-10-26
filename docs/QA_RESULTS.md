# QA results — FrameShift v10

**Date:** 27 October 2026
**Scope:** static source checks, exhaustive DILR answer-key validation, and a scripted Chromium interaction test using a fresh document with a seeded tab-storage snapshot. Direct file navigation was blocked by the environment (`ERR_BLOCKED_BY_ADMINISTRATOR`), so a manual refresh test on the downloaded file is still recommended.

## v10 checks

- DILR logic unit tests cover the Low / Medium / High answer keys by enumerating all permutations: Q1 answers E / E / G; Q2 answers A / A / C.
- JavaScript syntax check passes for the inline script.
- HTML contains a versioned `sessionStorage` snapshot and explicit resume/discard controls on the intro screen.
- TITA inputs no longer have their own Enter-to-submit keydown handler. The document-level global shortcut ignores input elements, so users submit with the Check answer button or by keyboard-focusing that button and activating it.
- The visual chart SVG is marked `aria-hidden="true"` and `focusable="false"`; the equivalent semantic HTML data table is present in a `<details open>` element.
- `.gitignore` excludes `*.csv`, `*.xlsx`, raw interview notes, and raw research data. No participant-level survey data is committed.
- Scripted Chromium interaction checks restored an unanswered Q1 with its selected answer, restored Q1 feedback, verified that Enter in TITA does not submit, verified keyboard activation of Check answer, and restored Q2 feedback and the results screen from seeded snapshots.
- Visual-DI inspection reported `aria-hidden="true"` on the SVG and an open semantic data table. The scripted flow produced no page-level JavaScript errors.
- Progressive hints, calculator, local Coach, light/dark theme, personalized result modal, three difficulty levels and CSV export remain in the source.

## Existing validated logic

- Python unit tests enumerate all permutations for Low / Medium / High DILR answer keys.
- Prior v9 scripted checks passed the six-task flow, calculator basics, hint progression, feedback modal and theme toggle. Those earlier checks do not, by themselves, validate the new v10 persistence/rehydration flow.

## Known limitations

- Session save/restore has passed a seeded-snapshot interaction test for Q1 selection/feedback, Q2 feedback and the results screen. Still manually verify a real refresh in Chrome and the remaining states: unanswered mixed item, already-answered mixed item, skipped mixed item, and Q2 with hints.
- Screen-reader behaviour and visual contrast have not been physically validated in this run.
- Sample questions are original illustrative items, not independently CAT-calibrated.
- The Coach remains a local rule-based demo; no live generative AI or human mentor is connected.
- The calculator is sequential and does not use a full BEDMAS expression parser.
- The personalized recap is a rule-based heuristic, not a validated diagnosis or CAT percentile prediction.
- No real-user study establishes learning transfer, score improvement, adoption or retention.
- The Google Forms sample is self-selected and small (15 submitted; 14 valid for most core questions).
- Keep raw participant data outside the repository, even if the GitHub Pages workflow deploys only `index.html`.
