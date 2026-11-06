"""Test whether an eccentric (Keplerian) orbit can reproduce the yuga timeline. It cannot."""
import numpy as np
from scipy.optimize import minimize
# target: fraction of EARTH time spent in each yuga (p=3 model), cosmic angle fractions .4,.3,.2,.1
L=np.array([427.6,760.1,1710.3,6841.1]); T=L.sum(); target=L/T
edges=np.array([0,.4,.7,.9,1.0])*2*np.pi
def M_of_theta(th,e):
    # mean anomaly from true anomaly, unwrapped
    E=2*np.arctan2(np.sqrt(1-e)*np.sin(th/2),np.sqrt(1+e)*np.cos(th/2))
    M=E-e*np.sin(E)
    return M
def fracs(e,th0):
    ths=np.linspace(0,2*np.pi,200001)
    M=np.unwrap(M_of_theta(ths+th0,e)); M=M-M[0]
    tot=M[-1]
    idx=[np.searchsorted(ths,x) for x in edges]; idx[-1]=len(ths)-1
    return np.array([(M[idx[i+1]]-M[idx[i]])/tot for i in range(4)])
def loss(x):
    e=1/(1+np.exp(-x[0])); return np.sum((np.log(fracs(e,x[1]))-np.log(target))**2)
best=None
for e0 in [-1,0,1,2,3]:
    for t0 in np.linspace(-np.pi,np.pi,9):
        r=minimize(loss,[e0,t0],method='Nelder-Mead')
        if best is None or r.fun<best.fun: best=r
e=1/(1+np.exp(-best.x[0])); th0=best.x[1]
f=fracs(e,th0)
print("total cycle",round(T),"yr; best e=%.3f periapsis offset=%.1f deg"%(e,np.degrees(th0)%360))
for n,a,b in zip(["Satya","Treta","Dvapara","Kali"],target*T,f*T): print(f"{n:8s} target {a:7.0f}  kepler {b:7.0f}")
# speed ratio
print("max/min angular speed ratio:",round(((1+e)/(1-e))**2,1))
