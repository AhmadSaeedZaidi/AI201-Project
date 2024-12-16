import numpy as np
import sympy as sp
import plotly.graph_objects as go

def plot_explicit_2d(equation, range_values, color='blue'):
    x, y = sp.symbols('x y')
    lhs, rhs = equation.lhs, equation.rhs
    x_min, x_max = range_values['x']
    y_min, y_max = range_values['y']

    if lhs == y or rhs == y:
        if lhs == y:
            expr = rhs
        else:
            expr = lhs

        try:
            x_vals = np.linspace(x_min, x_max, 1000)
            func = sp.lambdify(x, expr, modules=['numpy'])
            y_vals = func(x_vals)
            
            # Filter out points where the function changes too rapidly (asymptotes)
            dy = np.diff(y_vals)
            mask = np.abs(dy) < 100
            mask = np.append(mask, mask[-1])
            
            # Also filter infinite and NaN values
            mask = mask & np.isfinite(y_vals)
            
            x_vals, y_vals = x_vals[mask], y_vals[mask]
            
            # Split into continuous segments
            split_indices = np.where(np.abs(np.diff(y_vals)) > 10)[0] + 1
            x_segments = np.split(x_vals, split_indices)
            y_segments = np.split(y_vals, split_indices)
            
            fig = go.Figure()
            for x_seg, y_seg in zip(x_segments, y_segments):
                fig.add_trace(go.Scatter(
                    x=x_seg,
                    y=y_seg,
                    mode='lines',
                    line=dict(color=color),
                    showlegend=False
                ))
            
        except Exception as e:
            raise ValueError(f"Error evaluating the equation: {str(e)}")

        fig.update_layout(
            title="2D Plot",
            xaxis_title='X',
            yaxis_title='Y',
            template="plotly_dark",
            plot_bgcolor='black',
            paper_bgcolor='black',
            xaxis=dict(gridcolor='#333', zerolinecolor='#666', range=[x_min, x_max]),
            yaxis=dict(gridcolor='#333', zerolinecolor='#666', range=[y_min, y_max]),
            font=dict(color="white")
        )

    elif lhs == x or rhs == x:
        if lhs == x:
            expr = rhs
        else:
            expr = lhs

        try:
            y_vals = np.linspace(y_min, y_max, 1000)
            func = sp.lambdify(y, expr, modules=['numpy'])
            x_vals = func(y_vals)
            mask = np.isfinite(x_vals)
            x_vals, y_vals = x_vals[mask], y_vals[mask]
        except Exception as e:
            raise ValueError(f"Error evaluating the equation: {str(e)}")

        fig = go.Figure(data=go.Scatter(
            x=y_vals,
            y=x_vals,
            mode='lines',
            line=dict(color=color)
        ))
        fig.update_layout(
            title="2D Plot",
            xaxis_title='Y',
            yaxis_title='X',
            template="plotly_dark",
            plot_bgcolor='black',
            paper_bgcolor='black',
            xaxis=dict(gridcolor='#333', zerolinecolor='#666', range=[x_min, x_max]),
            yaxis=dict(gridcolor='#333', zerolinecolor='#666', range=[y_min, y_max]),
            font=dict(color="white")
        )

    else:
        raise ValueError("Equation is not in explicit form y = f(x) or x = f(y)")

    return fig.to_dict()
