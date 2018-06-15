import dash_core_components as dcc
import dash_html_components as html
import dash
from apps import faq_page, main_app
from app import app

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])
server = app.server


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return main_app.layout
    elif pathname == '/faq':
        return faq_page.layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)
