# scripts/

End-to-end reproducibility for every empirical claim in PG I–III.

**Requirements:** Python 3.10+, NumPy. That's it.

```bash
pip install numpy
```

Run in order. Each script is standalone and writes to `../data/` and `../results/`.

## Scripts (run order)

### 1. `pg_twin_angle_analysis.py` (~30 s)

Sieve of Eratosthenes to $10^9$, extract twin primes, verify TPB on the $10^9$ range, enumerate angle-records for $p_n < 10^8$, produce initial fits.

**Outputs:**
- `../data/twins_1e9.npy` — 3.4M twin primes
- `../data/angle_records_1e8.csv` — 440,312 record-setting pairs
- `../data/ratio_top20.csv`, `../data/decade_gap_table.csv`
- `../results/summary.md`

### 2. `pg_extend_1e10.py` (~5 min)

Segmented sieve to $10^{10}$, updated decade tables and envelope fits, refit β.

**Outputs:**
- `../data/twins_1e10.npy` — 27.4M twin primes
- `../data/ratio_top20_1e10.csv`, `../data/near_misses_1e10.csv`, `../data/decade_table_1e10.csv`
- `../results/comparison_1e9_vs_1e10.md`

### 3. `pg_structural_1e10.py` (~6 min)

Single sieve pass to $10^{10}$ extracting twin, cousin, and sexy pair-constellations. Computes all Bertrand statistics and the overshoot growth-law fits.

**Outputs:**
- `../data/cousins_1e10.npy` — 27.4M cousin-prime pairs (smaller member)
- `../data/sexy_1e10.npy` — 54.8M sexy-prime pairs (smaller member)
- `../data/constellation_ratios.csv`
- `../results/report_structural_1e10.md`

### 4. `pg_envelope_fits.py` (~5 s)

Per-constellation envelope fits $r_k - 1 \le C (\log T_k)^\delta / T_k$ and the pooled uniform fit used in PG III §6.

**Outputs:**
- `../data/envelope_fits.csv`
- `../results/uniform_envelope_fits.md`

### 5. `pg_twin_ramanujan.py` (~5 s)

Compute the twin-Ramanujan prime sequence $R^{\mathrm{twin}}_n$ via an event walk on $\pm 1$ transitions of $f(x) = \pi_2(x) - \pi_2(x/2)$.

**Outputs:**
- `../data/twin_ramanujan_primes.csv` — first $10^6$ terms
- `../results/twin_ramanujan_report.md`

## Design notes

- Sieves are implemented in plain NumPy; no C extensions or `primesieve`.
- The `10^{10}` segmented sieve in `pg_extend_1e10.py` and `pg_structural_1e10.py` uses an odd-only representation with a 128 MB-per-segment buffer, giving ~5 minutes wall time on a modern laptop.
- All fits use `np.polyfit` on log-transformed data. No external optimization libraries.
- Cross-segment boundary handling for pair extraction carries a three-entry buffer of recent primes.

## Not included

- `pg_extend_1e11.py` (an attempted $10^{11}$ extension) was dropped in favor of structural analysis on the $10^{10}$ data. See `../results/literature_review.md` for the reasoning.
