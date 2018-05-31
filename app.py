# Boxplots of all the different major infos
# Since we can't specify the median,q1,q3, we have to do q1,q1,median,median,q3,q3
# So that min = q1 and max = q1

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

df = pd.read_pickle('./final_v1.02.pkl')

LINE_GRAPH_COURSEOPTIONS = [{'label': str(clas), 'value': str(clas)} for clas in df['combined'].unique()]
LINE_GRAPH_YAXIS_OPTIONS = [{'label': 'Median Salary (Nominal)', 'value': 'Gross Monthly Salary Median'},
                            {'label': 'Median Salary (Inflation Adjusted)',
                             'value': 'Gross Monthly Salary Median (Inflation Adjusted)'},
                            {'label': 'Full-Time Employment Rate', 'value': 'Full-Time Permanent Employment Rate'},
                            {'label': 'Mean Salary (Nominal)', 'value': 'Gross Monthly Salary Mean'},
                            {'label': 'Mean Salary (Inflation Adjusted)',
                             'value': 'Gross Monthly Salary Mean (Inflation Adjusted)'},
                            {'label': 'Monthly Salary 25th Percentile (Nominal)',
                             'value': 'Gross Monthly Salary 25th Percentile'},
                            {'label': 'Monthly Salary 25th Percentile (Inflation Adjusted)',
                             'value': 'Gross Monthly Salary 25th Percentile (Inflation Adjusted)'},
                            {'label': 'Monthly Salary 75th Percentile (Nominal)',
                             'value': 'Gross Monthly Salary 75th Percentile'},
                            {'label': 'Monthly Salary 75th Percentile (Inflation Adjusted)',
                             'value': 'Gross Monthly Salary 75th Percentile (Inflation Adjusted)'}
                            ]

LINE_GRAPH_DEFAULT = ['Sector - Business (Average)',
                      'Sector - Computing (Average)',
                      'Sector - Design/Arts (Average)',
                      'Sector - Education (Average)',
                      'Sector - Engineering (Average)',
                      'Sector - Healthcare (Average)',
                      'Sector - Humanities and Social Science (Average)',
                      'Sector - Law (Average)',
                      'Sector - Science (Average)',
                      'Sector - Vocational (Average)']
LINE_GRAPH_SHAPES = {
    'Business': 'circle',
    'Computing': 'square',
    'Design/Arts': 'diamond',
    'Education': 'cross',
    'Engineering': 'x',
    'Healthcare': 'bowtie',
    'Humanities and Social Science': 'hourglass',
    'Law': 'star',
    'Science': 'hash-open',
    'Vocational': 'hexagram'}

COLOR_DICT = {'NUS': 'rgba(50,75,140,0.75)', 'NTU': 'rgba(220,110,170,0.75)', 'SMU': 'rgba(77,184,92,0.75)',
              'SUTD': 'rgba(180,140,100,0.75)', 'SIT': 'rgba(160,170,140,0.75)',
              'Average': 'rgba(207, 114, 255, 1)'}

SCATTER_GRAPH_CHOICE_DICT = {'FTER': 'Full-Time Permanent Employment Rate',
                             'SAL1': 'Gross Monthly Salary Mean',
                             'SAL2': 'Gross Monthly Salary Mean (Inflation Adjusted)'}

app = dash.Dash(__name__)
app.title = 'Graduate Employment Data'
server = app.server

app.scripts.config.serve_locally = True

app.css.append_css({'external_url': 'https://codepen.io/shermjj/pen/ZREaLY.css'})
app.css.append_css({'external_url': 'https://fonts.googleapis.com/css?family=Open+Sans'})

app.layout = html.Div(
    [
        html.Div([
            html.Div([
                html.H1([html.Strong('Nine '), ' years of graduate employment data in ',
                         html.Strong('Five '), 'public universities'],
                        style={'text-align': 'center', 'fontFamily': 'Open Sans', 'padding': '30px 0px'}),
                html.H1([html.Span('NUS ', style={'color': COLOR_DICT['NUS']}),
                         html.Span('NTU ', style={'color': COLOR_DICT['NTU']}),
                         html.Span('SMU ', style={'color': COLOR_DICT['SMU']}),
                         html.Span('SUTD ', style={'color': COLOR_DICT['SUTD']}),
                         html.Span('SIT', style={'color': COLOR_DICT['SIT']})],
                        style={'text-align': 'center'})
            ], style={'margin': 'auto'}),
            html.Hr(style={'width': '75%', 'margin': 'auto'}),
            html.Div([
                html.H4([html.Div("Unsure of what to study for in uni? Not passionate about any particular subject?"),
                         html.Div('Passion is overrated - try money instead!')],
                        style={'text-align': 'center', 'fontFamily': 'Open Sans'}),
            ], style={'width': '80%', 'margin': 'auto', 'padding': '20px 0px'}),
            html.P(
                'Click and drag to zoom in and out. Check the top right hand corner of the graph for more options. '
                '(This site works best on non mobile devices)'),
            html.Div([
                dcc.Dropdown(
                    id='yaxis-type-1',
                    options=[{'label': 'Median Salary (Nominal)', 'value': 'SAL1'},
                             {'label': 'Median Salary (Inflation Adjusted)', 'value': 'SAL2'}],
                    value='SAL1',
                    searchable=False,
                    clearable=False,
                    className='three columns'),
                dcc.Slider(
                    id='year-slider-1',
                    min=df.index.min(),
                    max=df.index.max(),
                    value=df.index.max(),
                    step=None,
                    marks={str(year): str(year) for year in df.index.unique()},
                    className='nine columns')
            ], className='row'),
            dcc.Graph(id='graph-1'),
            html.Hr(),
            html.Div([
                dcc.Dropdown(
                    id='yaxis-type-2',
                    options=[{'label': 'Full-Time Employment Rate', 'value': 'FTER'},
                             {'label': 'Mean Salary (Nominal)', 'value': 'SAL1'},
                             {'label': 'Mean Salary (Inflation Adjusted)', 'value': 'SAL2'}],
                    value='FTER',
                    searchable=False,
                    clearable=False,
                    className='three columns'),
                dcc.Slider(
                    id='year-slider-2',
                    min=df.index.min(),
                    max=df.index.max(),
                    value=df.index.max(),
                    step=None,
                    marks={str(year): str(year) for year in df.index.unique()},
                    className='nine columns')
            ], className='row'),

            dcc.Graph(id='graph-2'),
            html.Hr(),
            html.Div([
                dcc.Dropdown(
                    id='yaxis-type-3',
                    options=LINE_GRAPH_YAXIS_OPTIONS,
                    value='Gross Monthly Salary Mean',
                    searchable=False,
                    clearable=False,
                    className='three columns'
                ),
                dcc.Dropdown(
                    id='course-slider-3',
                    options=LINE_GRAPH_COURSEOPTIONS,
                    multi=True,
                    value=LINE_GRAPH_DEFAULT,
                    placeholder="Type in a course to search.... (or try the 'sector average'!)",
                    className='nine columns')
            ], className='row'),

            dcc.Graph(id='graph-3'),

            html.P('Source: Ministry of Education, data.gov.sg and sgcharts.sg)')

        ], className='container'),

    ])


@app.callback(
    dash.dependencies.Output('graph-1', 'figure'),
    [dash.dependencies.Input('year-slider-1', 'value'),
     dash.dependencies.Input('yaxis-type-1', 'value')])
def update_figure1(selected_year, yaxis_type):
    if yaxis_type == 'SAL1':
        choice_array = ['Gross Monthly Salary Median',
                        'Gross Monthly Salary 25th Percentile', 'Gross Monthly Salary 75th Percentile']
    else:
        choice_array = ['Gross Monthly Salary Median (Inflation Adjusted)',
                        'Gross Monthly Salary 25th Percentile (Inflation Adjusted)',
                        'Gross Monthly Salary 75th Percentile (Inflation Adjusted)']
    filtered_df = df.loc[selected_year, ['Classification',
                                         'combined',
                                         choice_array[0],
                                         choice_array[1],
                                         choice_array[2],
                                         'Institution']]
    traces = []
    for arr in filtered_df.values:
        traces.append(go.Box(
            y=[arr[3], arr[3], arr[2], arr[2], arr[4], arr[4]],
            name=arr[1],
            x0=arr[0],
            marker={'color': COLOR_DICT[arr[5]]},
            hoverinfo='y+name',
            hoverlabel={'namelength': -1}
        ))

    return {
        'data': traces,
        'layout': go.Layout(
            yaxis={'title': choice_array[0],
                   'type': 'linear',
                   'dtick': 250},
            height=700,
            boxmode='group',
            showlegend=False,
            plot_bgcolor='rgb(243, 243, 243)',
            paper_bgcolor='rgb(243, 243, 243)',
            margin=go.Margin(
                l=50,
                r=0,
                b=20,
                t=0
            )
        )
    }


@app.callback(
    dash.dependencies.Output('graph-2', 'figure'),
    [dash.dependencies.Input('year-slider-2', 'value'),
     dash.dependencies.Input('yaxis-type-2', 'value')])
def update_figure2(selected_year, yaxis_type):
    filtered_df = df.loc[selected_year, ['Classification',
                                         'combined',
                                         SCATTER_GRAPH_CHOICE_DICT[yaxis_type],
                                         'Institution']]
    traces = []
    for arr in filtered_df.values:
        traces.append(go.Scatter(
            y=[arr[2]],
            name=arr[1],
            x=[arr[0]],
            marker={'color': COLOR_DICT[arr[3]]},
            hoverinfo='y+name',
            hoverlabel={'namelength': -1},

        ))
    tick = 0.05 if yaxis_type == 'FTER' else 250
    return {
        'data': traces,
        'layout': go.Layout(
            yaxis={'title': SCATTER_GRAPH_CHOICE_DICT[yaxis_type],
                   'type': 'linear',
                   'dtick': tick
                   },
            height=700,
            boxmode='group',
            showlegend=False,
            plot_bgcolor='rgb(243, 243, 243)',
            paper_bgcolor='rgb(243, 243, 243)',
            margin=go.Margin(
                l=50,
                r=0,
                b=20,
                t=0
            )
        )
    }


@app.callback(
    dash.dependencies.Output('graph-3', 'figure'),
    [dash.dependencies.Input('course-slider-3', 'value'),
     dash.dependencies.Input('yaxis-type-3', 'value')])
def update_figure3(classes, yaxis_option):
    traces = []
    if classes is not None and yaxis_option is not None:
        for clas in classes:
            traces.append(
                go.Scatter(
                    y=list(df.loc[df['combined'] == clas].loc[:,
                           yaxis_option].values),
                    x=list(df.loc[df['combined'] == clas].loc[:,
                           yaxis_option].index),
                    text=clas,
                    name=clas,
                    hoverinfo='y+text',
                    showlegend=True,
                    legendgroup=df.loc[df['combined'] == clas].loc[:, 'Classification'].values[0],
                    marker={'symbol': LINE_GRAPH_SHAPES[df.loc[df['combined'] == clas].loc[:,
                                                        'Classification'].values[0]],
                            'size': 10}
                )
            )
    tick = 0.05 if yaxis_option == 'Full-Time Permanent Employment Rate' else 200
    return {
        'data': traces,
        'layout': go.Layout(
            yaxis={'title': yaxis_option, 'type': 'linear', 'dtick': tick},
            height=700,
            legend={'bgcolor': 'rgba(192,192,192,0.1)', 'x': 0},
            plot_bgcolor='rgb(243, 243, 243)',
            paper_bgcolor='rgb(243, 243, 243)',
            margin=go.Margin(
                l=50,
                r=0,
                b=20,
                t=0
            )

        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)
