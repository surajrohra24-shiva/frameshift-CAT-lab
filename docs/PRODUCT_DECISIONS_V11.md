# Product decisions — FrameShift v11

**Date:** 27 October 2026  
**Trigger:** Static review from Gemini of the v10 source.

## 1. Feedback-modal keyboard accessibility

The personalised feedback modal previously moved focus to its close button but did not constrain subsequent Tab navigation. v11 adds a document-level Tab trap while the modal is open and restores focus on close. Closing to the full-results action returns focus to the results heading; closing to open the Coach does not perform an intermediate focus restoration because the Coach immediately receives focus. Escape and backdrop closure remain supported.

**Validation:** Scripted browser interaction confirmed Shift+Tab from the first control wraps to the last control, Tab from the last control wraps to the first, and the “View full results” action returns focus to `resultTitle`. A real screen-reader audit remains outstanding.

## 2. Difficulty-aware TITA validation

Previously, any alphabetic character was accepted as an answer even when the variable did not appear in the chosen question. v11 derives valid labels from the selected difficulty: A–E for Low, A–F for Medium, and A–G for High. An unsupported letter leaves Check answer disabled, marks the input invalid, and announces the permitted range. The submitted answer is revalidated immediately before marking. Saved TITA answers also pass through validation during restoration.

**Validation:** Scripted browser test entered Z at High difficulty and confirmed the button stayed disabled with an accessible message; entering G enabled submission and returned the correct answer for Q1 High.

## 3. Pause active clocks when the tab is hidden

v10 calculated elapsed time from wall-clock differences. If the browser tab was hidden for a long period, elapsed session/question/review durations could increase even when the user was not using the prototype. v11 uses `timerNow()` and a `visibilitychange` handler to freeze the effective clock while hidden and shift active start timestamps by the hidden duration when the page becomes visible. The mechanism includes mixed-question feedback review timestamps. Saved elapsed values use the effective active clock.

**Validation:** A scripted browser check simulated a hidden interval and confirmed the elapsed timer remained at the same second after resume. Manual testing by hiding the downloaded page for several minutes is still recommended.

## 4. Session state and privacy

The tab-scoped storage key is now `frameshift-session-v11`. Existing `.gitignore` rules continue to exclude CSV, Excel, raw interview notes and raw research data. Keep participant-level data outside the repository; a GitHub Pages workflow deploying only `index.html` does not hide other files from visitors to a public source repository.

## 5. Deliberate non-change

No extra “fun” animation or gamification was added. The review did not identify evidence that these would improve learning. v11 prioritises keyboard accessibility, valid answer input and accurate active-time measurements.

## Limitations

The current Coach remains a local rule-based demonstration, not live AI. The question bank is illustrative rather than calibrated to official CAT difficulty. No live user study demonstrates improvement in CAT scores or durable concept transfer.
