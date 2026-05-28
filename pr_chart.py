import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go

# 1 sem
def scatter_1():
    file_path = 'data\Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-1I',skiprows=7,nrows=55)
    df = df.iloc[:, 1:]
    fig= go.Figure()
    # Create scatter plot
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['ENG_PR_TOT'], mode='markers', name='english theory Practical Total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['BSC_PR_TOT'], mode='markers', name='science theory Practical Total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['ICT_PR_TOT'], mode='markers', name='ICT Practical Total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['EGE_PR_TOT'], mode='markers', name='EGE Practical Total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['WPC_PR_TOT'], mode='markers', name='WPC Practical Total',marker=dict(size=12)))

    # Customize plot
    fig.update_layout(
        width=1480,  # Set the width of the chart to 800 pixels
        height=900,
        title='Scatter Plot',
        xaxis=dict(title='Name of Students'),
        yaxis=dict(title='Marks of practical subject')
    )

    # Convert Plotly figure to HTML
    pr_html1 = pio.to_html(fig, include_plotlyjs=False)

    return pr_html1

# 2 sem
def scatter_2():
    file_path = 'data\Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-2I',skiprows=7,nrows=55)
    df = df.iloc[:, 1:]
    fig= go.Figure()
    # Create scatter plot
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['EEC_PR_TOT'], mode='markers', name='Elements of Electrical Engineering practical total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['BCC_PR_TOT'], mode='markers', name='BCC practical total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['PCI_PR_TOT'], mode='markers', name='Programming in C  practical total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['CPH_PR_TOT'], mode='markers', name='CPH practical total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['WPD_PR_TOT'], mode='markers', name='WPD practical total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['BEC_PR_TOT'], mode='markers', name='Basic Electronics practical total',marker=dict(size=12)))

    # Customize plot
    fig.update_layout(
         width=1450,  # Set the width of the chart to 800 pixels
        height=900,
        title='Scatter Plot',
        xaxis=dict(title='Name of Students'),
        yaxis=dict(title='Marks of practical subject')
    )

    # Convert Plotly figure to HTML
    pr_html2 = pio.to_html(fig, include_plotlyjs=False)

    return pr_html2

# 3 sem
def scatter_3():
    file_path = 'data\Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-3I-COMBINE',skiprows=7,nrows=69)
    df = df.iloc[:, 1:]
    fig= go.Figure()
    # Create scatter plot
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['OOP_PR_TOT'], mode='markers', name='Object Oriented Programming practical total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['DSU_PR_TOT'], mode='markers', name='Data Structure Using C practical total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['CGR_PR_TOT'], mode='markers', name='Computer Graphics practical total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['DMS_PR_TOT'], mode='markers', name='Data Base Management System practical total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['DTE_PR_TOT'], mode='markers', name='Digital Techniques practical total',marker=dict(size=12)))

    # Customize plot
    fig.update_layout(
        width=1500,  # Set the width of the chart to 800 pixels
        height=900,
        title='Scatter Plot',
        xaxis=dict(title='Name of Students'),
        yaxis=dict(title='Marks of practical subject')
    )

    # Convert Plotly figure to HTML
    pr_html3 = pio.to_html(fig, include_plotlyjs=False)

    return pr_html3

# 4 sem
def scatter_4():
    file_path = 'data\Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-4I-COMBINE',skiprows=7,nrows=69)
    df = df.iloc[:, 1:]
    fig= go.Figure()
    # Create scatter plot
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['JPR_PR_TOT'], mode='markers', name='Java practical total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['SEN_PR_TOT'], mode='markers', name='Software Engineering practical total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['DCC_PR_TOT'], mode='markers', name='Data Communication And Computer Network practical total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['MPO_PR_TOT'], mode='markers', name='Microprocessor practical total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['GAD_PR_TOT'], mode='markers', name='GAD practical total',marker=dict(size=12)))

    # Customize plot
    fig.update_layout(
        width=1500,  # Set the width of the chart to 800 pixels
        height=900,
        title='Scatter Plot',
        xaxis=dict(title='Name of Students'),
        yaxis=dict(title='Marks of practical subject')
    )

    # Convert Plotly figure to HTML
    pr_html4 = pio.to_html(fig, include_plotlyjs=False)

    return pr_html4

# 5 sem
def scatter_5():
    file_path = 'data\Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-5I-combine',skiprows=7,nrows=68)
    df = df.iloc[:, 1:]
    fig= go.Figure()
    # Create scatter plot
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['OSY_PR_TOT'], mode='markers', name='Operating System practical total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['AJP_PR_TOT'], mode='markers', name='Advance Java Programming practical total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['STE_PR_TOT'], mode='markers', name='Software Testing practical total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['ACN_PR_TOT'], mode='markers', name='Advance Computer Network practical total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['ITR_PR_TOT'], mode='markers', name='ITR practical total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['CPP_PR_TOT'], mode='markers', name='CPP practical total',marker=dict(size=12)))
    # Customize plot
    fig.update_layout(
        width=1500,  # Set the width of the chart to 800 pixels
        height=900,
        title='Scatter Plot',
        xaxis=dict(title='Name of Students'),
        yaxis=dict(title='Marks of practical subject')
    )

    # Convert Plotly figure to HTML
    pr_html5 = pio.to_html(fig, include_plotlyjs=False)

    return pr_html5

# 6 sem
def scatter_6():
    file_path = 'data\Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-6I-combine',skiprows=7,nrows=68)
    df = df.iloc[:, 1:]
    fig= go.Figure()
    # Create scatter plot
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['PWP_PR_TOT'], mode='markers', name='Programming with Python practical total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['MAD_PR_TOT'], mode='markers', name='Mobile Application Development practical total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['NIS_PR_TOT'], mode='markers', name='Network in Security practical total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['EDE_PR_TOT'], mode='markers', name='EDE practical total',marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=df['Name Of Student'], y=df['CPE_PR_TOT'], mode='markers', name='CPE practical total',marker=dict(size=12)))

    # Customize plot
    fig.update_layout(
        width=1500,  # Set the width of the chart to 800 pixels
        height=900,
        title='Scatter Plot',
        xaxis=dict(title='Name of Students'),
        yaxis=dict(title='Marks of practical subject')
    )

    # Convert Plotly figure to HTML
    pr_html6 = pio.to_html(fig, include_plotlyjs=False)

    return pr_html6