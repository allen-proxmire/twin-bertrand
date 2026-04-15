# Prime Geometry — A Field Guide

*A narrative tour of PG I–III and the empirical laws that emerged along the way.*

**Allen Proxmire · April 2026**

---

## Preface

This is a field guide, not a paper. It collects the ideas from the three Prime Geometry notes (PG I, II, III) and the computational work behind them into a single story, aimed at a mathematically literate reader who is curious about prime numbers but hasn't seen the three papers. Proofs are pointed to, not repeated. Numbers are cited, not re-derived. If you finish reading this and want to see how a particular claim was verified, the scripts and datasets are listed at the end — everything reproduces from a laptop.

The thread running through all of it is simple: **attach a right triangle to every pair of consecutive primes and watch what happens**. Most of what happens is geometric fluff — the triangles just record the primes. But one quantity, the angle of each triangle, turns out to organize twin primes in an unexpected way; and that organization, when pushed, generalizes to all prime constellations (twins, cousins, sexy primes, and beyond). The result is a family of conjectural density bounds that sit in a well-defined spot within the analytic-number-theory landscape — weaker than the twin-prime conjecture, stronger than the Zhang–Maynard bounded-gaps theorems, and equivalent to a clean geometric statement about how primes approach 45° symmetry.

---

## 1. The Prime Triangle

Take two consecutive primes, $p$ and $q$, with $p < q$. Plant a right triangle with legs of length $p$ and $q$. Its hypotenuse is $C = \sqrt{p^2 + q^2}$, and the angle at the base of the shorter leg is

$$\alpha(p,q) = \arctan\!\left(\frac{p}{q}\right).$$

That's the whole construction.

For the very first pair, $(2, 3)$, the angle is $\arctan(2/3) = 33.69°$. For the pair $(3, 5)$ — which happens to be a twin prime — it's $\arctan(3/5) = 30.96°$ (a step *back*, because $3/5 < 2/3$). For the next pair $(5, 7)$, another twin, the angle is $35.54°$ — a step forward.

As $p$ grows, most consecutive prime pairs have $q$ only slightly larger than $p$, so the angle stays close to $45°$. The pairs that approach $45°$ fastest are the **twin primes**, where $q = p + 2$, giving

$$\alpha(p, p+2) = \arctan\!\left(\frac{p}{p+2}\right) \;\to\; 45° \quad \text{as } p \to \infty.$$

Every twin prime is a step closer to $45°$ than the last one. That alone isn't surprising — it's just because twin primes have the smallest possible even gap.

What *is* interesting is that when you look at the sequence of all consecutive-prime-pair angles and ask "which ones set new records for closeness to $45°$?", the answer turns out to be: **almost exclusively the twins.** The only exception across the first hundred million primes is the very first pair, $(2, 3)$, whose $33.69°$ is the initial record-holder by default.

That observation is PG II's main technical content, and the rest of this guide unpacks it.

---

## 2. The Angle-Record Story

### 2.1 The record sequence

Walk through consecutive primes in order. Keep a running maximum of the angle $\alpha(p_n, p_{n+1})$, and mark a pair as a **record** every time its angle exceeds all previous ones. You get a sparse subsequence of the consecutive-prime-pair list.

The first few records are:

| # | $p_n$ | $p_{n+1}$ | gap | angle | type |
|---|---|---|---|---|---|
| 1 | 2 | 3 | 1 | $33.69°$ | (gap 1, unique) |
| 2 | 5 | 7 | 2 | $35.54°$ | twin |
| 3 | 11 | 13 | 2 | $40.24°$ | twin |
| 4 | 17 | 19 | 2 | $41.82°$ | twin |
| 5 | 29 | 31 | 2 | $43.09°$ | twin |
| 6 | 41 | 43 | 2 | $43.64°$ | twin |
| 7 | 59 | 61 | 2 | $44.05°$ | twin |
| ⋮ | | | | | |

After the initial $(2,3)$, *every* record is a twin prime — for all $440{,}312$ records among primes below $10^8$, verified by direct computation. At the high end of that range, the record angles are at $44.999999\ldots°$, approaching $45°$ to ten decimal places.

### 2.2 The 2P-beats rule

Why should every record be a twin? Here's the elementary observation.

Suppose you currently hold the angle record with a twin pair $(Q, Q+2)$. Can a later non-twin pair — say a gap-4 pair $(P, P+4)$ — overtake you? A short calculation:

$$\frac{P}{P+4} > \frac{Q}{Q+2} \iff P(Q+2) > Q(P+4) \iff 2P > 4Q \iff P > 2Q.$$

So a gap-4 pair beats the twin record **if and only if its leading prime exceeds $2Q$**. For larger gaps the threshold only grows — a gap-6 pair needs $P > 3Q$, a gap-8 pair needs $P > 4Q$, and so on. The binding constraint is always the gap-4 pair and its factor of $2$.

That's the **2P-beats rule**. It says: if, between twin $(Q, Q+2)$ and the next twin $(Q', Q'+2)$, every consecutive-prime pair $(P, P+g)$ with $g \ge 4$ has $P \le 2Q$, then no non-twin can break the record. And that condition is automatically satisfied if the next twin $Q' < 2Q$.

### 2.3 Equivalence with a density bound

The 2P-beats rule turns the record structure into a **density question about twin primes**: every record is a twin if and only if consecutive twins never have a ratio $\ge 2$. Writing $T_k$ for the $k$th twin prime, the condition is

$$T_{k+1} < 2\, T_k \quad \text{for all } k \text{ with } T_k \ge 11.$$

This is exactly the statement that **every interval $(x, 2x]$ with $x \ge 11$ contains at least one twin prime** — a "Bertrand's postulate for twin primes." In the language of counting functions,

$$\pi_2(2x) - \pi_2(x) \ge 1 \quad \text{for all } x \ge 11,$$

where $\pi_2(x)$ counts primes $p \le x$ with $p + 2$ also prime.

This inequality — we call it $(\mathrm{TPB})$, the Twin-Prime Bertrand Postulate — is the substantive content. It is:

- **Weaker than the twin-prime conjecture**, which predicts $\pi_2(x) \to \infty$ at a specific rate.
- **Stronger than bounded-gaps results** (Zhang 2013, Maynard 2013, Polymath 2014), which give infinitely many prime pairs of bounded gap but say nothing about twin density in dyadic intervals.
- **Unproven** — but verifiable by direct computation, and empirically very robust.

### 2.4 The Angle-Record Theorem

Formally, PG II proves the following **three-way equivalence**:

> The following are equivalent:
>
> (i) $\pi_2(2x) \ge \pi_2(x) + 1$ for every $x \ge 11$.
>
> (ii) $T_{k+1} < 2\,T_k$ for every $T_k \ge 11$.
>
> (iii) Every angle-record among consecutive prime pairs with $p_n \ge 3$ is a twin prime.

Each form is useful in a different context: (i) for analytic-number-theory framing, (ii) for direct computational check, (iii) for the geometric picture. The 2P-beats lemma is the bridge.

---

## 3. The Twin-Prime Bertrand Postulate in Practice

### 3.1 Verified to $10^{10}$

Sieving all primes up to $10^{10}$ produces $27{,}412{,}679$ twin primes. For every one of them with $T_k \ge 11$,

$$T_{k+1} < 2\, T_k.$$

The only exception at any scale is the earliest case, $T_1 = 3, T_2 = 5, T_3 = 11$: specifically $T_3 / T_2 = 11/5 = 2.2$, which violates the bound. Once we're past $T_k \ge 11$, no violation occurs across 27 million twins.

The ratio $r_k = T_{k+1}/T_k$ decays extraordinarily fast:

| scope | $\sup r_k$ | at $T_k$ |
|---|---|---|
| all twins | $2.2000$ | $5 \to 11$ |
| $T_k > 10^3$ | $1.0819$ | $1{,}319$ |
| $T_k > 10^6$ | $1.000711$ | $1{,}122{,}281$ |
| $T_k > 10^9$ | $1.000004$ | $1{,}029{,}693{,}209$ |

At $T_k > 10^9$ the worst-case ratio is within **4 parts per million** of 1. The "danger zone" for TPB is entirely below $T_k \approx 1000$; beyond that, the bound holds with absurd slack.

### 3.2 Verified geometrically

Independently, direct verification of the angle-record theorem: among all $440{,}312$ record-setting consecutive-prime-pairs with $p_n < 10^8$, exactly one — the initial $(2, 3)$ pair, with gap 1 — is not a twin. The remaining $440{,}311$ records are all twin primes. This is the geometric shadow of the density bound, and it's already striking as an empirical statement in its own right.

### 3.3 Near-misses

The pairs that came closest to violating $T_{k+1} < 2T_k$ (excluding the single $T_k = 5$ case) all live at small $T_k$:

| $T_k$ | $T_{k+1}$ | ratio |
|---|---|---|
| 17 | 29 | 1.7059 |
| 11 | 17 | 1.5455 |
| 41 | 59 | 1.4390 |
| 71 | 101 | 1.4225 |
| 29 | 41 | 1.4138 |
| 107 | 137 | 1.2804 |

After $T_k = 881$, not a single ratio across our dataset exceeds $1.1$. The top twenty ratios all occur at $T_k < 1000$.

---

## 4. The Generalized Bertrand Principle

### 4.1 Other constellations

Twins are the pair-constellation $\{0, 2\}$: pairs $(p, p+2)$ with both members prime. There are two other low-gap pair-constellations people have named:

- **Cousin primes** $\{0, 4\}$: pairs $(p, p+4)$ with both prime.
- **Sexy primes** $\{0, 6\}$: pairs $(p, p+6)$ with both prime.

By the Hardy–Littlewood prime-tuple conjecture, all three constellations have the same asymptotic density, $\sim 2 C_2 x / (\log x)^2$, up to combinatorial factors. So if twins satisfy a Bertrand-type bound, it's natural to ask whether cousins and sexy primes do too.

### 4.2 The empirical answer

Extending the same methodology to cousins and sexies (via a single segmented sieve to $10^{10}$, streaming out pairs for gaps 2, 4, and 6):

| constellation | count $\le 10^{10}$ | max ratio | $\sup r$ at $P > 10^9$ | violations of $r < 2$ | threshold $P^*$ |
|---|---|---|---|---|---|
| twin (gap 2) | $27{,}412{,}679$ | $2.2000$ | $1.000004$ | 1 (only $5 \to 11$) | $11$ |
| cousin (gap 4) | $27{,}409{,}999$ | $2.3333$ | $1.000004$ | 1 (only $3 \to 7$) | $7$ |
| sexy (gap 6) | $54{,}818{,}296$ | $1.5714$ | $1.000002$ | **0** | $5$ |

The pattern is striking:

- All three constellations obey the **same** uniform Bertrand bound $r < 2$, once small-$P$ exceptions are excluded.
- Each has a tiny effective threshold $P^*$ — at most the first few constellation members.
- The tails are essentially identical. At $P > 10^9$, the three suprema agree to within a factor of 2 of each other.
- The cousin count ($27{,}409{,}999$) matches the twin count ($27{,}412{,}679$) to four significant figures, exactly as Hardy–Littlewood predicts.

### 4.3 The principle

PG III states the resulting conjecture formally:

> **Generalized Bertrand Principle ($\mathrm{GBP}$).**
> For every admissible pair-constellation $\mathcal{C} = \{0, g\}$, there exists a threshold $P^*_{\mathcal{C}}$ such that
> $$\pi_\mathcal{C}(2x) - \pi_\mathcal{C}(x) \ge 1 \quad \text{for all } x \ge P^*_\mathcal{C}.$$

Equivalently: leading members of $\mathcal{C}$ satisfy $P^{\mathcal{C}}_{j+1} < 2\, P^{\mathcal{C}}_j$ once past $P^*_\mathcal{C}$.

### 4.4 Why is the factor 2 universal?

One way to see it: the dyadic interval $(x, 2x]$ is the universal Bertrand scale. Under Hardy–Littlewood, $\pi_\mathcal{C}(2x) - \pi_\mathcal{C}(x) \sim 2\mathfrak{S}(\mathcal{C})\, x / (\log x)^2 \to \infty$, regardless of the constellation. So if *any* admissible $\mathcal{C}$ satisfies the dyadic Bertrand bound, they all should, with the same factor.

A second way — more geometric — is via a **generalized 2P-beats lemma**. For two constellations $\mathcal{C} = \{0, g\}$ and $\mathcal{C}' = \{0, 2g\}$ (the "doubled companion"), a $\mathcal{C}'$-pair at $P$ beats a $\mathcal{C}$-pair at $Q$ in angle iff $P > 2Q$. The factor 2 here is universal in $g$ — independent of which gap you chose — because doubling the gap doubles the beat threshold.

So the factor 2 in $(\mathrm{GBP})$ matches the factor 2 in the Prime Triangle's doubled-gap geometry. That's either a deep connection or a numerical coincidence, depending on taste.

---

## 5. The Empirical Laws

Beyond the Bertrand bound itself, the data surfaced three empirical regularities worth noting.

### 5.1 The extreme-gap envelope

Across all three constellations, the maximum gap $G^{\mathcal{C}}_j = P^{\mathcal{C}}_{j+1} - P^{\mathcal{C}}_j$ grows roughly like $(\log P)^{3.2}$. Fitting the envelope

$$G^{\mathcal{C}}_j \;\lesssim\; C_\mathcal{C}\,(\log P^{\mathcal{C}}_j)^{\delta_\mathcal{C}}$$

separately for each constellation gives:

| constellation | $\delta_\mathcal{C}$ | $C_\mathcal{C}$ | $R^2$ |
|---|---|---|---|
| twin | $3.29$ | $0.165$ | $0.997$ |
| cousin | $3.22$ | $0.201$ | $0.996$ |
| sexy | $3.15$ | $0.151$ | $0.993$ |

The **exponents agree within $4.2\%$**: within the measurement range, there is a single asymptotic $\delta^* \approx 3.2$ shared across constellations. The constants $C_\mathcal{C}$ vary by ~29%, driven mostly by which small-$P$ pair happens to be the record-holder.

A pooled fit across all three constellations yields the **uniform envelope**:

$$G^{\mathcal{C}}_j \;<\; 0.171\,(\log P^{\mathcal{C}}_j)^{3.22} \qquad (R^2 = 0.982).$$

This is strictly stronger than $(\mathrm{GBP})$ (which is the weak condition $r_j \to 1$) but compatible with Hardy–Littlewood. The exponent $\delta \approx 3.2 > 2$ captures the *extreme* gap, not the typical one; HL predicts typical gap $\sim (\log P)^2$.

### 5.2 Overshoot growth

Define the per-decade overshoot

$$\Omega(T) = \frac{\max_{T_k \in \text{decade}} G_k}{(\log T_k^\star)^2},$$

where $T_k^\star$ is the argmax. Tabulating across decades $10^3$ through $10^9$:

| decade | $\max G_k$ | $(\log T)^2$ | $\Omega$ |
|---|---|---|---|
| $10^3$ | 210 | 75.3 | $2.79$ |
| $10^4$ | 630 | 121.9 | $5.17$ |
| $10^5$ | 1,452 | 186.4 | $7.79$ |
| $10^6$ | 1,722 | 259.5 | $6.64$ |
| $10^7$ | 2,868 | 338.2 | $8.48$ |
| $10^8$ | 4,770 | 414.7 | $11.50$ |
| $10^9$ | 6,030 | 491.9 | $12.26$ |

The overshoot factor has grown about $4\times$ across six decades. Fitting it to candidate growth laws:

- $\Omega \sim (\log T)^{1.43}$ — $R^2 = 0.913$
- $\log \Omega \sim (\log\log T)^{0.69}$ — $R^2 = 0.914$
- $\Omega \sim A + B\log\log T$ (Cramér–Granville form) — $R^2 = 0.896$

No single model dominates, but all of them point to the same conclusion: **extreme twin-prime gaps grow like $(\log T)^2$ times a slow overshoot factor**, of order $(\log\log T)^c$ with $c \approx 0.7$. This is the twin-prime analog of the Cramér–Granville phenomenon for ordinary primes.

### 5.3 The $\beta$ drift toward 2

A related observation: fit the *average* twin gap to $G_k \approx A (\log T_k)^\beta$ by ordinary least squares. At $10^9$, this gave $\beta \approx 1.866$, stable across fit ranges. At $10^{10}$, every fit band has drifted upward:

| fit range | $\beta$ at $10^9$ | $\beta$ at $10^{10}$ |
|---|---|---|
| $T_k > 10^3$ | $1.8633$ | $1.8865$ |
| $T_k > 10^5$ | $1.8659$ | $1.8872$ |
| $T_k > 10^7$ | $1.8664$ | $1.8889$ |
| $T_k > 10^9$ | — | $1.8957$ |

This is consistent with $\beta \to 2$ (the Hardy–Littlewood prediction) asymptotically, with slow finite-size corrections. When PG II's initial draft was written on $10^9$ data alone, $\beta$ looked stuck near $1.87$ and we entertained a "sub-HL" interpretation; the $10^{10}$ data made the drift visible and killed that interpretation. It is an instructive case of an empirical fit whose parameter value is itself a function of the range, and the lesson is to refit whenever the range expands.

---

## 6. Why Violations Live at Tiny $P$

The near-misses for the Bertrand bound — the pairs with ratio closest to 2 — are concentrated at small $P$, across every constellation studied. By $P > 881$, no ratio exceeds $1.1$ anywhere in the $10^{10}$ dataset.

The reason is a straightforward density argument. In a dyadic interval $(P, 2P]$, the expected number of $\mathcal{C}$-pairs under Hardy–Littlewood is

$$\text{Expected}_\mathcal{C}(P) \;\approx\; 2\mathfrak{S}(\mathcal{C})\, \frac{P}{(\log P)^2}.$$

For $P \sim 10^4$, this gives around $10$ expected twin pairs in $(P, 2P]$. By $P \sim 10^6$, the expected count is in the thousands. For a fluctuation to produce *zero* pairs in the interval — i.e., a violation of $(\mathrm{GBP})$ — the count would have to be more than $\sqrt{\text{Expected}}$ standard deviations below the mean, which is astronomically unlikely. The Cramér-style heuristic pegs the probability of such a fluctuation as exponentially small in the expected count.

At small $P$, the expected count is itself only a small number, so fluctuations can genuinely drive it to zero — and that's where the rare violations live. Once the expected count is comfortably above 1, violations stop.

This is why the problem is *easy* in a sense: the dyadic Bertrand bound is always expected to hold for any fixed admissible constellation once $P$ is large enough that Hardy–Littlewood's mean dominates its variance. It is *hard* in another sense: proving the statement unconditionally requires us to rule out all possible fluctuations, and current sieve methods don't extend that far.

---

## 7. The Data Story

### 7.1 What was actually computed

All results above come from direct computation. The pipeline:

1. **Sieve of Eratosthenes** — odd-only segmented sieve of the primes up to $10^{10}$. 455 million primes. Runs in about 5 minutes on a laptop.
2. **Streaming pair extraction** — in each segment, extract pairs $(p, p+g)$ with both prime, for $g \in \{2, 4, 6\}$, using a three-entry boundary buffer for cross-segment continuity.
3. **Ratio and envelope analysis** — for each constellation, compute $r_k = P_{k+1}/P_k$, find the sup on tails, fit envelopes, tabulate per-decade statistics.
4. **Angle-record verification** — for primes below $10^8$, walk through consecutive-prime pairs in order, track the running max of $\rho(p_n, p_{n+1}) = p_n/p_{n+1}$, and classify each record-setter.

### 7.2 Dataset inventory

Saved artifacts in `data/`:

| file | contents | size |
|---|---|---|
| `twins_1e10.npy` | 27.4M twin primes (smaller member, int64) | 219 MB |
| `cousins_1e10.npy` | 27.4M cousin primes | 219 MB |
| `sexy_1e10.npy` | 54.8M sexy primes | 439 MB |
| `angle_records_1e8.csv` | 440,312 record-setting pairs ($p_n < 10^8$) | 20 MB |
| `ratio_top20_1e10.csv` | Top 20 twin-prime ratios | 0.5 KB |
| `near_misses_1e10.csv` | All $r_k > 1.1$ cases | 0.4 KB |
| `decade_table_1e10.csv` | Per-decade overshoot data | 0.5 KB |
| `envelope_fits.csv` | $\delta, C, R^2$ per constellation | 0.3 KB |
| `constellation_ratios.csv` | Constellation summary | 0.3 KB |

### 7.3 How the structural patterns emerged

The progression was:

1. **PG I** (December 2025) introduced the Prime Triangle and its identities (notably $C_2^2 - C_1^2 = p_{n+2}^2 - p_n^2$ and the PSD factor) as a standalone geometric construction, with no number-theoretic claim.

2. Experimenting with angle records on the twin-prime sequence revealed that twins were the only record-setters (modulo $(2,3)$). That observation prompted the search for a density interpretation.

3. **PG II** (April 2026) formalized this as $(\mathrm{TPB})$ and verified it to $10^9$. The writing-up process identified the three-way equivalence (dyadic, ratio, angle-record) and positioned the conjecture between Zhang–Maynard and the full twin-prime conjecture.

4. Extending to $10^{10}$ didn't add anything qualitative for TPB, but shifted $\beta$ upward and gave us the $\sup r < 1.000004$ endpoint. This made the "β → 2" story visible.

5. Applying the same methodology to cousin and sexy primes took a single sieve pass (355 seconds) and delivered the punchline: **the same uniform $r < 2$ bound works for all three constellations, with tiny exceptions at small $P$**. This is PG III's headline.

6. A uniform envelope fit across all three constellations ($R^2 = 0.98$) closed the loop and gave a data-driven refinement that is strictly stronger than $(\mathrm{GBP})$.

The whole pipeline — from raw sieve to PG III's final claims — fits in about 900 lines of Python.

---

## 8. What's Open

### 8.1 Unconditional proof

$(\mathrm{GBP})$, let alone the refined envelope conjecture, is not known unconditionally for any admissible constellation. It sits strictly above the current state of the art:

- **Bounded-gaps results** (Zhang 2013, Maynard 2013, Polymath8 2014) give infinitely many prime pairs of gap $\le 246$, but say nothing about density in dyadic intervals.
- **Short-interval results** (Heath-Brown, Friedlander–Iwaniec, and others) give $\pi_2(x + y) - \pi_2(x) > 0$ for $y \ge x^{1 - \delta}$ under various hypotheses, but the dyadic scale $y = x$ is beyond reach unconditionally.

To our knowledge, $(\mathrm{TPB})$ and its generalization $(\mathrm{GBP})$ have not been stated explicitly as named targets in the literature; this was a small surprise from the literature search and may represent a gap worth filling.

### 8.2 Conditional proof

Under the Hardy–Littlewood prime-tuple conjecture, $(\mathrm{GBP})$ follows for every admissible $\mathcal{C}$ for all sufficiently large $x$. The argument is a direct density estimate: HL gives

$$\pi_\mathcal{C}(2x) - \pi_\mathcal{C}(x) \sim 2\mathfrak{S}(\mathcal{C}) \cdot \frac{x}{(\log x)^2} \to \infty,$$

and once this asymptotic count exceeds 1 (which happens at an effective $x_0(\mathcal{C})$), the dyadic bound holds. Combining with our direct verification up to $10^{10}$ closes the small-$x$ gap, *provided* $x_0$ can be bounded above by $10^{10}$ for each constellation — a routine explicit-constant exercise in HL-conditional number theory.

So one has, conditionally, a complete proof of $(\mathrm{GBP})$ for twins, cousins, and sexy primes. This is a near-term paper in its own right.

### 8.3 Sieve-theoretic attack

A more ambitious direction: can the Maynard multi-dimensional sieve, originally designed to produce bounded-gaps results, be adapted to give a dyadic-scale density statement? The sieve already produces many primes in short intervals; the question is whether enough control exists to guarantee at least one twin pair (or one $\mathcal{C}$-pair) in every dyadic interval past a computable threshold.

This would require:
1. An explicit short-interval form of the Maynard sieve down to scale $y = x$.
2. A quantitative lower bound that survives to any fixed $\mathcal{C}$-pair constellation.

The first ingredient is partially present in existing work; the second would need new analysis. This is the direction with the highest potential payoff — it would give the first unconditional proof of a twin-prime density statement in dyadic intervals.

### 8.4 Extensions

Several directions generalize naturally:

- **Triples and $k$-tuples.** The natural analog is $(0, h_1, \ldots, h_{k-1})$ admissible and dyadic density for the leading member. The singular series becomes more delicate, but the dyadic density argument carries over.
- **Larger pair constellations.** Gap-8, gap-10, etc. are routine. The universal factor 2 almost certainly persists; the small-$P$ threshold $P^*_{\mathcal{C}}$ grows slowly with $g$.
- **Random models.** For Cramér-type random-prime models, what's the expected distribution of near-miss ratios? A probabilistic calculation should predict the "danger zone" below $P \sim 1000$ we observe empirically, and give expected sup-$r$ as a function of $T_\min$.
- **Other geometric constructions.** The Prime Triangle is one of many possible constructions. Are there geometric quantities — beyond the angle — whose records encode other density statements? PG I's PSD factor, curvature, and angle-drift are candidates waiting for their own empirical exploration.

### 8.5 Summary

We have a conjecture $(\mathrm{GBP})$ that is:

- **Geometrically motivated** (Prime Triangle angle-records).
- **Empirically robust** (verified to $10^{10}$ across three constellations).
- **Structurally clean** (equivalent dyadic, ratio, and angle-record forms).
- **Stated at the right level of generality** (every admissible pair-constellation).
- **Plausibly provable under HL** (immediate density argument).
- **Unconditionally open**, and apparently unstudied in this exact form in the prior literature.

That is a pleasant spot to be in.

---

## Appendix: Reproducibility

All computations reproduce from scripts in `scripts/`:

| script | purpose |
|---|---|
| `pg_twin_angle_analysis.py` | Twin sieve to $10^9$, angle-record verification to $10^8$, initial fits |
| `pg_extend_1e10.py` | Full sieve to $10^{10}$, decade tables, $\beta$ fits |
| `pg_structural_1e10.py` | Cousin + sexy extraction, overshoot fits, refined envelope |
| `pg_envelope_fits.py` | Per-constellation envelope fits, uniform pooled fit |

Outputs land in `data/` (numerical artifacts) and `results/` (markdown summaries).

Papers in `papers/`:

- `PG_I_Triangle.tex` — (from earlier work) Prime Triangle construction and identities.
- `PG_II_AngleRecord.tex` / `.pdf` — Twin-Prime Bertrand Postulate and Angle-Record Theorem.
- `PG_III_GBP.tex` / `.pdf` — Generalized Bertrand Principle for constellations.

---

*End of Field Guide.*
