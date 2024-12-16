from dash import Dash, Input, Output, State
from ui.layout import layout
from preprocessing.validate import preprocess_input
from utils.graph_handler import handle_graph

# Initialize app
app = Dash(__name__)
app.layout = layout

# Callback
@app.callback(
    [
        Output('plot-area', 'figure'),
        Output('z-range', 'style'),
        Output('t-range', 'style'),
        Output('x-range', 'style'),
        Output('y-range', 'style'),
    ],
    [
        Input('equation-input', 'value'),
        Input('dimension-picker', 'value'),
        Input('color-picker', 'value'),
        Input('x-min', 'value'),
        Input('x-max', 'value'),
        Input('y-min', 'value'),
        Input('y-max', 'value'),
        Input('t-min', 'value'),
        Input('t-max', 'value'),
        Input('z-min', 'value'),
        Input('z-max', 'value')
    ]
)
def update_plot(equation, dimension, color, x_min, x_max, y_min, y_max, t_min, t_max, z_min, z_max):
    is_3d = dimension == '3d'
    is_parametric = dimension == '2d_parametric'
    
    # Control visibility of range inputs
    z_style = {"display": "inline-block"} if is_3d else {"display": "none"}
    t_style = {"display": "inline-block"} if is_parametric else {"display": "none"}
    xy_style = {"display": "none"} if is_parametric else {"display": "inline-block"}
    
    empty_fig = {
        "data": [],
        "layout": {
            "template": "plotly_dark",
            "plot_bgcolor": "black",
            "paper_bgcolor": "black",
            "font": {"color": "white"},
            "xaxis": {"gridcolor": "#333", "zerolinecolor": "#666", "range": [-10, 10]},
            "yaxis": {"gridcolor": "#333", "zerolinecolor": "#666", "range": [-3, 3]}
        }
    }

    if not equation or equation.strip() == "":
        empty_fig["layout"]["title"] = "Enter an equation"
        return empty_fig, z_style, t_style, xy_style, xy_style

    try:
        equation_data = preprocess_input(equation)
        if isinstance(equation_data, tuple):  # Parametric case
            standardized_equation = equation_data
        else:  # Normal case
            standardized_equation = equation_data
            
        range_values = {
            "x": (x_min, x_max),
            "y": (y_min, y_max),
            "t": (t_min, t_max),
            "z": (z_min, z_max) if is_3d else None
        }
        figure = handle_graph(standardized_equation, range_values, color, dimension)
        return figure, z_style, t_style, xy_style, xy_style

    except Exception as e:
        empty_fig["layout"]["title"] = str(e)
        return empty_fig, z_style, t_style, xy_style, xy_style

if __name__ == "__main__":
    app.run_server(debug=True)