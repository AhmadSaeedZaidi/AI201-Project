from dash import html, dcc

def get_layout():
    return {
        'xaxis': {
            'range': [-10, 10],
            'gridcolor': '#333',
            'zerolinecolor': '#666'
        },
        'yaxis': {
            'range': [-10, 10],
            'gridcolor': '#333',
            'zerolinecolor': '#666'
        },
        'template': 'plotly_dark',
        'plot_bgcolor': 'black',
        'paper_bgcolor': 'black',
        'font': {'color': 'white'}
    }

layout = html.Div([
    html.Div([
        dcc.Input(
            id='equation-input',
            type='text',
            placeholder='Enter your equation (e.g., y = x^2)',
            className='equation-input'
        ),
    ], className='input-container'),
    
    html.Div([
        html.Div([
            html.Label('X Min', className='input-label'),
            dcc.Input(id='x-min', type='number', value=-10, className='input-field'),
            html.Label('X Max', className='input-label'),
            dcc.Input(id='x-max', type='number', value=10, className='input-field'),
        ], className='range-group', id='x-range'),
        
        html.Div([
            html.Label('Y Min', className='input-label'),
            dcc.Input(id='y-min', type='number', value=-3, className='input-field'),
            html.Label('Y Max', className='input-label'),
            dcc.Input(id='y-max', type='number', value=3, className='input-field'),
        ], className='range-group', id='y-range'),
        
        html.Div([
            html.Label('T Min', className='input-label'),
            dcc.Input(id='t-min', type='number', value=0, className='input-field'),
            html.Label('T Max', className='input-label'),
            dcc.Input(id='t-max', type='number', value=2*3.14159, className='input-field'),
        ], className='range-group', id='t-range', style={'display': 'none'}),
        
        html.Div([
            html.Label('Z Min', className='input-label'),
            dcc.Input(id='z-min', type='number', value=-10, className='input-field'),
            html.Label('Z Max', className='input-label'),
            dcc.Input(id='z-max', type='number', value=10, className='input-field'),
        ], className='range-group', id='z-range', style={'display': 'none'}),
    ], className='range-inputs'),
    
    html.Div([
        dcc.Dropdown(
            id='color-picker',
            options=[
                {'label': 'Blue', 'value': 'blue'},
                {'label': 'Red', 'value': 'red'},
                {'label': 'Green', 'value': 'green'},
                {'label': 'Yellow', 'value': 'yellow'},
                {'label': 'Purple', 'value': 'purple'},
                {'label': 'Orange', 'value': 'orange'}
            ],
            value='blue',
            className='dropdown-dark'
        ),
        dcc.Dropdown(
            id='dimension-picker',
            options=[
                {'label': '2D Cartesian', 'value': '2d'},
                {'label': '2D Parametric', 'value': '2d_parametric'},
                {'label': '3D', 'value': '3d'}
            ],
            value='2d',
            className='dropdown-dark'
        )
    ], className='controls-container'),
    
    dcc.Graph(
        id='plot-area',
        className='plot-area',
        config={'displayModeBar': True},
        figure={
            'data': [],
            'layout': get_layout()
        }
    )
], className='main-container')
