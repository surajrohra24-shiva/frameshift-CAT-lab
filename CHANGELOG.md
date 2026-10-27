## v12 — Accessible validation, user-controlled recap and OS theme sync (27 October 2026)

- Debounce TITA validation messaging by 600 ms so the `aria-live` region does not announce errors on every keystroke. Input normalization and Check Answer eligibility still update immediately; blur flushes validation promptly.
- Remove automatic opening of the personalised feedback modal at session completion. The results screen now presents an explicit **View Personalised Recap** button, and focus moves to the results heading when the screen appears.
- Synchronize light/dark theme with the operating-system preference when no explicit user override exists. Explicit theme toggles persist a separate manual-choice marker. Legacy theme values from earlier versions are migrated cautiously because old versions stored automatic OS choices as if they were user selections.
- Session restoration no longer overwrites the resolved theme from an old snapshot.
- Add source-integrity regression assertions for debounced TITA validation, explicit recap opening, OS theme synchronization, and theme migration behavior.

# Changelog

## v10 — Session recovery and accessibility hardening

- Add tab-scoped `sessionStorage` snapshots for active tasks, selected answers, feedback state, elapsed times, hints, review flags, scratchpad content and current mixed-practice position. A start-screen banner allows a participant to resume or discard saved progress after a refresh.
- Remove Enter-to-submit handlers from TITA text inputs; submission now requires activating the visible Check answer button (including normal keyboard activation when focused).
- Hide the SVG chart drawing from assistive technology and expose its equivalent semantic HTML data table open by default.
- Keep raw survey spreadsheets and session CSV exports excluded from version control; no participant-level data is included in the repository.
- Update the regression suite and documentation to cover persistence, TITA submission behaviour and chart-table accessibility.


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


## v11 — Gemini review fixes (27 October 2026)

- Added a keyboard focus trap to the personalised feedback modal and restored focus to the results heading or invoking context when the modal closes.
- Added difficulty-aware TITA answer validation, with visible and screen-reader-announced feedback for labels outside the valid entity range.
- Added active-time clock handling: elapsed timers pause when the page becomes hidden, then shift their start references on return so background time is not counted. The pause/resume behavior covers the session, active question, and feedback review intervals.
- Updated the local session-storage key to `frameshift-session-v11` to keep v11 snapshots separate from earlier prototype versions.
- Added source-integrity assertions for these behaviours and updated QA documentation.
- No new gamification or animation effects were added; focus remains on reliability and accessibility.
