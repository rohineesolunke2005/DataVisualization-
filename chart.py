import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go


def stack_bar_1():
    # Read Excel file
    file_path = 'data/Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-1I', skiprows=7, nrows=55)
    df = df.iloc[:, 1:]

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['ENG_TH_TOT'], name='english theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['BSC_TH_TOT'], name='science theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['BMS_TH_TOT'], name='maths theory total'))

    # Update layout
    fig.update_layout(
        width=1450,  # Set the width of the chart to 800 pixels
        height=900, # Set the height of the chart to 600 pixels
        xaxis=dict(tickangle=90),
        xaxis_title='Name Of Student',
        yaxis_title='Total Marks',
        barmode='stack'
    )

    # Convert Plotly figure to HTML
    chart_html1 = pio.to_html(fig, include_plotlyjs=False)

    return chart_html1

def stack_bar_2():
    # Read Excel file
    file_path = 'data/Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-2I', skiprows=7, nrows=55)
    df = df.iloc[:, 1:]

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['EEC_TH_TOT'], name='Elements of Electrical Engineering theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['AMI_TH_TOT'], name='Applied Mathematics theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['BEC_TH_TOT'], name='Basic Electronics theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['PCI_TH_TOT'], name='Programming in C theory total'))

    # Update layout
    fig.update_layout(
        width=1450,  # Set the width of the chart to 800 pixels
        height=900, # Set the height of the chart to 600 pixels
        xaxis=dict(tickangle=90),
        xaxis_title='Name Of Student',
        yaxis_title='Total Marks',
        barmode='stack'
    )

    # Convert Plotly figure to HTML
    chart_html2 = pio.to_html(fig, include_plotlyjs=False)

    return chart_html2

def stack_bar_3():
    # Read Excel file
    file_path = 'data/Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-3I-COMBINE', skiprows=7, nrows=69)
    df = df.iloc[:, 1:]

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['OOP_TH_TOT'], name='Object Oriented Programming theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['DSU_TH_TOT'], name='Data Structure Using C theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['CGR_TH_TOT'], name='Computer Graphics theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['DMS_TH_TOT'], name='Data Base Management System theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['DTE_TH_TOT'], name='Digital Techniques theory total'))    
    # Update layout
    fig.update_layout(
        width=1450,  # Set the width of the chart to 800 pixels
        height=900, # Set the height of the chart to 600 pixels
        xaxis=dict(tickangle=90),
        xaxis_title='Name Of Student',
        yaxis_title='Total Marks',
        barmode='stack'
    )

    # Convert Plotly figure to HTML
    chart_html3 = pio.to_html(fig, include_plotlyjs=False)

    return chart_html3

def stack_bar_4():
    # Read Excel file
    file_path = 'data/Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-4I-COMBINE', skiprows=7, nrows=69)
    df = df.iloc[:, 1:]

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['JPR_TH_TOT'], name='Java theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['SEN_TH_TOT'], name='Software Engineering theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['DCC_TH_TOT'], name='Data Communication And Computer Network theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['MPO_TH_TOT'], name='Microprocessor theory total'))

    # Update layout
    fig.update_layout(
        width=1450,  # Set the width of the chart to 800 pixels
        height=900, # Set the height of the chart to 600 pixels
        xaxis=dict(tickangle=90),
        xaxis_title='Name Of Student',
        yaxis_title='Total Marks',
        barmode='stack'
    )

    # Convert Plotly figure to HTML
    chart_html4 = pio.to_html(fig, include_plotlyjs=False)

    return chart_html4

def stack_bar_5():
    # Read Excel file
    file_path = 'data/Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-5I-combine', skiprows=7, nrows=68)
    df = df.iloc[:, 1:]

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['EST_TH_TOT'], name='Environmental Studies theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['OSY_TH_TOT'], name='Operating System theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['AJP_TH_TOT'], name='Advance Java Programming theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['STE_TH_TOT'], name='Software Testing theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['ACN_TH_TOT'], name='Advance Computer Network theory total'))    
    # Update layout
    fig.update_layout(
        width=1450,  # Set the width of the chart to 800 pixels
        height=900, # Set the height of the chart to 600 pixels
        xaxis=dict(tickangle=90),
        xaxis_title='Name Of Student',
        yaxis_title='Total Marks',
        barmode='stack'
    )

    # Convert Plotly figure to HTML
    chart_html5 = pio.to_html(fig, include_plotlyjs=False)

    return chart_html5

def stack_bar_6():
    # Read Excel file
    file_path = 'data/Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-6I-combine', skiprows=7, nrows=68)
    df = df.iloc[:, 1:]

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['MGT_TH_TOT'], name='Managment theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['PWP_TH_TOT'], name='Programming with Python theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['MAD_TH_TOT'], name='Mobile Application Development theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['ETI_TH_TOT'], name='Emerging Trends theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['NIS_TH_TOT'], name='Network in Security theory total'))    
    # Update layout
    fig.update_layout(
        width=1450,  # Set the width of the chart to 800 pixels
        height=900, # Set the height of the chart to 600 pixels
        xaxis=dict(tickangle=90),
        xaxis_title='Name Of Student',
        yaxis_title='Total Marks',
        barmode='stack'
    )

    # Convert Plotly figure to HTML
    chart_html6 = pio.to_html(fig, include_plotlyjs=False)

    return chart_html6
