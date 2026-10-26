# FrameShift v9 test plan

## Difficulty and session flow

1. Start a new session at Low, Medium and High; verify the selected question bank and level badge match the chosen level.
2. Complete Q1, the four mixed-practice tasks, and Q2. Confirm the session contains six tasks.
3. For High, enter the TITA letter answer for each DILR task; press Enter inside the text input and confirm only the current answer is submitted.
4. Confirm each level's DILR answer and explanation match the clues.
5. Confirm the visual DI task renders both an SVG chart with an accessible label and an expandable table containing the same data.
6. Check the personalised recap after all-correct, mixed-correct, and several-incorrect sessions. Confirm the next step changes according to the error pattern and the disclaimer is visible.
7. Close the modal using the close button, secondary action, Escape, and backdrop click where applicable.

## Coach and calculator

1. On each DILR task, request hints in order and verify the guidance becomes more specific without showing the final placement at Hint 1.
2. Use the Coach during Quant, VARC and visual DI; verify its responses correspond to the current task.
3. Verify chat scrolling reaches the newest message after a reply.
4. Test calculator add, subtract, multiply, divide, decimals, square root, reciprocal, sign, percentage, memory and division by zero. The calculator uses sequential-operation semantics rather than a full BEDMAS expression parser.

## Keyboard, themes, responsiveness

1. Tab to an answer option and press Enter; verify only that option is selected.
2. Focus Check answer and press Enter; confirm feedback appears exactly once without skipping the screen.
3. Verify high-level TITA fields accept one letter and Enter submits once.
4. Open and close calculator/Coach and test focus return and Escape behaviour.
5. Toggle light/dark themes and confirm readable text. Test at narrow mobile width and check for horizontal overflow.
6. Check reduced-motion preference and ensure motion is reduced.

## Privacy

1. Export session data to a temporary location, outside the repository.
2. Run `git status --short`; verify CSV, XLSX, raw notes and local data folders are not tracked.
3. Confirm chat message text is not in the exported session CSV.
4. Review the public Pages artifact separately from the repository source.

## Learning hypothesis validation

Run separately with real CAT aspirants. If testing transfer, use a documented protocol and unseen items. An option-level success, one simulated persona or one local session is not proof of durable transfer or CAT-score improvement. Record limitations and negative results.
