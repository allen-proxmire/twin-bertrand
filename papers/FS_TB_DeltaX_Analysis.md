# The Δx / Cascade Analysis

*A structured study of the gap sequence underlying the π(2p)-versus-twin-rank plot, and why its macroscopic line coexists with microscopic irregularity.*

Allen Proxmire, with Claude and GitHub Copilot · June 2026

Companion to [`FS_TB_Bridge.md`](FS_TB_Bridge.md). This note isolates one object from §4 of the bridge — the horizontal gap sequence `Δx_k` of the doubled-twin geometric shadow — and analyzes its distribution, its run-length structure, and the precise sense in which the apparent "cascade" of straight segments is a statistical artifact rather than a periodic law.

---

## 1. Definition of Δx

Recall the geometric construction (bridge §4): the twin lower-members `p_k` are doubled and placed on an evenly spaced prime-rank axis, so that the doubled value `2p_k` sits at horizontal position `π(2p_k)` (the number of primes below `2p_k`), and the vertical position is the twin rank `k`. The points are `(x_k, y_k) = (π(2p_k),\, k)`.

**Definition 1.1 (the gap sequence).** For consecutive twin pairs,

$$\Delta x_k \;=\; \pi(2p_{k+1}) \;-\; \pi(2p_k).$$

**Interpretation.** Since `π` counts primes, `Δx_k` is exactly the **number of primes in the interval `(2p_k, 2p_{k+1}]`**:

$$\Delta x_k \;=\; \#\{\, q \text{ prime} : 2p_k < q \le 2p_{k+1} \,\}.$$

Each step from one doubled twin to the next jumps the prime-rank axis by however many primes lie between the two doubled values.

**Slope.** Because the vertical coordinate increases by exactly `1` from each twin pair to the next (`y_{k+1} - y_k = 1`), the local slope of the geometric-shadow plot between consecutive points is

$$\text{slope}_k \;=\; \frac{y_{k+1}-y_k}{x_{k+1}-x_k} \;=\; \frac{1}{\Delta x_k}.$$

The whole shape of the plot — the near-line and its fluctuations — is therefore governed entirely by the sequence `(\Delta x_k)`. A constant stretch of `Δx` is a straight segment; a change in `Δx` is a kink.

---

## 2. Empirical Distribution of Δx

We computed `Δx_k` over **all 239,101 twin pairs with `2(p_k+2) \le N` for the uniform sieve bound `N = 10^8`**, yielding **239,100 gaps**. This single dataset underlies every section below; all statistics are measured, not modeled.

**Summary statistics.**

| quantity | value |
|---|---|
| count of gaps | 239,100 |
| mean | 24.10 |
| median | 17 |
| standard deviation | 23.02 |
| minimum | 0 |
| maximum | 332 |

**Histogram (coarse bins).**

| `Δx` range | count | fraction |
|---|---:|---:|
| `[0, 1)`   | 3,819  | 1.60% |
| `[1, 5)`   | 31,992 | 13.38% |
| `[5, 10)`  | 37,325 | 15.61% |
| `[10, 20)` | 56,487 | 23.62% |
| `[20, 30)` | 39,707 | 16.61% |
| `[30, 50)` | 40,503 | 16.94% |
| `[50, 75)` | 19,534 | 8.17% |
| `[75, 100)`| 6,465  | 2.70% |
| `[100, 150)`| 2,909 | 1.22% |
| `[150, 200)`| 323   | 0.14% |
| `[200, 300)`| 35    | 0.01% |
| `[300, 500)`| 1     | 0.00% |

**Shape.** The distribution is unimodal with a mode in the `[10, 20)` band, a short left shoulder (including 3,819 instances — 1.6% — of `Δx = 0`, where two consecutive doubled twins fall between the same pair of primes), and a long **right tail** reaching to `332` while the mean is only `24.10`. The standard deviation (`23.02`) is essentially equal to the mean — the hallmark of a roughly exponential / heavy-tailed spacing, consistent with `Δx` being a count of primes in an interval whose own length fluctuates with twin spacing. **`Δx` is highly irregular and heavy-tailed**, not concentrated near any preferred value.

---

## 3. Run-Length Structure

The visual question — "do three or more consecutive points lie on one straight line?" — is, by the slope identity of §1, exactly the question of whether `Δx` *repeats* in consecutive positions.

**Definition 3.1 (run).** A *run* of length `L` is a maximal block of consecutive equal gaps,

$$\Delta x_k = \Delta x_{k+1} = \cdots = \Delta x_{k+L-1},$$

with the entries just before and just after the block (where they exist) differing. A run of length `L` corresponds to **`L + 1` collinear plotted points** (a straight segment spanning `L` steps).

**Measured run-length distribution** (234,444 runs partitioning the 239,100 gaps):

| run length `L` | collinear dots `L+1` | count | fraction of runs |
|---:|---:|---:|---:|
| 1 | 2 | 229,914 | 98.07% |
| 2 | 3 | 4,409 | 1.881% |
| 3 | 4 | 117 | 0.050% |
| 4 | 5 | 3 | 0.001% |
| 5 | 6 | 1 | 0.0004% |
| ≥6 | ≥7 | 0 | 0.00% |

**Derived facts.**

- **Equal-adjacent gaps occur ≈ 1.9%** of the time (4,656 of 239,099 adjacent gap-pairs are equal — the direct count behind the run table).
- **The longest exact run is `L = 5`** (five equal gaps), i.e. a maximal straight segment of **6 collinear dots**, occurring exactly once in 239,100 gaps.
- **Singletons dominate:** 98.07% of all runs have length 1 — a gap value that differs from both of its neighbors. Only **3.8% of gaps** lie inside a run of length `≥ 2` at all.

The intuition that "at least three consecutive points always connect" is therefore **false**, and decisively so: not only is it not guaranteed, three-in-a-row collinearity is the rare exception (≈ 1.9%), and runs of more than three dots are essentially flukes (a single 6-dot run in a quarter-million gaps). Note the collinearity rate has *fallen* from the ≈ 2.9% seen in smaller samples: as the scale grows the gap distribution spreads (§7–8), so coincidences become rarer, not more common.

---

## 4. Interpretation

### 4.1. Why micro-collinearity is chance

By §1, three consecutive dots are collinear iff `Δx_k = Δx_{k+1}`. Each `Δx_k` is the count of primes in `(2p_k, 2p_{k+1}]`, a quantity driven by the irregular distribution of primes and by the fluctuating spacing of consecutive twins. There is no mechanism forcing this count to repeat from one step to the next. Treating the gap sequence as a noisy discrete random variable with the empirical distribution of §2, the chance that two independent draws coincide is `\sum_v \Pr[\Delta x = v]^2`, which for a distribution spread over `0`–`332` with mean `24.10` is small and of the same order as the observed **1.9%**. In other words, the measured collinearity rate is about what pure chance predicts: **micro-collinearity carries no signal.**

### 4.2. Why the macro-line persists

The contrast with the macroscopic plot — which fits a straight line at `R^2 \approx 0.996` — is resolved by separating trend from fluctuation. From the prime-counting and twin-counting asymptotics,

$$\pi(2p) \sim \frac{2p}{\log p}, \qquad \pi_2(p) \sim \frac{2C_2\,p}{(\log p)^2},$$

so the trend relating the axes is

$$\pi(2p) \;\approx\; \frac{\log p}{C_2}\,\pi_2(p),$$

a linear relation between `x_k = \pi(2p_k)` and `y_k = k = \pi_2(p_k)` with slope `\approx C_2/\log p`. Because `\log p` varies extremely slowly, the slope is nearly constant over any moderate range — hence the line — but it **drifts slowly downward** (measured: the decade-aggregate slope falls from `0.103` at `p \sim 10^2` to `0.040` at `p \sim 10^7`; see §8). The straight line is the leading-order term; the slow flattening is the genuine arithmetic correction. The trend is real and smooth; the per-step gaps `Δx_k` scatter around its reciprocal `\approx \log p / C_2 \approx 1/\text{slope}`.

### 4.3. The "cascade" is grouping, not periodicity

The eye, scanning the plot, naturally groups consecutive points of similar slope into short straight-looking segments, then perceives a "reset" when a large gap (a long right-tail `Δx`, e.g. values past `100` and up to `332`) abruptly changes the local slope. This produces the *appearance* of a repeating cascade of segments. But §3 shows the segments are almost all of length 1–2 steps and their lengths follow the chance distribution of repeated gaps; there is no fixed period, no recurring segment length, and no structural law generating the cascade. **The cascade is a perceptual grouping of prime-gap fluctuations, not a periodicity of the sequence.** The only genuine, reproducible structure in the picture is the smooth macro-trend of §4.2.

---

## 5. Forward Plan

This section establishes the baseline. The deep-dive continues along the following lines:

1. **Conditional distribution of `Δx_k` given `p_k`.** Bin the gaps by the scale `p_k` and test whether the shape of the `Δx` distribution is stable under rescaling by its local mean — i.e. whether `Δx_k / \mathbb{E}[\Delta x \mid p_k]` converges to a fixed law. The local mean is predicted to be `\approx 2(p_{k+1}-p_k)/\log(2p_k)`.

2. **Scaling behavior `Δx_k / (2p_{k+1} - 2p_k)`.** Compare the prime-rank gap to the raw integer gap between doubled twins. This ratio is an empirical local prime density near `2p_k` and should track `1/\log(2p_k)`; deviations measure the twin-induced bias.

3. **Comparison to Cramér-style models.** Model primes near `2p_k` as a Poisson process with rate `1/\log t` and twins via the Hardy–Littlewood density, then compare the predicted `Δx` distribution (mean, variance, tail) and the predicted collinearity rate against the measured values of §2–3. This quantifies precisely "how much of `Δx` is chance."

4. **Local slope-drift analysis.** Track the running slope `\approx C_2/\log p` against the measured local slope `1/\overline{\Delta x}` across decades, and fit the drift to verify the `\log p` law and extract any second-order correction.

5. **Visualization appendix.** A zoomed segment (e.g. pairs 40–90) showing individual `Δx` steps and the once-occurring 4-dot run; a histogram of `Δx`; and a slope-versus-scale plot, regenerated reproducibly from the sieve.

---

## 6. Cramér/Poisson comparison for Δx

Section 4 asserted that the ≈ 1.9% micro-collinearity rate is "chance." This section makes that quantitative by comparing the observed gap behavior to an explicit probabilistic model.

### 6.1. Model setup

Following Cramér, model the primes near `2p_k` as an inhomogeneous Poisson process with intensity `λ(t) ≈ 1/\log t`. Then the number of primes in `(2p_k, 2p_{k+1}]` — which is exactly `Δx_k` (Definition 1.1) — is approximately Poisson with mean

$$\mu_k \;\approx\; \int_{2p_k}^{2p_{k+1}} \frac{dt}{\log t}.$$

Crucially, `μ_k` is **not constant**: it scales with the spacing `2(p_{k+1}-p_k)` between consecutive doubled twins divided by `\log(2p_k)`, and twin spacings themselves fluctuate widely. The marginal distribution of `Δx` is therefore not a single Poisson but a **Poisson mixture** — a Poisson whose mean is itself a fluctuating random variable. This distinction drives everything below.

### 6.2. Predicted coincidence rate

If successive gaps were independent draws from a common discrete law with `p_v = \Pr[\Delta x = v]`, the expected adjacent-equal rate would be

$$R_{\text{model}} \;=\; \sum_v p_v^2.$$

Using the **exact per-value empirical frequencies** as the proxy for `p_v` (we use exact values rather than the coarse §2 bins, since binning would lump distinct values together and spuriously inflate the estimate):

$$R_{\text{empirical}} \;=\; \sum_v \Big(\frac{\text{freq}_v}{239100}\Big)^2 \;=\; 1.99\%.$$

This is to be compared with the **observed** adjacent-equal rate from §3, `1.95\%` (4,656 of 239,099 adjacent pairs). The agreement is close: `1.99\%` predicted versus `1.95\%` observed.

For contrast, a **single** Poisson with the empirical mean (`24.10`) predicts a coincidence rate of

$$\sum_v \text{Pois}(v;24.10)^2 \;=\; 5.76\%,$$

nearly three times the observed value. A single Poisson is too *concentrated* (it predicts gaps clustering tightly around 24.10, hence frequent coincidences); the real, overdispersed marginal spreads the gaps out and makes coincidences rarer. The matching model is the empirical marginal, **not** a single Poisson.

### 6.3. Tail behavior

The overdispersion is starkest in the tail. Comparing the empirical right tail `\Pr[\Delta x \ge T]` to a single `\text{Pois}(24.10)`:

| `T` | empirical `\Pr[\Delta x \ge T]` | `\text{Pois}(24.10)` | ratio |
|---:|---:|---:|---:|
| 30  | 29.18% (69,770/239,100) | 13.65%      | ~2× |
| 50  | 12.24% (29,267/239,100) | 2.6 × 10⁻⁴% | ~47,000× |
| 100 | 1.37% (3,268/239,100)   | 7.6 × 10⁻²⁹% | astronomical |

The empirical tail is **vastly heavier** than a single Poisson of the same mean. (At `T = 30`, just above the mean `24.10`, the excess is only ~2×; the heavy tail reveals itself further out, at `T = 50` and `100`.) The variance tells the same story: the empirical variance is `529.8` against a mean of `24.10` (variance-to-mean ratio ≈ 22), whereas a Poisson has variance equal to its mean (ratio 1, std `4.91` versus the empirical `23.02`). This is exactly the signature of a Poisson **mixture**: averaging Poissons over a widely varying mean `μ_k` produces an overdispersed, heavy-tailed marginal. The model of §6.1 — Poisson *conditional* on the local rate, mixed over fluctuating twin spacings — is consistent with this; a single unconditional Poisson is not.

### 6.4. Interpretation

- **The 1.9% collinearity rate is chance.** The independent-draws coincidence rate computed from the actual gap marginal (`1.99\%`) matches the observed adjacent-equal rate (`1.95\%`) to within sampling noise. The straight triples in the geometric shadow are exactly what a noisy gap process with this marginal produces; there is no excess collinearity to explain. This is the quantitative content of "micro-collinearity is chance."
- **The collinearity conclusion is robust to the modeling choice.** It does not rest on the Poisson assumption. Whatever the precise marginal, the coincidence rate is governed by `\sum_v p_v^2`, and the measured marginal already accounts for the observation. If anything, a naive single-Poisson null would *over*-predict collinearity (5.76%), so the chance interpretation is conservative.
- **The heavy tail is real but irrelevant to the collinearity story.** The strong overdispersion (variance-to-mean ≈ 22, tail orders of magnitude above single-Poisson) is a genuine feature — it reflects the wide variation in twin spacing through `μ_k` — but it concerns the *spread* of `Δx`, not the *repetition* of `Δx`. The collinearity question is settled by the empirical `\sum p_v^2` regardless of tail shape. The tail matters for other parts of the deep-dive (the slope-drift and scaling analyses of §§7–8), not here.

In sum: the Cramér/Poisson comparison confirms §4 quantitatively. Three-in-a-row collinearity occurs at the chance rate of a noisy, overdispersed gap process; the only systematic deviation from the simplest model — a heavy right tail — is a property of prime/twin spacing variability and leaves the "micro-collinearity is chance" conclusion intact.

---

## 7. Local-density scaling: Δx_k / (2Δp_k)

Section 6 established that `Δx` is heavily overdispersed and modeled it as a Poisson mixture whose rate `μ_k` fluctuates. This section identifies *what* drives that fluctuation by normalizing `Δx_k` by the length of the interval it counts over.

### 7.1. The scaling quantity

Let `Δp_k = p_{k+1} − p_k` be the **twin-to-twin integer gap** between consecutive lower-members. The interval `(2p_k, 2p_{k+1}]` over which `Δx_k` counts primes has length `2Δp_k`. Define the **scaled density estimator**

$$\rho_k \;=\; \frac{\Delta x_k}{2\,\Delta p_k} \;=\; \frac{\#\{\text{primes in }(2p_k, 2p_{k+1}]\}}{\text{length of }(2p_k, 2p_{k+1}]}.$$

By construction `ρ_k` is an empirical estimate of the **local prime density near `2p_k`**, which by the prime number theorem should satisfy

$$\rho_k \;\approx\; \lambda_k \;:=\; \frac{1}{\log(2p_k)}$$

up to second-order corrections. Where `Δx_k` confounds two effects — the local density and the width of the window — `ρ_k` isolates the density.

### 7.2. Distribution of ρ_k

Over all 239,100 gaps:

| quantity | `Δx_k` | `Δp_k` | `ρ_k` |
|---|---:|---:|---:|
| mean | 24.10 | 209.12 | 0.0578 |
| median | 17 | 150 | 0.0573 |
| std | 23.02 | 199.23 | 0.0173 |
| min | 0 | 2 | 0 |
| max | 332 | 2,832 | 0.3333 |
| coeff. of variation | 0.955 | 0.953 | **0.300** |

The first thing to note is that **`ρ_k` is far more stable than either `Δx_k` or `Δp_k`**: its coefficient of variation is `0.30`, versus `0.95` for both the raw gap and the twin gap. Dividing out the window width removes most of the spread.

**Histogram of `ρ_k`.**

| `ρ` range | count | fraction |
|---|---:|---:|
| `[0.00, 0.02)` | 5,266 | 2.20% |
| `[0.02, 0.04)` | 15,782 | 6.60% |
| `[0.04, 0.06)` | 121,582 | 50.85% |
| `[0.06, 0.08)` | 76,756 | 32.10% |
| `[0.08, 0.10)` | 15,303 | 6.40% |
| `[0.10, 0.15)` | 3,902 | 1.63% |
| `[0.15, 0.20)` | 465 | 0.19% |
| `[0.20, 0.40)` | 44 | 0.02% |

The distribution is unimodal and roughly symmetric about its mode in `[0.04, 0.06)`, with light tails — a striking contrast to the heavy-tailed `Δx` of §2. (The mode has shifted left relative to smaller samples because the dataset now reaches `2p \sim 10^8`, where the local density `1/\log(2p) \approx 0.055` is correspondingly lower.)

### 7.3. Comparison to the theoretical density

For each `k` compute `λ_k = 1/\log(2p_k)` and the ratio `r_k = ρ_k / λ_k`:

| quantity | value |
|---|---:|
| mean `r_k` | 0.992 |
| median `r_k` | 0.995 |
| std `r_k` | 0.285 |
| min / max | 0 / 4.57 |

**`ρ_k` tracks `λ_k` on the nose, on average.** The mean ratio is `0.99` and the median `0.99` — the empirical local density agrees with the PNT prediction `1/\log(2p)` to within about 1% in aggregate. The fluctuations are moderate: a standard deviation of `±29%`, with the bulk tightly concentrated,

| `r = ρ/λ` range | fraction |
|---|---:|
| `[0.00, 0.50)` | 3.75% |
| `[0.50, 0.75)` | 8.95% |
| `[0.75, 1.00)` | 38.60% |
| `[1.00, 1.50)` | 45.42% |
| `[1.50, 2.00)` | 2.63% |
| `[2.00, 4.57]` | 0.65% |

so 84% of all windows have local density within `[0.75, 1.5]×` the PNT value; a thin tail (0.65%) exceeds `2×`, reaching `4.57×` in the most prime-rich window. The PNT density is an excellent description of `ρ_k` in the mean, with bounded, well-behaved scatter.

### 7.4. Interpretation: twin-gap fluctuations dominate

Write the multiplicative decomposition

$$\Delta x_k \;=\; 2\,\Delta p_k \cdot \rho_k, \qquad \log \Delta x_k \;=\; \log(2\Delta p_k) \;+\; \log \rho_k.$$

The log-variances partition the variability of `Δx` between the two factors (with a small covariance):

| term | log-variance | share |
|---|---:|---:|
| `\log \Delta x_k` (total) | 1.122 | — |
| `\log(2\Delta p_k)` (twin-gap width) | 1.142 | ~100% |
| `\log \rho_k` (local density) | 0.076 | ~7% |

(The width term slightly *exceeds* the total; the density term `0.076` is almost entirely cancelled by a negative covariance, `2\,\mathrm{Cov} \approx -0.10`.) The conclusion is unambiguous and, on the full dataset, even sharper than before:

> **The fluctuations in `Δx_k` are driven essentially entirely by the twin-to-twin gap `Δp_k`, not by the local prime density `ρ_k`.**

The local density is comparatively rigid (it hugs `1/\log(2p)` with `±29%` scatter); the twin gap is wildly variable (`Δp_k` ranges from `2` to `2,832`, CV `0.95`). The heavy tail and overdispersion of `Δx` found in §6 are therefore **inherited from the heavy tail of the twin-gap distribution** — the Poisson-mixture rate `μ_k ≈ 2\Delta p_k / \log(2p_k)` fluctuates because `Δp_k` fluctuates, while the `1/\log` factor is nearly constant. This pins down the source of the §6 overdispersion precisely.

This is also the right object for understanding **slope drift**. Since `slope_k = 1/\Delta x_k`,

$$\text{slope}_k \;=\; \frac{1}{2\,\Delta p_k\,\rho_k} \;\approx\; \frac{\log(2p_k)}{2\,\Delta p_k}.$$

The slowly-growing factor `\log(2p_k)` is the systematic, predictable part — it produces the gentle downward drift of the macro-slope `≈ C_2/\log p` documented in §4 and §8. The factor `1/\Delta p_k` is the fast, noisy part — it produces the per-step scatter that makes micro-collinearity a matter of chance (§3, §6). The macro-trend and the micro-noise of the geometric shadow live in the two factors of this single identity.

### 7.5. The (λ_k, ρ_k) scatter (described)

A scatter plot of `ρ_k` (vertical) against `λ_k = 1/\log(2p_k)` (horizontal) — Figure 2 of §9 — shows a **cloud hugging the diagonal `ρ = λ`**, with these features:

- The bulk of points lies in a band around the line of slope 1 (consistent with mean `r ≈ 0.99`), confirming `ρ_k ≈ λ_k`.
- The vertical spread at any fixed `λ` is substantial but bounded — roughly `±29%` — reflecting the moderate fluctuation of the local density; a thin tail of points reaches up to `≈ 4.6×` the diagonal, and there is a floor at `ρ = 0` (the 3,819 windows with `Δx = 0`).
- Because `λ_k` itself shrinks slowly with scale (most points now cluster at small `λ`, near `0.05`–`0.06`, since the dataset reaches `2p \sim 10^8`, with a short spur toward larger `λ` from the smallest twins), the cloud is densest in the lower-left and thins toward the upper-right — the small-`p` end.

The picture visually confirms §7.3–7.4: a tight diagonal relationship (the PNT density) overlaid with bounded multiplicative noise, with the dramatic variability instead living in `Δp_k`, which this plot has divided out.

---

## 8. Slope-drift fit across decades

Section 7 split `Δx_k = 2Δp_k·ρ_k` into a slowly-drifting density factor and a noisy twin-gap factor. This section tests the drift directly: does the macro-slope of the geometric shadow follow the predicted `1/\log` law across decades of scale? The unified `N = 10^8` dataset (239,100 gaps) supplies **five full decades** `[10^2,10^7)` plus a partial sixth `[10^7, 5\times10^7)`.

### 8.1. The empirical slope (and a caveat)

The local slope of the `π(2p)`-versus-twin-rank plot between consecutive points is `\text{slope}_k = 1/\Delta x_k` (§1). As a **per-step** average this is ill-posed: 3,819 of the windows have `Δx_k = 0` (giving `1/0`), and even excluding those, `\text{mean}(1/\Delta x)` is Jensen-biased upward and does not estimate the plot's slope. For example, over `[10^3, 10^4)`:

$$\frac{1}{\text{mean}(\Delta x)} = 0.087 \quad\text{versus}\quad \text{mean}\!\left(\tfrac{1}{\Delta x}\right) = 0.188 \;(\text{zeros excluded}).$$

The quantity that **is** the plot's slope over a block of pairs — and that the `C_2/\log` law predicts — is the **aggregate slope**, the total rise over the total run:

$$\text{slope}_{\text{decade}} = \frac{\#\{\text{pairs in decade}\}}{\sum_{\text{decade}} \Delta x_k} = \frac{1}{\overline{\Delta x}_{\text{decade}}}.$$

We use this aggregate slope throughout §8.

### 8.2. The theoretical slope

The crude leading prediction is `\text{slope}_{\text{theory}} = C_2/\log(2p)` with `C_2 = 0.6601618`. But the macro-slope derived properly from the densities is sharper. Since `dk/dp \sim 2C_2/(\log p)^2` (twin density) and `d\pi(2p)/dp = 2/\log(2p)`,

$$\text{slope} = \frac{dk}{d\pi(2p)} = \frac{2C_2/(\log p)^2}{2/\log(2p)} = \frac{C_2\,\log(2p)}{(\log p)^2}.$$

This exceeds the crude `C_2/\log(2p)` by a factor `(\log(2p)/\log p)^2 \approx 1.1$–$1.15`, which (we will see) is exactly the size of the observed discrepancy.

### 8.3. Decade table

Binning by decades of `p_k` (aggregate slope `1/\overline{\Delta x}`; both theory columns averaged per pair over the decade):

| decade of `p_k` | N | mean `Δx` | median | std `Δx` | emp. slope | `C_2/\log(2p)` | ratio | `C_2\log(2p)/(\log p)^2` | ratio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `[10², 10³)` | 27 | 9.70 | 7 | 9.18 | 0.10305 | 0.10141 | 1.016 | 0.12743 | 0.809 |
| `[10³, 10⁴)` | 170 | 11.50 | 8 | 9.67 | 0.08696 | 0.07335 | 1.185 | 0.08619 | **1.009** |
| `[10⁴, 10⁵)` | 1,019 | 15.45 | 12 | 13.60 | 0.06471 | 0.05807 | 1.115 | 0.06588 | **0.982** |
| `[10⁵, 10⁶)` | 6,945 | 18.85 | 14 | 17.44 | 0.05304 | 0.04826 | 1.099 | 0.05356 | **0.990** |
| `[10⁶, 10⁷)` | 50,811 | 22.08 | 16 | 20.63 | 0.04530 | 0.04128 | 1.097 | 0.04511 | **1.004** |
| `[10⁷, 5·10⁷)` | 180,120 | 24.93 | 18 | 23.81 | 0.04011 | 0.03711 | 1.081 | 0.04018 | **0.998** |

Two facts stand out. First, **the slope drifts downward monotonically** — `0.103 → 0.087 → 0.065 → 0.053 → 0.045 → 0.040` — as the scale grows, exactly the qualitative `1/\log` behavior. Second, **the refined formula `C_2\log(2p)/(\log p)^2` matches the empirical slope to 1–2%** for every decade with `p_k \ge 10^3` (five decades), while the crude `C_2/\log(2p)` runs systematically `\sim 8$–$19\%` low. The only outlier is the first decade `[10^2,10^3)`, where `p` is too small for the asymptotics (the refined form overshoots and the crude form matches only by coincidence of the short range).

### 8.4. The A, B fit

Fitting the six decade slopes to the requested two-term model `\text{slope} \approx A/L + B/L^2` in `L = \log(2p)` (least squares, no intercept) gives

$$A = 0.795, \qquad B = -0.653.$$

Taken at face value, `A` is above `C_2 = 0.660` and `B` is negative — which would seem to contradict the leading-order prediction. It does not, for two reasons, and the contradiction is instructive:

1. **The bare `A/L` model is the wrong parametrization.** Expanding the *correct* slope in `L = \log(2p)` (using `\log p = L - \log 2`) gives
$$\frac{C_2\,\log(2p)}{(\log p)^2} = \frac{C_2}{L}\Big(1 - \tfrac{\log 2}{L}\Big)^{-2} = \frac{C_2}{L} + \frac{2C_2\log 2}{L^2} + \cdots = \frac{0.660}{L} + \frac{0.915}{L^2} + \cdots,$$
i.e. the theory predicts `A = C_2 = 0.660` with a **positive** `1/L^2` correction `B \approx +0.92`. A free fit on six decade points — one of which (`[10^2,10^3)`) lies in the non-asymptotic regime — is ill-conditioned and trades `A` upward against `B` to interpolate those points. (With the larger dataset `A = 0.795` has moved noticeably toward `C_2` compared with the `A = 0.845` of a four-decade fit, as expected, but the bare two-term fit remains the weaker instrument.) The fitted `(A,B)` should not be over-interpreted.
2. **The robust statement is the direct comparison of §8.3**, not the free fit: the empirical slope equals the theoretically-derived `C_2\log(2p)/(\log p)^2` to 1–2% for `p \ge 10^3`. That is the meaningful confirmation; the `A,B` fit is reported for completeness but is the weaker instrument here.

### 8.5. Interpretation

- **The macro-trend is confirmed.** The empirical slope follows the PNT/Hardy–Littlewood prediction `C_2\log(2p)/(\log p)^2` — whose leading coefficient is exactly `C_2 = C_H/2`, half the FS twin constant `C_H = 2C_2` of Theorem 4.7a — to within 1–2% across five decades. The slope drift is genuinely a `1/\log`-type law, with the second-order `(\log(2p)/\log p)^2` factor visible and accounted for.
- **The residuals are the §7 noise.** The decade *means* track the curve; the per-pair scatter around them (std `Δx` comparable to mean `Δx` in every decade) is the `1/\Delta p_k` twin-gap fluctuation isolated in §7, not a failure of the trend. The slope's predictable part lives in `\log(2p)`; its noise lives in `\Delta p_k`.
- **Verdict.** The empirical slope drift **matches the theoretical `1/\log` law** — specifically the refined leading term `C_2\log(2p)/(\log p)^2`. The crude `C_2/\log(2p)` is right in form and drift but low by the `(\log(2p)/\log p)^2` factor; the refined term closes the gap.

### 8.6. The slope-versus-`\log(2p)` plot (described)

A plot of `\text{slope}_k = 1/\Delta x_k` (vertical) against `\log(2p_k)` (horizontal) would show:

- a **noisy, downward-sloping cloud** — points scattered widely (the `1/\Delta p_k` noise, plus the integer granularity of `1/\Delta x_k` producing visible horizontal stripes at `1, 1/2, 1/3, \dots`), trending down as `\log(2p)` grows;
- the **decade-averaged points lying neatly on the curve `C_2\log(2p)/(\log p)^2`**, threading the noisy cloud — the smooth backbone of the scatter;
- the scatter at each `\log(2p)` dominated by the twin-gap fluctuation: tighter where `Δp` is small, fanning upward where consecutive twins are far apart (small slope) — the visual signature that the drift is deterministic and the spread is `Δp`-driven.

---

## 9. Visualization Appendix

The three figures below render the structure established analytically in §§2–8. All three use the unified `N = 10^8` dataset (239,100 gaps); Figure 2 plots a random 20,000-point subsample for legibility, and Figure 3 a random 30,000-point subsample, but all statistics and decade markers are computed on the full set.

### 9.1. Distribution of Δx

![Histogram of Delta x over all 239,100 twin-pair gaps](figures/deltax_histogram.png)

**Figure 1.** Histogram of `\Delta x_k` (primes in `(2p_k, 2p_{k+1}]`) over all 239,100 gaps, in bins of width 5; the dashed line marks the mean `24.1`. The shape is the one diagnosed in §2: a **mode in the `[10,20)` band**, a left shoulder that includes the **spike at `\Delta x = 0`** (the 3,819 windows where consecutive doubled twins share a prime slot), and a long, thin **right tail** stretching to `332`. The mean sits to the right of the mode, the signature of the right skew. This is the overdispersed, heavy-tailed marginal whose source §7 traced to the twin-gap distribution.

### 9.2. Local density ρ versus the PNT prediction λ

![Scatter of rho against lambda with the diagonal rho = lambda](figures/lambda_rho_scatter.png)

**Figure 2.** Scatter of the empirical local density `\rho_k = \Delta x_k/(2\Delta p_k)` against the PNT prediction `\lambda_k = 1/\log(2p_k)` (20,000-point random subsample), with the diagonal `\rho = \lambda` in red. The points form a **cloud centered on the diagonal** (mean ratio `\rho/\lambda = 0.99`), confirming that `\rho_k` tracks `1/\log(2p)` on average. The vertical spread is **bounded** (`\pm 29\%`; a thin tail reaches `\approx 4.6\times` the diagonal), and a **floor at `\rho = 0`** marks the zero-`\Delta x` windows. Because the dataset reaches `2p \sim 10^8`, the bulk of points is concentrated at small `\lambda` (`\approx 0.05$–$0.06`), with only the earliest twins reaching the larger-`\lambda`, upper-right part of the diagonal. The horizontal striping at low `\rho` is the integer granularity of small prime counts over short windows. The picture confirms §7: a tight diagonal (the PNT density) dressed in bounded multiplicative noise, with the wild variability instead residing in `\Delta p_k`, which this normalization has divided out.

### 9.3. Slope drift versus scale

![Slope 1/Delta x against log(2p) with theoretical backbone and decade points](figures/slope_vs_log2p.png)

**Figure 3.** The local slope `\text{slope}_k = 1/\Delta x_k` (gray, zeros omitted, 30,000-point random subsample) against `\log(2p_k)`, over the unified dataset. The red curve is the theoretically-derived backbone `C_2\,\log(2p)/(\log p)^2` (§8.2); the black squares are the **decade-aggregate slopes** `1/\overline{\Delta x}` from the §8.3 table, plotted at each decade's mean `\log(2p)`. The cloud is the expected noisy, downward-sloping scatter, organized into **horizontal stripes** at `1, \tfrac12, \tfrac13, \tfrac14, \dots` (the discrete values `1/\Delta x` can take), fanning toward zero as the scale grows. The five high-scale decade squares (`p \ge 10^3`) lie **squarely on the backbone curve**, the visual form of the 1–2% agreement of §8.3; the lowest square (`[10^2,10^3)`) sits just below the curve, in the non-asymptotic regime where the refined formula slightly overshoots. The figure makes the central message of the deep-dive visible at a glance: a **deterministic `1/\log` drift** (the red curve, threaded by the decade means) carrying **`\Delta p`-driven noise** (the gray scatter around it).

---

## 10. Conditional Δx distribution given p_k

The previous sections decomposed `Δx` into a window width (`2Δp_k`), a density trend (`1/\log(2p_k)`), and a residual. This section normalizes `Δx_k` by its full predicted conditional mean and asks whether what remains has a **scale-free shape**.

### 10.1. The conditional normalization

Using the §6.1 Poisson-mixture rate — the expected prime count in the window `(2p_k, 2p_{k+1}]` —

$$\mu_k \;=\; \frac{2(p_{k+1}-p_k)}{\log(2p_k)} \;=\; \frac{2\Delta p_k}{\log(2p_k)}, \qquad Z_k \;=\; \frac{\Delta x_k}{\mu_k}.$$

**An identity worth noting:** `Z_k` is exactly the ratio `r_k = \rho_k/\lambda_k` of §7, since

$$Z_k = \frac{\Delta x_k \,\log(2p_k)}{2\Delta p_k} = \rho_k\,\log(2p_k) = \frac{\rho_k}{\lambda_k} = r_k.$$

So §10 is the **decade-resolved** version of §7.3: it asks whether the local-density ratio `r_k` (aggregate mean `0.99`, std `0.29`) keeps the same distribution at every scale. The normalization divides out *both* the `Δp`-driven width (the §7 effect) and the `\log(2p)` density trend (the §8 effect) at once.

### 10.2. Decade statistics

Over the unified `N = 10^8` dataset, binned by decades of `p_k`:

| decade of `p_k` | N | mean `Z` | median `Z` | std `Z` | min | max |
|---|---:|---:|---:|---:|---:|---:|
| `[10², 10³)` | 27 | 0.940 | 0.983 | 0.256 | 0 | 1.391 |
| `[10³, 10⁴)` | 170 | 0.956 | 0.968 | 0.277 | 0 | 1.998 |
| `[10⁴, 10⁵)` | 1,019 | 0.976 | 0.992 | 0.256 | 0 | 2.003 |
| `[10⁵, 10⁶)` | 6,945 | 0.991 | 0.998 | 0.290 | 0 | 3.513 |
| `[10⁶, 10⁷)` | 50,811 | 0.992 | 0.994 | 0.288 | 0 | 4.189 |
| `[10⁷, 5·10⁷)` | 180,120 | 0.993 | 0.995 | 0.284 | 0 | 4.573 |

The mean creeps from `0.94` toward `0.99` (the same slight sub-unity bias as §7's `\bar r = 0.99`, a touch larger at small `p`), the median sits at `0.97$–$1.00`, and the standard deviation is nearly constant at `0.26$–$0.29` across six decades.

**Coarse histograms** (fraction of `Z` in each bin):

| decade | `[0,.5)` | `[.5,.75)` | `[.75,1.0)` | `[1.0,1.25)` | `[1.25,1.5)` | `\ge1.5` |
|---|---:|---:|---:|---:|---:|---:|
| `[10², 10³)` | 0.074 | 0.037 | 0.556 | 0.259 | 0.074 | 0.000 |
| `[10³, 10⁴)` | 0.053 | 0.094 | 0.412 | 0.353 | 0.065 | 0.024 |
| `[10⁴, 10⁵)` | 0.046 | 0.086 | 0.395 | 0.360 | 0.099 | 0.014 |
| `[10⁵, 10⁶)` | 0.040 | 0.098 | 0.366 | 0.389 | 0.071 | 0.035 |
| `[10⁶, 10⁷)` | 0.038 | 0.093 | 0.382 | 0.364 | 0.093 | 0.030 |
| `[10⁷, 5·10⁷)` | 0.037 | 0.088 | 0.388 | 0.374 | 0.079 | 0.033 |

Every decade is unimodal, peaked in `[0.75, 1.25)` (straddling `Z = 1`), with a thin floor near `0` (the `Δx = 0` windows) and a light right tail. The four largest decades (where the statistics are best resolved) are visibly near-identical.

### 10.3. Test for scale-collapse

Kolmogorov–Smirnov and 1-Wasserstein distances between decade distributions:

| pair | KS | `W_1` |
|---|---:|---:|
| `[10²,10³)` vs `[10³,10⁴)` | 0.166 | 0.057 |
| `[10³,10⁴)` vs `[10⁴,10⁵)` | 0.071 | 0.022 |
| `[10⁴,10⁵)` vs `[10⁵,10⁶)` | 0.063 | 0.023 |
| `[10⁵,10⁶)` vs `[10⁶,10⁷)` | 0.026 | 0.009 |
| `[10⁶,10⁷)` vs `[10⁷,5·10⁷)` | 0.021 | 0.009 |
| `[10³,10⁴)` vs `[10⁷,5·10⁷)` | 0.070 | 0.039 |

For every pair of decades with `p \ge 10^3`, the KS distance is `\le 0.071` and the Wasserstein distance `\le 0.039` — the distributions are **nearly indistinguishable**: same mode, same spread, same tail thickness. The collapse in fact *tightens* with scale: between the two largest, best-resolved decades the KS distance falls to `0.021`. The only sizeable distances involve the first decade `[10^2,10^3)` (KS `0.17`), which has just `N = 27` points — at that sample size a KS distance of `\sim 0.2` is within sampling noise of identical underlying laws — and lies in the non-asymptotic regime flagged repeatedly above.

### 10.4. Interpretation

- **`Z_k` follows a stable, scale-invariant law.** For `p \ge 10^3` the decade distributions of `Z_k = \Delta x_k/\mathbb{E}[\Delta x \mid p_k]` collapse onto a common shape — unimodal, centered just below `1`, std `\approx 0.28` — with KS distances at the few-percent level, falling to `0.021` between the largest decades. The conclusion is clean: **`\Delta x_k / \mathbb{E}[\Delta x \mid p_k]` has a stable, scale-invariant shape.** The apparent small-`p` deviation is a finite-sample / pre-asymptotic artifact, not a breakdown of the collapse.
- **The normalization removes the `Δp`-driven overdispersion.** This is the headline. The raw gap had coefficient of variation `0.95` (dominated, per §7, by twin-gap fluctuation); `Z_k` has CV `\approx 0.29` and is scale-stable. Dividing by `\mu_k` — which contains the actual `Δp_k` — *un-mixes* the Poisson mixture of §6: it strips out the fluctuating rate and leaves the within-window counting residual.
- **But a residual fluctuation floor remains — and it is not pure Poisson shot noise.** If `Δx \mid \mu` were exactly Poisson, `Z` would have std `1/\sqrt{\mu} \approx 1/\sqrt{\overline{\Delta x}}`, predicting `0.32, 0.30, 0.25, 0.23, 0.21, 0.20` across the six decades — a steady *tightening*. The observed std instead stays flat at `0.26$–$0.29` and increasingly *exceeds* the Poisson prediction: by the last decade `0.28` versus `0.20`, a widening gap. So the conditional distribution is mildly **super-Poissonian**, with a scale-stable spread that does not shrink to zero — and the larger dataset makes this sharper, since the Poisson reference keeps falling while the observed spread does not. This is consistent with the known excess variance of primes in short intervals (Montgomery–Soundararajan) and with the residual being a genuine, scale-free arithmetic fluctuation rather than a vanishing shot-noise term.

### 10.5. Connection to earlier sections

The three normalizations form a ladder, each removing one layer of variability identified earlier:

| object | removes | what remains | CV |
|---|---|---|---:|
| `Δx_k` | — | width + density + counting noise | 0.955 |
| `ρ_k = Δx_k/(2Δp_k)` (§7) | `Δp` width | density trend + counting noise | 0.300 |
| `Z_k = Δx_k/\mu_k` (§10) | `Δp` width **and** `\log(2p)` density | scale-free counting residual | 0.287 |

- **§6 (Poisson mixture):** `μ_k` fluctuates because `Δp_k` does. `Z_k` divides by `μ_k`, un-mixing the mixture; its near-constant shape across decades is the demixed residual, mean `\approx 1`, no longer overdispersed.
- **§7 (`Δp` dominates):** `Z_k \equiv r_k`. §7 reported its aggregate spread; §10 shows that spread is *scale-invariant* — confirming that what `ρ`/`λ` measures is a stable quantity, not an artifact of averaging over scales.
- **§8 (slope drift `\sim \log(2p)`):** `μ_k` carries the `1/\log(2p)` factor, so `Z_k` removes the deterministic slope drift too. `Z_k` is precisely what is left after subtracting both the §8 trend and the §7 width: a scale-free counting fluctuation.
- **Does `Z_k` remove the `Δp`-driven overdispersion?** Yes — CV collapses from `0.955` to `0.287`, and the residual is scale-invariant. What it does *not* remove is a modest, scale-stable, slightly super-Poissonian floor: the irreducible arithmetic fluctuation of prime counts in the windows. That floor is the genuine randomness; everything else (`Δp` width, `\log` density) is structure that normalization peels away.

---

## Appendix: Provenance of the numbers

All statistics and figures are produced from a single run of [`scripts/pg_deltax_unified.py`](scripts/pg_deltax_unified.py) (pure NumPy, no SciPy), recomputed from scratch and cross-checked.

- **Uniform sieve / pairs:** one Boolean sieve to `N = 10^8` (`100{,}000{,}000`); `5{,}761{,}455` primes. Valid twin pairs are the twin lower-members `p_k` with `2(p_k+2) \le N`, giving **239,101 pairs and 239,100 gaps** (`p_k` ranges up to `\approx 5\times10^7`). `\pi(2p_k)` obtained by `searchsorted` on the prime array. This one dataset underlies every section.
- **Distribution (§2):** mean `24.096`, median `17`, std `23.018`, min `0`, max `332`; `3,819` zero-gaps; histogram bins as tabulated.
- **Run lengths (§3):** `234,444` runs; `L=1`: `229,914` (98.07%), `L=2`: `4,409` (1.88%), `L=3`: `117` (0.05%), `L=4`: `3`, `L=5`: `1`; adjacent-equal rate `4,656/239,099 = 1.947\%`; `3.8\%` of gaps lie in runs of length `\ge 2`.
- **Cramér/Poisson comparison (§6):** `R_{\text{empirical}} = \sum_v (\text{freq}_v/239100)^2 = 1.99\%` from exact per-value gap frequencies (not the coarse §2 bins); compared to the observed adjacent-equal rate `1.95\%` (§3) and to a single `\text{Pois}(24.10)` coincidence rate `\sum_v \text{Pois}(v;24.10)^2 = 5.76\%` (summed in log-space via `\mathrm{lgamma}`). Tail probabilities `\Pr[\Delta x \ge T]` for `T = 30, 50, 100` from direct counts (`69{,}770`, `29{,}267`, `3{,}268` of 239,100) versus `\text{Pois}(24.10)` upper tails. Empirical variance `529.8` versus mean `24.10` (variance-to-mean ≈ 22).
- **Local-density scaling (§7):** `\rho_k = \Delta x_k / (2\Delta p_k)`, `\lambda_k = 1/\log(2p_k)`, `r_k = \rho_k/\lambda_k`. Means/medians/std/extrema and histograms as tabulated. Variance decomposition from `\log\Delta x = \log(2\Delta p) + \log\rho`: `\mathrm{Var}(\log\Delta x)=1.122`, `\mathrm{Var}(\log 2\Delta p)=1.142`, `\mathrm{Var}(\log\rho)=0.076` (log of positive gaps only; the 3,819 zero-`\Delta x` windows excluded). Coefficients of variation: `Δx` 0.955, `Δp` 0.953, `ρ` 0.300.
- **Slope-drift fit (§8):** decade boundaries `[10^2,10^3), [10^3,10^4), \dots, [10^6,10^7)` (five full) and `[10^7, 5\times10^7)` (partial). Per decade: aggregate slope `1/\overline{\Delta x}` (not `\text{mean}(1/\Delta x)`, which is Jensen-biased and undefined on the zero-gaps); theory columns `\text{mean}(C_2/\log(2p_k))` and `\text{mean}(C_2\log(2p_k)/(\log p_k)^2)` with `C_2 = 0.6601618`. The `A/L + B/L^2` fit (`L=\log(2p)`) by least squares without intercept over the six decade points gave `A=0.795, B=-0.653`; the theory-expansion coefficients are `A=C_2=0.660`, `B=2C_2\log2 = 0.915`.
- **Conditional distribution (§10):** `\mu_k = 2\Delta p_k/\log(2p_k)`, `Z_k = \Delta x_k/\mu_k` (algebraically `\equiv r_k` of §7). Per-decade mean/median/std/extrema and 0.25-width histograms as tabulated. KS distances = max absolute difference of empirical CDFs on the pooled sample; 1-Wasserstein = mean absolute difference of 1,000 matched quantiles (both in NumPy). Poisson shot-noise reference `1/\sqrt{\overline{\Delta x}}` per decade: `0.32, 0.30, 0.25, 0.23, 0.21, 0.20` versus observed std `0.26, 0.28, 0.26, 0.29, 0.29, 0.28`.
- **Figures (§9):** Matplotlib (Agg backend), saved to `figures/`. Fig. 1 (`deltax_histogram.png`): full 239,100-gap set, bins of width 5. Fig. 2 (`lambda_rho_scatter.png`): 20,000-point random subsample (seed 0), `\rho_k` vs `\lambda_k` with the `\rho=\lambda` diagonal. Fig. 3 (`slope_vs_log2p.png`): 30,000-point random subsample (seed 1) of `1/\Delta x_k` (zeros omitted) vs `\log(2p_k)`, with the backbone `C_2\log(2p)/(\log p)^2` and the six decade-aggregate points computed on the full set.
