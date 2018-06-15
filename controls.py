from app import df

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


