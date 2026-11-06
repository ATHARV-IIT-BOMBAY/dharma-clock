"""Shared constants for the Dharma-Clock model."""
import numpy as np

DHARMA = np.array([4, 3, 2, 1.0])          # Satya, Treta, Dvapara, Kali
YUGA_NAMES = ["Satya", "Treta", "Dvapara", "Kali"]
COSMIC_LENGTH = 432_000 * DHARMA            # scriptural lengths (years)

# Anchors (BCE as positive numbers, CE as negative where noted)
SATYA_START = 6000      # BCE
RAMA_BIRTH = 5114       # BCE
WAR = 3139              # BCE
KALI_START = 3102       # BCE
NOW = 2026              # CE
ORION_END = 2468        # CE (Alnilam culmination maximum over Giza)


def fmt(year_bce):
    """Format a year given as positive=BCE, negative=CE."""
    return f"{year_bce:.0f} BCE" if year_bce > 0 else f"{-year_bce + 1:.0f} CE"  # no year zero
