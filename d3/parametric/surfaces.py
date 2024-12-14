from sympy import symbols, lambdify
import numpy as np
import plotly.graph_objects as go

def plot_parametric_surface(parametric_eqs, range_value, color):
    u, v = symbols('u v')
    x_expr, y_expr, z_expr = parametric_eqs
    x_func = lambdify((u, v), x_expr)
    y_func = lambdify((u, v), y_expr)
    z_func = lambdify((u, v), z_expr)

    # Generate grid for parameters
    u_vals = np.linspace(-range_value, range_value, 50)
    v_vals = np.linspace(-range_value, range_value, 50)
    u_grid, v_grid = np.meshgrid(u_vals, v_vals)

    # Evaluate the parametric equations
    x_vals = x_func(u_grid, v_grid)
    y_vals = y_func(u_grid, v_grid)
    z_vals = z_func(u_grid, v_grid)

    fig = go.Figure()
    fig.add_trace(go.Surface(
        x=x_vals, y=y_vals, z=z_vals,
        colorscale=color
    ))
    return fig
