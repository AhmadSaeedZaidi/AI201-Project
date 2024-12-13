from dash import Dash, Input, Output
from ui.layout import layout
from preprocessing.validate import preprocess_input
from utils.graph_handler import handle_graph

# Initialize app
app = Dash(__name__)
app.layout = layout

# Callbacks
@app.callback(
    Output('plot-area', 'figure'),
    Input('plot-button', 'n_clicks'),
    Input('equation-input', 'value'),
    Input('range-slider', 'value'),
    Input('color-button', 'n_clicks')
)
def update_plot(n_clicks, equation, range_value, color_clicks):
    try:
        standardized_equation = preprocess_input(equation)
        return handle_graph(standardized_equation, range_value, color_clicks)
    except Exception as e:
        return {"data": [], "layout": {"title": f"Error: {e}"}}

if __name__ == "__main__":
    app.run_server(debug=True)
