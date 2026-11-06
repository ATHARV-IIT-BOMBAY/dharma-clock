"""Find new moons 2026-2999 with Sun, Moon and Jupiter all in Pushya (Bhagavata Purana 12.2.24). Swiss Ephemeris, Moshier, Lahiri."""
import swisseph as swe, numpy as np
swe.set_sid_mode(swe.SIDM_LAHIRI)
F=swe.FLG_MOSEPH|swe.FLG_SIDEREAL
def lon(jd,p): return swe.calc_ut(jd,p,F)[0][0]
def newmoons(y0,y1):
    jd=swe.julday(y0,1,1); end=swe.julday(y1,1,1); out=[]
    prev=(lon(jd,swe.MOON)-lon(jd,swe.SUN))%360
    while jd<end:
        jd+=1; d=(lon(jd,swe.MOON)-lon(jd,swe.SUN))%360
        if d<prev and prev>300:  # wrapped -> new moon in last day
            a,b=jd-1,jd
            for _ in range(30):
                m=(a+b)/2; dm=(lon(m,swe.MOON)-lon(m,swe.SUN))%360
                if dm>180: a=m
                else: b=m
            out.append(b)
        prev=d
    return out
strict=[];loose=[]
for jd in newmoons(2026,2999):
    s=lon(jd,swe.SUN); j=lon(jd,swe.JUPITER)
    if 90<=s<120 and 90<=j<120: loose.append(jd)
    if 93.333<=s<=106.667 and 93.333<=j<=106.667: strict.append(jd)
def ymd(jd): y,m,d,_=swe.revjul(jd); return f"{y}-{m:02d}-{int(d):02d}"
print("STRICT (Sun,Moon,Jupiter all in Pushya) 2026-2999:",len(strict))
for jd in strict: print("  ",ymd(jd))
print("LOOSE (all in Cancer) count:",len(loose)," first few:",[ymd(x) for x in loose[:6]])
