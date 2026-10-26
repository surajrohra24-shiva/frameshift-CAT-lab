# Changelog

## v9 — Difficulty levels, visual DI and personalised recap

- Add Low, Medium and High difficulty selection with distinct DILR and mixed-practice variants. High DILR tasks use TITA-style one-letter responses. Labels are exploratory, not CAT-calibrated.
- Add a visual data-interpretation question with an accessible SVG chart and expandable data table.
- Add a personalised results modal based on observed answers, skips and hint use, with rule-based next steps and a clear disclaimer that it is not a validated diagnosis or CAT score prediction.
- Make the focus-switch route six tasks, add level-aware explanations and hint wording, and make the route indicator use six columns.
- Keep local Coach messaging, calculator and CSV export; coach message text is not exported.
- Add and run browser smoke checks for all three difficulty paths, the visual chart/table, the feedback modal, calculator error handling, coach hints, TITA input, dark mode and mobile horizontal overflow.


## v8 — Progressive coaching and safety fixes

- Coach hints for both DILR tasks advance through three stages: nudge, structural hint, and elimination guidance.
- Track coach hint stages and total hints in local session data.
- Prevent the global Enter shortcut from firing when a native button is focused, avoiding double-action/race behavior.
- Add `.gitignore` rules for CSV/Excel exports, local research data and environment files.
- Add documented tests, product decisions, aggregate survey insights and competitor/UI review notes.
- Keep GitHub Pages artifact limited to `index.html`.

## v7 — Practice utility and local coach

- Added a local on-screen calculator and a rule-based contextual coach.
- Added session export and supporting product documentation.

Earlier iterations introduced the focus-switch flow, dark mode, animated transitions, progressive DILR feedback, scratchpads, review flags and session summary.
