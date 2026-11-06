"""Test 8 rate-law families against the anchor constraints, for several Satya start dates."""
import numpy as np
D=np.array([4,3,2,1.]); Y=432000*D
KALI0=3102; NOW=2026; RAMA=5114; WAR=3139
fam={
 "power  r=k*D^p":           (lambda D,a: D**a,              np.linspace(0.01,8,4000)),
 "expon  r=k*e^(bD)":        (lambda D,a: np.exp(a*D),       np.linspace(0.01,5,4000)),
 "Arrhenius r=k*e^(-E/D)":   (lambda D,a: np.exp(-a/D),      np.linspace(0.01,20,4000)),
 "log    r=k*ln(1+bD)":      (lambda D,a: np.log(1+a*D),     np.logspace(-3,3,4000)),
 "log-power r=k*(ln(1+D))^q":(lambda D,a: np.log(1+D)**a,    np.linspace(0.01,12,4000)),
 "horizon r=k/(1-D/Dc)":     (lambda D,a: 1/(1-D/a),         np.linspace(4.0001,40,4000)),
 "horizon r=k/sqrt(1-D/Dc)": (lambda D,a: 1/np.sqrt(1-D/a),  np.linspace(4.000001,40,4000)),
 "logistic r=k/(1+e^-(D-c)*4)":(lambda D,a: 1/(1+np.exp(-4*(D-a))), np.linspace(-5,10,4000)),
}
def solve(f,a,satya0):
    rel=Y/f(D,a); k=rel[:3].sum()/(satya0-KALI0); L=rel/k
    return L
def check(L):
    dv0=KALI0+L[2]; tr0=dv0+L[1]
    return (L[3]>KALI0+NOW) and (dv0<=RAMA<=tr0)
print("WITH A6 (Satya starts 6000 BCE)")
print(f"{'family':30s} {'feasible?':9s} {'Kali ends (CE)':>22s}  {'Satya len':>12s}")
for name,(f,grid) in fam.items():
    ends=[];sat=[]
    for a in grid:
        with np.errstate(all='ignore'):
            L=solve(f,a,6000)
        if np.all(np.isfinite(L)) and np.all(L>0) and check(L):
            ends.append(L[3]-KALI0); sat.append(L[0])
    if ends: print(f"{name:30s} {'YES':9s} {min(ends):9.0f} – {max(ends):9.0f}  {min(sat):5.0f}–{max(sat):5.0f}")
    else:    print(f"{name:30s} {'NO':9s}")
# hold-out: use Satya 8000 / 11500 BCE as alternative anchors
for s0 in [7000,8000]:
    print(f"\nSatya start {s0} BCE:")
    for name,(f,grid) in fam.items():
        ok=[]
        for a in grid:
            with np.errstate(all='ignore'): L=solve(f,a,s0)
            if np.all(np.isfinite(L)) and np.all(L>0) and check(L): ok.append(L[3]-KALI0)
        print(f"  {name:30s}", f"Kali ends {min(ok):.0f}–{max(ok):.0f} CE" if ok else "infeasible")

print("\n=== Parashurama test: Treta/Dvapara junction must lie ~5114-5000 BCE (around Rama's youth) ===")
for name,(f,grid) in fam.items():
    hits=[]
    for a in grid:
        with np.errstate(all='ignore'): L=solve(f,a,6000)
        if not (np.all(np.isfinite(L)) and np.all(L>0) and check(L)): continue
        j=KALI0+L[2]
        if 5000<=j<=5114: hits.append((a,j,L[3]-KALI0+1))
    if hits: print(f"{name:30s} junction {hits[-1][1]:.0f}-{hits[0][1]:.0f} BCE, Kali ends {min(h[2] for h in hits):.0f}-{max(h[2] for h in hits):.0f} CE")
    else: print(f"{name:30s} FAILS")
