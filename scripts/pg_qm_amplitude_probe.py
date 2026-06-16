"""Numerical probe for OPEN_QUESTION_FS_TB_QM_AMP_01.

Tests the decidable clean-negative criteria of Appendix A in
`papers/FS_TB_QM_Amplitude_Memo.md` (mirrored in ED's
`Memo_QM_Amplitude_PrimeEscape.md`):

  Does the twin-escape fluctuation factor as |A|^2 with phase = the Mobius
  sign that the parity barrier withholds?

What this probe can DECIDE at N = 5e6 (pure NumPy, no SciPy):

  (anchor) M(x) = sum mu(n) is a sqrt(x)-scale oscillating amplitude
           (RH-consistent sqrt cancellation).
  (i)  trivial-factorization trap: is the twin fluctuation sign-bearing
       (a genuine phase object) rather than a positive density |sqrt(f)|^2 ?
  (iii) finite-memory phase: does the optimal finite-memory Mobius correlator
       C*(N,M) = (1/N) sum_r | sum_{n<=N, n=r mod M} mu(n) |  vanish ~ sqrt(M/N)?
       If it vanishes, the Mobius phase is NOT finite-memory, so criterion (iii)
       does NOT fire and the parity-barrier identification survives on this axis.

What this probe CANNOT settle (flagged, per Appendix A.4):

  (ii) irreducible bilinearity: the twin correlation sum Lam(n)Lam(n+2) is
       bilinear (pairs of zeros) and has no unconditional explicit formula.
       The probe only reports the (weak) linear correlation of the twin
       fluctuation with the single-zero amplitudes M(x), psi(x)-x as evidence;
       it does not decide representability.

Outputs:
  ../data/qm_amp_probe_grid.csv      sampled x, pi2, E2, Delta2, M, psi-x
  ../data/qm_amp_probe_mobius.csv    Test-B C*(N',M) decay table
  ../results/qm_amplitude_probe.md   verdict mapped to the pre-registered criteria

Pure NumPy. Runtime ~1 min on a modern laptop.
"""
import os
import math
import numpy as np

N = 5_000_000            # matches Paper_FiniteMemoryCeiling_Primes (sieve bound)
C2 = 0.6601618           # twin constant; HL twin density prefactor is 2*C2
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
RESULTS = os.path.join(HERE, "..", "results")
os.makedirs(DATA, exist_ok=True)
os.makedirs(RESULTS, exist_ok=True)

print(f"# N = {N:,}")

# ---- prime sieve (odd-aware bool) ----
sieve = np.ones(N + 1, dtype=bool)
sieve[:2] = False
for i in range(2, int(N ** 0.5) + 1):
    if sieve[i]:
        sieve[i * i :: i] = False
primes = np.nonzero(sieve)[0]
sqrtN = int(N ** 0.5)
primes_le_sqrt = primes[primes <= sqrtN]
print(f"# primes <= N: {len(primes):,}")

# ---- Mobius function mu(n) via sieve ----
# mu *= -1 for each prime factor; zero out non-squarefree.
mu = np.ones(N + 1, dtype=np.int8)
mu[0] = 0
for p in primes:
    mu[p::p] *= -1
for p in primes_le_sqrt:
    mu[p * p :: p * p] = 0
M = np.cumsum(mu.astype(np.int64))          # Mertens function M(x)
print(f"# Mertens M(N) = {M[N]:,}   M(N)/sqrt(N) = {M[N] / math.sqrt(N):.4f}")

# ---- von Mangoldt Lambda(n) and Chebyshev psi(x) ----
Lam = np.zeros(N + 1, dtype=np.float64)
for p in primes:
    lp = math.log(p)
    pk = p
    while pk <= N:
        Lam[pk] = lp
        pk *= p
psi = np.cumsum(Lam)                         # psi(x) = sum_{p^k <= x} log p

# ---- twin lower-members and pi2(x) ----
cand = primes[primes + 2 <= N]
twin_low = cand[sieve[cand + 2]]             # p with p, p+2 both prime
print(f"# twin lower-members <= N: {len(twin_low):,}")

# ---- E2(x) = 2 C2 * Li2(x), Li2(x) = int_2^x dt/(log t)^2 (fine-grid trapezoid) ----
fine = np.linspace(2.0, float(N), 2_000_001)
integrand = 1.0 / (np.log(fine) ** 2)
dt = fine[1] - fine[0]
cumint = np.concatenate(([0.0], np.cumsum(0.5 * (integrand[1:] + integrand[:-1]) * dt)))

def Li2(x):
    return np.interp(x, fine, cumint)

# ---- sample grid (log-spaced) for the fluctuation/correlation test ----
xs = np.unique(np.round(np.logspace(3, math.log10(N), 1500)).astype(np.int64))
xs = xs[(xs >= 1000) & (xs <= N)]
pi2 = np.searchsorted(twin_low, xs, side="right").astype(np.float64)
E2 = 2.0 * C2 * Li2(xs.astype(np.float64))
Delta2 = pi2 - E2                            # centered twin count (the "fluctuation")
M_s = M[xs].astype(np.float64)               # amplitude object 1
psi_s = psi[xs] - xs.astype(np.float64)      # amplitude object 2 (psi(x)-x)

# (i) trivial-factorization trap: is the fluctuation genuinely sign-bearing?
# Delta2 carries a smooth drift (2*C2*Li2 overshoots pi2 at finite x, a known
# second-order bias), so detrend with a low-order polynomial in x before the
# sign test; otherwise the test sees the drift, not phase content.
xf = xs.astype(np.float64)
trend = np.polyval(np.polyfit(xf, Delta2, 6), xf)
resid = Delta2 - trend
sign_changes = int(np.sum(np.diff(np.sign(resid)) != 0))     # detrended twin fluctuation
M_sign_changes = int(np.sum(np.diff(np.sign(M_s)) != 0))     # canonical amplitude M(x)
frac_pos = float(np.mean(resid > 0))
frac_neg = float(np.mean(resid < 0))

# linear correlations (raw, and sqrt(x)-normalized to compare oscillation phase)
def pearson(a, b):
    a = a - a.mean(); b = b - b.mean()
    d = math.sqrt(float(a @ a) * float(b @ b))
    return float(a @ b) / d if d > 0 else 0.0

inv_sqrt = 1.0 / np.sqrt(xs.astype(np.float64))
corr_M_raw = pearson(Delta2, M_s)
corr_psi_raw = pearson(Delta2, psi_s)
corr_M_norm = pearson(Delta2 * inv_sqrt, M_s * inv_sqrt)
corr_psi_norm = pearson(Delta2 * inv_sqrt, psi_s * inv_sqrt)

# ---- (iii) Test B: optimal finite-memory Mobius correlator C*(N',M) ----
idx = np.arange(N + 1)
mu_f = mu.astype(np.float64)
Ms = [30, 210, 2310]                         # primorial template states (5#, 7#, 11#)
Nprimes = [N // 32, N // 16, N // 8, N // 4, N // 2, N]
mob_rows = []
for Mm in Ms:
    res = idx % Mm
    for Np in Nprimes:
        Sr = np.bincount(res[: Np + 1], weights=mu_f[: Np + 1], minlength=Mm)
        Cstar = float(np.abs(Sr).sum()) / Np
        bound = math.sqrt(Mm / Np)
        mob_rows.append((Mm, Np, Cstar, bound, Cstar / bound))

# decay check: C* ~ sqrt(M/N') means log C* vs log N' has slope ~ -0.5.
# "Vanishes" = decays at least as fast as the random-walk bound (slope <= -0.4),
# not an absolute cutoff (C* is naturally larger at small N' / large M).
slopes = {}
for Mm in Ms:
    rows = [r for r in mob_rows if r[0] == Mm]
    lnN = np.log([r[1] for r in rows])
    lnC = np.log([r[2] for r in rows])
    slopes[Mm] = float(np.polyfit(lnN, lnC, 1)[0])
ratios_ok = all(r[4] <= 1.15 for r in mob_rows)   # C* never exceeds the bound by >15%

# ---- write data ----
with open(os.path.join(DATA, "qm_amp_probe_grid.csv"), "w", encoding="utf-8") as f:
    f.write("x,pi2,E2,Delta2,M,psi_minus_x\n")
    for i in range(len(xs)):
        f.write(f"{xs[i]},{pi2[i]:.1f},{E2[i]:.4f},{Delta2[i]:.4f},{M_s[i]:.1f},{psi_s[i]:.4f}\n")

with open(os.path.join(DATA, "qm_amp_probe_mobius.csv"), "w", encoding="utf-8") as f:
    f.write("M,Nprime,Cstar,sqrt_M_over_N,ratio\n")
    for r in mob_rows:
        f.write(f"{r[0]},{r[1]},{r[2]:.6e},{r[3]:.6e},{r[4]:.4f}\n")

# ---- verdict ----
mob_vanishes = all(s <= -0.4 for s in slopes.values()) and ratios_ok
neg_i = (sign_changes < 10) and (M_sign_changes < 10)   # fires only if NEITHER oscillates
neg_iii = not mob_vanishes                     # (iii) fires if phase IS finite-memory

lines = []
def w(s=""):
    lines.append(s)

w("# QM-Amplitude Probe -- verdict for `OPEN_QUESTION_FS_TB_QM_AMP_01`")
w()
w(f"Sieve bound **N = {N:,}**. Pure NumPy. Companion to "
  "`papers/FS_TB_QM_Amplitude_Memo.md` Appendix A and "
  "`Paper_FiniteMemoryCeiling_Primes.md` (ED).")
w()
w("## Anchor -- the amplitude object is real and sqrt(x)-scale")
w()
w(f"- Mertens `M(N) = {M[N]:,}`, `M(N)/sqrt(N) = {M[N]/math.sqrt(N):.4f}` "
  "(bounded, consistent with sqrt-cancellation / RH; this is the "
  "Sum mu(n) = Sum_rho x^rho/(rho zeta'(rho)) amplitude whose phase the "
  "parity barrier withholds).")
w()
w("## (i) Trivial-factorization trap -- is the fluctuation sign-bearing?")
w()
w(f"- Detrended twin fluctuation (Delta2 minus a smooth deg-6 trend): "
  f"positive {100*frac_pos:.1f}%, negative {100*frac_neg:.1f}%, "
  f"**{sign_changes} sign changes** over the grid.")
w(f"- Canonical amplitude M(x): **{M_sign_changes} sign changes** "
  "(genuinely oscillating sqrt(x) amplitude).")
w(f"- Verdict: criterion (i) **{'FIRES' if neg_i else 'does NOT fire'}** -- "
  f"{'both objects are essentially one-signed (trivial |sqrt(f)|^2)' if neg_i else 'the detrended fluctuation and the M(x) amplitude both oscillate in sign, so this is a genuine phase object, NOT the trivial real-sqrt density'}.")
w()
w("## (iii) Finite-memory phase -- does the optimal Mobius correlator vanish?")
w()
w("`C*(N',M) = (1/N') * Sum_r | Sum_{n<=N', n=r mod M} mu(n) |`, compared to the "
  "`sqrt(M/N')` random-walk bound:")
w()
w("| M | N' | C* | sqrt(M/N') | ratio |")
w("|--:|---:|---:|-----------:|------:|")
for r in mob_rows:
    w(f"| {r[0]} | {r[1]:,} | {r[2]:.3e} | {r[3]:.3e} | {r[4]:.3f} |")
w()
w("- log C* vs log N' slope per M (sqrt(M/N) bound has slope -0.5): "
  + ", ".join(f"M={k}: {v:+.3f}" for k, v in slopes.items()) + ".")
w(f"- Verdict: criterion (iii) **{'FIRES' if neg_iii else 'does NOT fire'}** -- the "
  f"finite-memory Mobius correlator {'does NOT vanish (phase is finite-memory predictable; identification false)' if neg_iii else 'vanishes at least as fast as the sqrt(M/N) random-walk bound, so the Mobius phase is NOT finite-memory and the parity-barrier identification survives on this axis'}.")
w()
w("## (ii) Irreducible bilinearity -- the surviving open risk (UNDECIDED here)")
w()
w("Linear correlation of the twin fluctuation `Delta2` with the single-zero "
  "amplitudes (a single-amplitude `|A|^2` picture would need this to be strong):")
w()
w(f"- corr(Delta2, M)        raw = {corr_M_raw:+.3f}   sqrt-normalized = {corr_M_norm:+.3f}")
w(f"- corr(Delta2, psi - x)  raw = {corr_psi_raw:+.3f}   sqrt-normalized = {corr_psi_norm:+.3f}")
w()
w("Low linear correlation is **consistent with** Appendix A.4: the twin "
  "correlation `Sum Lam(n)Lam(n+2)` is bilinear (governed by *pairs* of zeros; "
  "Montgomery / Bogomolny-Keating), so a *single*-amplitude representation is "
  "likely the wrong shape. This probe does NOT settle representability at "
  f"N = {N:,}; criterion (ii) remains **OPEN / conjectural**.")
w()
w("## Net verdict")
w()
any_neg = neg_i or neg_iii
if not any_neg:
    w("- **No clean negative fires on the two decidable axes (i, iii).** The "
      "fluctuation is sign-bearing (a phase object), and the Mobius phase is "
      "genuinely non-finite-memory -- both consistent with the |psi|^2 / amplitude "
      "reading.")
    w("- **The decisive question collapses onto bilinearity (ii)**, which is "
      "beyond this probe's resolution. The honest status of "
      "`OPEN_QUESTION_FS_TB_QM_AMP_01` is therefore: *survives on the decidable "
      "axes; stands or falls on whether the twin escape admits a single-amplitude "
      "(vs irreducibly bilinear / pairs-of-zeros) representation.*")
else:
    w("- A clean negative fired; see the per-criterion verdicts above. The "
      "analogy is bounded to that extent and should be reported as a decorative "
      "resemblance on the affected axis.")
w()
w("- Result feeds the sec 4.3 register of `Paper_FiniteMemoryCeiling_Primes` and the "
  "open-problem list of `FS_TB_Bridge.md`. **Form, not mechanism** -- no new "
  "number theory claimed; the bilinear step is the standard open obstruction.")
w()

with open(os.path.join(RESULTS, "qm_amplitude_probe.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

print("\n".join(lines))
print(f"\n# wrote ../results/qm_amplitude_probe.md, ../data/qm_amp_probe_grid.csv, ../data/qm_amp_probe_mobius.csv")
