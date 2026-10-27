# FrameShift — Focus-Switch Learning Lab

A self-contained browser prototype exploring whether a short, guided practice sequence can help CAT aspirants apply reasoning to differently framed questions.

> **Prototype status:** Exploratory MVP. It is not an official CAT mock, validated diagnostic, percentile predictor, live AI tutor or evidence of improved CAT performance. All questions are original illustrative items and are not independently CAT-calibrated.

## v13 features

- Six-task guided practice journey: DILR ordering, Quant percentages, VARC inference, Quant scoring, visual data interpretation, and a new DILR transfer set.
- Step-by-step solutions, candidate-placement diagrams and expandable distractor rationales.
- Progressive three-tier DILR hints in the Coach, moving from a non-revealing prompt to more direct placement guidance.
- Optional confidence, scratchpads, review flags, elapsed-time tracking and a results dashboard with rule-based next actions.
- Light/dark theme with OS-preference synchronization until the user explicitly chooses a theme, animated transitions, reduced-motion support and keyboard shortcuts.
- Local calculator with arithmetic, square root, reciprocal, percentage, sign change, memory and recent calculation history.
- Contextual Coach drawer. The Coach is a **local rule-based demo**, not a generative AI service or a human mentor.
- Low / Medium / High difficulty selection at the start, with distinct DILR and mixed-practice banks. High-level DILR uses type-in-the-answer (TITA) input. Difficulty labels are prototype-defined, not officially CAT-calibrated.
- Accessible SVG chart questions with a corresponding data table.
- A results screen with a suggested next action; the personalised recap modal opens only when requested, and its recommendations are rule-based rather than a validated diagnostic.
- CSV session export, with coach messages excluded from the export; aggregate topic counts and hint levels may be recorded.
- In-progress sessions are saved in `sessionStorage` within the current browser tab and can be resumed after a refresh. A user can discard saved progress from the start screen. Active timers pause while the tab is hidden and resume without counting hidden time. This is tab-local persistence, not cloud sync.

## Run locally

Open `index.html` in a modern browser. No backend, API key, package installation or third-party JavaScript dependency is required.

## Privacy and source control

Session data remains in the browser. In-progress session state is saved in tab-scoped `sessionStorage` so a refresh can be resumed; theme preference is stored in `localStorage`; the app follows the operating-system theme unless an explicit manual choice is recorded. Session progress is not sent to a server unless a future version explicitly adds a backend. Do not enter sensitive information in participant-code or scratchpad fields. Keep exported CSV files, spreadsheet responses, raw interview notes and participant-level research data outside the repository. `.gitignore` excludes common CSV/Excel exports and local data folders, but always review `git status` before committing.

The Pages workflow publishes only `index.html`. A public repository still exposes its source and documentation.

## Research status

The provided Google Forms survey had 15 submitted records and 14 valid responses for most core questions. It is small and self-selected, so findings are directional, not representative. See [`docs/SURVEY_INSIGHTS.md`](docs/SURVEY_INSIGHTS.md); it contains aggregate counts only, not raw responses. Retrospective mentoring observations and public online discussions are not substitutes for required genuine interviews. The concept-transfer hypothesis needs testing with real aspirants.

## Documentation

- [`docs/PRODUCT_HYPOTHESES.md`](docs/PRODUCT_HYPOTHESES.md) — hypotheses and disconfirming evidence.
- [`docs/PRODUCT_DECISIONS_V8.md`](docs/PRODUCT_DECISIONS_V8.md) — rationale for progressive hints, keyboard handling and privacy protection.
- [`docs/PRODUCT_DECISIONS_V10.md`](docs/PRODUCT_DECISIONS_V10.md) — session recovery, explicit TITA submission and chart accessibility decisions.
- [`docs/PRODUCT_DECISIONS_V11.md`](docs/PRODUCT_DECISIONS_V11.md) — focus-trapped feedback modal, difficulty-aware TITA validation and active-time clock handling.
- [`docs/PRODUCT_DECISIONS_V12.md`](docs/PRODUCT_DECISIONS_V12.md) — debounced TITA announcements, opt-in personalised recap, and system theme synchronization.
- [`docs/PRODUCT_DECISIONS_V13.md`](docs/PRODUCT_DECISIONS_V13.md) — screen-heading focus, calculator/Coach focus traps and TITA timeout/layout-shift fixes.
- [`docs/COMPETITOR_REVIEW.md`](docs/COMPETITOR_REVIEW.md) — capability claims and overlap.
- [`docs/UI_BENCHMARK.md`](docs/UI_BENCHMARK.md) — UI principles applied.
- [`docs/SURVEY_INSIGHTS.md`](docs/SURVEY_INSIGHTS.md) — aggregate survey evidence with denominators and limitations.
- [`docs/TEST_PLAN.md`](docs/TEST_PLAN.md) and [`docs/QA_RESULTS.md`](docs/QA_RESULTS.md) — checks and regression steps.
- [`GEMINI_REVIEW_PROMPT.md`](GEMINI_REVIEW_PROMPT.md) — prompt for independent review.
- [`GITHUB_PUBLISH.md`](GITHUB_PUBLISH.md) — GitHub Pages publishing instructions.

## Run automated checks

The core checks need Python 3 and Node.js. The end-to-end browser smoke test additionally needs the Python Playwright package and Chromium:

```bash
python -m unittest discover -s tests -v
node tests/test_source_integrity.cjs
python tests/test_v13_browser.py  # requires Playwright + Chromium
```

## Publish with GitHub Pages

Create a GitHub repository, push the source, select **Settings → Pages → GitHub Actions**, then confirm the `Deploy FrameShift to GitHub Pages` workflow succeeds. The workflow stages only `index.html`. The repository source and internal docs remain public if the repository is public, so keep raw survey data out of it.
