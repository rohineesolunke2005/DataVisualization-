import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go

def line_c(enrollment):
    # Specify the file path of the Excel file
    file_path = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
    sheet_names = ['CO-1I', 'CO-2I', 'CO-3I-COMBINE', 'CO-4I-COMBINE', 'CO-5I-combine', 'CO-6I-combine']

    # Read data from multiple sheets and filter based on enrollment number
    all_results = []
    enrollment_number = enrollment
    for sheet_name in sheet_names:
        df = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=7, nrows=69, dtype={'Enrollment Number': str})
        df = df.iloc[:, 1:]  # Remove the first column
        df['Enrollment Number'] = df['Enrollment Number'].astype(str).str.strip()
        result = df[df['Enrollment Number'] == enrollment_number]
        all_results.append(result)
    
    # Define semesters
    semesters = ['1st semester', '2nd semester', '3rd semester', '4th semester', '5th semester', '6th semester']

    # Extract 'PER' column values for each semester from all_results
    x_values = []
    y_values = []
    text_values = []  # List to store text annotations for each marker
    for result_df in all_results:
        if not result_df.empty:
            per_values = result_df['PER'].tolist()
            y_values.extend(per_values)
            text_values.extend(per_values)  # Use percentage values as text annotations
            # Access the 'Name Of Student' column from the DataFrame
            stud_name = result_df['Name Of Student'].iloc[0]  # Assuming there's only one student per sheet
            

    x_values.extend(semesters * len(all_results))

    # Create line chart
    '''fig = go.Figure(data=go.Scatter(x=x_values, y=y_values, mode='lines+markers', hoverinfo='x+y'))'''
    fig = go.Figure(data=go.Scatter(x=x_values, y=y_values, mode='lines+markers', hoverinfo='skip'))
    for x, y, text in zip(x_values, y_values, text_values):
        fig.add_annotation(
            x=x,
            y=y,
            text=str(text),  # Convert to string for annotation
            showarrow=False,  # Disable arrow for annotation
            font=dict(color='black', size=12),  # Adjust font color and size
            xanchor='center',  # Center alignment for x-axis
            yanchor='bottom',  # Anchor to the bottom of the marker
            yshift=10  # Adjust vertical position of the annotation
        )
    
    fig.update_layout(title='PER vs Semester', xaxis_title='Semester', yaxis_title='Percentage',width=1300,height=500) # Set the height of the chart to 600 pixels)
    line_html1 = pio.to_html(fig, include_plotlyjs=False)
    return line_html1,stud_name

