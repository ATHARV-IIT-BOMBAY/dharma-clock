"""Meridian altitude of Alnilam (Orion's Belt) over Giza under precession, -14000..14000."""
import numpy as np
eps=np.radians(23.44); lat=np.radians(29.979)  # Giza
def eq2ecl(ra,dec):
    ra,dec=np.radians(ra),np.radians(dec)
    lam=np.arctan2(np.sin(ra)*np.cos(eps)+np.tan(dec)*np.sin(eps),np.cos(ra))
    beta=np.arcsin(np.sin(dec)*np.cos(eps)-np.cos(dec)*np.sin(eps)*np.sin(ra))
    return lam,beta
lam0,beta=eq2ecl(84.053,-1.2019)   # Alnilam J2000
years=np.arange(-14000,14001,1)
rate=np.radians(50.29/3600)
lam=lam0+rate*(years-2000)
dec=np.arcsin(np.sin(beta)*np.cos(eps)+np.cos(beta)*np.sin(eps)*np.sin(lam))
alt=90-np.degrees(lat-dec)  # meridian altitude (south)
i_min=np.argmin(alt[(years<0)]); y=years[years<0]
print("lowest culmination (past):", y[i_min], "alt %.1f deg"%alt[years<0][i_min])
i_max=np.argmax(alt); print("highest culmination:", years[i_max], "alt %.1f deg"%alt[i_max])
for yr in [-10500,-6000,-5114,-3139,-3102,0,2026]:
    print(yr, "alt %.1f"%alt[years==yr][0])
