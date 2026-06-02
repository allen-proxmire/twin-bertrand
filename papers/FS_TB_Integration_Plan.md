# Integration Plan: Folding the Δx Deep-Dive into PG II / PG III

*How to move the results of [`FS_TB_DeltaX_Analysis.md`](FS_TB_DeltaX_Analysis.md) (§§1–10 + figures) into the published Twin Bertrand papers.*

Allen Proxmire, with Claude and GitHub Copilot · June 2026

---

## 0. Recommendation in one line

Create **one new self-contained section in PG II** — "The Δx Structure and the Geometry of Doubled Twins" — placed after the Empirical Verification section and before the Twin-Ramanujan section, and add **two light cross-referencing touches in PG III** (one pointer in the Asymptotic Interpretation section, one future-work note on generalizing Δx to constellations). The Δx material is twin-specific, so PG II is its home; PG III only needs to point at it and flag the generalization.

---

## 1. Where each result lands

The Δx deep-dive contains five movable results. The table maps each to its destination, using the existing `\label`s of the two papers.

| Δx-note result | source §§ | primary destination | existing anchor to link |
|---|---|---|---|
| Geometric-shadow construction (`π(2p)` vs twin-rank; `slope = 1/Δx`; `R²≈0.996` line) | §§1, 4 | **PG II — new section**, opening subsection | `sec:2P` (doubling theme), `sec:angle` (sibling geometry) |
| Slope-drift law (`slope → C₂log(2p)/(log p)²`, coeff `C₂ = C_H/2`) | §8 | **PG II — new section**, drift subsection | PG II §6.3 *Twin-gap growth law*; PG III `sec:asymp` §7.1 |
| Δp-driven overdispersion (`Δx = 2Δp·ρ`, ~97% of log-variance from `Δp`; `ρ ≈ 1/log(2p)`) | §7 | **PG II — new section**, variance-decomposition subsection | PG II §6.3; PG III `sec:envelope` (twin-gap envelope) |
| Cramér/Poisson-mixture interpretation (collinearity 2.9% = chance; overdispersed mixture) | §§3, 6 | **PG II — new section**, statistical-model subsection | PG II `sec:HL`; PG III `sec:asymp` §7.4 *why violations only at tiny P* |
| Scale-collapse of `Z = Δx/μ` (scale-invariant for `p≥10³`, super-Poissonian floor) | §10 | **PG II — new section**, scale-collapse subsection | PG III `sec:asymp` (asymptotic universality) |

Note the two natural "magnets" in the existing papers: PG II §6.3 (*Twin-gap growth law*) already studies the distribution of twin gaps `Δp` — which §7 shows is the *source* of the Δx noise — so the new section should explicitly defer the `Δp` envelope to it rather than re-deriving it. Likewise PG III §7.4 already uses an `e^{−E}` Poisson argument for "why violations occur only at tiny P"; the §6 mixture model reinforces it and should cite it.

---

## 2. Proposed outline of the new PG II section

**Section title:** *The Δx Structure and the Geometry of Doubled Twins*
**Suggested label:** `\label{sec:deltax}`
**Placement:** new section between `sec:empirical` (Empirical Verification) and the Twin-Ramanujan section. Rationale: it is empirical and geometric, builds on the verification data, and is a twin-specific companion to the angle-record geometry.

| sub | working title | content | from |
|---|---|---|---|
| X.1 | The doubled-twin shadow | Define the prime-rank axis, the map `p_k ↦ (π(2p_k), k)`, the gap `Δx_k = #{primes in (2p_k, 2p_{k+1}]}`, and the slope identity `slope_k = 1/Δx_k`. State the macro-line `R²≈0.996` and the relation `π(2p) ≈ (log p/C₂)·π₂(p)`. Frame doubling as the dyadic endpoint of the `2P`-beats theme. | §§1, 4 |
| X.2 | Distribution of Δx | Heavy-tailed, unimodal, mean `15.68`, the `Δx=0` spike; **Figure 1**. | §2 |
| X.3 | The slope-drift law | Empirical decade slope `→ C₂ log(2p)/(log p)²` to 1–2%; crude `C₂/log(2p)` low by `(log2p/log p)²`; leading coefficient `C₂ = C_H/2` (**cite Theorem 4.7a**). **Figure 3**. Position as a new asymptotic law beside the twin-gap growth law. | §8 |
| X.4 | Variance decomposition: Δp dominates | `Δx = 2Δp·ρ`; log-variance ~97% from `Δp`, ~10% from density; `ρ` tracks `1/log(2p)` to ~2% (`r̄=0.98`, ±27%). **Figure 2**. Defer the `Δp` envelope to PG II §6.3 / PG III `sec:envelope`. | §7 |
| X.5 | The Poisson-mixture model | Run-length structure; micro-collinearity `2.9%` = chance (`∑p_v²=3.09%`); single-Poisson is the wrong null (overdispersed, var/mean≈13); the marginal is a Poisson **mixture** over fluctuating `μ_k`. Cite the `e^{−E}` argument of PG III §7.4. | §§3, 6 |
| X.6 | Scale-collapse of the conditional gap | `Z_k = Δx_k/μ_k ≡ r_k`; KS ≤ 0.07 across decades `p≥10³` → scale-invariant shape, mean ≈ 1, CV collapses `0.91→0.27`; residual mildly super-Poissonian (Montgomery–Soundararajan excess variance), does not vanish as `1/√μ`. | §10 |
| X.7 | Synthesis | The shadow = deterministic `1/log` drift + `Δp`-driven, scale-free counting noise. Tie to TPB via the FS escape/parity-barrier picture (**cite `FS_TB_Bridge.md`**): the candidates and their density (the deterministic part) are FS-template structure; the irreducible `Z`-residual is the escape randomness. | §§1–10 synthesis |

This is a 7-subsection section of roughly 4–6 pages with three figures — comparable in weight to the existing Empirical Verification section.

---

## 3. Figures

All three figures from Δx-note §9 (`Twin Bertrand/figures/`) move into the new section:

| figure | file | lands in | caption focus |
|---|---|---|---|
| Fig. 1 — Δx histogram | `figures/deltax_histogram.png` | X.2 | heavy tail, `Δx=0` spike, mode in `[5,15)` |
| Fig. 2 — `(λ, ρ)` scatter | `figures/lambda_rho_scatter.png` | X.4 | diagonal `ρ≈λ`, bounded ±27% spread |
| Fig. 3 — slope vs `log(2p)` | `figures/slope_vs_log2p.png` | X.3 | decade points on the `C₂log(2p)/(log p)²` backbone |

Fig. 3 is the section's centerpiece (it carries the slope-drift result) and should be the figure referenced from the abstract/intro if the new section is advertised there. For LaTeX, convert/copy the PNGs into the paper's figure directory and add `\includegraphics`; regeneration is reproducible from the Δx-note §9 provenance bullet (Matplotlib, stated sieve bounds and bin counts).

---

## 4. Cross-references required

**Outbound, from the new PG II section:**
- → **Theorem 4.7a** (`C_H = 2C₂`) in the FS foundation paper, §4.3.1 — cited in X.3 where the slope coefficient `C₂ = C_H/2` appears. This is the key cross-repo link and the reason the slope constant is *exact*, not fitted.
- → **FS foundation paper**: Template persistence (Theorem 4.8) in X.1/X.7 (candidates exist and grow); the five FS primitives / escape layer in X.5, X.7.
- → **`FS_TB_Bridge.md`**: in X.7 for the escape/parity-barrier framing (and optionally X.1 for the FS-template origin of the candidates). If the bridge note is itself to be published, replace with its eventual citation key; otherwise cite as a companion technical note.
- → **Internal PG II**: X.3 and X.4 cross-link to §6.3 (*Twin-gap growth law*); X.5 cross-links to `sec:HL`.

**Inbound, into PG III (the two light touches):**
- In `sec:asymp` (Asymptotic Interpretation): a one-paragraph pointer noting that the doubled-twin slope obeys `C₂log(2p)/(log p)²` and that the conditional gap distribution scale-collapses (cite PG II `sec:deltax`), complementing the `β→2` exponent drift.
- A future-work sentence (Conclusion or `sec:asymp`): the Δx construction generalizes to any admissible constellation `\mathcal{C}` via `Δx^{\mathcal C}_k = π(2p^{\mathcal C}_{k+1}) − π(2p^{\mathcal C}_k)`, with the `Δp`-driven overdispersion and scale-collapse expected to persist; the relevant constant becomes `C_{\mathcal C}` (the GBP singular series), tying back to PG III's constellation framework.

**Notation to reconcile before drafting:** confirm whether PG II/III already write the twin constant as `C₂` and the singular series as `2C₂` (vs `\mathfrak{S}`); the new section must match the existing convention, and the `C_H = 2C₂` identity should be introduced with whatever symbol the papers already use for the singular series.

---

## 5. Overlap / de-duplication checklist

To avoid restating what the papers already contain:

- **Twin-gap distribution / envelope.** Already in PG II §6.3 and PG III `sec:envelope` (`G < 0.171(log P)^{3.22}`). The new X.4 should *use* this (the `Δp` heavy tail) and cite it, not re-derive it. New content in X.4 is the *decomposition* showing `Δp` drives `Δx`, not the envelope itself.
- **Cramér/overshoot.** PG II §6.4 and PG III `sec:asymp` §7.2 already discuss extreme-gap overshoot and `β` drift. X.5/X.6 add the *gap-count* (`Δx`) Poisson-mixture and the *scale-collapse*, which are distinct objects; cross-reference rather than duplicate.
- **The factor 2 / doubling.** PG III `sec:asymp` §7.3 (*why factor 2 is natural and universal*) already motivates the dyadic 2. X.1 should reference it when introducing doubling, not re-argue it.
- **TPB statement and 2P-beats.** Already PG II `sec:tpb`, `sec:2P`. X.1 cites them; the new section assumes them.

---

## 6. Open decisions (for Allen / Copilot)

1. **PG II vs a standalone PG IV.** The recommendation is a new PG II section. If the Δx material is felt to be large or methodologically distinct enough (it introduces a new geometric object and a statistical-model layer), an alternative is a short standalone *PG IV: The Δx Geometry of Doubled Twins*. Default: fold into PG II; escalate to PG IV only if the section overgrows ~6 pages.
2. **Whether to publish `FS_TB_Bridge.md`.** The new section's X.7 leans on the escape/parity-barrier framing. If the bridge note is not published, X.7 should summarize the needed framing inline (a paragraph) rather than cite an unpublished file.
3. **Depth of the super-Poissonian claim (X.6).** The Montgomery–Soundararajan connection is stated as consistency, not proof. Decide whether the paper asserts it as an observation (recommended) or pursues a quantitative short-interval-variance comparison (a larger undertaking, possibly its own note).
4. **Extending the data.** Current figures/stats use sieves to `4×10⁵` (Figs 1–2) and `2×10⁶` (Fig. 3 / decade tables). For publication, consider regenerating uniformly to a single larger bound (e.g. `10⁸`) so all sections share one dataset and the decade table gains a fifth full decade.

---

## 7. Suggested sequence of edits

1. Reconcile constant notation (§4 above) across PG II, PG III, FS foundation.
2. Draft PG II `sec:deltax` X.1–X.7 per the §2 outline, pulling prose and numbers directly from the Δx note (already reviewed).
3. Insert the three figures (§3) with captions adapted from Δx-note §9.
4. Add the X.3 → Theorem 4.7a cross-reference and the X.7 → bridge/FS-foundation cross-references (§4).
5. Add the two PG III touches (`sec:asymp` pointer + future-work sentence).
6. Run the de-duplication checklist (§5) against the drafted section.
7. Optionally regenerate all data to a single uniform bound (§6.4) before final figures.

---

*All numerical results to be transferred have been recomputed and reviewed in `FS_TB_DeltaX_Analysis.md`; this plan moves them, it does not introduce new claims.*
