    # WavePro-X Development Roadmap

## Phase 1: Core Engine & Synthetic Data (Headless / No UI)
- [x] **Task 1.1:** Build `SyntheticFringeGenerator` to create mock interferograms with known phase and phase steps. *(In Progress)*
- [ ] **Task 1.2:** Implement `PhaseExtraction` module (e.g., 4-Step or Carré algorithms) to extract wrapped phase from a series of images.
- [ ] **Task 1.3:** Implement spatial phase unwrapping logic.
- [ ] **Task 1.4:** Build `ZernikeSolver` to fit polynomials, calculate phase residuals, PV, and RMS.
- [ ] **Task 1.5:** Create a standalone test script to run the full mathematical pipeline on synthetic data and plot results.

## Phase 2: Data Structures & State Management
- [ ] **Task 2.1:** Create a `MeasurementData` core class to hold raw 2D numpy arrays (the actual physics data).
- [ ] **Task 2.2:** Add logic to convert raw floating-point data into 8-bit normalized images for UI rendering.
- [ ] **Task 2.3:** Implement ROI and Mask handling (boolean arrays) alongside the raw data.

## Phase 3: Basic User Interface (PySide6)
- [ ] **Task 3.1:** Set up the main application window and layout architecture.
- [ ] **Task 3.2:** Integrate a central 2D canvas (using `pyqtgraph` or `matplotlib` Qt backend) for fast image rendering.
- [ ] **Task 3.3:** Implement basic interactive tools for drawing an ROI or applying a mask on the display image.
- [ ] **Task 3.4:** Link UI interactions (ROI selection) to slice and mask the actual `MeasurementData` in memory.

## Phase 4: Concurrency & Algorithm Integration
- [ ] **Task 4.1:** Create background workers (`QThread` / `QRunnable`) to prevent the UI from freezing during heavy physics calculations.
- [ ] **Task 4.2:** Connect the UI trigger (e.g., an "Analyze" button) to send data to the background extraction and Zernike threads.
- [ ] **Task 4.3:** Build UI side-panels to display numerical results (PV, RMS, Zernike coefficients table).

## Phase 5: Hardware Abstraction & Integration
- [ ] **Task 5.1:** Define abstract base classes (`Interfaces`) for a generic Camera and a Piezo Actuator.
- [ ] **Task 5.2:** Create a `MockHardware` module that inherits from the interfaces and uses the `SyntheticFringeGenerator` to mimic live hardware.
- [ ] **Task 5.3:** Integrate specific A/D controllers or camera SDKs to replace the mock hardware with real lab equipment.


## Project Structure

```text
WavePro-X/
│
├── .cursorrules           # AI behavior and project-specific rules
├── .gitignore             # Git exclusion rules
├── Roadmap.md             # Project progress and milestones
├── requirements.txt       # Project dependencies (numpy, scipy, pyside6, etc.)
├── main.py                # Main application entry point (UI setup)
│
├── core/                  # Core physics and mathematical algorithms
│   ├── __init__.py
│   ├── phase_math.py      # Extraction, unwrapping, and Zernike fitting
│   └── measurement.py     # Data models for holding raw and processed data
│
├── ui/                    # User Interface components (PySide6)
│   ├── __init__.py
│   ├── main_window.py     # Primary GUI layout
│   └── widgets/           # Custom UI widgets (Canvas, Toolbars)
│
├── hardware/              # Hardware abstraction layers
│   ├── __init__.py
│   ├── base_device.py     # Abstract interfaces for camera/piezo
│   └── mock_devices.py    # Simulated hardware for testing
│
└── dev_tools/             # Development and testing utilities (excluded from EXE)
    ├── __init__.py
    ├── synth_fringe_generator.py # Mock interferogram generation
    └── test_scripts/             # Isolated algorithm verification scripts

