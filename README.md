# Twin Bertrand

A conjectural dyadic-density inequality for twin primes, its geometric equivalent via the Prime Triangle construction, and a generalization to admissible prime constellations.

**Author:** Allen Proxmire · April 2026

---

## What's here

The repo contains three short papers, a field guide, reproducible scripts, and the derived data (excluding a few large `.npy` files that can be regenerated in minutes).

### The central conjecture — Twin-Prime Bertrand Postulate (TPB)

$$\pi_2(2x) - \pi_2(x) \ge 1 \qquad \text{for all } x \ge 11$$

where

$$\pi_2(2x)$$ - #{ 𝑝≤𝑥:𝑝 and 𝑝+2 are both prime }

is the twin-prime counting function. This asserts that every dyadic interval $(x, 2x]$ past $x = 11$ contains at least one twin prime.
Equivalent formulations:

1. **Ratio form:** $T_{k+1} < 2T_k$ for every twin prime $T_k \ge 11$.
2. **Geometric form:** every angle-record of the Prime Triangle sequence with $p_n \ge 3$ is a twin prime.
3. **Ramanujan-analog form:** $R^{\mathrm{twin}}_1 = 11$, where $R^{\mathrm{twin}}_n$ is the twin-prime analog of Ramanujan's classical $R_n$.

TPB is **verified to $x \le 10^{10}$** across $27{,}412{,}679$ twin primes, with exactly one exception at any scale — the trivial $(5,7) \to (11,13)$. Its generalization to cousin primes $(p, p+4)$ and sexy primes $(p, p+6)$ — the **Generalized Bertrand Principle (GBP)** — is also verified across all three constellations in the same range.

### Logical position

$$\underbrace{\text{twin-prime conjecture}}_{\pi_2(x) \to \infty}
\;\supset\;
\underbrace{\text{TPB}}_{\pi_2(2x) \ge \pi_2(x) + 1}
\;\supset\;
\underbrace{\text{bounded gaps}}_{\liminf(p_{n+1} - p_n) < \infty}$$

TPB is strictly weaker than the twin-prime conjecture and strictly stronger than the Zhang–Maynard bounded-gaps theorems. Under Hardy–Littlewood it is immediate; unconditionally it is open.

---

## Papers

| file | pages | content |
|---|---|---|
| [`papers/PG_I_PrimeTriangle.tex`](papers/PG_I_PrimeTriangle.tex) | 8 | The Prime Triangle construction, identities (PSD factor, $C_2^2 - C_1^2 = p_{n+2}^2 - p_n^2$), derived invariants (energy, curvature, angle drift), and the $2P$-beats lemma as the hinge to dyadic density. |
| [`papers/PG_II_AngleRecord.tex`](papers/PG_II_AngleRecord.tex) | 10 | Statement and proof of TPB equivalences, conditional proof under HL, empirical verification to $10^9$, and introduction of the twin-Ramanujan sequence $R^{\mathrm{twin}}_n$. |
| [`papers/PG_III_GBP.tex`](papers/PG_III_GBP.tex) | 9 | Generalized Bertrand Principle for admissible pair-constellations; verified for twins, cousins, and sexy primes to $10^{10}$; uniform envelope fit $G < 0.171(\log P)^{3.22}$. |

Compiled PDFs are committed alongside.

### Field guide

[`PG_FieldGuide.md`](PG_FieldGuide.md) — a ~12-page prose narrative of the whole program, aimed at a mathematically literate reader who hasn't read the three papers. Use this as the front door.

---

## Data

See [`data/README.md`](data/README.md). Small CSV tables are committed; large `.npy` arrays (27M twins, 27M cousins, 55M sexy-prime pairs) are not — they regenerate from the scripts in ~5 minutes.

## Scripts

See [`scripts/README.md`](scripts/README.md). All results reproduce end-to-end from four Python scripts using only NumPy.

## Results

See [`results/README.md`](results/README.md) for the standalone markdown reports (empirical summary, constellation comparisons, envelope fits, twin-Ramanujan report, literature review).

---

## Key empirical findings (to $10^{10}$)

| claim | status |
|---|---|
| TPB verified for $x \in [11, 10^{10}]$ | 0 exceptions in 27.4M twins |
| GBP verified for cousins, sexy primes | 0 exceptions past tiny small-$P$ cases |
| Angle-record theorem: every record with $p_n \ge 3$ is a twin | verified for $p_n < 10^8$ (440,311 of 440,312 records) |
| Twin-gap envelope: $G_k < 0.171(\log P)^{3.22}$ | pooled fit $R^2 = 0.982$ across constellations |
| Overshoot $\max G / (\log T)^2$ grows as $(\log T)^{1.4}$ | Cramér–Granville analog |
| Average-gap exponent $\beta$ drifting toward HL value 2 | 1.866 at $10^9 \to 1.896$ at $10^{10}$ |

## Open problems

1. **Unconditional proof of TPB.** Conjecturally follows from Hardy–Littlewood (see PG II §5). An unconditional proof likely needs a sieve-theoretic adaptation of the Maynard multi-dimensional sieve to the dyadic short-interval regime.
2. **Asymptotic exponent.** Does the twin-gap exponent $\beta$ converge exactly to 2? Needs data past $10^{11}$.
3. **OEIS submission of $R^{\mathrm{twin}}_n$.** The twin-Ramanujan sequence (11, 59, 101, 149, 179, …) is a candidate new entry; draft and first $10^6$ values are in `data/twin_ramanujan_primes.csv`.

## Citation

If you use any of this work:

```
A. Proxmire. Prime Geometry I–III: The Prime Triangle, Twin-Prime Bertrand Postulate, and Generalized Bertrand Principle. 2026.
https://github.com/allen-proxmire/twin-bertrand
```

## License

CC BY 4.0 for the papers and text; MIT for the scripts.
