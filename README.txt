# Mathematical Visualization Tool

A dynamic web-based application for visualizing mathematical equations in 2D and 3D space. Built with Python, Dash, and Plotly.

## Features

- **Multiple Plot Types**
  - 2D Explicit Functions (y = f(x))
  - 2D Implicit Relations
  - 2D Parametric Curves
  - 3D Surfaces

- **Interactive Interface**
  - Real-time equation parsing
  - Adjustable plotting ranges
  - Dynamic color schemes with gradients
  - Plot suggestions for exploration
  - Zoom, pan, and rotate capabilities

## Usage

1. Select plotting mode (2D/3D)
2. Enter mathematical equation
3. Adjust ranges if needed
4. Choose color scheme
5. Explore with interactive controls

## Example Equations

### 2D Plots
- `y = x^2`
- `sin(x)`
- `x^2 + y^2 = 1`

### Parametric
- `cos(t), sin(t)`

### 3D Surfaces
- `x^2 + y^2`
- `sin(sqrt(x^2 + y^2))`
- `sin(x)*cos(y)`

## Technical Details

- **Backend**: Python 3.12
- **Framework**: Dash
- **Libraries**: 
  - Plotly (Visualization)
  - SymPy (Mathematical Processing)
  - NumPy (Numerical Computations)

## Installation
