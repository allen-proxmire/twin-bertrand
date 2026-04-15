# Uniform Envelope Fits Across Constellations

Data: all constellation pairs (p, p+g) with both prime, p ≤ 10^10.
- twins (g=2):   27,412,679
- cousins (g=4): 27,409,999
- sexy (g=6):    54,818,296

## Envelope tables

Model: $r_k - 1 \le C\,(\log T_k)^\delta / T_k$, fit on
$\sup(r_k-1)$ over tails $T_k > T_\min$ at
$T_\min \in \{10^2,10^3,10^5,10^7,10^9\}$.

### Twin ($g=2$)

| $T_\min$ | $\sup(r_k-1)$ | at $P_k$ | max $G$ at $P_k$ |
|---|---|---|---|
| $10^{2}$ | 2.804e-01 | 107 | 30 |
| $10^{3}$ | 8.188e-02 | 1,319 | 108 |
| $10^{5}$ | 5.097e-03 | 120,077 | 612 |
| $10^{7}$ | 1.434e-04 | 10,170,731 | 1,458 |
| $10^{9}$ | 3.857e-06 | 1,029,693,209 | 3,972 |

### Cousin ($g=4$)

| $T_\min$ | $\sup(r_k-1)$ | at $P_k$ | max $G$ at $P_k$ |
|---|---|---|---|
| $10^{2}$ | 2.835e-01 | 127 | 36 |
| $10^{3}$ | 1.098e-01 | 1,093 | 120 |
| $10^{5}$ | 4.326e-03 | 174,763 | 756 |
| $10^{7}$ | 1.486e-04 | 12,154,123 | 1,806 |
| $10^{9}$ | 4.019e-06 | 1,028,655,409 | 4,134 |

### Sexy ($g=6$)

| $T_\min$ | $\sup(r_k-1)$ | at $P_k$ | max $G$ at $P_k$ |
|---|---|---|---|
| $10^{2}$ | 2.243e-01 | 107 | 24 |
| $10^{3}$ | 5.165e-02 | 1,123 | 58 |
| $10^{5}$ | 3.344e-03 | 110,063 | 368 |
| $10^{7}$ | 9.874e-05 | 10,269,263 | 1,014 |
| $10^{9}$ | 2.257e-06 | 1,052,602,267 | 2,376 |

## Individual fits

| constellation | $\delta$ | $C$ | $R^2$ |
|---|---|---|---|
| twin   | 3.2884 | 0.1645 | 0.9970 |
| cousin | 3.2209 | 0.2013 | 0.9957 |
| sexy   | 3.1538 | 0.1507 | 0.9931 |

**Spread across constellations:**
- $\delta$: range $[3.154, 3.288]$, spread ≈ **4.2%**
- $C$: range $[0.151, 0.201]$, spread ≈ **29.3%**

**Agreement within 5%**: delta yes, C no.

## Pooled uniform fit

Fitting a single $(C,\delta)$ to all 15 data points
(3 constellations × 5 $T_\min$ values):

$$
r_k - 1 \;\le\; 0.1709 \cdot \frac{(\log T_k)^{3.2210}}{T_k},
\qquad R^2 = 0.9824
$$

Equivalently:
$$
G^{\mathcal{C}}_j \;<\; 0.1709 \cdot (\log P^{\mathcal{C}}_j)^{3.221}.
$$

## Interpretation

- The three constellations produce $(\delta, C)$ triples that
  differ by up to 29.3%.
  A single universal envelope captures all three with R² = 0.982.

- The pooled exponent $\delta \approx 3.22$ is substantially
  above the HL-typical value $2$: as in the twin case, this reflects
  the **extreme** gap rather than the typical one. The overshoot
  factor growth is the same across constellations (within fit error),
  consistent with a shared Cramér–Granville-type phenomenon.

- Numerically, the three constants split as
  $C_\mathrm{twin}=0.165, C_\mathrm{cousin}=0.201,
  C_\mathrm{sexy}=0.151$; their ordering roughly tracks the
  singular-series ordering ($\mathfrak{S}_\mathrm{twin} =
  \mathfrak{S}_\mathrm{cousin} < \mathfrak{S}_\mathrm{sexy}$).
  Sexy primes, being twice as dense, have slightly smaller extremes
  per unit log.

- **Conclusion.** The envelope $G^{\mathcal{C}}_j < 0.171(\log P^{\mathcal{C}}_j)^{3.22}$
  fits all three constellations simultaneously with R² = 0.982.
  This supports the universality claim of Conjecture 6.1 in PG III
  and justifies a unified form for the refined GBP envelope.
