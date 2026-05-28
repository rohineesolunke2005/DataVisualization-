import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

def all_mk_1():
    # Read Excel file
    file_path = 'data/Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-1I', skiprows=7, nrows=55)
    df = df.iloc[:, 1:]

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['PER'], name='percentage'))

    # Define threshold values, corresponding colors, and labels
    thresholds = [ 60, 75]
    colors = [ 'yellow', 'green']
    labels = [ 'First Class', 'First Class dis']
    # Add threshold lines
    for threshold, color, label in zip(thresholds, colors, labels):
        fig.add_trace(go.Scatter(x=[df['Name Of Student'].iloc[0], df['Name Of Student'].iloc[-1]],y=[threshold, threshold],
                                 mode='lines',name=label,line=dict(color=color, width=3, dash='dash')))

    # Update layout
    fig.update_layout(
        width=1450,  # Set the width of the chart to 1450 pixels
        height=900,  # Set the height of the chart to 900 pixels
        xaxis=dict(tickangle=90),
        xaxis_title='Name Of Student',
        yaxis_title='Total Marks'
    )

    # Convert Plotly figure to HTML
    all_html = pio.to_html(fig, include_plotlyjs=False)

    return all_html

def all_mk_2():
    # Read Excel file
    file_path = 'data/Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-2I', skiprows=7, nrows=55)
    df = df.iloc[:, 1:]

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['PER'], name='percentage'))

    thresholds = [ 60, 75]
    colors = [ 'yellow', 'green']
    labels = [ 'First Class', 'First Class dis']
    # Add threshold lines
    for threshold, color, label in zip(thresholds, colors, labels):
        fig.add_trace(go.Scatter(x=[df['Name Of Student'].iloc[0], df['Name Of Student'].iloc[-1]],y=[threshold, threshold],
                                 mode='lines',name=label,line=dict(color=color, width=3, dash='dash')))

    # Update layout
    fig.update_layout(
        width=1450,  # Set the width of the chart to 1450 pixels
        height=900,  # Set the height of the chart to 900 pixels
        xaxis=dict(tickangle=90),
        xaxis_title='Name Of Student',
        yaxis_title='Total Marks'
    )

    # Convert Plotly figure to HTML
    all_html2 = pio.to_html(fig, include_plotlyjs=False)

    return all_html2

def all_mk_3():
    # Read Excel file
    file_path = 'data/Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-3I-COMBINE', skiprows=7, nrows=69)
    df = df.iloc[:, 1:]

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['PER'], name='percentage'))

    thresholds = [ 60, 75]
    colors = [ 'yellow', 'green']
    labels = [ 'First Class', 'First Class dis']
    # Add threshold lines
    for threshold, color, label in zip(thresholds, colors, labels):
        fig.add_trace(go.Scatter(x=[df['Name Of Student'].iloc[0], df['Name Of Student'].iloc[-1]],y=[threshold, threshold],
                                 mode='lines',name=label,line=dict(color=color, width=3, dash='dash')))

    # Update layout
    fig.update_layout(
        width=1450,  # Set the width of the chart to 1450 pixels
        height=900,  # Set the height of the chart to 900 pixels
        xaxis=dict(tickangle=90),
        xaxis_title='Name Of Student',
        yaxis_title='Total Marks'
    )

    # Convert Plotly figure to HTML
    all_html3 = pio.to_html(fig, include_plotlyjs=False)

    return all_html3

def all_mk_4():
    # Read Excel file
    file_path = 'data/Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-4I-COMBINE', skiprows=7, nrows=69)
    df = df.iloc[:, 1:]

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['PER'], name='percentage'))

    thresholds = [ 60, 75]
    colors = [ 'yellow', 'green']
    labels = [ 'First Class', 'First Class dis']
    # Add threshold lines
    for threshold, color, label in zip(thresholds, colors, labels):
        fig.add_trace(go.Scatter(x=[df['Name Of Student'].iloc[0], df['Name Of Student'].iloc[-1]],y=[threshold, threshold],
                                 mode='lines',name=label,line=dict(color=color, width=3, dash='dash')))

    # Update layout
    fig.update_layout(
        width=1450,  # Set the width of the chart to 1450 pixels
        height=900,  # Set the height of the chart to 900 pixels
        xaxis=dict(tickangle=90),
        xaxis_title='Name Of Student',
        yaxis_title='Total Marks'
    )

    # Convert Plotly figure to HTML
    all_html4 = pio.to_html(fig, include_plotlyjs=False)

    return all_html4

def all_mk_5():
    # Read Excel file
    file_path = 'data/Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-5I-combine', skiprows=7, nrows=68)
    df = df.iloc[:, 1:]

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['PER'], name='percentage'))

    thresholds = [ 60, 75]
    colors = [ 'yellow', 'green']
    labels = [ 'First Class', 'First Class dis']
    # Add threshold lines
    for threshold, color, label in zip(thresholds, colors, labels):
        fig.add_trace(go.Scatter(x=[df['Name Of Student'].iloc[0], df['Name Of Student'].iloc[-1]],y=[threshold, threshold],
                                 mode='lines',name=label,line=dict(color=color, width=3, dash='dash')))

    # Update layout
    fig.update_layout(
        width=1450,  # Set the width of the chart to 1450 pixels
        height=900,  # Set the height of the chart to 900 pixels
        xaxis=dict(tickangle=90),
        xaxis_title='Name Of Student',
        yaxis_title='Total Marks'
    )

    # Convert Plotly figure to HTML
    all_html5 = pio.to_html(fig, include_plotlyjs=False)

    return all_html5

def all_mk_6():
    # Read Excel file
    file_path = 'data/Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-6I-combine', skiprows=7, nrows=68)
    df = df.iloc[:, 1:]

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Bar(x=df['Name Of Student'], y=df['PER'], name='percentage'))

    thresholds = [ 60, 75]
    colors = [ 'yellow', 'green']
    labels = [ 'First Class', 'First Class dis']
    # Add threshold lines
    for threshold, color, label in zip(thresholds, colors, labels):
        fig.add_trace(go.Scatter(x=[df['Name Of Student'].iloc[0], df['Name Of Student'].iloc[-1]],y=[threshold, threshold],
                                 mode='lines',name=label,line=dict(color=color, width=3, dash='dash')))


    # Update layout
    fig.update_layout(
        width=1450,  # Set the width of the chart to 1450 pixels
        height=900,  # Set the height of the chart to 900 pixels
        xaxis=dict(tickangle=90),
        xaxis_title='Name Of Student',
        yaxis_title='Total Marks'
    )

    # Convert Plotly figure to HTML
    all_html6 = pio.to_html(fig, include_plotlyjs=False)

    return all_html6