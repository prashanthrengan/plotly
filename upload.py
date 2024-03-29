import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt

import json
import pandas as pd
import plotly
import io

app = dash.Dash()

app.scripts.config.serve_locally = True

app.layout = html.Div([

    html.Hr(),
    html.H3('Upload the files here'),
    dcc.Upload(
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select a File')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center'
        }
    ),

    html.Hr(),

], className="container")


app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

if __name__ == '__main__':
    app.run_server(debug=True)
