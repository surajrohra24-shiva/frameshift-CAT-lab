# FrameShift v8 test plan

## Core practice flow

1. Start a session and complete DILR Q1.
2. Ask the Coach for a hint once; verify the first response does not name the complete A–C–B block.
3. Ask for another hint; verify it advances to the second tier. Ask again and confirm the third tier is more direct.
4. Complete each mixed item and progress to DILR Q2.
5. Repeat the same staged-hint checks for C–B–A.
6. Check the answer and result dashboard; confirm all hint actions and total time are represented.
7. Export CSV to a temporary directory, not the repository.

## Keyboard regression

1. Use Tab to focus an answer option; press Enter and verify only that option is selected.
2. Use Tab to focus Check answer; press Enter and verify the feedback appears exactly once, without skipping to another screen.
3. Repeat for mixed question check/next buttons and the final view-results button.
4. Verify Enter in the Coach input submits the message and is not treated as a practice answer shortcut.

## Privacy regression

1. Export a practice CSV inside a temporary folder under the repository root.
2. Run `git status --short`; confirm the CSV is ignored.
3. Verify no raw survey export or participant-level data is committed.

## Learning hypothesis validation

Conduct separately with real aspirants. Compare immediate and interleaved practice only with a documented protocol. Observe mapping reasoning, answer accuracy on an unseen transfer item, hint use, time and task completion. Do not infer learning transfer from a single correct response or a simulated persona.
