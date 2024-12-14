from sympy import symbols, lambdify
import numpy as np
import plotly.graph_objects as go

def plot_plane(equation, range_value, color):
    x, y = symbols('x y')
    z_expr = equation.rhs
    z_func = lambdify((x, y), z_expr)

    x_vals = np.linspace(-range_value, range_value, 30)
    y_vals = np.linspace(-range_value, range_value, 30)
    x_grid, y_grid = np.meshgrid(x_vals, y_vals)
    z_grid = z_func(x_grid, y_grid)

    fig = go.Figure()
    fig.add_surface(x=x_grid, y=y_grid, z=z_grid, colorscale=color)
    return fig
