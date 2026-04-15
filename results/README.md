# results/

Standalone markdown reports produced by the scripts. Each is human-readable and internally consistent (no LaTeX rendering required).

## Contents

| file | produced by | contents |
|---|---|---|
| [`summary.md`](summary.md) | `pg_twin_angle_analysis.py` | Initial TPB & angle-record verification on the $10^9$ range. First numbers in the program. |
| [`comparison_1e9_vs_1e10.md`](comparison_1e9_vs_1e10.md) | `pg_extend_1e10.py` | Side-by-side comparison of $10^9$ and $10^{10}$ regimes. Documents the β-drift finding and updated overshoot table. |
| [`report_structural_1e10.md`](report_structural_1e10.md) | `pg_structural_1e10.py` | The three structural results: overshoot growth law, refined TPB envelope, and Generalized Bertrand Principle for cousins/sexy primes. |
| [`uniform_envelope_fits.md`](uniform_envelope_fits.md) | `pg_envelope_fits.py` | Per-constellation and pooled envelope fits used in PG III §6. |
| [`twin_ramanujan_report.md`](twin_ramanujan_report.md) | `pg_twin_ramanujan.py` | The twin-Ramanujan prime sequence $R^{\mathrm{twin}}_n$; first 30 values, logarithmic samples, OEIS submission draft. |
| [`literature_review.md`](literature_review.md) | manual review | Structured literature review establishing that TPB/GBP sit inside the Ramanujan-prime family but are not stated elsewhere in the searched literature. |

## Reading order

If you want the short version: **read [`../PG_FieldGuide.md`](../PG_FieldGuide.md)**. It narrates the whole program in ~12 pages.

For the original computational pipeline: `summary.md` → `comparison_1e9_vs_1e10.md` → `report_structural_1e10.md` → `uniform_envelope_fits.md` → `twin_ramanujan_report.md`.

For positioning within the existing literature: `literature_review.md`.

For the full mathematical content: the three papers in [`../papers/`](../papers/).
