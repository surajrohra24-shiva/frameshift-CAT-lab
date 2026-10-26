# Gemini review prompt — FrameShift v8

Act as a senior front-end engineer, accessibility reviewer, product analyst and learning-experience designer. Review the attached `index.html` and relevant docs as source code and product artifacts. Be explicit about whether you can execute the file in a live browser; do not claim to have tested interactions if you only inspected source.

Priorities:
1. Verify both DILR answer keys and explanations by enumerating the constraints.
2. Check that the first Coach hint for each DILR question does not reveal the complete block, and that follow-up hints progress logically.
3. Check the global Enter key handler for double-submission with focused native buttons and test keyboard-only flow.
4. Review calculator semantics, accessible labels/focus management, dark mode contrast, reduced-motion behaviour, mobile layout, DOM safety and CSV export.
5. Review `.gitignore` and deployment workflow for accidental exposure of user exports; distinguish deployed artifact from source repository visibility.
6. Compare advertised capabilities of CATin, AdaptHub, CATLab, IMS, iQuanta, 2IIM and MyCATPrep. Use official current sources; distinguish claims from independently verified facts.
7. Identify unsupported product or efficacy claims and propose the three highest-priority fixes.

Do not fabricate participants, interviews, quotations, test results or learning outcomes. Public posts and retrospective mentoring recollections must remain distinctly labelled from genuine interviews. Return source references and prioritized findings, not submission-ready competition prose.
