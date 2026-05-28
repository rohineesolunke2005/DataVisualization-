import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go

def fail_1():
    file_path2 = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
    df2 = pd.read_excel(file_path2, sheet_name='CO-1I', skiprows=73, nrows=5)
    df2 = df2.iloc[:, 3:]
    pass_stud = df2[df2['Categories'] == '% pass']
    
    pass_marks = pass_stud[['ENG_TH_TOT', 'ENG_PR_TOT', 'BSC_TH_TOT', 'BSC_PR_TOT', 'BMS_TH_TOT', 'ICT_PR_TOT', 'EGE_PR_TOT', 'WPC_PR_TOT']].values.flatten().tolist()
    subjects=[ 'english theory total', 'english practical total', 'science theory total', 'science practical total', 'maths theory total', 'ICT practical total',  'EGE practical total',  'WPC practical total']

    
    # Calculate fail percentages for the specified subjects
    fail_marks = [100 - mark for mark in pass_marks]
    
    # Create a pie donut chart using Plotly
    fig = go.Figure(data=[
        go.Pie(labels=subjects, values=pass_marks, hole=0.3, name='Pass Marks',marker=dict(line=dict(color='black', width=0.2))),
        go.Pie(labels=subjects, values=fail_marks, hole=0.8, name='Fail Marks',marker=dict(line=dict(color='black', width=0.2)))
    ])
    
    # Update layout for the chart
    fig.update_layout(title='Pass and Fail Marks Distribution by Subject',
                      annotations=[dict(text='Pass Marks', x=0.46, y=0.5, font_size=20, showarrow=False),
                                   dict(text='Fail Marks', x=0.85, y=0.5, font_size=20, showarrow=False)],
                      width=1350,  # Set the width of the chart to 800 pixels
                      height=800, # Set the height of the chart to 600 pixels
        )
    
    # Show the chart
    fail_html1 = pio.to_html(fig, include_plotlyjs=False)
    return fail_html1


def fail_2():
    file_path2 = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
    df2 = pd.read_excel(file_path2, sheet_name='CO-2I', skiprows=65, nrows=6)
    df2 = df2.iloc[:, 3:]
    pass_stud = df2[df2['Categories'] == '% pass']
    
    pass_marks = pass_stud[['EEC_TH_TOT','EEC_PR_TOT','AMI_TH_TOT','BEC_TH_TOT','BEC_PR_TOT','PCI_TH_TOT','PCI_PR_TOT','BCC_PR_TOT','CPH_PR_TOT','WPD_PR_TOT']].values.flatten().tolist()
    subjects=['Elements of Electrical Engineering theory total','Elements of Electrical Engineering practical total','Applied Mathematics theory total','Basic Electronics theory total','Basic Electronics practical total','Programming in C theory total','Programming in C practical total','BCC practical total','CPH practical total','WPD practical total']

    
    # Calculate fail percentages for the specified subjects
    fail_marks = [100 - mark for mark in pass_marks]
    
    # Create a pie donut chart using Plotly
    fig = go.Figure(data=[
        go.Pie(labels=subjects, values=pass_marks, hole=0.3, name='Pass Marks',marker=dict(line=dict(color='black', width=0.2))),
        go.Pie(labels=subjects, values=fail_marks, hole=0.8, name='Fail Marks',marker=dict(line=dict(color='black', width=0.2)))
    ])
    
    # Update layout for the chart
    fig.update_layout(title='Pass and Fail Marks Distribution by Subject',
                      annotations=[dict(text='Pass Marks', x=0.46, y=0.5, font_size=20, showarrow=False),
                                   dict(text='Fail Marks', x=0.85, y=0.5, font_size=20, showarrow=False)],
                      width=1350,  # Set the width of the chart to 800 pixels
                      height=800, # Set the height of the chart to 600 pixels
        )
    
    # Show the chart
    fail_html2 = pio.to_html(fig, include_plotlyjs=False)
    return fail_html2

def fail_3():
    file_path2 = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
    df2 = pd.read_excel(file_path2, sheet_name='CO-3I-COMBINE', skiprows=80, nrows=5)
    df2 = df2.iloc[:, 4:]
    pass_stud = df2[df2['Categories'] == '% pass']
    
    
    pass_marks=pass_stud[['OOP_TH_TOT','OOP_PR_TOT','DSU_TH_TOT','DSU_PR_TOT','CGR_TH_TOT','CGR_PR_TOT','DMS_TH_TOT','DMS_PR_TOT','DTE_TH_TOT','DTE_PR_TOT']].values.flatten().tolist()
    subjects=['Object Oriented Programming theory total','Object Oriented Programming practical total','Data Structure Using C theory total','Data Structure Using C practical total','Computer Graphics theory total','Computer Graphics practical total','Data Base Management System theory total','Data Base Management System practical total','Digital Techniques theory total','Digital Techniques practical total']

    
    # Calculate fail percentages for the specified subjects
    fail_marks = [100 - mark for mark in pass_marks]
    
    # Create a pie donut chart using Plotly
    fig = go.Figure(data=[
        go.Pie(labels=subjects, values=pass_marks, hole=0.3, name='Pass Marks',marker=dict(line=dict(color='black', width=0.2))),
        go.Pie(labels=subjects, values=fail_marks, hole=0.8, name='Fail Marks',marker=dict(line=dict(color='black', width=0.2)))
    ])
    
    # Update layout for the chart
    fig.update_layout(title='Pass and Fail Marks Distribution by Subject',
                      annotations=[dict(text='Pass Marks', x=0.46, y=0.5, font_size=20, showarrow=False),
                                   dict(text='Fail Marks', x=0.85, y=0.5, font_size=20, showarrow=False)],
                      width=1350,  # Set the width of the chart to 800 pixels
                      height=800, # Set the height of the chart to 600 pixels
        )
    
    # Show the chart
    fail_html3 = pio.to_html(fig, include_plotlyjs=False)
    return fail_html3

def fail_4():
    file_path2 = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
    df2 = pd.read_excel(file_path2, sheet_name='CO-4I-COMBINE', skiprows=78, nrows=5)
    df2 = df2.iloc[:, 4:]
    pass_stud = df2[df2['Categories'] == '% pass']
    
    pass_marks=pass_stud[['JPR_TH_TOT','JPR_PR_TOT','SEN_TH_TOT','SEN_PR_TOT','DCC_TH_TOT','DCC_PR_TOT','MPO_TH_TOT','MPO_PR_TOT','GAD_PR_TOT']].values.flatten().tolist()
    subjects=['Java theory total','Java practical total','Software Engineering theory total','Software Engineering practical total','Data Communication And Computer Network theory total','Data Communication And Computer Network practical total','Microprocessor theory total','Microprocessor practical total','GAD practical total']
  
    # Calculate fail percentages for the specified subjects
    fail_marks = [100 - mark for mark in pass_marks]
    
    # Create a pie donut chart using Plotly
    fig = go.Figure(data=[
        go.Pie(labels=subjects, values=pass_marks, hole=0.3, name='Pass Marks',marker=dict(line=dict(color='black', width=0.2))),
        go.Pie(labels=subjects, values=fail_marks, hole=0.8, name='Fail Marks',marker=dict(line=dict(color='black', width=0.2)))
    ])
    
    # Update layout for the chart
    fig.update_layout(title='Pass and Fail Marks Distribution by Subject',
                      annotations=[dict(text='Pass Marks', x=0.46, y=0.5, font_size=20, showarrow=False),
                                   dict(text='Fail Marks', x=0.85, y=0.5, font_size=20, showarrow=False)],
                      width=1350,  # Set the width of the chart to 800 pixels
                      height=800, # Set the height of the chart to 600 pixels
        )
    
    # Show the chart
    fail_html4 = pio.to_html(fig, include_plotlyjs=False)
    return fail_html4

def fail_5():
    file_path2 = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
    df2 = pd.read_excel(file_path2, sheet_name='CO-5I-combine', skiprows=79, nrows=5)
    df2 = df2.iloc[:, 4:]
    pass_stud = df2[df2['Categories'] == '% pass']
    
    pass_marks=pass_stud[['EST_TH_TOT','OSY_TH_TOT','OSY_PR_TOT','AJP_TH_TOT','AJP_PR_TOT','STE_TH_TOT','STE_PR_TOT','ACN_TH_TOT','ACN_PR_TOT','ITR_PR_TOT','CPP_PR_TOT']].values.flatten().tolist()
    subjects=['Environmental Studies theory total','Operating System theory total','Operating System practical total','Advance Java Programming theory total','Advance Java Programming pratical total','Software Testing theory total','Software Testing pratical total','Advance Computer Network theory total','Advance Computer Network practical total','ITR practical total','CPP practical total']

    # Calculate fail percentages for the specified subjects
    fail_marks = [100 - mark for mark in pass_marks]
    
    # Create a pie donut chart using Plotly
    fig = go.Figure(data=[
        go.Pie(labels=subjects, values=pass_marks, hole=0.3, name='Pass Marks',marker=dict(line=dict(color='black', width=0.2))),
        go.Pie(labels=subjects, values=fail_marks, hole=0.8, name='Fail Marks',marker=dict(line=dict(color='black', width=0.2)))
    ])
    
    # Update layout for the chart
    fig.update_layout(title='Pass and Fail Marks Distribution by Subject',
                      annotations=[dict(text='Pass Marks', x=0.46, y=0.5, font_size=20, showarrow=False),
                                   dict(text='Fail Marks', x=0.85, y=0.5, font_size=20, showarrow=False)],
                      width=1350,  # Set the width of the chart to 800 pixels
                      height=800, # Set the height of the chart to 600 pixels
        )
    
    # Show the chart
    fail_html5 = pio.to_html(fig, include_plotlyjs=False)
    return fail_html5

def fail_6():
    file_path2 = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
    df2 = pd.read_excel(file_path2, sheet_name='CO-6I-combine', skiprows=84, nrows=5)
    df2 = df2.iloc[:, 4:]
    pass_stud = df2[df2['Categories'] == '% pass']
    
    pass_marks=pass_stud[['MGT_TH_TOT','PWP_TH_TOT','PWP_PR_TOT','MAD_TH_TOT','MAD_PR_TOT','ETI_TH_TOT','NIS_TH_TOT','NIS_PR_TOT','EDE_PR_TOT','CPE_PR_TOT']].values.flatten().tolist()
    subjects=['Managment theory total','Programming with Python theory total','Programming with Python practical total','Mobile Application Development theory total','Mobile Application Development practical total','Emerging Trends theory total','Network in Security theory total','Network in Security practical total','EDE practical total','CPE practical total']

    # Calculate fail percentages for the specified subjects
    fail_marks = [100 - mark for mark in pass_marks]
    
    # Create a pie donut chart using Plotly
    fig = go.Figure(data=[
        go.Pie(labels=subjects, values=pass_marks, hole=0.3, name='Pass Marks',marker=dict(line=dict(color='black', width=0.2))),
        go.Pie(labels=subjects, values=fail_marks, hole=0.8, name='Fail Marks',marker=dict(line=dict(color='black', width=0.2)))
    ])
    
    # Update layout for the chart
    fig.update_layout(title='Pass and Fail Marks Distribution by Subject',
                      annotations=[dict(text='Pass Marks', x=0.46, y=0.5, font_size=20, showarrow=False),
                                   dict(text='Fail Marks', x=0.85, y=0.5, font_size=20, showarrow=False)],
                      width=1350,  # Set the width of the chart to 800 pixels
                      height=800, # Set the height of the chart to 600 pixels
        )
    
    # Show the chart
    fail_html6 = pio.to_html(fig, include_plotlyjs=False)
    return fail_html6