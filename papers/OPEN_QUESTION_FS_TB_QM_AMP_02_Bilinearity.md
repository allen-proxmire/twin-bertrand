# OPEN_QUESTION_FS_TB_QM_AMP_02 — The Bilinearity Fork

*The single remaining hinge of the QM-amplitude reading of the prime escape. Analytic, not computational. This file is the tracked parking spot for all future work on it.*

**Status:** OPEN. Frontier: Montgomery pair-correlation / Bogomolny–Keating. Not settleable by sieve-scale computation.
**Parent:** `FS_TB_QM_Amplitude_Memo.md` (Appendix A) · ED `Paper_FiniteMemoryCeiling_Primes.md` §4.5 · `FS_TB_Bridge.md`.
**Predecessor:** `OPEN_QUESTION_FS_TB_QM_AMP_01` — closed on its decidable axes by `scripts/pg_qm_amplitude_probe.py` (verdict `results/qm_amplitude_probe.md`).

---

## 1. The hinge

> **Does the twin-escape fluctuation admit a *single-amplitude* representation `P = |A|²` with `A` built from the explicit-formula zero-waves `{x^ρ}` (so `arg A` is the Möbius/zero phase the parity barrier withholds) — or is it irreducibly *bilinear*, a connected correlation over *pairs* of zeros that no single amplitude can carry?**

This is criterion **(ii)** of the memo's Appendix A.5. It is the only axis the §4.1 probe could not decide.

## 2. Why it is the only remaining obstruction

The `N = 5×10⁶` probe (`pg_qm_amplitude_probe.py`) closed the two *decidable* axes — both non-negative:

- **(i) trivial-factorization trap — non-negative.** The detrended twin fluctuation (111 sign changes) and the Mertens amplitude `M(x)` (190 sign changes; `M(N)/√N = −0.317`) genuinely oscillate in sign. The escape is a *phase* object, not a positive density trivially equal to `|√f|²`.
- **(iii) finite-memory phase — non-negative.** The optimal finite-memory Möbius correlator `C*(N′,M)` vanishes at least as fast as the `√(M/N)` random-walk bound (log-log slopes −0.73 / −0.62 / −0.53). The Möbius phase is **not** finite-memory; the parity-barrier↔hidden-phase identification survives.
- **(ii) bilinearity — OPEN.** The twin fluctuation has ≈0 linear correlation with the single-zero amplitudes (`corr(Δ₂, M) ≈ 0.06`, `corr(Δ₂, ψ−x) ≈ −0.03`). Consistent with — but not proof of — irreducible bilinearity.

So the analogy survives everything decidable; **the mechanism reduces entirely to this fork.**

## 3. What a verdict would mean

- **Positive** (a genuine single-amplitude `|A|²` with the Möbius phase): upgrades the QM reading from *form* to *mechanism*. "You can't know where in the window" becomes literally the √-level phase-inaccessibility of QM, anchored to theorems. This would be a strong and surprising result.
- **Negative** (the twin correlation is irreducibly bilinear): bounds the analogy. The escape is *not* a single-particle `|ψ|²`; the right object is a **two-point / pair** structure. This is the *expected* outcome (see §5) and is itself a clean, publishable limit for the §4.5 register.

## 4. Why sieve-scale computation cannot settle it

The twin correlation `ψ₂(x) = Σ_{n≤x} Λ(n)Λ(n+2)` is **bilinear** and has **no unconditional explicit formula**. Its fluctuations are governed by *sums over pairs* of zeros `(ρ, ρ′)` — the connected two-point structure, not the single-zero sum that gives `ψ(x)−x` and `M(x)`. Resolving that pair structure empirically would require either (a) the conjectural two-point correlation machinery itself, or (b) high-lying zero statistics far beyond what a sieve to `N` exposes. A bigger sieve sharpens the *template* (§4.1) and the `√(M/N)` *rate* (§4.3); it does **not** reach the pair-correlation layer. Hence: analytic frontier, not a compute target.

## 5. Anticipated shape of the answer *(not a result — a disciplined expectation)*

A connected pair correlation is a **second cumulant (a covariance)**, and a covariance is generically **not** the squared modulus of a *single*-mode amplitude — it is a sum over *pair*-modes. The honest expectation is therefore that **(ii) fires as a bounded negative for the single-amplitude form**, but that a *weaker, more interesting* analogy may hold: the twin escape as a **two-particle / pair amplitude** — a covariance `⟨F(x) F(x+2)⟩` of the explicit-formula amplitude `F`, rather than a single `|A|²`. That is exactly the object Montgomery's pair correlation and the Bogomolny–Keating form factor describe. If anything survives to "mechanism," it is likely this two-point (entangled-pair) reading, not the one-particle `|ψ|²` reading. **Record, do not pursue, until the fork is worked.**

## 6. Pointers (the toolset, not new theory)

- H. L. Montgomery, *The pair correlation of zeros of the zeta function* (1973) — the GUE pair-correlation conjecture.
- E. B. Bogomolny & J. P. Keating, *Random matrix theory and the Riemann zeros I–II* (1995–96) — deriving the Hardy–Littlewood prime-pair correlations from the zeros via the semiclassical **form factor**; the canonical bridge between the twin singular series `2C₂` and zero pair-statistics.
- D. A. Goldston & H. L. Montgomery (1987) — variance of primes in short intervals ↔ pair correlation (the second-moment / covariance link this fork rests on).
- Keating & Snaith (2000); Conrey & Snaith — moments and lower-order terms from RMT.
- Selberg's parity problem; T. Tao's expository notes on the parity barrier — why finite-local (sieve) methods cannot cross to the pair/escape layer.

## 7. Freeze (discipline guardrail)

**No further single-amplitude `|A|²` model attempts — in either memo, in code, or in new operators — until this fork returns a verdict.** Per the memo guardrail box: any construction must be anchored to the zeros / explicit formula or it is out of scope. The next legitimate move on this question is *analytic work on the two-point object of §5*, or *nothing*.

## 8. Landing pads — post-fork integration path *(pre-registered; do not act until a verdict exists, per §7)*

Routing is fixed in advance so the resolution integrates deterministically and without drift.

**Landing pad A — form-level outcome (predicted; see §5).** *Verdict: bilinearity is irreducible; the twin escape is a pairs-of-zeros (covariance) object; no single-amplitude `|A|²`.*
- Mark `OPEN_QUESTION_FS_TB_QM_AMP_01` and `_02` **CLOSED-NEGATIVE (single-amplitude form)**.
- In parent-paper §4.5 and memo Appendix A: change (ii) from OPEN to a **stated bounded limit** — "the analogy holds only at the L²/L¹ structural level; the mechanism is irreducibly bilinear."
- Open **at most one** successor question: the **two-point / pair-amplitude** reading (`⟨F(x) F(x+2)⟩` as a covariance / "two-particle" amplitude), *iff* it can be anchored to the Montgomery / Bogomolny–Keating form factor; otherwise stop.
- Lift the amplitude freeze **only** for that two-point object — never for single `|A|²`.

**Landing pad B — mechanism-level outcome (unlikely; see §3).** *Verdict: a single amplitude `A` with `arg A` = the Möbius phase exists; twin escape = `|A|²` with hidden phase.*
- Mark `_02` **CLOSED-POSITIVE**. This is a strong, surprising result — **flag for independent review (Copilot + external) before any promotion.**
- Promote from §4.5 "tested analogy" to a mechanism claim **only after review**, under the parent paper's form-FORCED / value-INHERITED discipline and a NOT-claims preamble.
- Re-examine the ED bridge: this would make the prime escape a literal `|ψ|²` with the parity barrier as the no-phase-without-measurement statement — but it is still *form*, still **not a confirmation of ED**; keep the unpaid-bill framing.
- Lift the amplitude freeze.

**Either way:** the result feeds the §4.5 register and `FS_TB_Bridge.md`; **no number theory is claimed**; the verdict is recorded here (fork resolution note) alongside `results/qm_amplitude_probe.md`.

---

*The decidable axes are closed; the analogy survives them; what remains is whether the escape is a single amplitude or an irreducible pair. That is an analytic question on the Montgomery–Bogomolny–Keating frontier, and it is parked here until it is worked.*
