import numpy as np
import plotly.graph_objects as go

def plot_explicit_surface(equation, range_value, color):
    # Create a meshgrid for x and y values
    x_vals = np.linspace(-range_value, range_value, 50)
    y_vals = np.linspace(-range_value, range_value, 50)
    x_grid, y_grid = np.meshgrid(x_vals, y_vals)

    # Define the function for z based on the equation
    # Assuming the equation is of the form z = f(x, y)
    # For example: z = x^2 + y^2 (a paraboloid)
    z_vals = equation(x_grid, y_grid)

    # Plot the surface
    fig = go.Figure(data=[go.Surface(
        x=x_grid, y=y_grid, z=z_vals,
        colorscale=color
    )])

    fig.update_layout(
        title="Explicit Surface Plot",
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z'
        )
    )

    return fig
