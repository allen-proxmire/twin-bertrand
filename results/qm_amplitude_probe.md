# QM-Amplitude Probe -- verdict for `OPEN_QUESTION_FS_TB_QM_AMP_01`

Sieve bound **N = 5,000,000**. Pure NumPy. Companion to `papers/FS_TB_QM_Amplitude_Memo.md` Appendix A and `Paper_FiniteMemoryCeiling_Primes.md` (ED).

## Anchor -- the amplitude object is real and sqrt(x)-scale

- Mertens `M(N) = -709`, `M(N)/sqrt(N) = -0.3171` (bounded, consistent with sqrt-cancellation / RH; this is the Sum mu(n) = Sum_rho x^rho/(rho zeta'(rho)) amplitude whose phase the parity barrier withholds).

## (i) Trivial-factorization trap -- is the fluctuation sign-bearing?

- Detrended twin fluctuation (Delta2 minus a smooth deg-6 trend): positive 56.9%, negative 43.1%, **111 sign changes** over the grid.
- Canonical amplitude M(x): **190 sign changes** (genuinely oscillating sqrt(x) amplitude).
- Verdict: criterion (i) **does NOT fire** -- the detrended fluctuation and the M(x) amplitude both oscillate in sign, so this is a genuine phase object, NOT the trivial real-sqrt density.

## (iii) Finite-memory phase -- does the optimal Mobius correlator vanish?

`C*(N',M) = (1/N') * Sum_r | Sum_{n<=N', n=r mod M} mu(n) |`, compared to the `sqrt(M/N')` random-walk bound:

| M | N' | C* | sqrt(M/N') | ratio |
|--:|---:|---:|-----------:|------:|
| 30 | 156,250 | 1.469e-02 | 1.386e-02 | 1.060 |
| 30 | 312,500 | 8.605e-03 | 9.798e-03 | 0.878 |
| 30 | 625,000 | 5.322e-03 | 6.928e-03 | 0.768 |
| 30 | 1,250,000 | 3.292e-03 | 4.899e-03 | 0.672 |
| 30 | 2,500,000 | 1.917e-03 | 3.464e-03 | 0.553 |
| 30 | 5,000,000 | 1.177e-03 | 2.449e-03 | 0.480 |
| 210 | 156,250 | 4.024e-02 | 3.666e-02 | 1.098 |
| 210 | 312,500 | 2.624e-02 | 2.592e-02 | 1.012 |
| 210 | 625,000 | 1.756e-02 | 1.833e-02 | 0.958 |
| 210 | 1,250,000 | 1.135e-02 | 1.296e-02 | 0.876 |
| 210 | 2,500,000 | 7.257e-03 | 9.165e-03 | 0.792 |
| 210 | 5,000,000 | 4.709e-03 | 6.481e-03 | 0.727 |
| 2310 | 156,250 | 9.593e-02 | 1.216e-01 | 0.789 |
| 2310 | 312,500 | 6.816e-02 | 8.598e-02 | 0.793 |
| 2310 | 625,000 | 4.706e-02 | 6.079e-02 | 0.774 |
| 2310 | 1,250,000 | 3.241e-02 | 4.299e-02 | 0.754 |
| 2310 | 2,500,000 | 2.225e-02 | 3.040e-02 | 0.732 |
| 2310 | 5,000,000 | 1.523e-02 | 2.149e-02 | 0.708 |

- log C* vs log N' slope per M (sqrt(M/N) bound has slope -0.5): M=30: -0.726, M=210: -0.619, M=2310: -0.533.
- Verdict: criterion (iii) **does NOT fire** -- the finite-memory Mobius correlator vanishes at least as fast as the sqrt(M/N) random-walk bound, so the Mobius phase is NOT finite-memory and the parity-barrier identification survives on this axis.

## (ii) Irreducible bilinearity -- the surviving open risk (UNDECIDED here)

Linear correlation of the twin fluctuation `Delta2` with the single-zero amplitudes (a single-amplitude `|A|^2` picture would need this to be strong):

- corr(Delta2, M)        raw = +0.064   sqrt-normalized = +0.076
- corr(Delta2, psi - x)  raw = -0.025   sqrt-normalized = +0.069

Low linear correlation is **consistent with** Appendix A.4: the twin correlation `Sum Lam(n)Lam(n+2)` is bilinear (governed by *pairs* of zeros; Montgomery / Bogomolny-Keating), so a *single*-amplitude representation is likely the wrong shape. This probe does NOT settle representability at N = 5,000,000; criterion (ii) remains **OPEN / conjectural**.

## Net verdict

- **No clean negative fires on the two decidable axes (i, iii).** The fluctuation is sign-bearing (a phase object), and the Mobius phase is genuinely non-finite-memory -- both consistent with the |psi|^2 / amplitude reading.
- **The decisive question collapses onto bilinearity (ii)**, which is beyond this probe's resolution. The honest status of `OPEN_QUESTION_FS_TB_QM_AMP_01` is therefore: *survives on the decidable axes; stands or falls on whether the twin escape admits a single-amplitude (vs irreducibly bilinear / pairs-of-zeros) representation.*

- Result feeds the sec 4.3 register of `Paper_FiniteMemoryCeiling_Primes` and the open-problem list of `FS_TB_Bridge.md`. **Form, not mechanism** -- no new number theory claimed; the bilinear step is the standard open obstruction.

