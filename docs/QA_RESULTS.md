# QA results — FrameShift v9

**Date:** 27 October 2026
**Scope:** static source checks, exhaustive DILR answer-key validation, and scripted Chromium smoke tests using an injected DOM. This is not a full browser navigation audit, assistive-technology audit or learning-efficacy study.

## Automated checks

- Python unit tests: 4 passed, including brute-force enumeration across all permutations for Low / Medium / High DILR answer keys.
- Node source-integrity test: passed; unique IDs, inline JavaScript syntax, native-button Enter guard, staged hints, and Git ignore rules verified.
- Scripted browser smoke tests completed the six-task flow at all three difficulty levels. The correct-answer path reached the personalised feedback modal at each level.
- High-level TITA accepted a typed letter and submitted on Enter.
- Visual DI rendered an SVG chart and an expandable data table at all three levels.
- A failure-path test reached the recap and produced a section-specific next step.
- Coach hints advanced across stages on a DILR question; calculator addition and divide-by-zero handling behaved as expected.
- Light/dark toggle worked. No JavaScript page exceptions or console errors were captured in the scripted runs.
- At a 390px viewport, the tested results screen had no horizontal document overflow. Intro screenshot and feedback screenshot were captured.

## Static answer-key validation

Brute-force enumeration confirms the forced answers: Low Q1 E in slot 5, Medium Q1 E in slot 6, High Q1 G in slot 7; Low Q2 A at stop 3, Medium Q2 A at stop 3, High Q2 C at stop 3.

## Important limitations

- Browser tests use a programmatically injected HTML DOM because direct local-file/localhost navigation is blocked by the environment's administrator policy. Manual Chrome testing remains recommended.
- Sample questions are original illustrative items, not independently CAT-calibrated.
- The Coach remains a local rule-based demo; no live generative AI or human mentor is connected.
- The calculator is sequential and does not use a full BEDMAS expression parser.
- The personalised recap is a transparent ruleset, not a validated diagnosis or CAT percentile prediction.
- No real-user study establishes learning transfer, score improvement, adoption or retention.
- The Google Forms sample is self-selected and small (15 submitted, 14 valid for most core questions).
- Further keyboard-only and assistive-technology testing is recommended before broad public deployment.
