# FrameShift — Focus-Switch Learning Lab

A self-contained browser prototype exploring whether a short, guided practice sequence can help CAT aspirants apply reasoning to differently framed questions.

> **Prototype status:** Exploratory MVP. It is not an official CAT mock, validated diagnostic, percentile predictor, live AI tutor or evidence of improved CAT performance. All questions are original illustrative items and are not independently CAT-calibrated.

## v8 features

- Guided five-task practice journey: DILR ordering, Quant percentages, VARC inference, Quant scoring and a second DILR constraint set.
- Step-by-step solutions, candidate-placement diagrams and expandable distractor rationales.
- Progressive three-tier DILR hints in the Coach, moving from a non-revealing prompt to more direct placement guidance.
- Optional confidence, scratchpads, review flags, elapsed-time tracking and a results dashboard with rule-based next actions.
- Light/dark theme, animated transitions, reduced-motion support and keyboard shortcuts.
- Local calculator with arithmetic, square root, reciprocal, percentage, sign change, memory and recent calculation history.
- Contextual Coach drawer. The Coach is a **local rule-based demo**, not a generative AI service or a human mentor.
- CSV session export, with coach messages excluded from the export; aggregate topic counts and hint levels may be recorded.

## Run locally

Open `index.html` in a modern browser. No backend, API key, package installation or third-party JavaScript dependency is required.

## Privacy and source control

Session data remains in page memory unless the user chooses to export a CSV. Theme preference is stored in `localStorage`. Do not enter sensitive information in participant-code or scratchpad fields. Keep exported CSV files, spreadsheet responses, raw interview notes and participant-level research data outside the repository. `.gitignore` excludes common CSV/Excel exports and local data folders, but always review `git status` before committing.

The Pages workflow publishes only `index.html`. A public repository still exposes its source and documentation.

## Research status

The provided Google Forms survey had 15 submitted records and 14 valid responses for most core questions. It is small and self-selected, so findings are directional, not representative. See [`docs/SURVEY_INSIGHTS.md`](docs/SURVEY_INSIGHTS.md); it contains aggregate counts only, not raw responses. Retrospective mentoring observations and public online discussions are not substitutes for required genuine interviews. The concept-transfer hypothesis needs testing with real aspirants.

## Documentation

- [`docs/PRODUCT_HYPOTHESES.md`](docs/PRODUCT_HYPOTHESES.md) — hypotheses and disconfirming evidence.
- [`docs/PRODUCT_DECISIONS_V8.md`](docs/PRODUCT_DECISIONS_V8.md) — rationale for progressive hints, keyboard handling and privacy protection.
- [`docs/COMPETITOR_REVIEW.md`](docs/COMPETITOR_REVIEW.md) — capability claims and overlap.
- [`docs/UI_BENCHMARK.md`](docs/UI_BENCHMARK.md) — UI principles applied.
- [`docs/SURVEY_INSIGHTS.md`](docs/SURVEY_INSIGHTS.md) — aggregate survey evidence with denominators and limitations.
- [`docs/TEST_PLAN.md`](docs/TEST_PLAN.md) and [`docs/QA_RESULTS.md`](docs/QA_RESULTS.md) — checks and regression steps.
- [`GEMINI_REVIEW_PROMPT.md`](GEMINI_REVIEW_PROMPT.md) — prompt for independent review.
- [`GITHUB_PUBLISH.md`](GITHUB_PUBLISH.md) — GitHub Pages publishing instructions.

## Run automated checks

Python 3 and Node.js are sufficient:

```bash
python -m unittest discover -s tests -v
node tests/test_source_integrity.cjs
```

## Publish with GitHub Pages

Create a GitHub repository, push the source, select **Settings → Pages → GitHub Actions**, then confirm the `Deploy FrameShift to GitHub Pages` workflow succeeds. The workflow stages only `index.html`. The repository source and internal docs remain public if the repository is public, so keep raw survey data out of it.
