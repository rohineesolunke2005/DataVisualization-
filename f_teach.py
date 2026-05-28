import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go
def front_1():
    
    # Read Excel file
    file_path = 'data/Toppers List.xlsx'
    df = pd.read_excel(file_path,engine='openpyxl')
    fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),font=dict(size=20)),
    cells=dict(values=[df[col] for col in df.columns],font=dict(size=18)))
    ])
    # Adjust layout to increase the size of the table
    fig.update_layout(width=1300, height=500)
    front_html1 = pio.to_html(fig, include_plotlyjs=False)
    return front_html1
