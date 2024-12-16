import numpy as np
import sympy as sp
import plotly.graph_objects as go

def plot_explicit_3d(equation, range_values, color='blue'):
    x, y, z = sp.symbols('x y z')
    x_min, x_max = float(range_values['x'][0]), float(range_values['x'][1])
    y_min, y_max = float(range_values['y'][0]), float(range_values['y'][1])
    z_min, z_max = float(range_values['z'][0]), float(range_values['z'][1])
    
    # Get z expression from equation
    if equation.lhs == z:
        expr = equation.rhs
    else:
        expr = equation.lhs
    
    try:
        # Create grid of x, y points
        x_vals = np.linspace(x_min, x_max, 100)
        y_vals = np.linspace(y_min, y_max, 100)
        X, Y = np.meshgrid(x_vals, y_vals)
        
        # Convert expression to numpy function
        f = sp.lambdify((x, y), expr, modules=['numpy'])
        Z = f(X, Y)
        
        # Filter invalid values
        mask = np.isfinite(Z)
        Z = np.where(mask, Z, np.nan)
        
        # Map colors to colorscales
        colorscale_map = {
            'blue': 'Blues',
            'red': 'Reds',
            'green': 'Greens',
            'yellow': 'YlOrRd',
            'purple': 'Purples',
            'orange': 'Oranges',
            'plasma': 'Plasma',
            'viridis': 'Viridis',
            'magma': 'Magma'
        }
        
        # Create 3D surface plot
        fig = go.Figure(data=[go.Surface(
            x=X,
            y=Y,
            z=Z,
            colorscale=colorscale_map.get(color, 'Plasma'),  # Default to Plasma if color not found
            showscale=True  # Show the colorbar
        )])
        
        # Update layout for 3D
        fig.update_layout(
            title="3D Surface Plot",
            scene=dict(
                xaxis=dict(range=[x_min, x_max], gridcolor='#333', zerolinecolor='#666'),
                yaxis=dict(range=[y_min, y_max], gridcolor='#333', zerolinecolor='#666'),
                zaxis=dict(range=[z_min, z_max], gridcolor='#333', zerolinecolor='#666'),
                bgcolor='black'
            ),
            template="plotly_dark",
            paper_bgcolor='black',
            font=dict(color="white")
        )
        
    except Exception as e:
        raise ValueError(f"Error evaluating the 3D equation: {str(e)}")
    
    return fig.to_dict() 