# QA results — FrameShift v11

**Date:** 27 October 2026  
**Scope:** DILR permutation checks, JavaScript/source integrity, and a scripted headless Chromium interaction using the HTML loaded via `page.set_content`.

## v11 checks

- DILR answer-key unit tests enumerate all permutations for Low / Medium / High: Q1 answers E / E / G; Q2 answers A / A / C.
- JavaScript syntax check passes.
- HTML contains no duplicate IDs.
- Modal focus trap: Shift+Tab from the first feedback-modal control wraps to `feedbackOpenCoach`; Tab from the last control wraps to `closeFeedbackBtn`. The “View full results” action restores focus to `resultTitle`.
- TITA validation rejects an unsupported `Z` at High difficulty, keeps Check answer disabled, and announces that the label range is A–G. Entering `G` enables submission and the High Q1 feedback is correct.
- Active-time timer pause/resume logic was simulated in Chromium by pausing the effective clock and dispatching a visibility change; the displayed elapsed seconds were unchanged across the hidden interval. This does not replace a physical multi-minute tab-background test.
- Full six-task Medium flow reached the personalised feedback modal. No browser JavaScript exceptions were captured in this run.
- `.gitignore` excludes CSV, XLSX and raw respondent data.
- Updated source-integrity tests assert the focus trap, return focus, TITA bounds and active-time pause behavior.

## Notes on test environment

Navigation to a local HTTP server was blocked by the test environment's administrator policy, so the scripted interaction loaded the file with `page.set_content`. This run therefore did not validate actual `sessionStorage` recovery across a real page reload. Existing v10 seeded-state checks remain useful, and a manual refresh/resume check in the downloaded v11 file is recommended. Screen-reader behavior and visual contrast have not been physically audited.

## Known limitations

- The Coach is a local rule-based demo, not live generative AI or a human mentor.
- The calculator evaluates chained operations sequentially rather than with full BEDMAS precedence.
- Difficulty levels are prototype-defined and not officially CAT-calibrated.
- The personalised recap is rule-based, not a validated diagnosis or percentile predictor.
- No real-user study establishes learning transfer, score improvement, adoption or retention.
- The survey remains small and self-selected (15 submitted; 14 valid for most core questions).
- Keep raw survey response files outside the repository and review `git status` before every commit.
