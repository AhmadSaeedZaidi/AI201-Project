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
    ],
    [
        Input('equation-input', 'value'),
        Input('toggle-2d-3d', 'n_clicks'),
        Input('color-picker', 'value'),
        Input('x-min', 'value'),
        Input('x-max', 'value'),
        Input('y-min', 'value'),
        Input('y-max', 'value'),
        Input('z-min', 'value'),
        Input('z-max', 'value')
    ]
)
def update_plot(equation, toggle_clicks, color, x_min, x_max, y_min, y_max, z_min, z_max):
    is_3d = (toggle_clicks or 0) % 2 != 0
    z_style = {"display": "inline-block"} if is_3d else {"display": "none"}

    empty_fig = {
        "data": [],
        "layout": {
            "template": "plotly_dark",
            "plot_bgcolor": "black",
            "paper_bgcolor": "black",
            "font": {"color": "white"},
            "xaxis": {"gridcolor": "#333", "zerolinecolor": "#666"},
            "yaxis": {"gridcolor": "#333", "zerolinecolor": "#666"}
        }
    }

    if not equation or equation.strip() == "":
        empty_fig["layout"]["title"] = "Enter an equation"
        return empty_fig, z_style

    try:
        standardized_equation = preprocess_input(equation)
        range_values = {
            "x": (x_min, x_max),
            "y": (y_min, y_max),
            "z": (z_min, z_max) if is_3d else None
        }
        figure = handle_graph(standardized_equation, range_values, color, is_3d)
        return figure, z_style

    except Exception as e:
        empty_fig["layout"]["title"] = str(e)
        return empty_fig, z_style

if __name__ == "__main__":
    app.run_server(debug=True)
