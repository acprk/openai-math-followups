# Borsuk numbers of projective-space projector sets (towards dimension 8)

OpenAI family 156: the set X of rank-one projectors of ℝ⁴ (≅ ℝP³) in the 9-dimensional trace-one
space cannot be covered by 10 sets of smaller diameter, so Borsuk fails in dimension 9.
A set piece has smaller diameter iff it contains no two orthogonal lines.

## Results (numerical, reproducible; not yet interval-certified)
1. **ℂP² is not an 8-dimensional counterexample.** The projectors of ℂ³ lie in the 8-dimensional
   trace-one Hermitian space. Partition by nearest line among the 9 Hesse SIC lines
   (|⟨c_i,c_j⟩|² = 1/4): inside every cell min |⟨u,v⟩| ≈ 0.10–0.16 on 2·10⁵ samples, and targeted
   search finds no orthogonal pair (smallest deficit 0.069). So b(ℂP²-projector set) ≤ 9.
   (`scripts/borsuk/sic_cover.py`)
2. **b(X) = 11 numerically.** Nearest-line partitions of ℝP³ by K optimized lines:
   K = 11 valid with margin 0.036; K = 12 valid (margin 0.001); K = 10 invalid, consistent with
   OpenAI's theorem (negative control). With OpenAI's lower bound this gives b(X) = 11.
   (`scripts/borsuk/rp3_voronoi.py`)
3. **Consequence.** There is no slack: an 8-dimensional section/subset of X would need b ≥ 10 while
   losing a topological dimension, so the "cut X down to dimension 8" route is essentially dead.
   Spectrum-symmetric SU(3) adjoint orbits in ℝ⁸ have diameter pairs = antipodal pairs and need at
   most 8 pieces. A dimension-8 counterexample would need a new family with an orthogonality-type
   (not antipodal) diameter relation.

To make (2) a theorem, the 11 cells must be certified (interval arithmetic / branch-and-bound over
u ∈ S³, v ⊥ u).
