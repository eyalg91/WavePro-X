import numpy as np

def extract_phase_4step(i1: np.ndarray, i2: np.ndarray, i3: np.ndarray, i4: np.ndarray) -> np.ndarray:
    """
    Standard 4-step phase shifting algorithm.
    Expected phase shifts: 0, 90, 180, 270 degrees.
    Formula: phi = arctan2(I4 - I2, I1 - I3)
    """
    # Convert to float64 for calculation precision
    f1, f2, f3, f4 = [f.astype(np.float64) for f in [i1, i2, i3, i4]]
    
    numerator = f4 - f2
    denominator = f1 - f3
    
    return np.arctan2(numerator, denominator)

def extract_phase_hariharan(i1: np.ndarray, i2: np.ndarray, i3: np.ndarray, 
                           i4: np.ndarray, i5: np.ndarray) -> np.ndarray:
    """
    Schwider-Hariharan 5-step phase shifting algorithm.
    Expected phase shifts: -180, -90, 0, 90, 180 degrees.
    Robust against linear phase-shift calibration errors and intensity gradients.
    """
    # Convert to float64 for calculation precision
    f = [img.astype(np.float64) for img in [i1, i2, i3, i4, i5]]
    
    # Hariharan Formula: 2*(I2 - I4) / (2*I3 - I5 - I1)
    numerator = 2.0 * (f[1] - f[3])
    denominator = 2.0 * f[2] - f[4] - f[0]
    
    return np.arctan2(numerator, denominator)