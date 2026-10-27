# Product decisions — FrameShift v12

**Date:** 27 October 2026

## Decision 1: Debounce TITA validation announcements

- **Problem:** Updating the `aria-live` error region on every input event can create repetitive screen-reader announcements.
- **Change:** Normalize the typed answer and update the enabled state of Check Answer immediately, but debounce the validation text and `aria-invalid` state by 600 ms. On blur, flush the current validation immediately.
- **Trade-off:** A brief delay is introduced before the invalid state is exposed; the visible input and submission eligibility remain responsive.
- **Validation needed:** Test with NVDA, VoiceOver, and keyboard-only use. Confirm messages are announced once after typing pauses and on blur.

## Decision 2: Make personalised recap opt-in

- **Problem:** Automatically opening a modal at the end of the session interrupts the results page and takes control away from the user.
- **Change:** Show the results dashboard first, move focus to its heading, and offer an explicit “View Personalised Recap” button.
- **Trade-off:** Some users may never open the recap; this is preferable to forcing the interaction. The results screen still displays the suggested next activity.
- **Validation needed:** Check keyboard navigation, focus return, and whether users can find and open the recap without instruction.

## Decision 3: Follow OS theme until an explicit override

- **Problem:** Earlier versions stored the detected OS theme in localStorage during initialization, so the application could mistake an automatic choice for a manual preference and stop following OS changes.
- **Change:** Separate the stored theme value from an explicit manual-choice marker. If no explicit override exists, use `prefers-color-scheme` and listen for changes. Manual toggles persist both the selected theme and the explicit marker. A legacy value that conflicts with current OS appearance is conservatively treated as a likely manual preference; a matching legacy value remains system-controlled because its origin cannot be known.
- **Trade-off:** A legacy manual choice that happens to match the current OS theme may be treated as a system preference on first v12 load. This is an unavoidable ambiguity because previous versions did not record whether the choice was automatic or manual.
- **Validation needed:** Test with clean storage, legacy stored values, explicit dark/light choices, storage errors, and live OS changes.

## Scope guardrails

- No additional gamification or animation was added. The focus remains on clarity, user control, accessibility and credible CAT practice.
- The local Coach remains rule-based and offline. No student data or chat transcript is transmitted.
- The personalised recap remains heuristic and must not be described as a validated ability diagnosis or CAT score prediction.
