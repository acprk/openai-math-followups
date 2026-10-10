# ω(F) ≤ 9/4 over every field

**Priority.** This was first obtained and fully formalized in Lean by
github.com/selanavot/matrix-multiplication-all-fields (2026-10-06). We found the same three changes
independently on 2026-10-09; we record our checks only.

Changes to the OpenAI argument: (1) Fourier separation with period L ∈ {5M, 5M+1}, whichever is
nonzero in the field (their difference is 1), still with 3(M−1) < L; (2) interpolation nodes chosen
distinct and nonzero in an infinite algebraically closed field; (3) descent: if E/F has degree k,
rank_F(T) ≤ k²·rank_E(T) (apply an F-linear φ: E→F with φ(1)=1), then pass to tensor powers.

Artifacts: `lean/AllFields94_Fourier.lean` (Fourier filter over any field, period choice, primitive
roots in algebraically closed fields) and `lean/AllFields94_Descent.lean` (rank descent) — checked with
Lean 4 / Mathlib v4.33.1, axioms propext, Classical.choice, Quot.sound only.
`scripts/omega94/prop_separation_endtoend.sage`: end-to-end ε-degeneration check of the modified
separation over F_{p^k}, 12 parameter sets incl. p | 5M; negative control with too-small period fails.
