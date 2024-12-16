# Mathematical Visualization Tool

A dynamic web-based application for visualizing mathematical equations in 2D and 3D space. Built with Python, Dash, and Plotly, this tool offers an interactive experience for mathematical exploration.

## Features

- **Multiple Plot Types**
  - 2D Explicit Functions (e.g., `y = f(x)`)
  - 2D Implicit Relations (e.g., `x^2 + y^2 = 1`)
  - 2D Parametric Curves (e.g., `x = cos(t), y = sin(t)`)
  - 3D Surfaces (e.g., `z = sin(x) * cos(y)`)

- **Interactive Interface**
  - Real-time equation parsing and plotting
  - Adjustable ranges for axes
  - Dynamic color schemes
  - Zoom, pan, and rotate features for plots

## Technical Details

- **Backend**: Python 3.12
- **Framework**: Dash
- **Libraries**:
  - Plotly (Visualization)
  - SymPy (Mathematical processing)
  - NumPy (Numerical computations)

## Installation

### Prerequisites
- Python 3.12 or higher
- Pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/AhmadSaeedZaidi/AI201-Project.git
   cd AI201-Project
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Usage

1. Launch the app in your browser (default: `http://127.0.0.1:8050/`).
2. Choose a plotting mode (2D/3D).
3. Input an equation in the provided field.
4. Adjust axis ranges and select a color scheme as needed.
5. Interact with the plots using zoom, pan, and rotate controls.

## Example Equations

### 2D Explicit:
- `y = x^2`
- `y = sin(x)`

### 2D Implicit:
- `x^2 + y^2 = 1`

### 3D Surface:
- `z = sin(x) * cos(y)`
- `z = x^2 + y^2`

## Contribution
Contributions are welcome! Feel free to submit issues or pull requests to improve the application.

## License
This project is open-source under the MIT License. See the LICENSE file for details.

## Contact
For queries, reach out via the repository's Issues section.

