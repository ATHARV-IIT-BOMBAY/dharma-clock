"""Fit the Dharma-Clock power law d(tau)/dt = k * D^p.

Two conditions fix the two constants:
  1. Satya begins c. 6000 BCE  -> sum of Satya+Treta+Dvapara Earth lengths = 6000-3102
  2. Kali ends at Orion's precessional turning point c. 2468 CE
"""
from scipy.optimize import brentq
from common import *

L_KALI = ORION_END + KALI_START - 1          # no year zero
SPAN = SATYA_START - KALI_START

def lengths(p):
    rel = DHARMA ** (1 - p)
    return L_KALI * rel / rel[3]

p = brentq(lambda p: lengths(p)[:3].sum() - SPAN, 1.5, 6)
L = lengths(p)
k = COSMIC_LENGTH[3] / L[3]
print(f"p = {p:.4f}   k = {k:.4f} cosmic years per Earth year\n")
print(f"{'Yuga':8s} {'rate':>8s} {'Earth yr':>9s}   dates")
start = SATYA_START
for name, D, l in zip(YUGA_NAMES, DHARMA, L):
    end = start - l
    print(f"{name:8s} {k*D**p:8.1f} {l:9.0f}   {fmt(start)} -> {fmt(end)}")
    start = end

# linear-model trilemma
c_min = (KALI_START + NOW) / 432_000
c_max = (RAMA_BIRTH - KALI_START) / 864_000
print(f"\nLinear model: Kali alive needs c > {c_min:.4f}; Rama in Treta needs c < {c_max:.4f} -> impossible")
