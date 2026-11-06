# The Dharma-Clock

**A non-linear rate-law model of the Yuga cycle, calibrated to epic chronology and the precession of Orion's Belt.**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23997935.svg)](https://doi.org/10.5281/zenodo.23997935)

Paper: [`paper/dharma_clock.pdf`](paper/dharma_clock.pdf) · Zenodo record: https://doi.org/10.5281/zenodo.23997935

## The idea

Read as Earth years, the Puranic yuga lengths (lakhs of years) put Rama's birth before the human species existed. A single constant conversion factor cannot fix this: keeping Kali running today and Rama (5114 BCE) in Treta requires factors that differ by about 5×.

The Dharma-Clock lets cosmic yuga time τ advance relative to Earth time t at a rate set by Dharma D (4, 3, 2, 1 for Satya, Treta, Dvapara, Kali):

```
dτ/dt = k · D^p        p = 2.774,  k = 77.57
```

| Yuga | Earth years | Dates | Anchor |
|---|---|---|---|
| Satya | 476 | 6000 – 5524 BCE | – |
| Treta | 793 | 5524 – 4731 BCE | Rama, 5114 BCE |
| Dvapara | 1,629 | 4731 – 3102 BCE | Krishna 3228 BCE; war 3139 BCE |
| Kali | 5,569 | 3102 BCE – c. 2468 CE | running now (92%) |

Kali, the shortest yuga in cosmic time, becomes the longest in Earth time.

## Reproduce the results

```bash
pip install -r requirements.txt
cd src
python model.py                     # fit p and k, print the timeline
python robustness_families.py       # 8 rate laws vs the anchor constraints
python robustness_chronologies.py   # Aryabhata / Aihole / Varahamihira chronologies
python sensitivity_anchors.py       # sensitivity to Rama's date and Satya's start
python orion_precession.py          # Orion's Belt altitude over Giza under precession
python kepler_orbit_test.py         # eccentric-orbit hypothesis (fails)
python pushya_alignment.py          # Bhagavata 12.2.24 alignment search, 2026-2999
```

## Status and limitations

This is an exploratory modelling exercise by an undergraduate student, not peer-reviewed. The model is fitted to its anchors, so its fit is consistency, not confirmation. The anchor dates are contested, and the Orion link was chosen, not derived. See Section 5 of the paper for the full list, and Section 6 for the falsifiable predictions registered on 6 November 2026.

## Citation

> Chauhan, A. P. S. (2026). *The Dharma-Clock: A Non-Linear Rate-Law Model of the Yuga Cycle, Calibrated to Epic Chronology and the Precession of Orion's Belt* (v1.0). Zenodo. https://doi.org/10.5281/zenodo.23997935

## License

Code: MIT. Paper (`paper/`): CC BY 4.0.

---
Atharv Pratap Singh Chauhan · B.Tech student, Mechanical Engineering, IIT Bombay
