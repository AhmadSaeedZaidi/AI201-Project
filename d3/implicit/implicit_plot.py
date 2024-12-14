from sympy import symbols, lambdify
import numpy as np
import plotly.graph_objects as go

def plot_implicit_surface(equation, range_value):
    x, y, z = symbols('x y z')
    f = lambdify((x, y, z), equation.lhs - equation.rhs)

    # Generate a 3D grid
    x_vals = np.linspace(-range_value, range_value, 50)
    y_vals = np.linspace(-range_value, range_value, 50)
    z_vals = np.linspace(-range_value, range_value, 50)
    x_grid, y_grid, z_grid = np.meshgrid(x_vals, y_vals, z_vals)

    # Compute the surface values
    values = f(x_grid, y_grid, z_grid)
    surface = np.abs(values) < 0.1  # Threshold for visualization

    # Get the coordinates for the surface points
    x_surface = x_grid[surface]
    y_surface = y_grid[surface]
    z_surface = z_grid[surface]

    fig = go.Figure()
    fig.add_trace(go.Scatter3d(
        x=x_surface, y=y_surface, z=z_surface,
        mode='markers', marker=dict(size=2, color='blue')
    ))
    return fig
