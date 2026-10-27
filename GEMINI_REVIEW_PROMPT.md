# Gemini review prompt — FrameShift v13

Review the attached `index.html` as a senior front-end engineer, accessibility reviewer and learning-experience designer. Static review is fine, but clearly distinguish inspection from live execution.

FrameShift is an exploratory CAT practice prototype, not an official CAT mock, validated diagnostic, percentile predictor or live AI tutor. Existing competitors advertise analytics, adaptive practice, hints and personalised recommendations, so do not claim these utilities are unique.

## v13 changes to review

1. Tab-scoped `sessionStorage` saves active session state and allows resume/discard from the intro screen after refresh.
2. TITA inputs no longer submit on Enter directly; the user activates the Check answer button.
3. Visual chart SVG is `aria-hidden="true"` and the equivalent semantic HTML data table is open by default.
4. `.gitignore` excludes CSV/XLSX exports and raw research data.
5. Personalised feedback modal traps Tab focus and restores focus on close.
6. TITA input is limited to valid labels for the selected difficulty and exposes an error message for unsupported letters.
7. Active timers pause when the tab becomes hidden and resume without charging hidden-tab time.
8. TITA aria-live validation is debounced by 600 ms; validation is flushed on blur and answer-button state remains immediate.
9. Results no longer automatically open the personalised feedback modal; a user-triggered “View Personalised Recap” button opens it.
10. Theme follows OS preference dynamically until the user explicitly overrides it; legacy theme preferences from earlier versions are migrated cautiously.
11. Screen transitions move focus to the destination screen heading.
12. Calculator and Coach drawers trap Tab / Shift+Tab focus and restore focus to their launchers on close.
13. TITA submit clears pending validation timeouts and reserves a stable validation-line height so clearing an error does not shift the Check answer button during pointer activation.

## Review tasks

- Verify DILR answer logic at all three difficulty levels.
- Inspect `persistSessionState`, `safeSessionRead`, `updateResumeBanner` and `restoreSavedSession` for state loss, invalid state, edge cases and loops.
- Check restore scenarios: Q1 unanswered/feedback, mixed unanswered/answered/skipped, Q2 with hints/feedback, and results.
- Confirm Enter in a TITA field does not submit but keyboard activation of the Check answer button works normally. Check unsupported labels (e.g. Z) are rejected at every difficulty tier. Verify debounced live-region messaging does not go stale and blur flushes validation.
- Review the chart's accessible table, SVG semantics, feedback-modal and drawer focus traps/return paths, screen-heading focus, keyboard order and reduced-motion behaviour. Verify the active timer pauses and resumes when document visibility changes. Confirm results do not open a modal without user action, and theme changes follow the OS only when no explicit override is stored.
- Identify any XSS, storage, data-loss, or privacy issues. Session notes must not be sent to a server; raw respondent data must not be committed.
- Assess whether the practice questions and explanations remain logically correct. Do not claim CAT difficulty calibration without evidence.
- Provide the three highest-priority defects, concrete fixes and test steps. Do not invent user-test results or market statistics.
