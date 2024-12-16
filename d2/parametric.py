import numpy as np
import sympy as sp
import plotly.graph_objects as go

def plot_parametric_2d(equation, range_values, color='blue'):
    color_map = {
        'blue': '#00CED1',    # Turquoise/Aqua
        'red': '#FF6B6B',     # Soft coral red
        'green': '#98FB98',   # Pale green
        'yellow': '#FFD700',  # Gold
        'purple': '#DDA0DD',  # Plum
        'orange': '#FFA07A',  # Light salmon
        'plasma': 'Plasma',   
        'viridis': 'Viridis', 
        'magma': 'Magma'      
    }
    plot_color = color_map.get(color, color_map['blue'])
    
    t = sp.Symbol('t')
    
    # Extract expressions from equation tuple
    x_expr, y_expr = equation[0]  # Note: equation[0] because preprocess_input returns (expr, None, "parametric")
    
    try:
        # Convert symbolic expressions to numpy functions
        x_func = sp.lambdify(t, x_expr, modules=['numpy'])
        y_func = sp.lambdify(t, y_expr, modules=['numpy'])
        
        # Generate t values using the t range
        t_min, t_max = range_values['t']
        t_vals = np.linspace(float(t_min), float(t_max), 1000)
        
        # Calculate x and y values
        x_vals = x_func(t_vals)
        y_vals = y_func(t_vals)
        
        # Filter out invalid values
        mask = np.isfinite(x_vals) & np.isfinite(y_vals)
        x_vals, y_vals = x_vals[mask], y_vals[mask]
        
        fig = go.Figure(data=go.Scatter(
            x=x_vals,
            y=y_vals,
            mode='lines',
            line=dict(color=plot_color),
            showlegend=False
        ))
        
        fig.update_layout(
            title="2D Parametric Plot",
            xaxis_title='X',
            yaxis_title='Y',
            template="plotly_dark",
            plot_bgcolor='black',
            paper_bgcolor='black',
            xaxis=dict(
                gridcolor='#333',
                zerolinecolor='#666',
                range=[float(range_values['x'][0]), float(range_values['x'][1])]
            ),
            yaxis=dict(
                gridcolor='#333',
                zerolinecolor='#666',
                range=[float(range_values['y'][0]), float(range_values['y'][1])]
            ),
            font=dict(color="white")
        )
        
    except Exception as e:
        raise ValueError(f"Error evaluating the parametric equations: {str(e)}")
    
    return fig.to_dict()
