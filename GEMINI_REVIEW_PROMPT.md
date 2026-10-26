# Gemini review prompt — FrameShift v10

Review the attached `index.html` as a senior front-end engineer, accessibility reviewer and learning-experience designer. Static review is fine, but clearly distinguish inspection from live execution.

FrameShift is an exploratory CAT practice prototype, not an official CAT mock, validated diagnostic, percentile predictor or live AI tutor. Existing competitors advertise analytics, adaptive practice, hints and personalised recommendations, so do not claim these utilities are unique.

## v10 changes to review

1. Tab-scoped `sessionStorage` saves active session state and allows resume/discard from the intro screen after refresh.
2. TITA inputs no longer submit on Enter directly; the user activates the Check answer button.
3. Visual chart SVG is `aria-hidden="true"` and the equivalent semantic HTML data table is open by default.
4. `.gitignore` excludes CSV/XLSX exports and raw research data.

## Review tasks

- Verify DILR answer logic at all three difficulty levels.
- Inspect `persistSessionState`, `safeSessionRead`, `updateResumeBanner` and `restoreSavedSession` for state loss, invalid state, edge cases and loops.
- Check restore scenarios: Q1 unanswered/feedback, mixed unanswered/answered/skipped, Q2 with hints/feedback, and results.
- Confirm Enter in a TITA field does not submit but keyboard activation of the Check answer button works normally.
- Review the chart's accessible table, SVG semantics, keyboard order and reduced-motion behaviour.
- Identify any XSS, storage, data-loss, or privacy issues. Session notes must not be sent to a server; raw respondent data must not be committed.
- Assess whether the practice questions and explanations remain logically correct. Do not claim CAT difficulty calibration without evidence.
- Provide the three highest-priority defects, concrete fixes and test steps. Do not invent user-test results or market statistics.
