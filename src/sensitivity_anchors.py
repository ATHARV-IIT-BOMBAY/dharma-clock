"""Sensitivity of the power-law fit to Rama's birth date and the start of Satya."""
import numpy as np
from scipy.optimize import brentq
D={'S':4,'T':3,'Dv':2,'K':1}
NOW=2026; KALI0=3102
def run(rama, satya0=None):
    print(f"\n=== Rama {rama} BCE, Satya start {satya0} ===")
    ok=[]
    for p in np.arange(1.0,8.01,0.01):
        w={k:v**(1-p) for k,v in D.items()}
        if satya0:
            LK=(satya0-KALI0)/(w['S']+w['T']+w['Dv'])
        else:
            LK=None
        if LK is None: continue
        L={k:LK*w[k] for k in w}
        dv0=KALI0+L['Dv']; tr0=dv0+L['T']
        kali_running = LK > KALI0+NOW
        rama_in_treta = dv0 <= rama <= tr0
        if kali_running and rama_in_treta: ok.append((round(p,2),round(LK),round(LK-KALI0)))
    if ok: print("p range",ok[0][0],"-",ok[-1][0],"| Kali ends CE",ok[0][2],"to",ok[-1][2])
    else: print("NO p works")
for rama in [5114,7323,12209]:
    for s0 in [6000,8000,11500,14000]:
        if s0>rama: run(rama,s0)
        else: print(f"\nRama {rama}, Satya start {s0}: impossible (Rama before Satya starts)")
# without A6: only need 2^p >= ratio, LK free
for rama in [5114,7323,12209]:
    span=rama-KALI0
    print(f"\nNo A6, Rama {rama}: need Dvapara<= {span} yrs, Kali>{KALI0+NOW}; min p from 2^(p-1)*... ")
    # L_Dv = LK*2^(1-p) <= span, LK> 5128 -> 2^(p-1) >= 5128/span
    print("  p >=", round(1+np.log2((KALI0+NOW)/span),2))
