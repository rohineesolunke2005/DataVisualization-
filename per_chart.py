import pandas as pd
import plotly.io as pio
import plotly.graph_objs as go

def pie_chart_1(enrollment):
    file_path = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-1I',skiprows=7,nrows=55)
    df = df.iloc[:, 1:]

    # Convert 'Enrollment Number' column to string type
    df['Enrollment Number'] = df['Enrollment Number'].astype(str)
    # Strip leading and trailing spaces
    df['Enrollment Number'] = df['Enrollment Number'].str.strip()
    result = df[df['Enrollment Number'] == enrollment]

    values_columns = ['ENG_TH_TOT','ENG_PR_TOT','BSC_TH_TOT','BSC_PR_TOT','BMS_TH_TOT','ICT_PR_TOT','EGE_PR_TOT','WPC_PR_TOT']
    subject = ['English Theory', 'English Practical', 'Basic Science Theory', 'Basic Science Practical', 'Mathematics Theory', 'ICT Practical', 'EGE Practical', 'WPC Practical']
    

    values_columns_table = ['ENG_TH_TOT', 'ENG_PR_TOT', 'BSC_TH_TOT', 'BSC_PR_TOT', 'BMS_TH_TOT', 'ICT_PR_TOT', 'EGE_PR_TOT', 'WPC_PR_TOT','Total out of (700)', 'PER', 'Status']
    subject_table = ['English Theory', 'English Practical', 'Basic Science Theory', 'Basic Science Practical', 'Mathematics Theory', 'ICT Practical', 'EGE Practical', 'WPC Practical','Total out of (700)', 'PER', 'Status']
    marks_values = result[values_columns_table].values.flatten()  # Flatten the values into a 1D array
    
    if result.empty:
        return "No data found for the provided enrollment number."
    # Create pie chart
    fig = go.Figure(data=[go.Pie(labels=subject, values=result[values_columns].iloc[0], title='Status Distribution')])
    fig.update_layout(
        width=1350,  # Set the width of the chart to 800 pixels
        height=800, # Set the height of the chart to 600 pixels
    )
    
    fig2 = go.Figure(data=[go.Table(header=dict(values=subject_table),cells=dict(values=marks_values))])
# Update layout if needed
    fig2.update_layout(title='Result Table (Source)',height=315)

    per_src1 = pio.to_html(fig2, include_plotlyjs=False)
    per_html1 = pio.to_html(fig, include_plotlyjs=False)
    return per_html1,per_src1

def pie_chart_2(enrollment):
    file_path = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-2I',skiprows=7,nrows=55)
    df = df.iloc[:, 1:]

    # Convert 'Enrollment Number' column to string type
    df['Enrollment Number'] = df['Enrollment Number'].astype(str)
    # Strip leading and trailing spaces
    df['Enrollment Number'] = df['Enrollment Number'].str.strip()
    result = df[df['Enrollment Number'] == enrollment]

    values_columns = ['EEC_TH_TOT','EEC_PR_TOT','AMI_TH_TOT','BEC_TH_TOT','BEC_PR_TOT','PCI_TH_TOT','PCI_PR_TOT','BCC_PR_TOT','CPH_PR_TOT','WPD_PR_TOT']
    values_columns_table = ['EEC_TH_TOT','EEC_PR_TOT','AMI_TH_TOT','BEC_TH_TOT','BEC_PR_TOT','PCI_TH_TOT','PCI_PR_TOT','BCC_PR_TOT','CPH_PR_TOT','WPD_PR_TOT','Total out of (800)','PER','Status']
    
    subjects=['Elements of Electrical Engineering theory total','Elements of Electrical Engineering practical total','Applied Mathematics theory total','Basic Electronics theory total','Basic Electronics practical total','Programming in C theory total','Programming in C practical total','BCC practical total','CPH practical total','WPD practical total']
    subjects_table=['Elements of Electrical Engineering theory total','Elements of Electrical Engineering practical total','Applied Mathematics theory total','Basic Electronics theory total','Basic Electronics practical total','Programming in C theory total','Programming in C practical total','BCC practical total','CPH practical total','WPD practical total','Total out of (800)','PER','Status']

    marks_values = result[values_columns_table].values.flatten()  # Flatten the values into a 1D array
    
    
    if result.empty:
        return "No data found for the provided enrollment number."
    
    # Create pie chart
    fig = go.Figure(data=[go.Pie(labels=subjects, values=result[values_columns].iloc[0], title='Status Distribution')])
    fig.update_layout(
        width=1350,  # Set the width of the chart to 800 pixels
        height=800, # Set the height of the chart to 600 pixels
    )
    
    fig2 = go.Figure(data=[go.Table(header=dict(values=subjects_table),cells=dict(values=marks_values))])
    # Update layout if needed
    fig2.update_layout(title='Result Table (Source)',height=315)

    per_src2 = pio.to_html(fig2, include_plotlyjs=False)
    
    per_html2 = pio.to_html(fig, include_plotlyjs=False)
    return per_html2,per_src2



def pie_chart_3(enrollment):
    file_path = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-3I-COMBINE',skiprows=7,nrows=69)
    df = df.iloc[:, 1:]

    # Convert 'Enrollment Number' column to string type
    df['Enrollment Number'] = df['Enrollment Number'].astype(str)
    # Strip leading and trailing spaces
    df['Enrollment Number'] = df['Enrollment Number'].str.strip()
    result = df[df['Enrollment Number'] == enrollment]

    values_columns = ['OOP_TH_TOT','OOP_PR_TOT','DSU_TH_TOT','DSU_PR_TOT','CGR_TH_TOT','CGR_PR_TOT','DMS_TH_TOT','DMS_PR_TOT','DTE_TH_TOT','DTE_PR_TOT']
    values_columns_table = ['OOP_TH_TOT','OOP_PR_TOT','DSU_TH_TOT','DSU_PR_TOT','CGR_TH_TOT','CGR_PR_TOT','DMS_TH_TOT','DMS_PR_TOT','DTE_TH_TOT','DTE_PR_TOT','Total out of (750)','PER','Status']
    
    subjects=['Object Oriented Programming theory total','Object Oriented Programming practical total','Data Structure Using C theory total','Data Structure Using C practical total','Computer Graphics theory total','Computer Graphics practical total','Data Base Management System theory total','Data Base Management System practical total','Digital Techniques theory total','Digital Techniques practical total']
    subjects_table=['Object Oriented Programming theory total','Object Oriented Programming practical total','Data Structure Using C theory total','Data Structure Using C practical total','Computer Graphics theory total','Computer Graphics practical total','Data Base Management System theory total','Data Base Management System practical total','Digital Techniques theory total','Digital Techniques practical total','Total out of (750)','PER','Status']

    if result.empty:
        return "No data found for the provided enrollment number."
    fig= go.Figure()
    # Create pie chart
    fig = go.Figure(data=[go.Pie(labels=subjects, values=result[values_columns].iloc[0], title='Status Distribution')])

    fig.update_layout(
        width=1350,  # Set the width of the chart to 800 pixels
        height=800, # Set the height of the chart to 600 pixels
    )
    
    marks_values = result[values_columns_table].values.flatten()  # Flatten the values into a 1D array
    fig2 = go.Figure(data=[go.Table(header=dict(values=subjects_table),cells=dict(values=marks_values))])
    # Update layout if needed
    fig2.update_layout(title='Result Table (Source)',height=315)

    per_src3 = pio.to_html(fig2, include_plotlyjs=False)
    
    per_html3 = pio.to_html(fig, include_plotlyjs=False)
    return per_html3,per_src3


def pie_chart_4(enrollment):
    file_path = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-4I-COMBINE',skiprows=7,nrows=69)
    df = df.iloc[:, 1:]

    # Convert 'Enrollment Number' column to string type
    df['Enrollment Number'] = df['Enrollment Number'].astype(str)
    # Strip leading and trailing spaces
    df['Enrollment Number'] = df['Enrollment Number'].str.strip()
    result = df[df['Enrollment Number'] == enrollment]

    values_columns = ['JPR_TH_TOT','JPR_PR_TOT','SEN_TH_TOT','SEN_PR_TOT','DCC_TH_TOT','DCC_PR_TOT','MPO_TH_TOT','MPO_PR_TOT','GAD_PR_TOT']
    values_columns_table = ['JPR_TH_TOT','JPR_PR_TOT','SEN_TH_TOT','SEN_PR_TOT','DCC_TH_TOT','DCC_PR_TOT','MPO_TH_TOT','MPO_PR_TOT','GAD_PR_TOT','Total out of (750)','PER','Status']
    
    subjects=['Java theory total','Java practical total','Software Engineering theory total','Software Engineering practical total','Data Communication And Computer Network theory total','Data Communication And Computer Network practical total','Microprocessor theory total','Microprocessor practical total','GAD practical total']
    subjects_table=['Java theory total','Java practical total','Software Engineering theory total','Software Engineering practical total','Data Communication And Computer Network theory total','Data Communication And Computer Network practical total','Microprocessor theory total','Microprocessor practical total','GAD practical total','Total out of (750)','PER','Status']

    if result.empty:
        return "No data found for the provided enrollment number."
    fig= go.Figure()
    # Create pie chart
    fig = go.Figure(data=[go.Pie(labels=subjects, values=result[values_columns].iloc[0], title='Status Distribution')])

    fig.update_layout(
        width=1350,  # Set the width of the chart to 800 pixels
        height=800, # Set the height of the chart to 600 pixels
    )
    
    marks_values = result[values_columns_table].values.flatten()  # Flatten the values into a 1D array
    fig2 = go.Figure(data=[go.Table(header=dict(values=subjects_table),cells=dict(values=marks_values))])
    # Update layout if needed
    fig2.update_layout(title='Result Table (Source)',height=315)

    per_src4 = pio.to_html(fig2, include_plotlyjs=False)
    
    per_html4 = pio.to_html(fig, include_plotlyjs=False)
    return per_html4,per_src4



def pie_chart_5(enrollment):
    file_path = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-5I-combine',skiprows=7,nrows=68)
    df = df.iloc[:, 1:]

    # Convert 'Enrollment Number' column to string type
    df['Enrollment Number'] = df['Enrollment Number'].astype(str)
    # Strip leading and trailing spaces
    df['Enrollment Number'] = df['Enrollment Number'].str.strip()
    result = df[df['Enrollment Number'] == enrollment]
    values_columns = ['EST_TH_TOT','OSY_TH_TOT','OSY_PR_TOT','AJP_TH_TOT','AJP_PR_TOT','STE_TH_TOT','STE_PR_TOT','ACN_TH_TOT','ACN_PR_TOT','ITR_PR_TOT','CPP_PR_TOT']
    values_columns_table = ['EST_TH_TOT','OSY_TH_TOT','OSY_PR_TOT','AJP_TH_TOT','AJP_PR_TOT','STE_TH_TOT','STE_PR_TOT','ACN_TH_TOT','ACN_PR_TOT','ITR_PR_TOT','CPP_PR_TOT','Total out of (750)','PER','Status']

    subjects=['Environmental Studies theory total','Operating System theory total','Operating System practical total','Advance Java Programming theory total','Advance Java Programming pratical total','Software Testing theory total','Software Testing pratical total','Advance Computer Network theory total','Advance Computer Network practical total','ITR practical total','CPP practical total']
    subjects_table=['Environmental Studies theory total','Operating System theory total','Operating System practical total','Advance Java Programming theory total','Advance Java Programming pratical total','Software Testing theory total','Software Testing pratical total','Advance Computer Network theory total','Advance Computer Network practical total','ITR practical total','CPP practical total','Total out of (750)','PER','Status']

    if result.empty:
        return "No data found for the provided enrollment number."
    fig= go.Figure()
    # Create pie chart
    fig = go.Figure(data=[go.Pie(labels=subjects, values=result[values_columns].iloc[0], title='Status Distribution')])

    fig.update_layout(
        width=1350,  # Set the width of the chart to 800 pixels
        height=800, # Set the height of the chart to 600 pixels
    )
    
    marks_values = result[values_columns_table].values.flatten()  # Flatten the values into a 1D array
    fig2 = go.Figure(data=[go.Table(header=dict(values=subjects_table),cells=dict(values=marks_values))])
    # Update layout if needed
    fig2.update_layout(title='Result Table (Source)',height=315)

    per_src5 = pio.to_html(fig2, include_plotlyjs=False)
    
    per_html5 = pio.to_html(fig, include_plotlyjs=False)
    return per_html5,per_src5



def pie_chart_6(enrollment):
    file_path = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-6I-combine',skiprows=7,nrows=68)
    df = df.iloc[:, 1:]

    # Convert 'Enrollment Number' column to string type
    df['Enrollment Number'] = df['Enrollment Number'].astype(str)
    # Strip leading and trailing spaces
    df['Enrollment Number'] = df['Enrollment Number'].str.strip()
    result = df[df['Enrollment Number'] == enrollment]

    values_columns = ['MGT_TH_TOT','PWP_TH_TOT','PWP_PR_TOT','MAD_TH_TOT','MAD_PR_TOT','ETI_TH_TOT','NIS_TH_TOT','NIS_PR_TOT','EDE_PR_TOT','CPE_PR_TOT']
    values_columns_table = ['MGT_TH_TOT','PWP_TH_TOT','PWP_PR_TOT','MAD_TH_TOT','MAD_PR_TOT','ETI_TH_TOT','NIS_TH_TOT','NIS_PR_TOT','EDE_PR_TOT','CPE_PR_TOT','Total out of (850)','PER','Status']
    
    subjects=['Managment theory total','Programming with Python theory total','Programming with Python practical total','Mobile Application Development theory total','Mobile Application Development practical total','Emerging Trends theory total','Network in Security theory total','Network in Security practical total','EDE practical total','CPE practical total']
    subjects_table=['Managment theory total','Programming with Python theory total','Programming with Python practical total','Mobile Application Development theory total','Mobile Application Development practical total','Emerging Trends theory total','Network in Security theory total','Network in Security practical total','EDE practical total','CPE practical total','Total out of (850)','PER','Status']

    if result.empty:
        return "No data found for the provided enrollment number."
    fig= go.Figure()
    # Create pie chart
    fig = go.Figure(data=[go.Pie(labels=subjects, values=result[values_columns].iloc[0], title='Status Distribution')])

    fig.update_layout(
        width=1350,  # Set the width of the chart to 800 pixels
        height=800, # Set the height of the chart to 600 pixels
    )
    
    marks_values = result[values_columns_table].values.flatten()  # Flatten the values into a 1D array
    fig2 = go.Figure(data=[go.Table(header=dict(values=subjects_table),cells=dict(values=marks_values))])
    # Update layout if needed
    fig2.update_layout(title='Result Table (Source)',height=315)

    per_src6 = pio.to_html(fig2, include_plotlyjs=False)
    
    per_html6 = pio.to_html(fig, include_plotlyjs=False)
    return per_html6,per_src6