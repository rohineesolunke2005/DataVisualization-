import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go

def cmp_1(enrollment):
  file_path = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
  df = pd.read_excel(file_path, sheet_name='CO-1I', skiprows=7, nrows=55)
  df = df.iloc[:, 1:]

  file_path2 = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
  df2 = pd.read_excel(file_path2, sheet_name='CO-1I', skiprows=73, nrows=2)
  df2 = df2.iloc[:, 3:]
  low_r = df2[df2['Categories'] == 'Lowest']
  high_r = df2[df2['Categories'] == 'Highest']

  # Convert 'Enrollment Number' column to string type
  df['Enrollment Number'] = df['Enrollment Number'].astype(str)
  # Strip leading and trailing spaces
  df['Enrollment Number'] = df['Enrollment Number'].str.strip() 
  result = df[df['Enrollment Number'] == enrollment]

  marks=result[[ 'ENG_TH_TOT', 'ENG_PR_TOT', 'BSC_TH_TOT', 'BSC_PR_TOT', 'BMS_TH_TOT', 'ICT_PR_TOT',  'EGE_PR_TOT',  'WPC_PR_TOT']].values.flatten().tolist()
  subjects=[ 'english theory total', 'english practical total', 'science theory total', 'science practical total', 'maths theory total', 'ICT practical total',  'EGE practical total',  'WPC practical total']

  high_m=high_r[[ 'ENG_TH_TOT', 'ENG_PR_TOT', 'BSC_TH_TOT', 'BSC_PR_TOT', 'BMS_TH_TOT', 'ICT_PR_TOT',  'EGE_PR_TOT',  'WPC_PR_TOT']].values.flatten().tolist()
  low_m=low_r[[ 'ENG_TH_TOT', 'ENG_PR_TOT', 'BSC_TH_TOT', 'BSC_PR_TOT', 'BMS_TH_TOT', 'ICT_PR_TOT',  'EGE_PR_TOT',  'WPC_PR_TOT']].values.flatten().tolist()

  # Plot radar chart
  fig = go.Figure()

  fig.add_trace(go.Scatterpolar(
        r=high_m,
        theta=subjects,
        fill='toself',
        name='Higher'
  ))

  fig.add_trace(go.Scatterpolar(
        r=marks,
        theta=subjects,
        fill='toself',
        name='Your marks'
  ))

  fig.add_trace(go.Scatterpolar(
        r=low_m,
        theta=subjects,
        fill='toself',
        name='Lower'
  ))

  fig.update_layout(
    polar=dict(
      radialaxis=dict(
        visible=True,
        range=[0, 100]  # Assuming marks are out of 100
      )),
    showlegend=True,
    width=1350,  # Set the width of the chart to 800 pixels
    height=800, # Set the height of the chart to 600 pixels
  )
  
  
  fig2 = go.Figure(data=[go.Table(header=dict(values=subjects   ),cells=dict(values=high_m))])
    # Update layout if needed
  fig2.update_layout(title='Result Table high marks (Source)',height=235)
  
  
  fig3 = go.Figure(data=[go.Table(header=dict(values=subjects   ),cells=dict(values=low_m))])
    # Update layout if needed
  fig3.update_layout(title='Result Table low marks (Source)',height=235)

  cmp_src2_1 = pio.to_html(fig2, include_plotlyjs=False)
  cmp_src3_1 = pio.to_html(fig3, include_plotlyjs=False)
  
  cmp_html1 = pio.to_html(fig, include_plotlyjs=False)
  return cmp_html1,cmp_src2_1,cmp_src3_1



def cmp_2(enrollment):
  file_path = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
  df = pd.read_excel(file_path, sheet_name='CO-2I', skiprows=7, nrows=55)
  df = df.iloc[:, 1:]

  file_path2 = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
  df2 = pd.read_excel(file_path2, sheet_name='CO-2I', skiprows=65, nrows=2)
  df2 = df2.iloc[:, 3:]
  low_r = df2[df2['Categories'] == 'Lowest']
  high_r = df2[df2['Categories'] == 'Highest']

  # Convert 'Enrollment Number' column to string type
  df['Enrollment Number'] = df['Enrollment Number'].astype(str)
  # Strip leading and trailing spaces
  df['Enrollment Number'] = df['Enrollment Number'].str.strip()
  result = df[df['Enrollment Number'] == enrollment]

  marks=result[['EEC_TH_TOT','EEC_PR_TOT','AMI_TH_TOT','BEC_TH_TOT','BEC_PR_TOT','PCI_TH_TOT','PCI_PR_TOT','BCC_PR_TOT','CPH_PR_TOT','WPD_PR_TOT']].values.flatten().tolist()
  subjects=[ 'Elements of Electrical Engineering theory total','Elements of Electrical Engineering practical total','Applied Mathematics theory total','Basic Electronics theory total','Basic Electronics practical total','Programming in C theory total','Programming in C practical total','BCC practical total','CPH practical total','WPD practical total']

  high_m=high_r[[ 'EEC_TH_TOT','EEC_PR_TOT','AMI_TH_TOT','BEC_TH_TOT','BEC_PR_TOT','PCI_TH_TOT','PCI_PR_TOT','BCC_PR_TOT','CPH_PR_TOT','WPD_PR_TOT']].values.flatten().tolist()
  low_m=low_r[['EEC_TH_TOT','EEC_PR_TOT','AMI_TH_TOT','BEC_TH_TOT','BEC_PR_TOT','PCI_TH_TOT','PCI_PR_TOT','BCC_PR_TOT','CPH_PR_TOT','WPD_PR_TOT']].values.flatten().tolist()

  # Plot radar chart
  fig = go.Figure()

  fig.add_trace(go.Scatterpolar(
        r=high_m,
        theta=subjects,
        fill='toself',
        name='Higher'
  ))

  fig.add_trace(go.Scatterpolar(
        r=marks,
        theta=subjects,
        fill='toself',
        name='Your marks'
  ))

  fig.add_trace(go.Scatterpolar(
        r=low_m,
        theta=subjects,
        fill='toself',
        name='Lower'
  ))

  fig.update_layout(
    polar=dict(
      radialaxis=dict(
        visible=True,
        range=[0, 100]  # Assuming marks are out of 100
      )),
    showlegend=True,
    width=1350,  # Set the width of the chart to 800 pixels
    height=800, # Set the height of the chart to 600 pixels
  )
  
  fig2 = go.Figure(data=[go.Table(header=dict(values=subjects   ),cells=dict(values=high_m))])
    # Update layout if needed
  fig2.update_layout(title='Result Table high marks (Source)',height=280)
  
  
  fig3 = go.Figure(data=[go.Table(header=dict(values=subjects   ),cells=dict(values=low_m))])
    # Update layout if needed
  fig3.update_layout(title='Result Table low marks (Source)',height=280)

  cmp_src2_2 = pio.to_html(fig2, include_plotlyjs=False)
  cmp_src3_2 = pio.to_html(fig3, include_plotlyjs=False)

  cmp_html2 = pio.to_html(fig, include_plotlyjs=False)
  return cmp_html2,cmp_src2_2,cmp_src3_2



def cmp_3(enrollment):
  file_path = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
  df = pd.read_excel(file_path, sheet_name='CO-3I-COMBINE', skiprows=7, nrows=69)
  df = df.iloc[:, 1:]

  file_path2 = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
  df2 = pd.read_excel(file_path2, sheet_name='CO-3I-COMBINE', skiprows=80, nrows=2)
  df2 = df2.iloc[:, 3:]
  low_r = df2[df2['Categories'] == 'Lowest']
  high_r = df2[df2['Categories'] == 'Highest']

  # Convert 'Enrollment Number' column to string type
  df['Enrollment Number'] = df['Enrollment Number'].astype(str)
  # Strip leading and trailing spaces
  df['Enrollment Number'] = df['Enrollment Number'].str.strip()
  result = df[df['Enrollment Number'] == enrollment]
 

  marks=result[['OOP_TH_TOT','OOP_PR_TOT','DSU_TH_TOT','DSU_PR_TOT','CGR_TH_TOT','CGR_PR_TOT','DMS_TH_TOT','DMS_PR_TOT','DTE_TH_TOT','DTE_PR_TOT']].values.flatten().tolist()
  subjects=['Object Oriented Programming theory total','Object Oriented Programming practical total','Data Structure Using C theory total','Data Structure Using C practical total','Computer Graphics theory total','Computer Graphics practical total','Data Base Management System theory total','Data Base Management System practical total','Digital Techniques theory total','Digital Techniques practical total']

  high_m=high_r[['OOP_TH_TOT','OOP_PR_TOT','DSU_TH_TOT','DSU_PR_TOT','CGR_TH_TOT','CGR_PR_TOT','DMS_TH_TOT','DMS_PR_TOT','DTE_TH_TOT','DTE_PR_TOT']].values.flatten().tolist()
  low_m=low_r[['OOP_TH_TOT','OOP_PR_TOT','DSU_TH_TOT','DSU_PR_TOT','CGR_TH_TOT','CGR_PR_TOT','DMS_TH_TOT','DMS_PR_TOT','DTE_TH_TOT','DTE_PR_TOT']].values.flatten().tolist()

  # Plot radar chart
  fig = go.Figure()

  fig.add_trace(go.Scatterpolar(
        r=high_m,
        theta=subjects,
        fill='toself',
        name='Higher'
  ))

  fig.add_trace(go.Scatterpolar(
        r=marks,
        theta=subjects,
        fill='toself',
        name='Your marks'
  ))

  fig.add_trace(go.Scatterpolar(
        r=low_m,
        theta=subjects,
        fill='toself',
        name='Lower'
  ))

  fig.update_layout(
    polar=dict(
      radialaxis=dict(
        visible=True,
        range=[0, 100]  # Assuming marks are out of 100
      )),
    showlegend=True,
    width=1350,  # Set the width of the chart to 800 pixels
    height=800, # Set the height of the chart to 600 pixels
  )
  
  fig2 = go.Figure(data=[go.Table(header=dict(values=subjects   ),cells=dict(values=high_m))])
    # Update layout if needed
  fig2.update_layout(title='Result Table high marks (Source)',height=280)
  
  
  fig3 = go.Figure(data=[go.Table(header=dict(values=subjects   ),cells=dict(values=low_m))])
    # Update layout if needed
  fig3.update_layout(title='Result Table low marks (Source)',height=280)

  cmp_src2_3 = pio.to_html(fig2, include_plotlyjs=False)
  cmp_src3_3 = pio.to_html(fig3, include_plotlyjs=False)

  cmp_html3 = pio.to_html(fig, include_plotlyjs=False)
  return cmp_html3,cmp_src2_3,cmp_src3_3

  

def cmp_4(enrollment):
  file_path = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
  df = pd.read_excel(file_path, sheet_name='CO-4I-COMBINE', skiprows=7, nrows=69)
  df = df.iloc[:, 1:]

  file_path2 = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
  df2 = pd.read_excel(file_path2, sheet_name='CO-4I-COMBINE', skiprows=78, nrows=2)
  df2 = df2.iloc[:, 3:]
  
  low_r = df2[df2['Categories'] == 'Lowest']
  high_r = df2[df2['Categories'] == 'Highest']

  # Convert 'Enrollment Number' column to string type
  df['Enrollment Number'] = df['Enrollment Number'].astype(str)
  # Strip leading and trailing spaces
  df['Enrollment Number'] = df['Enrollment Number'].str.strip()
  result = df[df['Enrollment Number'] == enrollment]
 

  marks=result[['JPR_TH_TOT','JPR_PR_TOT','SEN_TH_TOT','SEN_PR_TOT','DCC_TH_TOT','DCC_PR_TOT','MPO_TH_TOT','MPO_PR_TOT','GAD_PR_TOT']].values.flatten().tolist()
  subjects=['Java theory total','Java practical total','Software Engineering theory total','Software Engineering practical total','Data Communication And Computer Network theory total','Data Communication And Computer Network practical total','Microprocessor theory total','Microprocessor practical total','GAD practical total']

  high_m=high_r[['JPR_TH_TOT','JPR_PR_TOT','SEN_TH_TOT','SEN_PR_TOT','DCC_TH_TOT','DCC_PR_TOT','MPO_TH_TOT','MPO_PR_TOT','GAD_PR_TOT']].values.flatten().tolist()
  low_m=low_r[['JPR_TH_TOT','JPR_PR_TOT','SEN_TH_TOT','SEN_PR_TOT','DCC_TH_TOT','DCC_PR_TOT','MPO_TH_TOT','MPO_PR_TOT','GAD_PR_TOT']].values.flatten().tolist()
  
  # Plot radar chart
  fig = go.Figure()

  fig.add_trace(go.Scatterpolar(
        r=high_m,
        theta=subjects,
        fill='toself',
        name='Higher'
  ))

  fig.add_trace(go.Scatterpolar(
        r=marks,
        theta=subjects,
        fill='toself',
        name='Your marks'
  ))

  fig.add_trace(go.Scatterpolar(
        r=low_m,
        theta=subjects,
        fill='toself',
        name='Lower'
  ))

  fig.update_layout(
    polar=dict(
      radialaxis=dict(
        visible=True,
        range=[0, 100]  # Assuming marks are out of 100
      )),
    showlegend=True,
    width=1350,  # Set the width of the chart to 800 pixels
    height=800, # Set the height of the chart to 600 pixels
  )
  fig2 = go.Figure(data=[go.Table(header=dict(values=subjects   ),cells=dict(values=high_m))])
    # Update layout if needed
  fig2.update_layout(title='Result Table high marks (Source)',height=280)
  
  
  fig3 = go.Figure(data=[go.Table(header=dict(values=subjects   ),cells=dict(values=low_m))])
    # Update layout if needed
  fig3.update_layout(title='Result Table low marks (Source)',height=280)

  cmp_src2_4 = pio.to_html(fig2, include_plotlyjs=False)
  cmp_src3_4 = pio.to_html(fig3, include_plotlyjs=False)

  cmp_html4 = pio.to_html(fig, include_plotlyjs=False)
  return cmp_html4,cmp_src2_4,cmp_src3_4


def cmp_5(enrollment):
  file_path = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
  df = pd.read_excel(file_path, sheet_name='CO-5I-combine', skiprows=7, nrows=68)
  df = df.iloc[:, 1:]

  file_path2 = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
  df2 = pd.read_excel(file_path2, sheet_name='CO-5I-combine', skiprows=79, nrows=2)
  df2 = df2.iloc[:, 3:]
  
  low_r = df2[df2['Categories'] == 'Lowest']
  high_r = df2[df2['Categories'] == 'Highest']

  # Convert 'Enrollment Number' column to string type
  df['Enrollment Number'] = df['Enrollment Number'].astype(str)
  # Strip leading and trailing spaces
  df['Enrollment Number'] = df['Enrollment Number'].str.strip()
  result = df[df['Enrollment Number'] == enrollment]
  

  marks=result[['EST_TH_TOT','OSY_TH_TOT','OSY_PR_TOT','AJP_TH_TOT','AJP_PR_TOT','STE_TH_TOT','STE_PR_TOT','ACN_TH_TOT','ACN_PR_TOT','ITR_PR_TOT','CPP_PR_TOT']].values.flatten().tolist()
  subjects=['Environmental Studies theory total','Operating System theory total','Operating System practical total','Advance Java Programming theory total','Advance Java Programming pratical total','Software Testing theory total','Software Testing pratical total','Advance Computer Network theory total','Advance Computer Network practical total','ITR practical total','CPP practical total']

  high_m=high_r[['EST_TH_TOT','OSY_TH_TOT','OSY_PR_TOT','AJP_TH_TOT','AJP_PR_TOT','STE_TH_TOT','STE_PR_TOT','ACN_TH_TOT','ACN_PR_TOT','ITR_PR_TOT','CPP_PR_TOT']].values.flatten().tolist()
  low_m=low_r[['EST_TH_TOT','OSY_TH_TOT','OSY_PR_TOT','AJP_TH_TOT','AJP_PR_TOT','STE_TH_TOT','STE_PR_TOT','ACN_TH_TOT','ACN_PR_TOT','ITR_PR_TOT','CPP_PR_TOT']].values.flatten().tolist()
  
  # Plot radar chart
  fig = go.Figure()

  fig.add_trace(go.Scatterpolar(
        r=high_m,
        theta=subjects,
        fill='toself',
        name='Higher'
  ))

  fig.add_trace(go.Scatterpolar(
        r=marks,
        theta=subjects,
        fill='toself',
        name='Your marks'
  ))

  fig.add_trace(go.Scatterpolar(
        r=low_m,
        theta=subjects,
        fill='toself',
        name='Lower'
  ))

  fig.update_layout(
    polar=dict(
      radialaxis=dict(
        visible=True,
        range=[0, 150]  # Assuming marks are out of 100
      )),
    showlegend=True,
    width=1350,  # Set the width of the chart to 800 pixels
    height=800, # Set the height of the chart to 600 pixels
  )
  
  fig2 = go.Figure(data=[go.Table(header=dict(values=subjects   ),cells=dict(values=high_m))])
    # Update layout if needed
  fig2.update_layout(title='Result Table high marks (Source)',height=280)
  
  
  fig3 = go.Figure(data=[go.Table(header=dict(values=subjects   ),cells=dict(values=low_m))])
    # Update layout if needed
  fig3.update_layout(title='Result Table low marks (Source)',height=280)

  cmp_src2_5 = pio.to_html(fig2, include_plotlyjs=False)
  cmp_src3_5 = pio.to_html(fig3, include_plotlyjs=False)

  cmp_html5 = pio.to_html(fig, include_plotlyjs=False)
  return cmp_html5,cmp_src2_5,cmp_src3_5


def cmp_6(enrollment):
  file_path = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
  df = pd.read_excel(file_path, sheet_name='CO-6I-combine', skiprows=7, nrows=68)
  df = df.iloc[:, 1:]

  file_path2 = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
  df2 = pd.read_excel(file_path2, sheet_name='CO-6I-combine', skiprows=84, nrows=2)
  df2 = df2.iloc[:, 3:]
  
  
  low_r = df2[df2['Categories'] == 'Lowest']
  high_r = df2[df2['Categories'] == 'Highest']

  # Convert 'Enrollment Number' column to string type
  df['Enrollment Number'] = df['Enrollment Number'].astype(str)
  # Strip leading and trailing spaces
  df['Enrollment Number'] = df['Enrollment Number'].str.strip()
  result = df[df['Enrollment Number'] == enrollment]
  

  marks=result[['MGT_TH_TOT','PWP_TH_TOT','PWP_PR_TOT','MAD_TH_TOT','MAD_PR_TOT','ETI_TH_TOT','NIS_TH_TOT','NIS_PR_TOT','EDE_PR_TOT','CPE_PR_TOT']].values.flatten().tolist()
  subjects=['Managment theory total','Programming with Python theory total','Programming with Python practical total','Mobile Application Development theory total','Mobile Application Development practical total','Emerging Trends theory total','Network in Security theory total','Network in Security practical total','EDE practical total','CPE practical total']

  high_m=high_r[['MGT_TH_TOT','PWP_TH_TOT','PWP_PR_TOT','MAD_TH_TOT','MAD_PR_TOT','ETI_TH_TOT','NIS_TH_TOT','NIS_PR_TOT','EDE_PR_TOT','CPE_PR_TOT']].values.flatten().tolist()
  low_m=low_r[['MGT_TH_TOT','PWP_TH_TOT','PWP_PR_TOT','MAD_TH_TOT','MAD_PR_TOT','ETI_TH_TOT','NIS_TH_TOT','NIS_PR_TOT','EDE_PR_TOT','CPE_PR_TOT']].values.flatten().tolist()
  
  # Plot radar chart
  fig = go.Figure()

  fig.add_trace(go.Scatterpolar(
        r=high_m,
        theta=subjects,
        fill='toself',
        name='Higher'
  ))

  fig.add_trace(go.Scatterpolar(
        r=marks,
        theta=subjects,
        fill='toself',
        name='Your marks'
  ))

  fig.add_trace(go.Scatterpolar(
        r=low_m,
        theta=subjects,
        fill='toself',
        name='Lower'
  ))

  fig.update_layout(
    polar=dict(
      radialaxis=dict(
        visible=True,
        range=[0, 100]  # Assuming marks are out of 100
      )),
    showlegend=True,
    width=1350,  # Set the width of the chart to 800 pixels
    height=800, # Set the height of the chart to 600 pixels
  )
  
  fig2 = go.Figure(data=[go.Table(header=dict(values=subjects   ),cells=dict(values=high_m))])
    # Update layout if needed
  fig2.update_layout(title='Result Table high marks (Source)',height=280)
  
  
  fig3 = go.Figure(data=[go.Table(header=dict(values=subjects   ),cells=dict(values=low_m))])
    # Update layout if needed
  fig3.update_layout(title='Result Table low marks (Source)',height=280)

  cmp_src2_6 = pio.to_html(fig2, include_plotlyjs=False)
  cmp_src3_6 = pio.to_html(fig3, include_plotlyjs=False)

  cmp_html6 = pio.to_html(fig, include_plotlyjs=False)
  return cmp_html6,cmp_src2_6,cmp_src3_6
