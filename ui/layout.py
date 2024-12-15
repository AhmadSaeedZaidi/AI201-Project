from dash import dcc, html

layout = html.Div([
    html.H1("Equation Plotter", className="title"),

    html.Div([
        dcc.Input(
            id='equation-input',
            type='text',
            placeholder='Enter your equation (e.g., y = x^2)',
            className="equation-input"
        ),
    ], className="input-container"),

    html.Div([
        html.Div([
            html.Label("X Min", className="input-label"),
            dcc.Input(id='x-min', type='number', value=-10, className="input-field"),
            html.Label("X Max", className="input-label"),
            dcc.Input(id='x-max', type='number', value=10, className="input-field"),
        ], className="range-group"),

        html.Div([
            html.Label("Y Min", className="input-label"),
            dcc.Input(id='y-min', type='number', value=-10, className="input-field"),
            html.Label("Y Max", className="input-label"),
            dcc.Input(id='y-max', type='number', value=10, className="input-field"),
        ], className="range-group"),

        html.Div([
            html.Div([
                html.Label("Z Min", className="input-label"),
                dcc.Input(id='z-min', type='number', value=-10, className="input-field"),
                html.Label("Z Max", className="input-label"),
                dcc.Input(id='z-max', type='number', value=10, className="input-field"),
            ], id='z-range', style={"display": "none"}),
        ], className="range-group"),
    ], className="range-inputs"),

    html.Div([
        dcc.Dropdown(
            id='color-picker',
            options=[
                {'label': 'Blue', 'value': 'blue'},
                {'label': 'Red', 'value': 'red'},
                {'label': 'Green', 'value': 'green'},
                {'label': 'Purple', 'value': 'purple'},
                {'label': 'Orange', 'value': 'orange'}
            ],
            value='blue',
            placeholder="Select a color",
            className="dropdown-dark"
        ),
        html.Button('Toggle 2D/3D', id='toggle-2d-3d', n_clicks=0, className="toggle-button"),
    ], className="controls-container"),

    dcc.Graph(id='plot-area', className="plot-area"),
], className="main-container")
