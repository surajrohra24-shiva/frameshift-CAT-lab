# Product decisions — v13

**Date:** 27 October 2026

## Changes

1. **Screen-transition focus management.** When moving between the intro, task screens and results, focus moves to the destination screen's main heading. Headings receive `tabindex="-1"` only when needed for programmatic focus. This helps keyboard and screen-reader users track context after a screen change.
2. **Drawer focus traps.** The calculator and Coach drawers now keep Tab / Shift+Tab navigation inside the active dialog and return focus to the launcher when closed. Their launch buttons expose `aria-expanded` and `aria-controls` states.
3. **TITA timeout cleanup on submission.** Submitting Q1/Q2 cancels a pending validation timer, synchronizes the current input, and flushes the final validation state immediately. Fired timer handles are nulled, preventing stale timeout state and stale live-region messages.
4. **No additional animations.** This is a reliability/accessibility patch, not a visual redesign. Avoid motion or gamification changes without a user need and test evidence.

## Limits

Automated browser tests can verify focus order and DOM behavior, but cannot establish screen-reader announcement quality or full WCAG conformance. A manual test with NVDA/VoiceOver and a manual browser appearance change remain recommended. Learning transfer and CAT outcome claims remain unvalidated.
