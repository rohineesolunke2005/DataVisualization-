import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go

def bar_pt_5():
    # Read Excel file
    file_path = 'data/Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-5I-combine', skiprows=7, nrows=68)
    df = df.iloc[:, 1:]

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['STE_TH_TOT'], name='Software Testing theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['STE_PR_TOT'], name='Software Testing practical total'))
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
    th_pt_html5 = pio.to_html(fig, include_plotlyjs=False)

    return th_pt_html5

def bar_pt_6():
    # Read Excel file
    file_path = 'data/Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-6I-combine', skiprows=7, nrows=68)
    df = df.iloc[:, 1:]

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['ETI_TH_ESE'], name='eti_th_tot'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['ETI_TH_PA'], name='eti_pr_tot'))
   
    # Update layout
    fig.update_layout(
        width=1480,  # Set the width of the chart to 800 pixels
        height=900, # Set the height of the chart to 600 pixels
        xaxis=dict(tickangle=90),
        xaxis_title='Name Of Student',
        yaxis_title='Total Marks',
        barmode='stack'
    )

    # Convert Plotly figure to HTML
    th_pt_html6 = pio.to_html(fig, include_plotlyjs=False)

    return th_pt_html6
