# OPEN_QUESTION_FS_TB_QM_AMP_02 — The Bilinearity Fork

*The single remaining hinge of the QM-amplitude reading of the prime escape. Analytic, not computational. This file is the tracked parking spot for all future work on it.*

**Status:** RESOLVED (heuristic-structural, 2026-06-16) → **Landing Pad A: CLOSED-NEGATIVE for single-amplitude `|A|²`** (see §9). Rigorous version remains open (Bogomolny–Keating). One successor opened: whether the **one-object (non-separable) twin pattern** is *quantum*-entangled (Bell-non-classical) or merely classically correlated (§9.5).
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

## 9. Resolution — routed to Landing Pad A *(heuristic-structural, 2026-06-16)*

**9.1 The reformulation.** "Single-amplitude `|A|²`" means the zero-pair kernel `K(ρ,ρ')` is **separable / rank-1**: `K(ρ,ρ') = c_ρ c̄_{ρ'}`. (Note `|A|²` of *any* single sum `A = Σ_ρ c_ρ(·)` is already a double sum over pairs — so "bilinear" alone does not settle it; **separability** does.) QM dictionary: rank-1 = a **pure, separable** state — effectively *two independent things*; rank > 1 = a **non-separable** density matrix — *one object that cannot be split into independent parts* (the structural core of entanglement; in our working terms, **one pattern sampled twice**).

**9.2 The argument.** With the standard heuristic `Λ(n) = 1 − Σ_ρ n^{ρ-1} − …`, the twin correlation `ψ₂(N) = Σ_{n≤N} Λ(n)Λ(n+2)` splits into a mean, single-zero (linear, `~√N`, *not* twin-specific) terms, and a pair term

$$\sum_{\rho,\rho'} \sum_{n\le N} n^{\rho-1}(n+2)^{\rho'-1} \;\approx\; \sum_{\rho,\rho'} \frac{N^{\rho+\rho'-1}}{\rho+\rho'-1}.$$

The pair-kernel `K(ρ,ρ') ∝ N^ρ N^{ρ'}/(ρ+ρ'−1)` fails to factor: the coupling `1/(ρ+ρ'−1)` is a **Hilbert kernel**, and the Hilbert matrix `1/(i+j−1)` is the classical **infinite-rank** positive operator (bounded, norm π, continuous spectrum `(0,π)`, never finite-rank). Via `1/(ρ+ρ'−1) = ∫_0^1 u^{ρ-1}u^{ρ'-1}\,du` the kernel is a *continuous superposition* of rank-1 pieces — a density matrix with continuous Schmidt spectrum.

**9.3 Verdict (Pad A) — one object, sampled twice.** The twin escape is **non-separable: no single-amplitude `|A|²` / no pure-state square** — the zero-pair kernel is Hilbert / infinite-rank, so it does **not** factor into a fact-about-`n` times a fact-about-`n+2`. Criterion (ii) is answered **NEGATIVE** for the single-amplitude form; the QM analogy is **form-only** at that level. The correct reading is therefore *not* "two correlated particles" but **one object sampled twice**: the twin is a single pattern — the non-separable pair-kernel — read out at offset 0 and offset 2. The **Schmidt decomposition makes this exact**: the two sampling sites share **one** spectrum `{λᵢ}` and one set of modes (`ρ(ρ,ρ') ∝ N^{ρ+ρ'}/(ρ+ρ'−1)`), not two spectra that happen to match. The phase the parity barrier withholds belongs to the *one* object and is visible only by comparing the two samplings — it is not a wire strung between two pre-existing things. *Single primes ↔ a pure single-particle amplitude (`ψ(x)−x`, `M(x)`); a twin ↔ one un-individuated pattern sampled at two offsets.*

**9.4 The individuation block (the load-bearing consequence).** ED's entanglement arc (Papers 063–072) reads entanglement as the **unresolved regime of participation-rule individuation** — one undivided pattern not yet split into separate things. What performs the split ("individuation") is commitment / doing the work; for the primes that work is the sieve, and **the parity barrier is exactly the proof that finite-memory work cannot perform the split.** Consequence, stated plainly:

> **A finite-memory (sieve / finite-local) observer cannot individuate a twin into two independent primality facts. Relative to that observer it remains one un-resolved pattern.**

So the parity barrier is not merely "a phase you can't read" — it is *the thing that keeps the twin un-individuated.* "Can't know where in the window" and "can't factor the twin into two independent facts" are the same wall. This is the bridge's strongest structural statement; it is **heuristic-structural** and **observer-relative** (it concerns what finite-memory methods can resolve, not a claim that the integers are physically un-individuated).

*The information-theoretic face — no-signaling by correlation-without-control.* The same fact has an information reading. The two offsets **are** correlated (the kernel; conditioning one site shifts the other — that is what `2C₂ ≠ 1` means), but primality is a **fixed, unchooseable** fact: there is no free variable to set at one site to steer the other. *Correlation you cannot control carries no signal* — which is exactly how quantum mechanics reconciles entanglement with the **no-signaling theorem** (outcomes correlated, outcomes uncontrollable, marginals unmoved). So the determinism caveat that has anchored this whole reading (primes are already fixed; the uncertainty is the observer's) is precisely *what produces* the no-signaling. The structural roots are elementary and worth naming without mysticism: by the **Chinese Remainder Theorem** each prime is an *independent coordinate*, so the sieve is a **product of independent local factors** `∏(1−1/p)`; the global survival pattern is that product, and **no single factor ever sees the product** (a prime `p` begins eliminating new candidates only from `p²` onward — the √n activation horizon). In a deliberately figurative shorthand:

> *Primes don't coordinate. They don't share information. They don't "know" where the primes are. And because of that, a finite-memory observer cannot individuate the pattern without unbounded work.*

(The "know" is a figure of speech for CRT factor-independence, not cognition.) Two honesty stamps. **Not novel:** the parity barrier was already an information-theoretic object — Sarnak's Möbius-randomness is its zero-mutual-information statement, and §4.2/§4.3 of `Paper_FiniteMemoryCeiling_Primes` measure the escape *in bits*; what is added here is the *individuation / no-signaling reading*, not the informational nature. **A consistency, not a discriminator:** no-signaling holds whether the one-object correlation is quantum (Bell-non-classical) or merely classical, so it **cannot** settle the open successor of §9.5 — the Bell–Tsirelson test remains the only discriminator.

**9.5 Honesty line + the sharpened successor.** What is established (heuristically) is **non-separability** — one object, two samplings, no faithful factorization — which is the structural core of entanglement *and* matches the project's own working definition of it (entanglement = two samplings of one pattern). What is **not** established is the stricter, quantum-only sense: non-classical (Bell-violating) correlation that no classical shared randomness can mimic. A non-separable mixed kernel can be either. **The one sanctioned successor** is therefore well-posed: using the ED entanglement arc's machinery (Schmidt decomposition, monogamy via the V5 cross-chain bandwidth, the **Bell–Tsirelson polytope**), test whether the twin kernel's Schmidt spectrum lies **outside** the classical polytope (genuinely quantum-entangled) or **inside** it (one object, but classically correlated). That single test decides whether "twins are entangled" is a *structural* statement or a *quantum* one. It anchors to Bogomolny–Keating (the kernel) and to the ED entanglement arc (the polytope); it is the only direction the freeze now opens.

**9.6 Rigor.** Heuristic-structural: the `Λ ≈ 1 − Σ_ρ n^{ρ-1}` expansion and the zero-sum / `n`-sum interchange are formal — the conjectural step of §A.4 above, rigorously the open Bogomolny–Keating program. The **non-separability argument is robust**: the heuristic corrections (the `(n+2)` expansion, off-diagonal form-factor terms) do not turn a Hilbert / non-separable kernel into a separable one, so the *direction* — one object, not factorable — stands even though the precise kernel is not a proven object. **Status: single-amplitude question CLOSED-NEGATIVE (heuristic); quantum-vs-classical (Bell) of the one-object pattern OPEN; rigorous kernel OPEN.**

---

*The twin is not two particles linked; it is one pattern sampled at offset 0 and offset 2, and the parity barrier is what stops a finite-memory observer from splitting it into two independent facts. Form-only and non-separable at the structural level; whether the one object is quantum-entangled (Bell-non-classical) or merely classically correlated is the open successor, posed against the ED entanglement arc.*
