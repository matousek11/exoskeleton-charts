# Exoskeleton Charts

This repository contains data analysis and visualization tools for pneumatic artificial muscles (PAMs) used in an exoskeleton project. The project focuses on testing and optimizing various muscle configurations, control algorithms, and performance characteristics to improve exoskeleton functionality.

## Table of Contents

- [Repository Overview](#repository-overview)
- [Notebook Files](#notebook-files)
  - [Cycle test charts](#cycle-test-charts)
  - [Muscle weight lift charts](#muscle-weight-lift-charts)
  - [PID algorithm tuning](#pid-algorithm-tuning)
  - [Tube charts](#tube-charts)
- [Additional Files](#additional-files)
- [Usage](#usage)
  - [PID test visualization](#pid-test-visualization)
- [Project Context](#project-context)

## Repository Overview

This repository serves as an analysis toolkit for:
- **Muscle Endurance Testing**: Evaluating different muscle construction methods and their cycle life
- **Performance Characterization**: Analyzing weight lifting capacity and tube retraction characteristics
- **Control System Tuning**: PID controller parameter optimization through iterative testing
- **Data Visualization**: Creating informative charts and graphs to understand system behavior

The analysis covers various factors including:
- Different sleeve materials (PET, Kevlar) and diameters (¾", 1")
- Tube lengths (6" to 30")
- Operating pressures (30 PSI, 60 PSI)
- Different ending configurations (barbed fittings vs clamps)
- PID control parameters and system responses

## Notebook Files

### [Cycle test charts](cycle-test-charts.ipynb)
**Purpose**: Visualizes cycle endurance test results for different pneumatic muscle constructions.

**Description**: This notebook analyzes and displays the number of cycles until failure for various muscle configurations. The visualization helps identify which construction methods provide the best durability and longevity.

---

### [Muscle weight lift charts](muscle-weight-lift-charts.ipynb)
**Purpose**: Analyzes the weight lifting capacity of pneumatic muscles under different conditions.

**Description**: This notebook visualizes how different muscle lengths and materials perform when lifting various weights.

---

### [PID algorithm tuning](pid-algorithm-tuning.ipynb)
**Purpose**: PID controller tuning and analysis through iterative testing.

**Description**: This notebook documents 40+ PID control algorithm tests, tracking the evolution of control parameters and system performance. It visualizes PID controller responses including target angles, current angles, errors, PID components (proportional, integral, derivative), valve outputs, and loop execution times.

**Key Features**:
- Detailed test documentation with system configurations
- Multi-axis control visualization (lateral, longitudinal, upper leg)
- PID component analysis (P, I, D contributions)
- Muscle output visualization for antagonistic muscle pairs
- Loop time performance analysis
- Support for 1 DOF, 2 DOF, and 3 DOF control systems

---

### [Tube charts](tube-charts.ipynb)
**Purpose**: Analyzes tube retraction and shortening characteristics under different pressures and configurations.

**Description**: This notebook examines how pneumatic tubes shorten (contract) when pressurized, analyzing the relationship between tube length, outer diameter, sleeve diameter, material type, and pressure. The goal is to identify optimal tube configurations that provide maximum shortening percentage with minimal pressure.

---

## Additional Files

### [transform-test-data.py](transform-test-data.py)
Utility script for transforming raw PID test data into a format for analysis.

### [PID test data](pid-tests/)
Directory containing:
- Raw PID test data files (`pid-test-*.txt`)
- Transformed data files (`transformed-data/pid-test-*.txt`)

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Open any notebook in Jupyter:
   ```bash
   jupyter notebook <notebook-name>.ipynb
   ```

3. Run cells to generate visualizations and analysis

### PID test visualization
1. Create `pid-test-xx.txt` file in `pid-tests` and `pid-tests/transformed-data` folder
2. Paste in data from test to both files, data should look like this:
    ```
    PHYSICAL MOVEMENT: Closing Inlet valve, pin: 10

    PHYSICAL MOVEMENT: Closing Outlet valve, pin: 7

    Target: -20.00 | Angle: -3.29 | Error: -16.71 | Output: -2.12 | Time (ms): 100040 | Prop: -1.67 | Der: -0.05 | Int: -0.40 | Long target: 80.00 | Long angle: 107.62 | Long error: -27.62 | Long output: -4.48 | Long prop: -2.76 | Long der: 0.07 | Long int: -1.78 | left bottom front muscle open(ms): 2 | right bottom front muscle open(ms): -7 | left bottom back muscle open(ms): 6 | right bottom back muscle open(ms): -1 | Loop time (ms): 347

    PHYSICAL MOVEMENT: Closing Outlet valve, motor: 1 on board with address: 60

    PHYSICAL MOVEMENT: Opening Inlet valve, pin: 13
    ```
3. Modify path to test file in `transform-test-data.py`
4. Run `python3 transform-test-data.py`
5. Add code for charts generation in `pid-algorithm-tuning.ipynb` notebook
    ```
    with open("pid-tests/transformed-data/pid-test-xx.txt", "r") as f:
    lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    plot_pid_chart(lines)
    ```
6. Run the cell

## Project Context

This repository is part of an exoskeleton development project, focusing on optimizing pneumatic artificial muscle systems for robotic assistance applications. The analysis helps inform design decisions regarding muscle construction, control algorithms, and system parameters.
