import Mathlib

/-!
# Trace-type descent of tensor rank (Lemma 2 of the note)

If `E/F` is a finite extension of degree `k` and a tensor with entries in `F`
has an `E`-decomposition of length `r`, then it has an `F`-decomposition of
length `r * k * k`.
-/

namespace AllFields94

open Module

/-- A decomposition of `T` into `ι`-indexed rank-one terms. -/
def HasDecomp {R : Type*} [CommSemiring R] {X Y Z ι : Type*} [Fintype ι]
    (T : X → Y → Z → R) : Prop :=
  ∃ (a : ι → X → R) (b : ι → Y → R) (c : ι → Z → R),
    ∀ x y z, T x y z = ∑ t, a t x * b t y * c t z

/-- A linear functional `E → F` sending `1` to `1`. -/
theorem exists_unit_functional (F E : Type*) [Field F] [Field E] [Algebra F E] :
    ∃ φ : E →ₗ[F] F, φ 1 = 1 := by
  obtain ⟨ψ, hψ⟩ : ∃ ψ : Module.Dual F E, ψ 1 ≠ 0 := by
    by_contra h
    push Not at h
    exact one_ne_zero ((Module.forall_dual_apply_eq_zero_iff F (1 : E)).mp h)
  exact ⟨(ψ 1)⁻¹ • ψ, by simp [hψ]⟩

theorem rank_descent {F E : Type*} [Field F] [Field E] [Algebra F E] [FiniteDimensional F E]
    {X Y Z : Type*} (T : X → Y → Z → F) (r : ℕ)
    (h : HasDecomp (ι := Fin r) (fun x y z => algebraMap F E (T x y z))) :
    HasDecomp (ι := Fin r × Fin (finrank F E) × Fin (finrank F E)) T := by
  classical
  obtain ⟨a, b, c, habc⟩ := h
  obtain ⟨φ, hφ⟩ := exists_unit_functional F E
  set B := Module.finBasis F E
  refine ⟨fun s x => B.repr (a s.1 x) s.2.1, fun s y => B.repr (b s.1 y) s.2.2,
    fun s z => ∑ l, B.repr (c s.1 z) l * φ (B s.2.1 * B s.2.2 * B l), ?_⟩
  intro x y z
  have hT : T x y z = φ (algebraMap F E (T x y z)) := by
    rw [Algebra.algebraMap_eq_smul_one, map_smul, hφ, smul_eq_mul, mul_one]
  have hx := habc x y z
  simp only at hx
  rw [hT, hx, map_sum, Fintype.sum_prod_type]
  refine Finset.sum_congr rfl fun t _ => ?_
  conv_lhs =>
    rw [← B.sum_repr (a t x), ← B.sum_repr (b t y), ← B.sum_repr (c t z)]
  simp only [Finset.sum_mul, Finset.mul_sum, map_sum, smul_mul_assoc, mul_smul_comm,
    map_smul, smul_eq_mul, Fintype.sum_prod_type]
  -- LHS is ∑ γ ∑ β ∑ α, RHS is ∑ α ∑ β ∑ γ: reverse the order of summation
  rw [Finset.sum_comm]
  rw [Finset.sum_congr rfl fun _ _ => Finset.sum_comm]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ =>
    Finset.sum_congr rfl fun l _ => ?_
  ring

end AllFields94
