import matplotlib.pyplot as plt
import numpy as np
from synth_fringe_generator import AdvancedSyntheticFringeGenerator

def test_interferogram_generation():
    # 1. Initialize the generator (This defines 'gen')
    gen = AdvancedSyntheticFringeGenerator(width=512, height=512)
    
    # 2. Define 5 phase shifts for Hariharan (-180, -90, 0, 90, 180 degrees)
    shifts_deg = [-180, -90, 0, 90, 180]
    
    # Setup the plot
    fig, axes = plt.subplots(1, 5, figsize=(20, 4))
    fig.suptitle("Advanced Synthetic Interferograms (Hariharan Sequence)", fontsize=16)
    
    for i, shift_deg in enumerate(shifts_deg):
        # Convert degrees to radians
        shift_rad = np.radians(shift_deg)
        
        # 3. Get the 8-bit image from the generator
        # Note: We are using the parameter names defined in AdvancedSyntheticFringeGenerator
        img = gen.get_interferogram(phase_shift_ideal=shift_rad, camera_noise_level=5.0)
        
        # Plotting
        ax = axes[i]
        ax.imshow(img, cmap='gray', vmin=0, vmax=255)
        ax.set_title(f"Shift: {shift_deg}°")
        ax.axis('off')
        
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    test_interferogram_generation()