from sympy import symbols, lambdify
import numpy as np
import plotly.graph_objects as go

def plot_parametric_2d(parametric_eqs, range_value, color):
    t = symbols('t')
    x_expr, y_expr = parametric_eqs
    x_func = lambdify(t, x_expr)
    y_func = lambdify(t, y_expr)

    t_vals = np.linspace(-range_value, range_value, 100)
    x_vals = [x_func(val) for val in t_vals]
    y_vals = [y_func(val) for val in t_vals]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', line=dict(color=color)))
    return fig
