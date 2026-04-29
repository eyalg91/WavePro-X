import numpy as np

class AdvancedSyntheticFringeGenerator:
    def __init__(self, width: int = 512, height: int = 512):
        self.width = width
        self.height = height
        
        # Create normalized coordinate grid between -1 and 1
        x = np.linspace(-1, 1, width)
        y = np.linspace(-1, 1, height)
        self.X, self.Y = np.meshgrid(x, y)
        
        # --- AGGRESSIVE NON-UNIFORM ILLUMINATION ---
        
        # 1. Off-center Laser Beam (Gaussian Profile)
        # Simulates the laser hotspot being shifted to the top-left (-0.5, -0.5)
        laser_center_x, laser_center_y = -0.5, -0.5
        beam_width = 0.8
        gaussian_beam = np.exp(-((self.X - laser_center_x)**2 + (self.Y - laser_center_y)**2) / (2 * beam_width**2))
        
        # 2. Strong Linear Gradient (Shadowing effect)
        # Intensity drops from top-right to bottom-left
        linear_gradient = (self.X - self.Y + 2) / 4.0 
        
        # Combined Illumination Map (A)
        # Base intensity with a strong hotspot and significant drop-off
        self.background_map = 40.0 + 160.0 * (gaussian_beam * linear_gradient)
        
        # Contrast/Modulation Map (B)
        # Visibility of fringes drops in darker areas (this is the real test for the algorithm)
        self.modulation_map = 20.0 + 80.0 * (gaussian_beam * linear_gradient)
        
    def generate_mock_phase(self) -> np.ndarray:
        """
        Generates a complex synthetic phase map (Ground Truth).
        Includes Defocus, Astigmatism, and Tilt.
        """
        # Mathematical model of the wavefront
        defocus = 8.0 * (self.X**2 + self.Y**2)
        astigmatism = 4.0 * (self.X**2 - self.Y**2)
        tilt_x = 2.0 * self.X
        
        return defocus + astigmatism + tilt_x

    def get_interferogram(self, 
                           phase_shift_ideal: float = 0.0, 
                           vibration_error: float = 0.0,
                           camera_noise_level: float = 2.0) -> np.ndarray:
        """
        Generates an interferogram with the aggressive illumination model,
        phase shift errors (vibration), and camera noise.
        """
        # Calculate ground truth and apply actual phase shift (including error)
        ground_truth_phase = self.generate_mock_phase()
        actual_shift = phase_shift_ideal + vibration_error
        
        # Total phase term inside the cosine
        total_phase = ground_truth_phase + actual_shift
        
        # Full interference equation: I = A(x,y) + B(x,y) * cos(Phi + delta)
        intensity = self.background_map + self.modulation_map * np.cos(total_phase)
        
        # Add random Gaussian camera noise
        noise = np.random.normal(0, camera_noise_level, intensity.shape)
        intensity += noise
        
        # Clip to 8-bit range and convert to uint8 (simulating actual camera output)
        intensity = np.clip(intensity, 0, 255)
        
        return intensity.astype(np.uint8)