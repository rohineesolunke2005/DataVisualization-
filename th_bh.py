import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go


def bar_bh_1():
    # Read Excel file
    file_path = 'data/Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-1I', skiprows=7, nrows=55)
    df = df.iloc[:, 1:]

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['ICT_PR_ESE'], name='ict_pr_ese'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['ICT_PR_PA'], name='ict_pr_pa'))

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
    th_bh_html1 = pio.to_html(fig, include_plotlyjs=False)

    return th_bh_html1


def bar_bh_3():
    # Read Excel file
    file_path = 'data/Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-3I-COMBINE', skiprows=7, nrows=69)
    df = df.iloc[:, 1:]

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['OOP_TH_TOT'], name='Object Oriented Programming theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['OOP_PR_TOT'], name='Object Oriented Programming practical total'))
    # Update layout
    fig.update_layout(
        width=1650,  # Set the width of the chart to 800 pixels
        height=900, # Set the height of the chart to 600 pixels
        xaxis=dict(tickangle=90),
        xaxis_title='Name Of Student',
        yaxis_title='Total Marks',
        barmode='group'
    )

    # Convert Plotly figure to HTML
    th_bh_html3 = pio.to_html(fig, include_plotlyjs=False)

    return th_bh_html3

def bar_bh_6():
    # Read Excel file
    file_path = 'data/Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-6I-combine', skiprows=7, nrows=68)
    df = df.iloc[:, 1:]

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['MAD_TH_TOT'], name='Mobile Application Development theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['MAD_PR_TOT'], name='Mobile Application Development practical total'))
   
    # Update layout
    fig.update_layout(
        width=1650,  # Set the width of the chart to 800 pixels
        height=900, # Set the height of the chart to 600 pixels
        xaxis=dict(tickangle=90),
        xaxis_title='Name Of Student',
        yaxis_title='Total Marks',
        barmode='group'
    )

    # Convert Plotly figure to HTML
    th_bh_html6 = pio.to_html(fig, include_plotlyjs=False)

    return th_bh_html6
