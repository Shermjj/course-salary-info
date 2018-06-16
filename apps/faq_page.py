import dash_html_components as html
import dash_core_components as dcc


layout = html.Div([
    html.Div([dcc.Link(html.I(className='chevron left icon',
                              style={'position': 'absolute', 'top': '35px', 'font-size': '30px',
                                     'text-decoration': 'none', 'color': 'black'}), href='/'),
              html.H3('FAQ', style={'text-align': 'center'})], className='ui block header'),
    html.H4('How do I zoom out/pan the graph?'),
    html.P('Select the zoom out/pan option in the toolbar available on the top right side of the graph'),
    html.H4('How do I stop all the hover labels on the same x axis from showing up at the same time?'),
    html.P('Change the hover behavior on the graph toolbar to "Show Closest Data on Hover"'),
    html.H4("What's the difference between nominal and inflation adjusted?"),
    html.P(
        'Nominal wages do not account for the fact that inflation erodes purchasing power of wages. '
        'So a $3000 salary in 2010 would have higher purchasing power than $3000 today. '
        'Hence, we adjust past year wages to 2017 dollars in order to more accurately compare historical wage data.'),
    html.H4('Where is (insert course here)?'),
    html.P('Data here is limited to the data available from the survey'),
    html.H4('Where did this data come from?'),
    html.P('All the data here is obtained from the annual Ministry of Education graduate employment survey (GES).'),
    html.H4('How accurate is the data?'),
    html.P('As the data is entirely self-reported, there are inherent statistical biases in the data. '
           'Hence, the data available here is at best, indicative.'),
    html.H4('Can I view the source code?'),
    html.P(['The source code is available on github ',
            html.A('here', href='https://github.com/Shermjj/course-salary-info')]),
    html.H4('I have feedback/suggestions/bug reports!'),
    html.P('Feel free to email knujjia@gmail.com for any sort of feedback'),

], className='container-faq')
