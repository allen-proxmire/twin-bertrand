# papers/

The three-part PG series. LaTeX source plus compiled PDFs.

## Contents

| file | pages | compile with |
|---|---|---|
| [`PG_I_PrimeTriangle.tex`](PG_I_PrimeTriangle.tex) | 8 | `pdflatex PG_I_PrimeTriangle.tex` |
| [`PG_II_AngleRecord.tex`](PG_II_AngleRecord.tex) | 10 | `pdflatex PG_II_AngleRecord.tex` |
| [`PG_III_GBP.tex`](PG_III_GBP.tex) | 9 | `pdflatex PG_III_GBP.tex` |

Each is a self-contained `\documentclass{article}` using only `amsmath`, `amssymb`, `amsthm`, `booktabs`, `hyperref` — no custom style files. Single-pass `pdflatex` produces clean output; no bibtex needed (each `.tex` has an inline `thebibliography`).

## Reading order

**PG I** establishes the geometric construction (Prime Triangle, angle $\alpha$, derived invariants) and states the $2P$-beats lemma as the hinge to the later dyadic-density content.

**PG II** states the Twin-Prime Bertrand Postulate, proves the three-way equivalence (dyadic / ratio / angle-record), gives a conditional proof under Hardy–Littlewood, documents the empirical verification to $10^9$, and introduces the twin-Ramanujan prime sequence $R^{\mathrm{twin}}_n$ (with $R^{\mathrm{twin}}_1 = 11$).

**PG III** generalizes to admissible pair-constellations via the Generalized Bertrand Principle, verifies it for twins, cousins, and sexy primes to $10^{10}$, and establishes a uniform envelope $G < 0.171(\log P)^{3.22}$.

## Style

All three papers use identical preambles and shared notation:

- $\rho(p, q) = p/q$, the closeness-to-$45°$ proxy
- $\alpha(p, q) = \arctan(p/q)$, the Prime Triangle angle
- $\pi_\mathcal{C}(x)$, the constellation-counting function
- $R^{\mathcal{C}}_n$, the constellation-Ramanujan prime sequence
- $T_k$, the ordered sequence of twin primes (smaller members)

## Compiling

Requires a standard LaTeX distribution (MiKTeX, TeX Live, MacTeX). No external packages beyond the standard ones listed above.

```bash
cd papers/
pdflatex PG_I_PrimeTriangle.tex
pdflatex PG_II_AngleRecord.tex
pdflatex PG_III_GBP.tex
```

A single pass is sufficient for each paper.
