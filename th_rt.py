import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go


def bar_rt_2():
    # Read Excel file
    file_path = 'data/Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-2I', skiprows=7, nrows=55)
    df = df.iloc[:, 1:]

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['WPD_PR_ESE'], name='wpd_pr_ese'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['WPD_PR_PA'], name='wpd_pr_pa'))

    # Update layout
    fig.update_layout(
        width=1460,  # Set the width of the chart to 800 pixels
        height=900, # Set the height of the chart to 600 pixels
        xaxis=dict(tickangle=90),
        xaxis_title='Name Of Student',
        yaxis_title='Total Marks',
        barmode='stack'
    )

    # Convert Plotly figure to HTML
    th_rt_html2 = pio.to_html(fig, include_plotlyjs=False)

    return th_rt_html2


def bar_rt_3():
    # Read Excel file
    file_path = 'data/Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-3I-COMBINE', skiprows=7, nrows=69)
    df = df.iloc[:, 1:]

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['DMS_TH_TOT'], name='Data Base Management System theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['DMS_PR_TOT'], name='Data Base Management System practical total'))
    # Update layout
    fig.update_layout(
        width=1480,  # Set the width of the chart to 800 pixels
        height=900, # Set the height of the chart to 600 pixels
        xaxis=dict(tickangle=90),
        xaxis_title='Name Of Student',
        yaxis_title='Total Marks',
        barmode='group'
    )

    # Convert Plotly figure to HTML
    th_bh_html3 = pio.to_html(fig, include_plotlyjs=False)

    return th_bh_html3

def bar_rt_4():
    # Read Excel file
    file_path = 'data/Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-4I-COMBINE', skiprows=7, nrows=69)
    df = df.iloc[:, 1:]

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['DCC_TH_TOT'], name='Data Communication And Computer Network theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['DCC_PR_TOT'], name='Data Communication And Computer Network practical total'))
    # Update layout
    fig.update_layout(
        width=1480,  # Set the width of the chart to 800 pixels
        height=900, # Set the height of the chart to 600 pixels
        xaxis=dict(tickangle=90),
        xaxis_title='Name Of Student',
        yaxis_title='Total Marks',
        barmode='group'
    )

    # Convert Plotly figure to HTML
    th_rt_html4 = pio.to_html(fig, include_plotlyjs=False)

    return th_rt_html4

def bar_rt_5():
    # Read Excel file
    file_path = 'data/Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-5I-combine', skiprows=7, nrows=68)
    df = df.iloc[:, 1:]

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['ACN_TH_TOT'], name='Advance Computer Network theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['ACN_PR_TOT'], name='Advance Computer Network practical total'))
    # Update layout
    fig.update_layout(
        width=1480,  # Set the width of the chart to 800 pixels
        height=900, # Set the height of the chart to 600 pixels
        xaxis=dict(tickangle=90),
        xaxis_title='Name Of Student',
        yaxis_title='Total Marks',
        barmode='group'
    )

    # Convert Plotly figure to HTML
    th_rt_html5 = pio.to_html(fig, include_plotlyjs=False)

    return th_rt_html5

def bar_rt_6():
    # Read Excel file
    file_path = 'data/Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-6I-combine', skiprows=7, nrows=68)
    df = df.iloc[:, 1:]

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['NIS_TH_TOT'], name='Network in Security theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['NIS_PR_TOT'], name='Network in Security practical total'))
   
    # Update layout
    fig.update_layout(
        width=1480,  # Set the width of the chart to 800 pixels
        height=900, # Set the height of the chart to 600 pixels
        xaxis=dict(tickangle=90),
        xaxis_title='Name Of Student',
        yaxis_title='Total Marks',
        barmode='group'
    )

    # Convert Plotly figure to HTML
    th_rt_html6 = pio.to_html(fig, include_plotlyjs=False)

    return th_rt_html6
