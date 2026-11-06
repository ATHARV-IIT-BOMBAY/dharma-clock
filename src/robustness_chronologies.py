"""Fit each surviving family to three historical chronologies (Aryabhata, Aihole, Varahamihira) with the Orion end date."""
import numpy as np
from scipy.optimize import brentq
D=np.array([4,3,2,1.]); Y=432000*D
fam={"power":(lambda D,a:D**a,(0.5,8)),"arrhenius":(lambda D,a:np.exp(-a/D),(0.1,40)),
     "logpower":(lambda D,a:np.log(1+D)**a,(0.5,20)),"logistic":(lambda D,a:1/(1+np.exp(-4*(D-a))),(-3,8))}
sets={"A Aryabhata (Kali 3102, war 3139)":(3102,3139),
      "B Aihole (war 3102, Kali 3066)":(3066,3102),
      "C Varahamihira-adjusted (war 2449, Kali 2413)":(2413,2449)}
S0=6000; RAMA=5114; END=2468
for sn,(K0,WAR) in sets.items():
    print("\n"+sn); LK=END+K0-1
    for n,(f,(lo,hi)) in fam.items():
        g=lambda a:(Y/f(D,a))[:3].sum()/(Y/f(D,a))[3]*LK-(S0-K0)
        try: a=brentq(g,lo,hi)
        except: print(f"  {n:10s} no solution"); continue
        rel=Y/f(D,a); L=rel/rel[3]*LK; dv0=K0+L[2]; tr0=dv0+L[1]
        ok=dv0<=RAMA<=tr0; warpct=100*(dv0-WAR)/L[2]
        print(f"  {n:10s} shape={a:7.4f}  Treta {tr0:.0f}-{dv0:.0f} BCE  Rama in Treta={'YES' if ok else 'NO '}  war {warpct:5.1f}% into Dvapara")
