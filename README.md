# Twin Bertrand

A Bertrand-type postulate for twin primes.

## The conjecture

**Twin-Prime Bertrand Postulate (TPB):**
$$\pi_2(2x) - \pi_2(x) \ge 1 \qquad \text{for all } x \ge 11,$$
where $\pi_2$ counts twin primes — i.e. **every dyadic interval $(x, 2x]$ past 11 contains a twin prime.** Equivalent forms:

1. **Ratio:** $T_{k+1} < 2T_k$ for every twin prime $T_k \ge 11$.
2. **Geometric:** every angle-record of the Prime Triangle sequence (with $p_n \ge 3$) is a twin prime.
3. **Ramanujan-analog:** $R^{\text{twin}}_1 = 11$.

## What it shows

- **Verified to $x \le 10^{10}$** across $27{,}412{,}679$ twin primes — with exactly one exception at any scale, the trivial $(5,7)\to(11,13)$.
- **Generalizes** to cousins $(p,p+4)$ and sexy primes $(p,p+6)$: the **Generalized Bertrand Principle (GBP)**, verified across all three constellations to $10^{10}$, with a uniform envelope $G < 0.171(\log P)^{3.22}$.
- **Logical position:** strictly weaker than the twin-prime conjecture, strictly stronger than the Zhang–Maynard bounded-gaps theorems. Immediate under Hardy–Littlewood; unconditionally open.

$$\underbrace{\text{twin-prime conjecture}}_{\pi_2(x)\to\infty} \;\supset\; \underbrace{\text{TPB}}_{\pi_2(2x)\ge\pi_2(x)+1} \;\supset\; \underbrace{\text{bounded gaps}}_{\liminf(p_{n+1}-p_n)<\infty}$$

## Papers ([`papers/`](papers/))

| paper | content |
|---|---|
| [PG I — Prime Triangle](papers/PG_I_PrimeTriangle.pdf) | the construction, PSD identities, and the "$2P$-beats" lemma that TPB rests on |
| [PG II — Angle Record](papers/PG_II_AngleRecord.pdf) | **states and proves the TPB equivalences**, conditional proof under HL, the twin-Ramanujan sequence |
| [PG III — GBP](papers/PG_III_GBP.pdf) | the Generalized Bertrand Principle for admissible pair-constellations |
| [FS–TB Bridge](papers/FS_TB_Bridge.md) | ties TPB to the Factor Skyline (TB lives inside the ~0.26-bit parity-barrier escape) |

Empirical reports and datasets in [`results/`](results/) and [`data/`](data/); scripts in [`scripts/`](scripts/) (verified to $10^{10}$).

Part of the [Primes](../) collection.
