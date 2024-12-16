from dash import Dash, Input, Output, State, ctx
from ui.layout import layout
from preprocessing.validate import preprocess_input
from utils.graph_handler import handle_graph
import dash

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
            "font": {"color": "white"}
        }
    }

    # Add proper 3D scene configuration
    if is_3d:
        empty_fig["layout"]["scene"] = {
            "xaxis": {"gridcolor": "#333", "zerolinecolor": "#666", "range": [x_min, x_max]},
            "yaxis": {"gridcolor": "#333", "zerolinecolor": "#666", "range": [y_min, y_max]},
            "zaxis": {"gridcolor": "#333", "zerolinecolor": "#666", "range": [z_min, z_max]},
            "bgcolor": "black"
        }
    else:
        empty_fig["layout"].update({
            "xaxis": {"gridcolor": "#333", "zerolinecolor": "#666", "range": [x_min, x_max]},
            "yaxis": {"gridcolor": "#333", "zerolinecolor": "#666", "range": [y_min, y_max]}
        })

    if not equation or equation.strip() == "":
        empty_fig["layout"]["title"] = "Enter an equation"
        return empty_fig, z_style, t_style, xy_style, xy_style

    try:
        equation_data = preprocess_input(equation, dimension)
        if isinstance(equation_data, tuple):
            standardized_equation = equation_data
        else:
            standardized_equation = equation_data
            
        range_values = {
            "x": (float(x_min), float(x_max)),
            "y": (float(y_min), float(y_max)),
            "t": (float(t_min), float(t_max)),
            "z": (float(z_min), float(z_max))
        }
        
        print(f"Plotting in {dimension} mode")  # Debug print
        figure = handle_graph(standardized_equation, range_values, color, dimension)
        return figure, z_style, t_style, xy_style, xy_style

    except Exception as e:
        print(f"Error: {str(e)}")  # Debug print
        empty_fig["layout"]["title"] = str(e)
        return empty_fig, z_style, t_style, xy_style, xy_style

@app.callback(
    Output('suggestions-modal', 'style'),
    [Input('open-suggestions', 'n_clicks'),
     Input('close-suggestions', 'n_clicks')],
    [State('suggestions-modal', 'style')]
)
def toggle_modal(open_clicks, close_clicks, current_style):
    if not ctx.triggered:
        return {'display': 'none'}
    
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if button_id == 'open-suggestions':
        return {'display': 'block'}
    elif button_id == 'close-suggestions':
        return {'display': 'none'}
    
    return current_style

@app.callback(
    Output('equation-input', 'value'),
    [Input('suggestion-1', 'n_clicks'),
     Input('suggestion-2', 'n_clicks'),
     Input('suggestion-3', 'n_clicks'),
     Input('suggestion-4', 'n_clicks'),
     Input('suggestion-5', 'n_clicks'),
     Input('suggestion-6', 'n_clicks'),
     Input('suggestion-7', 'n_clicks'),
     Input('suggestion-8', 'n_clicks')],
    [State('suggestion-1', 'data-equation'),
     State('suggestion-2', 'data-equation'),
     State('suggestion-3', 'data-equation'),
     State('suggestion-4', 'data-equation'),
     State('suggestion-5', 'data-equation'),
     State('suggestion-6', 'data-equation'),
     State('suggestion-7', 'data-equation'),
     State('suggestion-8', 'data-equation')]
)
def handle_suggestion_click(*args):
    if not ctx.triggered:
        raise dash.exceptions.PreventUpdate
        
    clicked_id = ctx.triggered[0]['prop_id'].split('.')[0]
    suggestion_index = int(clicked_id.split('-')[1]) - 1
    equations = args[8:]  # Second half of args contains the equations
    
    return equations[suggestion_index]

if __name__ == "__main__":
    app.run_server(debug=True)