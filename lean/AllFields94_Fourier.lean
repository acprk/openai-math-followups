import Mathlib

/-!
# Field-independent ingredients for `ω(F) ≤ 9/4` (Fourier filter, period choice)

Generalizes `OAI/LinearAlgebra/MatrixMultiplication/AuxiliarySeparation/Separation/Fourier.lean`
from `ℂ` to an arbitrary field, and supplies the only new arithmetic input:
a period `L` with `3(M-1) < L ≤ 5M+1` that is nonzero in the field.
-/

namespace AllFields94

/-- Fourier filter over an arbitrary field with a primitive `L`-th root of unity. -/
theorem sum_zpow_primitive_root {K : Type*} [Field K] {ζ : K} {L : ℕ}
    (hζ : IsPrimitiveRoot ζ L) (e : ℤ) :
    (∑ r ∈ Finset.range L, ζ ^ ((r : ℤ) * e)) =
      if (L : ℤ) ∣ e then (L : K) else 0 := by
  have hpow : (ζ ^ e) ^ L = 1 := by
    rw [← zpow_natCast, ← zpow_mul, mul_comm, zpow_mul, hζ.zpow_eq_one, one_zpow]
  have hterm (r : ℕ) : ζ ^ ((r : ℤ) * e) = (ζ ^ e) ^ r := by
    rw [← zpow_natCast, ← zpow_mul, mul_comm]
  simp_rw [hterm]
  split_ifs with hd
  · have : ζ ^ e = 1 := (hζ.zpow_eq_one_iff_dvd e).mpr hd
    simp [this]
  · have hne : ζ ^ e ≠ 1 := fun h => hd ((hζ.zpow_eq_one_iff_dvd e).mp h)
    have hsum : (1 - ζ ^ e) * ∑ r ∈ Finset.range L, (ζ ^ e) ^ r = 0 := by
      rw [mul_neg_geom_sum, hpow, sub_self]
    exact (mul_eq_zero.mp hsum).resolve_left (sub_ne_zero.mpr (Ne.symm hne))

/-- Normalized filter: needs only `(L : K) ≠ 0` (replaces `L ≠ 0` over `ℂ`). -/
theorem normalized_filter {K : Type*} [Field K] {ζ : K} {L : ℕ}
    (hL : (L : K) ≠ 0) (hζ : IsPrimitiveRoot ζ L) {e : ℤ} (he : |e| < (L : ℤ)) :
    (L : K)⁻¹ * (∑ r ∈ Finset.range L, ζ ^ ((r : ℤ) * e)) = if e = 0 then 1 else 0 := by
  rw [sum_zpow_primitive_root hζ e]
  have key : (L : ℤ) ∣ e ↔ e = 0 := by
    constructor
    · intro hd
      exact abs_eq_zero.mp (Int.eq_zero_of_dvd_of_nonneg_of_lt (abs_nonneg e) he
        ((dvd_abs (L : ℤ) e).mpr hd))
    · rintro rfl; exact dvd_zero _
  simp only [key]
  split_ifs <;> simp [hL]

/-- In every field one of `5M`, `5M+1` is nonzero, and both exceed `3(M-1)`. -/
theorem exists_good_period (K : Type*) [Field K] (M : ℕ) :
    ∃ L : ℕ, 3 * (M - 1) < L ∧ L ≤ 5 * M + 1 ∧ 0 < L ∧ (L : K) ≠ 0 := by
  by_cases h : ((5 * M : ℕ) : K) = 0
  · refine ⟨5 * M + 1, by omega, le_rfl, by omega, ?_⟩
    intro h'
    push_cast at h h'
    have : (1 : K) = 0 := by linear_combination h' - h
    exact one_ne_zero this
  · rcases Nat.eq_zero_or_pos M with hM | hM
    · subst hM; exact ⟨1, by omega, by omega, by omega, by simp⟩
    · exact ⟨5 * M, by omega, by omega, by omega, h⟩

/-- An algebraically closed field has a primitive `L`-th root whenever `L ≠ 0` in it. -/
theorem exists_primitive_root (K : Type*) [Field K] [IsAlgClosed K] {L : ℕ}
    (hL : (L : K) ≠ 0) : ∃ ζ : K, IsPrimitiveRoot ζ L := by
  haveI : NeZero (L : K) := ⟨hL⟩
  exact HasEnoughRootsOfUnity.exists_primitiveRoot K L

end AllFields94
