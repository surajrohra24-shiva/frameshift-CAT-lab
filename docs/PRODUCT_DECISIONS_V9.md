# Product decisions — v9

## Why this iteration exists

Gemini's static review of v8 recommended richer challenge calibration, varied question types, visual questions, and performance-based feedback. v9 explores these directions without claiming learning efficacy.

## Scope

- **Difficulty picker:** Low, Medium, High selected before the session. These are internally curated prototype variants, not externally benchmarked CAT difficulty levels.
- **Practice types:** DILR ordering, Quant, VARC inference, scoring arithmetic, and visual data interpretation.
- **Visual DI:** SVG bars are generated from hard-coded sample data and accompanied by a details table for non-visual access.
- **TITA:** The high-level DILR questions use a one-letter text response to reduce multiple-choice back-solving.
- **Personalised recap:** A local ruleset uses question correctness, skips, section tags and hint use to recommend a next step. It is not an AI diagnosis, a CAT percentile predictor or a validated learning assessment.
- **Calculator and Coach:** Calculator is a local basic practice calculator. Coach is a rule-based demo with built-in responses, not a live LLM or human mentor.
- **Privacy:** Answers stay in page memory unless the user exports a CSV. Coach message text is not placed into the CSV. Keep exported data and survey response spreadsheets outside source control.

## Limitations

- Sample questions are original prototype exercises and are not certified CAT questions or independently calibrated to official difficulty.
- A six-task session and a single post-session summary cannot diagnose a student's underlying learning difficulty reliably.
- A correct second answer does not establish long-term transfer; this requires real aspirant testing with unseen questions and an appropriate comparison.
- The small self-selected survey (15 submitted records, 14 valid for most core questions) supports feature exploration only; it does not establish market prevalence or adoption.
- The prototype is static/local and has no backend, account system, live AI model, server-side telemetry or multi-device history.

## Competitive boundary

Current competitor pages already advertise mock analysis, personalised plans, adaptive practice, AI insights, hints and question banks. The product hypothesis is the curated focus-switch sequence and differently framed transfer task—not the calculator, chatbot, visual chart, dark mode, confidence control or feedback summary in isolation. See `COMPETITOR_REVIEW.md`.
