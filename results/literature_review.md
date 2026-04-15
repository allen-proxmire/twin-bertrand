# Literature Review on Dyadic Density of Prime Constellations

*Prepared in support of PG II / PG III · April 2026*

---

## Executive Summary

The dyadic inequality $\pi_2(2x) - \pi_2(x) \ge 1$ (TPB) and its generalization $\pi_\mathcal{C}(2x) - \pi_\mathcal{C}(x) \ge 1$ (GBP) **do not appear explicitly in the searched literature as named conjectures for twin primes or prime constellations**. However, they sit inside a well-developed framework — the **Ramanujan-prime framework** — that has been extensively studied for ordinary primes but not, in the exact form we propose, for constellations.

The three most relevant bodies of work are:

1. **Ramanujan primes** (Ramanujan 1919; Sondow 2009 and subsequent). These are the explicit thresholds for $\pi(x) - \pi(x/2) \ge n$, i.e., the ordinary-prime dyadic density version of Bertrand's postulate. The framework exists but is applied to ordinary primes, not to twin primes.
2. **Bounded-gaps machinery** (Zhang 2013; Maynard 2013; Polymath8 2014). Produces infinitely many prime pairs of gap $\le 246$ but says nothing about twin density in dyadic intervals.
3. **Short-interval results for twin primes** (Heath-Brown 1983; Jia; Mikawa; others). Conditional estimates for $\pi_2(x+y) - \pi_2(x) > 0$ at scales $y \ge x^{1-\delta}$, but not at the dyadic scale $y = x$.

The ratio form $T_{k+1} < 2 T_k$ and the geometric angle-record equivalence are, to the best of our knowledge, new.

---

## 1. The Ramanujan-Prime Framework (closest prior art)

### 1.1 Ramanujan's original theorem (1919)

Ramanujan proved that the function $\pi(x) - \pi(x/2)$ is eventually $\ge n$ for every fixed $n \ge 1$, and defined the **$n$-th Ramanujan prime** $R_n$ as the smallest integer satisfying
$$\pi(x) - \pi(x/2) \ge n \quad \text{for all } x \ge R_n.$$

- $R_1 = 2$ (this is Bertrand's postulate itself).
- $R_2 = 11$, $R_3 = 17$, $R_4 = 29$, $R_5 = 41$, ...

**OEIS:** [A104272](https://oeis.org/A104272). The Ramanujan primes form a proper subsequence of the primes.

### 1.2 Sondow (2009)

Sondow [[arXiv:0907.5232](https://arxiv.org/abs/0907.5232)] established the asymptotic $R_n \sim p_{2n}$ (twice the $n$-th prime), proved elementary upper and lower bounds, and initiated the modern study of $R_n$. This is *"Ramanujan Primes and Bertrand's Postulate"* — explicitly framing Ramanujan's inequality as a refined Bertrand postulate.

### 1.3 Generalizations of Ramanujan primes

Several generalizations exist, all for **ordinary primes**:

- **$c$-Ramanujan primes** [Amersi, Beckwith, Miller, Ronan, Sondow, 2014]: for $c \in (0, 1)$, $R_{c,n}$ is the smallest $R$ such that $\pi(x) - \pi(cx) \ge n$ for all $x \ge R$. [[paper](https://web.williams.edu/Mathematics/sjmiller/public_html/math/papers/Amersi-Miller-CANT2011arxiv.pdf)]
- **Derived Ramanujan primes** [Paksoy, 2012]: iterated applications of the Ramanujan construction. [[arXiv:1210.6991](https://arxiv.org/pdf/1210.6991)]
- **Shevelev–Greathouse–Moses (2013)** [[arXiv:1212.2785](https://arxiv.org/abs/1212.2785)]: characterized the set of $k$ for which every interval $(kn, (k+1)n)$ contains a prime for all $n > 1$. The set is exactly $\{1, 2, 3, 5, 9, 14\}$ (to $n \le 10^8$). This is a direct generalization of Bertrand's postulate to other interval shapes.

### 1.4 What's missing: Ramanujan primes for constellations

None of the above work considers the twin-prime analog: the **smallest $R^{\mathrm{twin}}_n$ such that $\pi_2(x) - \pi_2(x/2) \ge n$ for all $x \ge R^{\mathrm{twin}}_n$**. The "twin Ramanujan primes" studied by Sondow–Nicholson–Noe [[JIS 2011](https://cs.uwaterloo.ca/journals/JIS/VOL14/Noe/noe12.pdf), [arXiv:1105.2249](https://arxiv.org/abs/1105.2249)] are instead **Ramanujan primes that happen to be twin primes** — a different object.

Our $(\mathrm{TPB})$ states $R^{\mathrm{twin}}_1 \le 11$ (equivalently, the dyadic inequality holds for $x \ge 11$). Computing $R^{\mathrm{twin}}_n$ for $n \ge 2$ from our dataset is a natural direct extension and, as far as we can tell, has not been done before.

---

## 2. Bounded-Gaps Machinery (orthogonal)

### 2.1 Zhang, Maynard, Polymath

- **Zhang (2013)** [*Annals of Math* 179]: $\liminf(p_{n+1} - p_n) < 7 \times 10^7$.
- **Maynard (2013)** [*Annals of Math* 181]: Independent proof, simpler sieve, $\liminf \le 600$.
- **Polymath8a/8b**: Reduced the bound to $246$ unconditionally, $12$ under Elliott–Halberstam, $6$ under generalized EH.

**What these results say:** There are infinitely many prime pairs $(p_n, p_{n+m})$ with $p_{n+m} - p_n \le 246$, for some $m$.

**What they do NOT say:** That such a pair appears in every dyadic interval $(x, 2x]$.

The existence statement is scale-invariant only in the weak sense "at arbitrarily large scales"; it provides no lower bound on the frequency of such pairs in a particular interval. In particular, $(\mathrm{TPB})$ is **not implied** by any current bounded-gaps result.

### 2.2 Pintz (2014): ratios of consecutive prime gaps

Pintz [[arXiv:1406.2658](https://arxiv.org/abs/1406.2658)] proved that the ratio $(p_{n+1} - p_n)/(p_n - p_{n-1})$ takes both arbitrarily large and arbitrarily small values infinitely often, answering a 60-year-old question of Erdős. This concerns **consecutive gaps** (not twin primes specifically) and does not address dyadic density.

---

## 3. Short-Interval Twin-Prime Results

### 3.1 Heath-Brown and Siegel zeros

Heath-Brown (1983) [*Proc LMS*] proved:

> If there are infinitely many Siegel zeros, then there are infinitely many twin primes.

Discussed in [Tao's blog](https://terrytao.wordpress.com/2015/08/26/heath-browns-theorem-on-prime-twins-and-siegel-zeroes/). This is a conditional short-interval result of a different flavor: it produces twin primes from a hypothetical zero-configuration, not a dyadic count.

### 3.2 Tao–Teräväinen and successors

Tao & Teräväinen [[IMRN 2023](https://academic.oup.com/imrn/article/2023/23/20337/7111993)]: *"Siegel Zeros, Twin Primes, Goldbach's Conjecture, and Primes in Short Intervals."* Strengthens and unifies Heath-Brown-type conditional connections between Siegel zeros and twin-prime existence, again at large but unspecified scales rather than dyadic.

### 3.3 Friedlander–Iwaniec, Mikawa, Jia

These authors have produced short-interval results of the form
$$\pi_2(x + y) - \pi_2(x) > 0 \quad \text{for } y \ge x^{1-\delta}$$
under various hypotheses (GRH, averaged Elliott–Halberstam). The gap from $y = x^{1-\delta}$ (some $\delta > 0$) to $y = x$ (dyadic scale) is fundamental and has not been closed unconditionally.

### 3.4 Matomäki and recent work

Matomäki et al. [[*JLMS* 2022](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/jlms.12592)]: *"Almost primes in almost all very short intervals."* Establishes existence of products of at most two primes in short intervals of length $\sim \log^c X$ for almost all positions. Does not give twin primes.

---

## 4. Explicit Sieve Bounds on $\pi_2$

Brun-sieve and Selberg-sieve upper bounds give $\pi_2(x) \le C x/(\log x)^2$ for explicit $C$. The state of the art:
- Selberg sieve: $\pi_2(x) \le 8.2 x/(\log x)^2$ for $x \ge 2$ (various authors).
- Under GRH, Bordignon-Starichkova-Johnston (2024) [[Bull AMS](https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/improved-upper-bound-on-bruns-constant-under-grh/47DDCC2EB96C56B3F009DC9AA173CD72)] improve Brun's constant bounds.

**These are upper bounds only.** No explicit *lower* bound of the form $\pi_2(2x) - \pi_2(x) \ge 1$ is known unconditionally past direct computation.

---

## 5. Cousin and Sexy Primes

Cousin primes $(p, p+4)$ and sexy primes $(p, p+6)$ are catalogued in:
- Cousin primes: [OEIS A023200](https://oeis.org/A023200).
- Sexy primes: [OEIS A023201](https://oeis.org/A023201).
- Admissible prime constellations tables: [Oliveira e Silva](https://sweet.ua.pt/tos/apc.html).

No published paper isolates the dyadic inequality $\pi_\mathcal{C}(2x) - \pi_\mathcal{C}(x) \ge 1$ for these constellations either. HL predicts the asymptotic count
$$\pi_\mathcal{C}(2x) - \pi_\mathcal{C}(x) \sim 2 \mathfrak{S}(\mathcal{C}) \, x / (\log x)^2,$$
which trivially goes to infinity, implying the dyadic bound for large $x$ conditionally on HL. The explicit form with a named threshold $P^*_\mathcal{C}$ is new.

---

## 6. Does TPB / GBP appear in the literature?

**Short answer: No, not in the exact form we state.**

| Form | Appears explicitly? | Most similar prior work |
|---|---|---|
| $\pi_2(2x) - \pi_2(x) \ge 1$ for $x \ge 11$ | No | Ramanujan primes for $\pi$ (not $\pi_2$) |
| $T_{k+1} < 2 T_k$ for $T_k \ge 11$ | No | — |
| Angle-record theorem (PG II) | No | — |
| $\pi_\mathcal{C}(2x) \ge \pi_\mathcal{C}(x) + 1$ (GBP) | No | — |
| Cousin/sexy Bertrand bound | No | — |

**Closest precedents:**
1. **Ramanujan's theorem** — the ordinary-prime version; conceptually the parent.
2. **Shevelev–Greathouse–Moses** — explicit Bertrand-like bounds for various interval ratios, still for ordinary primes.
3. **Short-interval twin-prime papers** — estimate $\pi_2$ in intervals but not at dyadic scale.

The "dyadic density of admissible pair-constellations" framing we use is at a spot nobody seems to have occupied.

---

## 7. Conditional Status

Under Hardy–Littlewood, $(\mathrm{GBP})$ is immediate for all admissible $\mathcal{C}$: the expected count $\sim 2\mathfrak{S}(\mathcal{C}) x / (\log x)^2$ diverges, so the dyadic count eventually exceeds 1. An explicit $x_0(\mathcal{C})$ can be extracted from any quantitative HL-type hypothesis with explicit error bounds.

Under GRH alone, short-interval results for primes exist but do not immediately transfer to twin primes at dyadic scale.

Under Elliott–Halberstam, the Maynard–Polymath apparatus gets closer but still does not yield dyadic density for any specific constellation.

---

## 8. Gaps and Opportunities

1. **The $R^{\mathrm{twin}}_n$ sequence.** The natural analog of Ramanujan primes for twins is $R^{\mathrm{twin}}_n =$ smallest $R$ such that $\pi_2(x) - \pi_2(x/2) \ge n$ for all $x \ge R$. Our computation already gives $R^{\mathrm{twin}}_1 = 11$. Computing $R^{\mathrm{twin}}_n$ for $n = 2, 3, 4, \ldots$ from the $10^{10}$ dataset is a 10-line script. This is a clean new sequence worth contributing to OEIS.

2. **A conditional-HL proof of TPB.** Straightforward; nobody has written it down because nobody has stated TPB. A short note establishing this (and then extending to GBP) is a plausible first publication.

3. **A Maynard-style unconditional proof of a weaker version.** Instead of "at least one pair of gap $\le 246$ in every $(x, 2x]$," one might try "at least one pair of gap $\le B$ in every $(x, 2x]$ past a computable $x_0$" for some $B$. This would sit between current bounded-gaps results and TPB, and is a reasonable sieve-theoretic target.

4. **Cousin/sexy Ramanujan analog.** Similarly define $R^{\mathrm{cousin}}_n$ and $R^{\mathrm{sexy}}_n$. Our data gives the $n=1$ values directly ($P^*_{\{0,4\}} = 7$, $P^*_{\{0,6\}} = 5$).

5. **Angle-record theorem in other constructions.** Whether other geometric constructions (beyond the Prime Triangle) also encode density statements via their record structure is open.

---

## 9. Implications for PG II / PG III Framing

### Required edits (honesty)

1. **PG II §7 (Related Work) should cite Ramanujan primes as the conceptual parent.** The current draft mentions HL and bounded-gaps but omits the Ramanujan framework entirely. This is the single most important omission.

2. **PG II's claim that TPB "has not been articulated explicitly as a conjecture"** is defensible but should be tightened to: *"while the Ramanujan-prime framework (Ramanujan 1919, Sondow 2009 et seq.) establishes the analogous dyadic density bound for ordinary primes, the extension to twin primes and admissible pair-constellations has not, to our knowledge, been explicitly stated."*

3. **PG III §7 (Related Work — to be added).** Should include the same Ramanujan-prime contextualization. The $c$-Ramanujan generalization of Amersi et al. is a particularly natural reference point: they vary $c$ in $(cx, x]$ for fixed ordinary-prime counting; we vary constellation $\mathcal{C}$ for fixed dyadic $(x/2, x]$.

### Strategic opportunity

Frame TPB and GBP as the "**Ramanujan-prime analog for admissible pair-constellations.**" This:
- Gives the work a clean intellectual heritage.
- Makes the novelty claim more precise and more defensible.
- Suggests a natural extension (compute $R^\mathcal{C}_n$ for $n \ge 2$ across constellations).
- Positions the paper within an existing, active line of research.

### Recommended new sequence

Add to PG II an appendix defining
$$R^\mathrm{twin}_n = \min\{R : \pi_2(x) - \pi_2(x/2) \ge n \text{ for all } x \ge R\}$$
and compute $R^\mathrm{twin}_n$ for $n = 1, 2, 3, \ldots$ up to as large as the $10^{10}$ data permits. Submit the sequence to OEIS. This is a clean deliverable, gives the paper a unique named object, and immediately connects to the Ramanujan-prime literature.

---

## 10. Summary of Prior Work Positioning

```
Ramanujan 1919:       π(x) - π(x/2) ≥ 1  for ordinary primes, x ≥ 2  (Bertrand)
                      π(x) - π(x/2) ≥ n  for ordinary primes, x ≥ R_n  (Ramanujan's theorem)

Sondow 2009:          Asymptotics & elementary bounds for R_n
Sondow-Nicholson-Noe: Twin primes WITHIN the R_n sequence
Amersi et al 2014:    c-Ramanujan:  π(x) - π(cx) ≥ n  for ordinary primes, x ≥ R_{c,n}
Shevelev et al 2013:  π((k+1)n) - π(kn) ≥ 1 for ordinary primes, n ≥ N_k, k ∈ {1,2,3,5,9,14}

Zhang 2013:           liminf of gaps between ordinary primes ≤ 7×10^7
Maynard 2013, Polymath: ≤ 246 unconditionally

Heath-Brown 1983:     Siegel zeros ⇒ ∞-many twin primes
Tao-Teräväinen 2023:  refined conditional Siegel/twin connections

Friedlander, Iwaniec, Mikawa, Jia:  short-interval π_2 estimates at scale x^{1-δ}

————————————————————————————————————
PG II (this work):    π_2(x) - π_2(x/2) ≥ 1  for twin primes, x ≥ 11  (TPB)  [NEW]
PG III (this work):   π_C(x) - π_C(x/2) ≥ 1  for admissible C, x ≥ P*_C  (GBP)  [NEW]
                      Angle-record geometric equivalence  [NEW]
```

The bottom two rows are unstaked territory.

---

## Sources

- [Bertrand's postulate — Wikipedia](https://en.wikipedia.org/wiki/Bertrand%27s_postulate)
- [Ramanujan prime — Wikipedia](https://en.wikipedia.org/wiki/Ramanujan_prime)
- [Sondow (2009), arXiv:0907.5232](https://arxiv.org/abs/0907.5232)
- [Amersi-Beckwith-Miller-Ronan-Sondow, Generalized Ramanujan Primes](https://web.williams.edu/Mathematics/sjmiller/public_html/math/papers/Amersi-Miller-CANT2011arxiv.pdf)
- [Paksoy, Derived Ramanujan Primes, arXiv:1210.6991](https://arxiv.org/pdf/1210.6991)
- [Sondow-Nicholson-Noe, Ramanujan Primes: Bounds, Runs, Twins, and Gaps, arXiv:1105.2249](https://arxiv.org/abs/1105.2249)
- [Shevelev-Greathouse-Moses (2013), arXiv:1212.2785](https://arxiv.org/abs/1212.2785)
- [Pintz, On the ratio of consecutive gaps, arXiv:1406.2658](https://arxiv.org/abs/1406.2658)
- [Polymath Wiki — Bounded gaps between primes](https://michaelnielsen.org/polymath/index.php?title=Bounded_gaps_between_primes)
- [Tao blog — Heath-Brown's theorem on prime twins and Siegel zeros](https://terrytao.wordpress.com/2015/08/26/heath-browns-theorem-on-prime-twins-and-siegel-zeroes/)
- [Tao-Teräväinen IMRN 2023](https://academic.oup.com/imrn/article/2023/23/20337/7111993)
- [Matomäki et al. JLMS 2022 — Almost primes in almost all very short intervals](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/jlms.12592)
- [OEIS A104272 — Ramanujan primes](https://oeis.org/A104272)
- [OEIS A001359 — Lesser of twin primes](https://oeis.org/A001359)
- [OEIS A023200 — Cousin primes](https://oeis.org/A023200)
- [OEIS A023201 — Sexy primes](https://oeis.org/A023201)
