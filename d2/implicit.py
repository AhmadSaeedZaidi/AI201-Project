import numpy as np
import sympy as sp
import plotly.graph_objects as go

def plot_implicit_2d(equation, range_value, color='blue'):
    x, y = sp.symbols('x y')
    equation_lambda = sp.lambdify((x, y), equation.lhs - equation.rhs, "numpy")
    x_vals = np.linspace(-range_value, range_value, 400)
    y_vals = np.linspace(-range_value, range_value, 400)
    x_grid, y_grid = np.meshgrid(x_vals, y_vals)
    z_vals = equation_lambda(x_grid, y_grid)
    fig = go.Figure(data=go.Contour(
        z=z_vals,
        x=x_vals,
        y=y_vals,
        contours=dict(
            start=0, end=0,
            coloring='lines',
            showlabels=True
        ),
        line=dict(color=color),
        colorbar=dict(title="Value of f(x, y)")
    ))
    fig.update_layout(
        title="Implicit 2D Plot",
        xaxis_title='X',
        yaxis_title='Y'
    )
    return fig.to_dict()
