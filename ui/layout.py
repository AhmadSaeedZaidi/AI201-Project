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
        ], className='range-group'),
        
        html.Div([
            html.Label('Y Min', className='input-label'),
            dcc.Input(id='y-min', type='number', value=-3, className='input-field'),
            html.Label('Y Max', className='input-label'),
            dcc.Input(id='y-max', type='number', value=3, className='input-field'),
        ], className='range-group'),
        
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
        html.Button('Toggle 2D/3D', id='toggle-2d-3d', className='toggle-button')
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
