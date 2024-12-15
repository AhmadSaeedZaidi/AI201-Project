import numpy as np
import sympy as sp
import plotly.graph_objects as go

def plot_implicit_2d(equation, range_values, color='blue'):
    x, y = sp.symbols('x y')
    x_min, x_max = float(range_values['x'][0]), float(range_values['x'][1])
    y_min, y_max = float(range_values['y'][0]), float(range_values['y'][1])
    
    expr = equation.lhs - equation.rhs
    
    # Create a finer mesh for better resolution
    x_vals = np.linspace(x_min, x_max, 300)
    y_vals = np.linspace(y_min, y_max, 300)
    X, Y = np.meshgrid(x_vals, y_vals)
    
    try:
        func = sp.lambdify((x, y), expr, modules=['numpy'])
        Z = func(X, Y)
        
        # Handle infinities and NaN values
        mask = np.isfinite(Z)
        Z[~mask] = np.nan
        
        fig = go.Figure(data=go.Contour(
            x=x_vals,
            y=y_vals,
            z=Z,
            contours=dict(
                coloring='none',
                showlabels=False,
                start=0,
                end=0,
                type='constraint'
            ),
            line=dict(
                color=color,
                width=2
            ),
            showscale=False
        ))
        
        # Set the axis ranges explicitly
        fig.update_xaxes(range=[x_min, x_max])
        fig.update_yaxes(range=[y_min, y_max])
        
        fig.update_layout(
            title="Implicit 2D Plot",
            xaxis_title='X',
            yaxis_title='Y',
            template="plotly_dark",
            plot_bgcolor='black',
            paper_bgcolor='black',
            xaxis=dict(
                gridcolor='#333',
                zerolinecolor='#666',
                showgrid=True
            ),
            yaxis=dict(
                gridcolor='#333',
                zerolinecolor='#666',
                showgrid=True
            ),
            font=dict(color="white")
        )
        
    except Exception as e:
        raise ValueError(f"Error evaluating the equation: {str(e)}")
    
    return fig.to_dict()
