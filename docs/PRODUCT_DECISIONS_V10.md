# FrameShift v10 product decisions

## Objective

Improve session continuity and remove avoidable accessibility/usability defects identified in Gemini's static review without adding novelty features that do not demonstrate learning value.

## Decisions

1. **Recover a session after refresh.** The prototype stores the active screen, difficulty, selected answers, feedback status, task timers, hints, review flags, scratchpad text and response records in tab-scoped `sessionStorage`. The intro screen offers Resume or Discard. This is local recovery, not account sync or cloud storage.
2. **TITA submission is explicit.** Enter in the TITA input no longer submits immediately. The user activates Check answer by click or keyboard focus + activation, avoiding an accidental submission while typing.
3. **Chart table is exposed by default.** The generated SVG is hidden from assistive technology, and a semantic HTML table is open by default. The chart and table are equivalent representations, so screen readers do not have to parse a long SVG label before reaching tabular values.
4. **No new gamification solely for novelty.** Keep the existing restrained visual treatment and reduced-motion support. Prioritise question quality, clarity of feedback, session recovery and correctness over confetti, streak multipliers or unnecessary animation.
5. **Privacy by default.** Raw survey spreadsheets and exported session CSVs stay outside source control. `.gitignore` covers common CSV/XLSX formats and research-data folders, but local `git status` must still be checked before every commit.

## Validation still required

- Refresh after answering and before answering each task; confirm that Resume restores the exact state.
- Check resume of an already answered mixed item and of the final results screen.
- Use Tab and Enter through the TITA field and Check answer button; confirm Enter in the field does not submit.
- Inspect the visual-DI question with a screen reader and visually confirm the table is open but not overwhelming.
- Verify that discarding saved progress removes only the current tab's saved session and that starting a new drill clears the old session.

## Non-claims

Session recovery, a calculator, a local rule-based Coach, progressive hints and tailored recap are prototype features. Their presence does not prove improved CAT scores, durable learning transfer, market demand or competitive uniqueness.
