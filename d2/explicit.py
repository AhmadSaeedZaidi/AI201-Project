import numpy as np
import sympy as sp
import plotly.graph_objects as go

def plot_explicit_2d(equation, range_value, color='blue'):
    x, y = sp.symbols('x y')
    lhs, rhs = equation.lhs, equation.rhs

    if lhs == y or rhs == y:
        if lhs == y:
            expr = rhs
        else:
            expr = lhs

        x_vals = np.linspace(-range_value, range_value, 400)
        y_vals = np.array([float(expr.subs(x, val)) for val in x_vals])

        fig = go.Figure(data=go.Scatter(
            x=x_vals,
            y=y_vals,
            mode='lines',
            line=dict(color=color)
        ))
        fig.update_layout(
            title="Explicit 2D Plot (y = f(x))",
            xaxis_title='X',
            yaxis_title='Y'
        )

    elif lhs == x or rhs == x:
        if lhs == x:
            expr = rhs
        else:
            expr = lhs

        y_vals = np.linspace(-range_value, range_value, 400)
        x_vals = np.array([float(expr.subs(y, val)) for val in y_vals])

        fig = go.Figure(data=go.Scatter(
            x=y_vals,
            y=x_vals,
            mode='lines',
            line=dict(color=color)
        ))
        fig.update_layout(
            title="Explicit 2D Plot (x = f(y))",
            xaxis_title='Y',
            yaxis_title='X'
        )

    else:
        raise ValueError("Equation is not in explicit form y = f(x) or x = f(y).")

    return fig.to_dict()
