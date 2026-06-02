"""Unified Delta-x dataset for FS_TB_DeltaX_Analysis.md (single sieve bound).

Recomputes, from one sieve to N, every statistic and figure used in
sections 2,3,6,7,8,10 (and the figures in 9) of the Delta-x note.
Pure NumPy; no SciPy.
"""
import os, math
import numpy as np
from collections import Counter
from itertools import groupby
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

N = 100_000_000          # uniform sieve bound
C2 = 0.6601618

print(f"# Sieve bound N = {N:,}")

# ---- sieve (numpy bool, slice assignment) ----
sieve = np.ones(N + 1, dtype=bool)
sieve[:2] = False
for i in range(2, int(N**0.5) + 1):
    if sieve[i]:
        sieve[i * i :: i] = False
primes = np.nonzero(sieve)[0]
print(f"# primes <= N: {len(primes):,}")

# ---- twin lower-members with 2(p+2) <= N ----
cand = primes[primes + 2 <= N]
tl = cand[sieve[cand + 2]]               # all twin lowers <= N-2
low = tl[2 * (tl + 2) <= N].astype(np.int64)   # doubled stays in range
print(f"# twin pairs with 2(p+2)<=N: {len(low):,}")

xl = np.searchsorted(primes, 2 * low, side="right")   # pi(2 p_k)
dx = np.diff(xl).astype(float)            # Delta x_k
dp = np.diff(low).astype(float)           # Delta p_k
pk = low[:-1].astype(float)               # p_k aligned to step k
print(f"# gaps (Delta x): {len(dx):,}")

lam = 1.0 / np.log(2 * pk)
rho = dx / (2 * dp)
r = rho / lam
mu = 2 * dp / np.log(2 * pk)
Z = dx / mu

def desc(name, a):
    print(f"{name:10s} mean={a.mean():.4f} median={np.median(a):.4f} "
          f"std={a.std():.4f} min={a.min():.4f} max={a.max():.4f} cv={a.std()/a.mean():.4f}")

print("\n## SECTION 2 — Delta x distribution")
desc("dx", dx)
print(f"zeros (dx==0): {int((dx==0).sum())}")
bins2 = [0,1,5,10,20,30,50,75,100,150,200,300,500]
h,_ = np.histogram(dx, bins=bins2)
for i in range(len(h)):
    print(f"  [{bins2[i]:4d},{bins2[i+1]:4d}): {h[i]:7d} ({100*h[i]/len(dx):5.2f}%)")

print("\n## SECTION 3 — run lengths")
gaps = dx.astype(int).tolist()
runs = [len(list(g)) for _, g in groupby(gaps)]
rc = Counter(runs); tot = len(runs)
for L in sorted(rc):
    print(f"  L={L}  count={rc[L]:7d} ({100*rc[L]/tot:6.3f}% of runs) -> {L+1} collinear dots")
eq = sum(1 for i in range(len(gaps)-1) if gaps[i]==gaps[i+1])
print(f"  total runs={tot}  adjacent-equal={eq}/{len(gaps)-1} = {100*eq/(len(gaps)-1):.3f}%")
print(f"  longest run L={max(rc)} -> {max(rc)+1} dots")

print("\n## SECTION 6 — Poisson / coincidence")
c = Counter(gaps); M = len(gaps)
R_emp = sum((n/M)**2 for n in c.values())
print(f"  R_empirical = sum p_v^2 (exact) = {100*R_emp:.4f}%")
print(f"  observed adjacent-equal       = {100*eq/(len(gaps)-1):.4f}%")
mean_dx = dx.mean()
def pois(v,m): return math.exp(-m + v*math.log(m) - math.lgamma(v+1))
R_pois = sum(pois(v,mean_dx)**2 for v in range(0, int(mean_dx*8)))
print(f"  single-Pois({mean_dx:.2f}) coincidence sum pois^2 = {100*R_pois:.4f}%")
print(f"  variance={dx.var():.2f}  mean={mean_dx:.2f}  var/mean={dx.var()/mean_dx:.2f}")
for T in [30,50,100]:
    emp = (dx>=T).mean()
    pt = sum(pois(v,mean_dx) for v in range(T, int(mean_dx*10)))
    print(f"  T={T:3d}: empirical P>= ={100*emp:.3f}% ({int((dx>=T).sum())})  Pois>= ={100*pt:.3e}%")

print("\n## SECTION 7 — variance decomposition")
desc("dx", dx); desc("dp", dp); desc("rho", rho); desc("lambda", lam); desc("r=rho/lam", r)
pos = dx>0
print(f"  Var(log dx)={np.log(dx[pos]).var():.4f}  Var(log 2dp)={np.log(2*dp).var():.4f}  Var(log rho)={np.log(rho[pos]).var():.4f}")
binsr=[0,0.02,0.04,0.06,0.08,0.10,0.15,0.20,0.40]
hr,_=np.histogram(rho,bins=binsr)
print("  rho histogram:")
for i in range(len(hr)): print(f"    [{binsr[i]:.2f},{binsr[i+1]:.2f}): {hr[i]:7d} ({100*hr[i]/len(rho):5.2f}%)")
binsR=[0,0.25,0.5,0.75,1.0,1.5,2.0,3.0,6.0]
hR,_=np.histogram(r,bins=binsR)
print("  r=rho/lam histogram:")
for i in range(len(hR)): print(f"    [{binsR[i]:.2f},{binsR[i+1]:.2f}): {hR[i]:7d} ({100*hR[i]/len(r):5.2f}%)")

decs = [(100,1000),(1000,10000),(10000,100000),(100000,1000000),
        (1000000,10000000),(10000000,50000000)]
print("\n## SECTION 8 — slope drift by decade")
print(f"{'decade':22s} {'N':>7s} {'meanDx':>8s} {'medDx':>6s} {'stdDx':>7s} {'emp_slope':>10s} {'C2/log2p':>9s} {'ratio':>6s} {'refined':>9s} {'ratio':>6s}")
Lc=[]; Sc=[]
for a,b in decs:
    m=(pk>=a)&(pk<b); d=dx[m]; pp=pk[m]
    if len(d)==0: continue
    emp=1/d.mean(); L2=np.log(2*pp); L1=np.log(pp)
    crude=(C2/L2).mean(); refined=(C2*L2/L1**2).mean()
    Lbar=L2.mean(); Lc.append(Lbar); Sc.append(emp)
    print(f"[{a:9d},{b:10d}) {len(d):7d} {d.mean():8.3f} {np.median(d):6.0f} {d.std():7.2f} {emp:10.5f} {crude:9.5f} {emp/crude:6.3f} {refined:9.5f} {emp/refined:6.3f}")
Lc=np.array(Lc); Sc=np.array(Sc); u=1/Lc
A=np.vstack([u,u**2]).T
coef,_,_,_=np.linalg.lstsq(A,Sc,rcond=None)
print(f"  fit slope=A/L+B/L^2:  A={coef[0]:.4f}  B={coef[1]:.4f}   (theory A=C2={C2:.4f}, B=2*C2*ln2={2*C2*math.log(2):.4f})")

print("\n## SECTION 10 — conditional Z by decade")
def ks(x,y):
    allv=np.sort(np.concatenate([x,y]))
    cx=np.searchsorted(np.sort(x),allv,side='right')/len(x)
    cy=np.searchsorted(np.sort(y),allv,side='right')/len(y)
    return np.max(np.abs(cx-cy))
def wass(x,y):
    q=np.linspace(0,1,1000); return np.mean(np.abs(np.quantile(x,q)-np.quantile(y,q)))
print(f"{'decade':22s} {'N':>7s} {'meanZ':>6s} {'medZ':>6s} {'stdZ':>6s} {'minZ':>5s} {'maxZ':>6s} {'1/sqrt(meanDx)':>14s}")
Zd={}
for a,b in decs:
    m=(pk>=a)&(pk<b); z=Z[m]; Zd[(a,b)]=z
    if len(z)==0: continue
    print(f"[{a:9d},{b:10d}) {len(z):7d} {z.mean():6.3f} {np.median(z):6.3f} {z.std():6.3f} {z.min():5.3f} {z.max():6.3f} {1/np.sqrt(dx[m].mean()):14.3f}")
binsZ=list(np.arange(0,2.51,0.25))+[100]
print("  Z histograms (fractions, bins 0,.25,...,2.25,2.5,>=2.5):")
for a,b in decs:
    z=Zd[(a,b)]
    if len(z)==0: continue
    hh,_=np.histogram(z,bins=binsZ); hh=hh/len(z)
    print(f"  [{a:9d},{b:10d}) "+" ".join(f"{x:.3f}" for x in hh))
keys=[k for k in Zd if len(Zd[k])>0]
print("  KS / W1 between adjacent decades and extremes:")
for i in range(len(keys)-1):
    print(f"    {keys[i]} vs {keys[i+1]}: KS={ks(Zd[keys[i]],Zd[keys[i+1]]):.4f} W1={wass(Zd[keys[i]],Zd[keys[i+1]]):.4f}")
print(f"    {keys[1]} vs {keys[-1]}: KS={ks(Zd[keys[1]],Zd[keys[-1]]):.4f} W1={wass(Zd[keys[1]],Zd[keys[-1]]):.4f}")

# ---- figures ----
os.makedirs("figures", exist_ok=True)
# Fig 1
plt.figure(figsize=(8,5))
mx=int(dx.max())
plt.hist(dx, bins=range(0, mx+10, 5), color="tab:blue", edgecolor="none")
plt.axvline(dx.mean(), color="k", ls="--", lw=1, label=f"mean={dx.mean():.1f}")
plt.xlabel("Delta x_k  (primes in (2p_k, 2p_{k+1}])"); plt.ylabel("count")
plt.title(f"Distribution of Delta x  (all {len(dx):,} twin-pair gaps, N=1e8)")
plt.legend(); plt.tight_layout(); plt.savefig("figures/deltax_histogram.png", dpi=130); plt.close()
# Fig 2 (subsample for plotting clarity)
idx = np.random.default_rng(0).choice(len(rho), size=min(20000,len(rho)), replace=False)
plt.figure(figsize=(7,7))
plt.scatter(lam[idx], rho[idx], s=4, alpha=0.15, color="tab:blue")
xs=np.linspace(lam.min(), lam.max(), 50); plt.plot(xs, xs, "r-", lw=1.5, label="rho = lambda (PNT)")
plt.xlabel("lambda_k = 1/log(2p_k)"); plt.ylabel("rho_k = Delta x_k/(2 Delta p_k)")
plt.title(f"Local density rho vs PNT lambda  (20k random of {len(rho):,})")
plt.legend(); plt.tight_layout(); plt.savefig("figures/lambda_rho_scatter.png", dpi=130); plt.close()
# Fig 3
m=dx>0
slope=1/dx[m]; L2=np.log(2*pk[m])
ii=np.random.default_rng(1).choice(int(m.sum()), size=min(30000,int(m.sum())), replace=False)
plt.figure(figsize=(9,5.5))
plt.scatter(L2[ii], slope[ii], s=4, alpha=0.10, color="gray", label="slope_k = 1/Delta x_k")
xs=np.linspace(L2.min(), L2.max(), 200); logp=xs-math.log(2)
plt.plot(xs, C2*xs/logp**2, "r-", lw=2, label="C2 log(2p)/(log p)^2")
for a,b in decs:
    mm=(pk>=a)&(pk<b)
    if mm.sum()==0: continue
    plt.plot(np.log(2*pk[mm]).mean(), 1/dx[mm].mean(), "ks", ms=9, zorder=5)
plt.plot([],[],"ks",ms=9,label="decade aggregate slope 1/mean(Delta x)")
plt.ylim(0,0.4); plt.xlabel("log(2p_k)"); plt.ylabel("slope_k = 1/Delta x_k")
plt.title("Slope drift vs scale, with theoretical backbone (N=1e8)")
plt.legend(); plt.tight_layout(); plt.savefig("figures/slope_vs_log2p.png", dpi=130); plt.close()
print("\n# figures regenerated in figures/")
