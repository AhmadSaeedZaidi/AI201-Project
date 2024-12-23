import numpy as np
import sympy as sp
import plotly.graph_objects as go

def plot_explicit_3d(equation, range_values, color='blue'):
    x, y, z = sp.symbols('x y z')
    x_min, x_max = float(range_values['x'][0]), float(range_values['x'][1])
    y_min, y_max = float(range_values['y'][0]), float(range_values['y'][1])
    z_min, z_max = float(range_values['z'][0]), float(range_values['z'][1])
    
    print("Equation:", equation)
    print("Range values:", range_values)
    
    # Get z expression from equation
    if equation.lhs == z:
        expr = equation.rhs
    else:
        expr = equation.lhs
    
    print("Expression:", expr)
    
    try:
        # Create grid of x, y points
        x_vals = np.linspace(x_min, x_max, 100)
        y_vals = np.linspace(y_min, y_max, 100)
        X, Y = np.meshgrid(x_vals, y_vals)
        
        print("X shape:", X.shape)
        print("Y shape:", Y.shape)
        
        # Convert expression to numpy function
        f = sp.lambdify((x, y), expr, modules=['numpy', 'sympy'])
        Z = f(X, Y)
        
        print("Z shape:", Z.shape)
        print("Z dtype:", Z.dtype)
        print("Z nan count:", np.isnan(Z).sum())
        
        # Filter out points where the function changes too rapidly (asymptotes)
        dz_dx = np.diff(Z, axis=1)
        dz_dy = np.diff(Z, axis=0)
        mask_x = np.abs(dz_dx) < 100
        mask_y = np.abs(dz_dy) < 100
        mask_x = np.append(mask_x, mask_x[:, -1:], axis=1)
        mask_y = np.append(mask_y, mask_y[-1:, :], axis=0)
        mask = mask_x & mask_y
        
        # Also filter infinite and NaN values
        mask = mask & np.isfinite(Z)
        
        X = np.where(mask, X, np.nan)
        Y = np.where(mask, Y, np.nan)
        Z = np.where(mask, Z, np.nan)
        
        print("Filtered X shape:", X.shape)
        print("Filtered Y shape:", Y.shape)
        print("Filtered Z shape:", Z.shape)
        print("Filtered Z nan count:", np.isnan(Z).sum())
        
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
            colorscale=colorscale_map.get(color, 'Plasma'),  # Default to Plasma
            showscale=True
        )])
        
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
        print("Error details:", e)
        raise ValueError("Error evaluating the 3D equation: " + str(e))
    
    return fig.to_dict() 