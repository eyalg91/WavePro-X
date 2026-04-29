import matplotlib.pyplot as plt
import numpy as np
import sys
import os

# Add the project root to the Python path to allow imports from 'core'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from synth_fringe_generator import AdvancedSyntheticFringeGenerator
from core.phase_math import extract_phase_hariharan

def run_extraction_test():
    # 1. Setup the simulation
    width, height = 512, 512
    gen = AdvancedSyntheticFringeGenerator(width, height)
    
    # 2. Generate 5 frames for Hariharan (-180, -90, 0, 90, 180 degrees)
    shifts = np.radians([-180, -90, 0, 90, 180])
    frames = [gen.get_interferogram(phase_shift_ideal=s, camera_noise_level=2.0) for s in shifts]
    
    # 3. Extract the phase using our core function
    wrapped_phase = extract_phase_hariharan(*frames)
    
    # 4. Get ground truth for verification
    gt_phase = gen.generate_mock_phase()
    # Wrap ground truth to [-pi, pi] to match algorithm output
    gt_wrapped = (gt_phase + np.pi) % (2 * np.pi) - np.pi
    
    # 5. Visualization
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle("Phase Extraction Test: Hariharan Algorithm vs Aggressive Gradients", fontsize=16)
    
    # Show input (one frame)
    axes[0].imshow(frames[2], cmap='gray')
    axes[0].set_title("Dirty Input Frame (0°)")
    
    # Show extracted wrapped phase
    im1 = axes[1].imshow(wrapped_phase, cmap='jet')
    axes[1].set_title("Extracted Wrapped Phase")
    plt.colorbar(im1, ax=axes[1], fraction=0.046, pad=0.04)
    
    # Show error (Extracted - Ground Truth)
    # We account for 2pi wrap-around in the error calculation
    error = (wrapped_phase - gt_wrapped + np.pi) % (2 * np.pi) - np.pi
    im2 = axes[2].imshow(error, cmap='RdBu', vmin=-0.1, vmax=0.1)
    axes[2].set_title("Extraction Error (Radians)")
    plt.colorbar(im2, ax=axes[2], fraction=0.046, pad=0.04)
    
    for ax in axes: ax.axis('off')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_extraction_test()