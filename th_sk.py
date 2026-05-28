import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go

def bar_sk_3():
    # Read Excel file
    file_path = 'data/Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-3I-COMBINE', skiprows=7, nrows=69)
    df = df.iloc[:, 1:]

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['DSU_TH_TOT'], name='Data Structure Using C theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['DSU_PR_TOT'], name='Data Structure Using C practical total'))
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
    th_sk_html3 = pio.to_html(fig, include_plotlyjs=False)

    return th_sk_html3


def bar_sk_6():
    # Read Excel file
    file_path = 'data/Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-6I-combine', skiprows=7, nrows=68)
    df = df.iloc[:, 1:]

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['PWP_TH_TOT'], name='Programming with Python theory total'))
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['PWP_PR_TOT'], name='Programming with Python practical total'))
   
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
    th_sk_html6 = pio.to_html(fig, include_plotlyjs=False)

    return th_sk_html6
