# Product decisions — FrameShift v8

## Why this iteration exists

The v7 review identified three implementation priorities: stage the coach hints, prevent Enter-key double actions on focused buttons, and keep respondent-level exports out of source control.

## Decision 1: Progressive DILR coaching

Coach hint tiers move from a non-revealing prompt, to a structural block clue, to more direct candidate-placement guidance. The intent is to provide help without immediately revealing the decisive deduction. The tier text and user-reported hint stage are recorded locally; this does not itself prove that the hints improve learning.

## Decision 2: Native keyboard activation

The global Enter shortcut now ignores Enter when the target/focused element is a button. Native button activation should perform the requested action once. The keyboard flow still needs manual testing with Tab/Enter throughout the complete session.

## Decision 3: Private session exports

CSV and spreadsheet files are ignored by Git, as are `.env` files and raw respondent data directories. Do not commit raw Google Forms exports, participant-level notes, or other identifiable research information into a public repository. Aggregate and anonymised summaries should be reviewed before sharing.

## Product hypothesis status

FrameShift is exploring whether a short, guided sequence helps students apply reasoning structures to differently framed questions. This remains a hypothesis. Calculator and local coach features are supporting utilities rather than proven differentiators. The survey was small and self-selected; it cannot establish broad market demand or causal product impact.
