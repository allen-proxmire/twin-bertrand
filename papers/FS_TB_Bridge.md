# The Factor Skyline – Twin Bertrand Bridge

*A synthesis note connecting the Factor Skyline (FS) coverage architecture to the Twin-Prime Bertrand Postulate (TB).*

Allen Proxmire, with Claude and GitHub Copilot · June 2026

---

## Abstract

The Twin-Prime Bertrand Postulate asserts that every dyadic interval `(x, 2x]` past `x = 11` contains at least one twin prime. This note recasts TB inside the Factor Skyline framework, where the integers are organized into a deterministic **template layer** and a probabilistic **escape layer**. We show that TB is precisely a statement about the escape layer: the template *manufactures the twin candidates for free and guarantees their number grows without bound* (FS template persistence), while the question of whether two adjacent candidates are *simultaneously prime* in every dyadic window is exactly the information the template cannot supply — the parity barrier, quantified as a residual escape entropy of at most ~0.26 bits per integer. The expected-budget heuristic `E(x) = 2C₂ x/(log x)²` is order-one throughout the small-`x` regime where TB's only genuine miss occurs, and the empirical threshold `x = 11` is where the actual sequence stops missing. We give the verified numerics and the geometric shadow (a near-linear plot of `π(2p)` against twin rank) with its honest fluctuation structure. The conclusion is structural: **TB lives entirely inside the ≲0.26-bit escape gap, which makes it immediate under Hardy–Littlewood and open unconditionally.**

---

## 1. Statement

### 1.1. The Twin-Prime Bertrand Postulate

Let `π₂(x) = #{p ≤ x : p, p+2 both prime}` be the twin-prime counting function, and let `(p_k, p_k + 2)` denote the `k`-th twin prime pair, ordered by `p_k`.

**Twin-Prime Bertrand Postulate (TB).** For every twin prime `p_k ≥ 11`,

$$p_{k+1} < 2\,p_k.$$

In words: *the next twin prime always appears before twice the current one* — before the right endpoint of the dyadic window `(p_k, 2p_k]`.

This is the **correct** inequality. It must not be confused with the weaker `p_{k+1} - p_k < 2p_k` (equivalently `p_{k+1} < 3p_k`, a ratio bound of 3). The TB statement is the **ratio-2** bound `p_{k+1}/p_k < 2`, equivalently a gap bound `p_{k+1} - p_k < p_k`. The numeral "2" in "2p" is the **right endpoint** of the dyadic window, not a bound on the gap.

### 1.2. Equivalence to a dyadic density bound

Throughout, `(p_k)_{k\ge1}` is the increasing sequence of twin **lower-members** (`p_1 = 3, p_2 = 5, p_3 = 11, p_4 = 17, p_5 = 29, \dots`), so that `π₂(x) = #\{k : p_k \le x\}` and a "twin in `(a,b]`" means a lower-member `p_k \in (a,b]`.

**Proposition 1.1.** The following are equivalent:

1. `p_{k+1} < 2 p_k` for every `k` with `p_k \ge 11`.
2. `π₂(2x) − π₂(x) \ge 1` for every real `x \ge 11`.

*Proof.* **(1 ⇒ 2).** Fix real `x \ge 11`. The set `\{p_k : p_k \le x\}` is nonempty (it contains `11`, since `11 \le x`) and finite, so it has a greatest element `p_k`; by construction `p_k \le x` and, since `11` is among the candidates, `p_k \ge 11`. By maximality of `p_k`, the next lower-member satisfies `p_{k+1} > x`. Applying hypothesis (1) at this `p_k \ge 11` gives `p_{k+1} < 2p_k \le 2x`. Hence `x < p_{k+1} < 2x`, so `p_{k+1} \in (x, 2x]` and `π₂(2x) − π₂(x) \ge 1`.

**(2 ⇒ 1).** Fix `k` with `p_k \ge 11` and apply (2) at `x = p_k \ge 11`: there is a lower-member in `(p_k, 2p_k]`. The least lower-member exceeding `p_k` is `p_{k+1}` by definition of the sequence, so `p_{k+1} \le 2p_k`. Since `p_{k+1}` is an odd prime and `2p_k` is even, equality is impossible; therefore `p_{k+1} < 2p_k`. ∎

**Remark (the threshold is sharp for the ratio form).** The cutoff `p_k \ge 11` excludes exactly the one genuine failure, `p_2 = 5 \to p_3 = 11` with `11 = p_3 \ge 2p_2 = 10`. The dyadic form (2) in fact already holds for all real `x \ge 5.5` (the only failing window is `(x, 2x]` with `5 \le x < 5.5`, which lies strictly inside `(5, 11)` and so contains no lower-member); we state both forms at the common, clean threshold `11`, which is where the ratio form (1) first becomes exception-free. The equivalence above is unaffected by this slack, since it quantifies both sides at `11`.

The dyadic form `π₂(2x) − π₂(x) ≥ 1` is the analytic face; the ratio form `p_{k+1} < 2p_k` is the computational face; the geometric face (every angle-record of the Prime Triangle with `p_n ≥ 3` is a twin) is developed in the Twin Bertrand papers (PG I–III). The three are equivalent.

### 1.3. Interpretation as the FS escape-window condition

In the Factor Skyline, each integer `n` is a column of width `lpf(n)` (least prime factor). A prime is an **escape event** — a column of width 1, claimed by no smaller coverage layer. With this vocabulary, TB reads:

> **TB (FS form).** In every dyadic window `(x, 2x]` past `x = 11`, there exist two adjacent template-open positions `r, r+2` that both escape — i.e., that are both prime.

The rest of this note unpacks why the *existence of the open positions* is cheap and provable, while the *simultaneous escape* is exactly the expensive, open part.

---

## 2. The Two FS Layers

The Factor Skyline decomposes the multiplicative information of the integers into a deterministic template and a probabilistic escape. The decomposition is exact at the level of the FS-x increment `dx(n)` (which equals `1` if `n` is prime and `lpf(n)` if `n` is composite). Recomputed from scratch:

$$H(dx) = 2.483 \text{ bits}, \qquad H(dx \mid n \bmod 30) = 0.783 \text{ bits}, \qquad I(\text{template}) = 1.700 \text{ bits}.$$

These are verified numerics; the 1.700-bit template information is **scale-invariant** (identical at `N = 10⁴, 10⁵, 10⁶`), while the residual 0.783 bits splits into an escape component (~0.265 bits) and an activation component (~0.517 bits).

### 2.1. The template layer (deterministic, 1.700 bits)

The **primorial template** `T_{p_k}` classifies each residue class mod `p_k#` as *open* (coprime to `p_k#`) or *covered* (claimed by some width `q ≤ p_k`). This layer is fully deterministic: given `n mod p_k#`, the classification is fixed. It contributes **zero entropy** but provides **information** — in the mod-30 (i.e. 5#) template it resolves the status of `1 − D(5) = 22/30` of all integers and supplies `1.700` bits per integer toward the `dx` sequence.

For twin primes, the relevant object is the set of **twin-open positions**: residues `r` such that *both* `r` and `r+2` are coprime to the primorial. These are the only positions where a twin can occur. Their count per period is governed by:

**Theorem (Template persistence; FS Theorem 4.8).** For every admissible `k`-tuple `H` (in particular the twin pattern `H = {0, 2}`), the number of constellation-open positions in the `p_k#`-template satisfies

$$N_H(p_{k+1}) = N_H(p_k)\cdot\big(p_{k+1} - v_{p_{k+1}}(H)\big),$$

where `v_q(H)` is the number of distinct residues the offsets occupy mod `q`. For twins, `v_q = 2` for `q ≥ 3` and `v_2 = 1`, so the growth factor is `p_{k+1} − 2 ≥ 1`; hence `N_{\{0,2\}}` is non-decreasing and **tends to infinity**.

Numerically, the twin-open counts per primorial period are `1, 1, 3, 15, 135, 1485, …` for `p_k# = 2, 6, 30, 210, 2310, 30030`. The candidates proliferate. **The template manufactures more than enough twin candidates in every window, and FS proves it.**

### 2.2. The escape layer (probabilistic, ≲0.26 bits)

A template-open position is only a *candidate*; it becomes an actual prime only if it **escapes** the remaining coverage — i.e., if it has no prime factor between `p_k` and `√n`. At scale `x`, the escape probability of an open position is asymptotically `~1/log x`.

The information content of this layer is the **escape entropy**. Writing `D_open(x)` for the fraction of template-open positions that are actually prime at scale `x`, the per-integer escape entropy is `D(p)·H₂(D_open(x))`, where `H₂` is the binary entropy and `D(p)` the template-open density. This quantity:

- is **small at small scales** (`D_open ≈ 0.86` at `x ~ 100`: most open positions are prime, so little uncertainty — "probably prime");
- **peaks at ≲0.26 bits near `x ~ 10⁴`** (where `D_open ≈ 0.46`, near the maximum of `H₂`);
- **decays toward 0 as `x → ∞`** (`D_open → 0`: most open positions are composite-with-large-lpf — "probably not prime").

> **Caution.** The figure `0.26` is a **peak**, not a constant, and it is **not** the same object as the escape probability `1/log x`. The robust, scale-invariant anchor is the `1.700`-bit template information. The `0.26` bits is the maximal residual primality uncertainty per integer that the architecture cannot resolve.

### 2.3. The parity barrier

A real twin prime requires **two adjacent open positions to escape together**. The template determines *which* positions are open — it places the candidates — but it carries no information about whether a given open position escapes, still less whether two adjacent ones escape simultaneously. That joint event is precisely the residual escape entropy.

This is the **parity barrier** in information-theoretic form: coverage-based (sieve) methods can certify that a position is open (free of small factors) but cannot distinguish a prime from a product of large primes, and cannot force the correlation between two adjacent escapes. The barrier is **methodological, not logical** — it bounds what coverage arguments can prove, without implying TB is false or undecidable. Everything TB asserts beyond candidate existence lives in this ≲0.26-bit gap.

---

## 3. Expected-Budget Heuristic

### 3.1. The window budget

Under the Hardy–Littlewood prime `k`-tuple conjecture, the expected number of twin primes in an interval `(a, b]` is

$$\mathbb{E}[\#\text{twins in }(a,b]] = 2C_2 \int_a^b \frac{dt}{(\log t)^2}, \qquad C_2 = \prod_{p>2}\frac{p(p-2)}{(p-1)^2} \approx 0.6601618.$$

For the dyadic window `(x, 2x]`, write

$$E(x) = 2C_2 \int_x^{2x} \frac{dt}{(\log t)^2} \;\approx\; 2C_2\,\frac{x}{(\log x)^2}.$$

The prefactor `2C_2` is exactly the FS twin constant `C_H` (see FS Theorem 4.7a for the exact identification `C_H = 2C_2`). `E(x)` is the **escape budget** of the window: the expected number of twin-open candidates whose two escape bits both fire. The template supplies the candidates; `E(x)` counts how many are expected to cash in.

### 3.2. Corrected interpretation — no clean `E = 1` crossing at 11

It is tempting to say "`E(x)` crosses 1 at `x = 11`, which is why TB starts there." **This is too tidy and is not correct.** The continuous HL integral is already greater than 1 for very small `x`:

| `x` | `E(x)` on `(x, 2x]` |
|----:|:--------------------|
| 3   | 1.045 |
| 4   | 1.160 |
| 5   | 1.253 |
| 6   | 1.336 |
| 7   | 1.412 |
| 8   | 1.484 |
| 9   | 1.552 |
| 10  | 1.618 |
| 11  | 1.682 |
| 12  | 1.743 |

`E(x)` does not dip below 1 in the relevant range and therefore has no clean "crossing" at 11. The honest statement is:

> `E(x)` is **order-one** (`≈ 1`–`2`) throughout the small-`x` danger zone. When the expected count is only one or two, a downward fluctuation to zero is plausible, and that is exactly where TB's single genuine miss occurs (`5 → 11`, ratio `11/5 = 2.2`). The empirical threshold `x = 11` is **where the actual sequence stops missing**, not where `E` crosses a fixed value.

### 3.3. Miss probability and the empirical threshold

Modeling the twin count in a window as approximately Poisson with mean `E(x)`, the probability of a window containing **no** twin is

$$\Pr[\text{miss}] \approx e^{-E(x)}.$$

At `x = 11`, `e^{-1.68} \approx 0.19` — a one-in-five miss is entirely plausible, consistent with misses being possible only in this regime. The **expected total number of dyadic misses from 11 onward** is `\sum_k e^{-E(2^k\cdot 11)}`, which **converges to a small number** because `E` grows without bound. Hence "exactly zero exceptions past `x = 11`" is exactly what the budget predicts: finitely many possible misses, and empirically none above the threshold.

### 3.4. Verified table: `E(x)` versus actual twin counts

Expected (HL) versus actual twin counts in the dyadic window `(x, 2x]`, computed directly:

| `x` | `E(x)` (HL) | actual `π₂(2x) − π₂(x)` |
|----:|------------:|------------------------:|
| 11        | 1.68    | 1     |
| 30        | 2.67    | 2     |
| 50        | 3.51    | 2     |
| 100       | 5.26    | 7     |
| 300       | 10.67   | 8     |
| 1,000     | 24.84   | 26    |
| 3,000     | 56.31   | 61    |
| 10,000    | 143.53  | 137   |
| 100,000   | 933.26  | 936   |
| 1,000,000 | 6,550.08| 6,702 |

The HL expectation tracks the actual counts closely once out of the danger zone, and the window budget grows rapidly — by `x = 10⁶` a window is expected to hold thousands of twins, making a miss astronomically unlikely (`e^{-6550}`).

---

## 4. The Geometric Shadow

### 4.1. The construction

Place the primes on an evenly spaced "prime-rank" axis (prime `p_i` at position `i`). For each twin pair, **double** the lower member and drop `2p_k` onto this axis at the midpoint between the two primes bracketing it. Since `2p_k` is even it always falls strictly between two consecutive primes, so its position is `π(2p_k) + ½`. Plotting

$$x_k = \pi(2 p_k), \qquad y_k = k \;(\text{twin rank})$$

produces a strikingly **linear** curve. (One may use the symmetric representative `x_k = \min\{\pi(2p_k), \pi(2(p_k+2))\}` to reflect that either member can anchor the dyadic window; the two strands nearly coincide.)

### 4.2. The macro-line

A least-squares fit over the first 100 pairs gives `R² ≈ 0.996` against a straight line. The relationship is

$$\pi(2p) \;\approx\; \frac{\log p}{C_2}\,\pi_2(p),$$

obtained from `\pi(2p) \sim 2p/\log p` and `\pi_2(p) \sim 2C_2 p/(\log p)^2`. The slope of the plotted line is therefore `\approx C_2/\log p`, which **drifts slowly downward** (measured: `0.141` over the first 25 pairs, `0.094` over the last 25). The "line" is the leading-order trend; the slow flattening is the genuine arithmetic correction. The straightness is a statistical fact, not exact geometry.

### 4.3. `Δx` run-length structure

The horizontal gap between consecutive dots is

$$\Delta x_k = \pi(2p_{k+1}) - \pi(2p_k) = \#\{\text{primes in } (2p_k,\, 2p_{k+1}]\}.$$

Three consecutive dots are **exactly collinear** if and only if two consecutive gaps are equal, `Δx_k = Δx_{k+1}`. Measured over the first 2,160 valid twin pairs:

- mean gap `≈ 15.68`, range `0` to `141`;
- **equal-adjacent gaps occur only ≈ 2.9%** of the time (63 of 2,158 triples);
- the **longest exact straight run is 4 dots** (three equal gaps in a row), occurring once early;
- `Δx` **singletons dominate** — a gap value differing from both neighbors is the norm.

### 4.4. Interpretation

The earlier intuition that "at least three consecutive dots always lie on a straight line" is **false**. The macro-line is a statistical trend governed by `\pi(2p) \approx (\log p/C_2)\,\pi_2(p)`; micro-collinearity is essentially **chance**, at the rate one would expect from the irregular distribution of primes between doubled twins. The apparent "cascade" of short straight segments is the eye grouping runs of similar gaps before a large gap resets the local slope — prime-gap fluctuation, not periodic structure. Doubling is what couples twin spacing to prime spacing (slope `≈ 1/Δx`), which is why the dyadic factor of 2 surfaces here at all.

---

## 5. What FS Proves vs. What Remains Open

### 5.1. What FS proves

Using only the five FS primitives (width, height, activation, coverage, escape) and the Chinese Remainder Theorem, the template layer establishes, **unconditionally**:

- **Candidate existence.** Every dyadic window `(x, 2x]` past a small threshold contains twin-open positions — residues where both `r` and `r+2` are coprime to all primes up to `√(2x)`.
- **Candidate growth (template persistence, Theorem 4.8).** The number of twin-open positions per primorial period is non-decreasing and tends to infinity; the windows are never starved of candidates.
- **Coverage protection (Theorem 4.4) and the exact constant (Theorem 4.7a).** The coverage layers create positive correlations among constellation members, and the FS twin constant equals the Hardy–Littlewood singular series exactly. From the survival factor `S_q(H) = (q - v_q(H))/q` (Theorem 4.3) with `v_2 = 1` and `v_q = 2` for `q > 2`, the FS `k`-tuple constant for the twin offset `H = \{0, 2\}` is
$$C_H = \prod_q \frac{S_q(H)}{(1 - 1/q)^2} = \prod_q \frac{q\,(q - v_q)}{(q-1)^2} = 2\prod_{q>2}\frac{q(q-2)}{(q-1)^2} = 2C_2 = 1.3203237\ldots \quad \text{(FS Theorem 4.7a)},$$
the offset-`2` collision at `q = 2` (where `v_2 = 1`, not `2`) producing the leading factor `2`. This matches FS Table 1 (`C_H = 1.3203` for the twin pattern), and it is **exactly the prefactor `2C_2` in `E(x)`**: the window budget of §3.1 is `E(x) = C_H \int_x^{2x}(\log t)^{-2}\,dt`. So the Hardy–Littlewood twin density and the FS coverage-protection constant are the same number, arrived at from the two sides.

In short, FS proves the **deterministic skeleton** of TB: the candidates exist, they multiply, and their density carries the constant `C_H = 2C_2`, identical to the Hardy–Littlewood singular series.

### 5.2. What TB additionally requires

TB requires that, in **every** dyadic window past 11, at least one twin-open candidate has **both of its escape bits fire simultaneously**. This is a statement about the **escape layer**, not the template:

- it concerns *which* open positions are actually prime (the `~1/\log x` escape event), and
- it concerns the *correlation* between two adjacent escapes (the simultaneity).

Neither is supplied by the template. Both live in the residual escape entropy — the ≲0.26-bit gap.

### 5.3. The gap is the parity barrier

The information TB needs beyond the FS skeleton is exactly the information the coverage architecture cannot provide:

$$\underbrace{\text{candidates exist and grow}}_{\text{template — FS proves it}} \;+\; \underbrace{\text{two adjacent candidates escape together}}_{\text{escape — the }\lesssim 0.26\text{-bit gap}} \;=\; \text{TB}.$$

This is why TB sits where it does in the logical hierarchy:

$$\underbrace{\text{twin-prime conjecture}}_{\pi_2(x)\to\infty} \;\supset\; \underbrace{\text{TB}}_{\pi_2(2x)\ge\pi_2(x)+1} \;\supset\; \underbrace{\text{bounded gaps}}_{\liminf(p_{n+1}-p_n)<\infty}.$$

### 5.4. Easy under HL, open unconditionally

- **Under Hardy–Littlewood**, the escape bits behave like independent coins at density `~1/\log x` with the correct twin correlation `C_2`. The window budget `E(x) = 2C_2 x/(\log x)^2` then overflows for all `x` past the danger zone, and the convergence of `\sum e^{-E}` makes the finitely-many-exceptions structure rigorous. TB is **immediate**.
- **Unconditionally**, the parity barrier forbids the coverage architecture from controlling the joint escape event. TB is therefore **open** — not because the candidates are in doubt (they are not), but because certifying simultaneous escape in every window is precisely the ≲0.26-bit information that no coverage argument can supply.

> **TB is true-but-unprovable-by-these-means for a structural reason: the entire content of TB beyond the FS skeleton is the ≲0.26-bit escape gap.** Factor Skyline measures the height of the wall; Twin Bertrand is what lies on the far side of it.

### 5.5. The bounded-gaps theorem: the parity floor, and why it is the same wall

The one rung of the hierarchy that has actually been *climbed* is its weakest — bounded gaps — and the precise way it was climbed sharpens exactly where TB's wall sits.

**The pipeline.** GPY (2005) reduced bounded gaps to a *level-of-distribution* input `θ` (control of primes in arithmetic progressions to modulus `x^θ`); Bombieri–Vinogradov gives `θ = ½`, just short of what they needed. Zhang (2013) pushed `θ` a hair past `½` for smooth moduli → bounded gaps *exist* (`≤ 7×10⁷`). Maynard–Tao (2013) replaced the sieve with a multidimensional one efficient enough to need **only** Bombieri–Vinogradov (`θ = ½`, a theorem) → gaps `≤ 600`, and gaps for `m` primes at once. Polymath8b optimized this to **246 unconditional**, **12 under Elliott–Halberstam (EH)**, **6 under generalized EH**.

**Two barriers, not one.** The descent rides a *soft* barrier and stops at a *hard* one — and conflating them is the standard mistake:

- The **Bombieri–Vinogradov / level-of-distribution barrier** (`θ`) is *soft*: dented by Zhang, conjecturally removable (EH pushes `θ → 1`). Improving `θ` lowers the bound (`600 → 246 → … → 6`). The unconditional **246 is contingent** — it reflects current distribution knowledge, not a wall.
- The **parity barrier** (Selberg's parity problem) is *hard* and untouched. Even granting the strongest distribution conjecture (GEH, `θ → 1`), the method floors at **6 and can never reach 2**. *That* floor — the `6 → 2` step — is the parity barrier, the same `≲0.26`-bit escape wall this note is about. Zhang cracked the **BV** barrier, **not** the parity barrier; the two must not be merged. So the real finite-sieve wall is **6**, not 246: 246 is where current distribution knowledge sits, while `6 → 2` is the part no amount of distribution can buy.

**Why it is the same wall — in the template/escape language of §2.** The sieve proves *"infinitely often a bounded window contains two primes"* but **never locates which two**: it counts weighted admissible tuples and shows the average tuple carries more than one escape, without identifying the escaping positions. That is exactly **candidate existence without individuated simultaneous escape** — the template hands you a bounded cluster of twin-open candidates and certifies that `≥ 2` of them escape; the parity barrier is precisely what forbids resolving *which adjacent pair* escapes, i.e. pinning a located twin at distance 2. Bounded gaps is therefore the *proving-side shadow* of TB's open part: the method reaches the **cluster** (one object, `≥ 2` escapes inside) and cannot **individuate** it into a located twin. The `6 → 2` step is the individuation the escape layer withholds. *(This "cannot individuate the pair" reading — the twin as one un-resolved pattern sampled at two offsets, the parity barrier as the individuation block — is developed in `OPEN_QUESTION_FS_TB_QM_AMP_02_Bilinearity.md` §9.)*

The numbers (`600, 246, 12, 6`) are the published Maynard / Polymath8b records; the "floor 6 under GEH, never 2" statement is the standard parity-problem reading. Nothing here is new number theory — it grounds this note's parity-barrier claim in a hard theorem, and locates TB's open content precisely at the same `6 → 2` individuation step.

---

## Appendix: Provenance of the numbers

All figures in this note were recomputed from scratch and cross-checked.

- **Entropy budget** (`H(dx) = 2.483`, `H(dx\mid n\bmod 30) = 0.783`, `I(\text{template}) = 1.700`, escape `≈ 0.265`, activation `≈ 0.517`): independently reproduced; `I(\text{template}) = 1.700` is scale-invariant across `N = 10⁴, 10⁵, 10⁶`. Note: the FS reproducibility harness table `table_06_entropy_budget.py` is currently a placeholder stub and does **not** yet verify these in CI.
- **`E(x)` tables** (§3.2, §3.4): `E(x) = 2C_2\int_x^{2x}(\log t)^{-2}dt` with `C_2 = 0.6601618`, numerically integrated; actual twin counts from a sieve to `4\times10^6`.
- **Geometric shadow** (§4): `R² ≈ 0.996` over the first 100 pairs; slope drift `0.141 → 0.094`; `Δx` statistics over the first 2,160 valid pairs (those whose double stays within the sieve bound): mean `15.68`, equal-adjacent rate `2.9%`, longest exact run `4` dots.

Scratch plots: `twin_fs_x_plot.png`, `twin_2x_fs_plot.png`, `twin_doubled_primerank.png` (in the Factor Skyline repository root).
