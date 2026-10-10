# Follow-ups to OpenAI's math manuscripts (openai/math, Oct 2026)

Results obtained while building on three OpenAI result families. Each file states what is proved,
what is numerical, and what was found earlier by others.

| # | Topic | Status | File |
|---|---|---|---|
| 1 | The 9/4 matrix-multiplication argument is exactly tight; barrier extended to a broad class of new valid inequalities and laser extractions | proved (core statement first in eliottcassidy2000/math THM-4568; extensions new) | `results/01-omega94-profile-barrier.md` |
| 2 | ω(F) ≤ 9/4 over every field | proved; **priority: selanavot/matrix-multiplication-all-fields**; our Lean lemmas included | `results/02-omega94-all-fields.md` |
| 3 | Borsuk: ℂP² is not an 8-dim counterexample; b(ℝP³ projector set) = 11 | numerical | `results/03-borsuk.md` |
| 4 | Sensitivity vs block sensitivity: any explicit seed needs s ≥ 4 and n ≥ 31 | proved (uses Amano 2017) + RUP-checked SAT | `results/04-sensitivity-seed.md` |

No improvement of ω below 9/4 and no Borsuk counterexample below dimension 9 was found.

Reproduction: `scripts/` (Python 3 with numpy/scipy; SageMath for `.sage`), `lean/` (Lean 4 + Mathlib
v4.33.1). Work done with Claude (Anthropic) and Codex (gpt-6-astra) as assistants.
