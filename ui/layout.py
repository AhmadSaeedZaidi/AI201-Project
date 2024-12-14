from dash import dcc, html

layout = html.Div([
    html.H1("Equation Plotter"),
    dcc.Input(id='equation-input', type='text', placeholder='Enter your equation'),
    html.Button('Plot', id='plot-button'),
    dcc.Graph(id='plot-area'),
    dcc.Slider(id='range-slider', min=-10, max=10, step=1, value=5),
    html.Button('Change Color', id='color-button')
])
