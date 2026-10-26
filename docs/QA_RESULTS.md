# QA results — FrameShift v8

**Date:** 27 October 2026  
**Scope:** source-level checks, logical validation, and scripted browser smoke tests. These checks do not substitute for real-user validation or a full accessibility audit.

## Changes carried forward from the Gemini v7 review

- The coach's DILR hints are progressive. The first hint prompts the learner to find relationships without naming the full block; the second identifies the chained block; the third guides legal-placement elimination.
- Hint-stage use is recorded in the local session export.
- The global Enter shortcut exits early when a button has focus, allowing native button activation to handle Enter once.
- `.gitignore` excludes CSV/Excel exports, respondent-level research files, and local environment files.
- The Pages workflow stages only `index.html`; internal research notes, tests and user exports are not included in the published artifact.

## Logic checks

Brute-force enumeration across all 6! permutations confirms:

- DILR Q1 has 3 valid arrangements, with E in slot 6 in each.
- DILR Q2 has 6 valid arrangements, with A in stop 3 in each.
- Progressive hint text is distinct across the three tiers for both DILR questions.
- The Enter-key handler has a guard for focused native buttons.
- Local CSV export is available, but CSV and spreadsheet exports are ignored by Git.

## Known limitations

- Practice questions are original illustrative items, not independently CAT-calibrated.
- FrameShift Coach remains a local rule-based demo, not a live AI service or human mentor.
- Calculator operations are sequential (simple calculator semantics); they do not implement a full expression parser with BEDMAS precedence.
- The product has not been validated on a representative CAT aspirant sample. Prototype activity does not establish learning transfer, CAT score improvement, or market demand.
- No webcam, facial, biometric, eye-tracking or inferred panic detection is implemented.
- Manual cross-browser, assistive-technology and mobile device testing remains necessary before public launch.

## Follow-up browser smoke test (v8 changes)

A scripted Chromium test loaded the HTML source into the browser DOM (direct local-file and localhost navigation were blocked by the environment's administrator policy). The script checked:

- First, second and third Coach hints advance through distinct progressively more direct guidance on DILR Q1.
- Pressing Enter while the Check answer button is focused shows feedback without skipping to the next screen.
- The full five-task path completes, displays the results screen, and starts a CSV download.
- The theme toggle changes the document theme.
- No page-level JavaScript exceptions were captured.

The downloaded file name is `frameshift_v8_session.csv`. These are smoke checks for implemented behavior, not a learning-efficacy test or a full accessibility audit.
- A second scripted browser path reached DILR Q2 and verified that Coach hint 1 does not reveal C–B–A, hint 2 reveals the chained block, and hint 3 provides candidate-placement elimination guidance.
