# The 9/4 matrix-multiplication argument is exactly tight (profile barrier)

**Context.** OpenAI's manuscript *An Upper Bound of 9/4 for the Matrix Multiplication Exponent*
(openai/math, 2026-10-02) proves ω(ℂ) ≤ 9/4 using only five properties of the symmetrized profile
P(a,b) of the polynomial-multiplication tensor C(a,b):
(S) symmetry; (B) P(1,b)=b; (U) P(a,b) ≤ (a+b−1)^{1/t}, t=(p_X+p_Y+p_Z)/3;
(C) discrete concavity in each argument; (T) P(a,3h+a−1) ≥ 3P(a,h).

**Prior art.** The core statement below (minimal profile = P*, "9/4 is the limit of the argument")
was published first in eliottcassidy2000/math, THM-4568 (2026-10-07). We obtained it independently
on 2026-10-09; the extensions in §3 are, to our knowledge, not covered there.

## 1. The extremal profile
Let φ(1)=1, φ(a)=∏_{j=1}^{a−1}(1+1/(3j)) = Γ(a+1/3)/(Γ(4/3)Γ(a)), and
  **P\*(a,b) = φ(m)·(M + (m−1)/2),  m=min(a,b), M=max(a,b).**

**Theorem.** P\* satisfies (S),(B),(C),(T) and (U) with 1/t = 4/3. Hence these properties cannot
yield t < 3/4, i.e. ω < 9/4. Moreover P\*(a,a) = (3a−1)φ(a)/2 equals the lower bound of the paper's
diagonal-growth lemma, so that lemma is exactly optimal.

## 2. Proof sketch
- (C) For b ≥ a, P\*(a,·) is linear with slope φ(a). For b ≤ a the increment is
  φ(b)(a/(3b)+2/3); it is non-increasing iff (3b+1)(a+2b+2) ≤ (a+2b)(3b+3) iff b ≤ a−1.
  Across the diagonal the two increments are both φ(a) (equality).
- (T) For h ≥ a both sides equal φ(a)(3h+3(a−1)/2) (equality). For h < a, compare
  L(a)=φ(a)(3h+1.5a−1.5) and R(a)=φ(h)(3a+1.5h−1.5): equal at a=h, and the increments satisfy
  φ(a)(2+h/a) ≥ 3φ(h) (the successive-ratio numerator factors as 2(a−h)(a−h+1) ≥ 0).
- (U) Elementary induction φ(m)^3 ≤ 2m−1 (or Wendel's inequality) gives
  P\*(a,b) ≤ (M+(m−1)/2)(2m−1)^{1/3} ≤ (a+b−1)^{4/3}.
Exact rational checks: `scripts/omega94/barrier_extra.py`. LP view (`profile_lp.py`, `mind.py`):
under the paper's axioms the local exponent of min P(N,N) is 1.366 → 1.350 → 4/3 (N = 12…32).

## 3. Extensions (joint work with Codex / gpt-6-astra, three rounds, exact arithmetic)
The balanced assignment λ\*(C(a,b)^π)=P\*(a,b)^{3/4}, λ\*(B(m))=m^{3/4}, λ\*(T_m)=m^{9/4}
satisfies, **at all sizes (proved)**, the following additional valid inequalities, so none of them can
push below 9/4:
- all non-symmetrized (per leg-permutation) entropy forms of the paper's inequalities;
- (A) concavity along a+b = const: 2P(a,b) ≥ P(a+1,b−1)+P(a−1,b+1), from sectors on both inputs
  with a shared output leg (auxiliary B_Z(m)); general m version;
- (B) higher determinant filtrations with B_X(m): mP(a,b) ≥ Σ_i P(a, b+m−1−2i);
- (C),(D) bivariate multiplication C(a,b)⊗C(c,d) filtered by powers of D=uw−vs, then graded
  extraction (D gives a full direct sum and the inequality [P(a,b)P(c,d)]^t ≥ Σ P(a+c−1−2i, b+d−1−2i)^t);
- Kronecker super-multiplicativity, unequal and 5-sector chains, costed Fourier filtering;
- wrap-around extraction P(n,n)^t ≥ n and the small Coppersmith–Winograd laser inequality via
  C(n,n) ⇝ CW_{n−2} ≥ cw_{n−2}: P(n,n)^t ≥ (27/4)^{1/3}(n−2)^t;
- any extraction of a single matrix block by monomial degeneration in convolution coordinates
  (abelian triple-product lemma ehl ≤ |G|, with arbitrary powers and dot-product auxiliaries);
- any degeneration T_m ⇝ ⊕ C(a_s,b_s)^{π_s}.
Certified laser lower bounds for C(n,n) at τ=3/4 (interval partitions and the 0/rest partition,
n ≤ 30) stay near 1.26n, below the 1.46n needed to refute P\* and far below the rank 2n−1.

**Still open.** Multi-block laser extractions from higher powers of C after non-monomial base change,
and further T⊗C relations. λ\* is not claimed to be a tensor character (that would imply ω = 9/4).
