from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

from app import app

layout = html.Div([
    html.H3('FAQ'),
    html.P('pimco'),
    html.P('tuits')
], className='container')

