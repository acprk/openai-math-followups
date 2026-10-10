# Explicit seeds for a superquadratic bs vs s separation (OpenAI family 132)

OpenAI proves bs(f) ≥ s(f)^α for some α > 2 via a seed f with f(0)=0, bs(f,0) > s(f)² and
composition. Their seed is asymptotic; with their displayed parameters (d=9, M=9^10) the guaranteed
exponent is α ≈ 2.000252, with s ≈ 5.8·10⁹⁶ and n ≈ 3.5·10²³⁷.

## Results (joint with Codex / gpt-6-astra; SAT refutations RUP-checked by an independent checker)
- **No seed with s ≤ 3**, in any dimension: s ≤ 2 gives bs ≤ 3 (Ambainis–Prūsis–Vihrovs 2015), and for
  s = 3 the maximum block sensitivity is 6 (Amano, ISIT 2017 enumeration). Our full-cube SAT search
  independently confirms max bs(f,0) = 3 at s = 2 and recovers (s,bs,n) = (3,6,9).
- **Lemma.** If f(0)=0, s(f) ≤ S, and a disjoint family of minimal sensitive blocks at 0 contains S
  singletons and q two-bit blocks, then 2q ≤ S(S−1).
- **No seed on n ≤ 30 variables.** Minimal blocks have size ≤ s and at most s are singletons; with the
  lemma, S = 4 needs n ≥ 31 and S ≥ 5 needs n ≥ 47. Hence every seed has **s ≥ 4 and n ≥ 31**.
- The smallest open configuration: s = 4, bs(f,0) = 17 on 31 inputs with three singletons and fourteen
  two-bit blocks. Width-S DNF families cannot work (Ambainis–Prūsis bound gives bs0 ≤ (2/3)S(S+1/2) ≤ S²).
