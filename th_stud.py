import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go

def th_sd_1(enrollment):
    # Read Excel file
    file_path = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-1I', skiprows=7, nrows=55)
    df = df.iloc[:, 1:]

    # Convert 'Enrollment Number' column to string type
    df['Enrollment Number'] = df['Enrollment Number'].astype(str)
    # Strip leading and trailing spaces
    df['Enrollment Number'] = df['Enrollment Number'].str.strip()
    result = df[df['Enrollment Number'] == enrollment]
    # Check if enrollment was found
    if len(result) == 0:
        return "No data found in database."


    # Choose the column you want to use for the stacked bar chart
    selected_columns_eng_th = ['ENG_TH_ESE', 'ENG_TH_PA']
    selected_columns_eng_pr = ['ENG_PR_ESE', 'ENG_PR_PA']
    selected_columns_bsc_th = ['BSC_TH_ESE', 'BSC_TH_PA']
    selected_columns_bsc_pr = ['BSC_PR_ESE', 'BSC_PR_PA']
    selected_columns_bms_th = ['BMS_TH_ESE', 'BMS_TH_PA']
    selected_columns_ict_pr = ['ICT_PR_ESE', 'ICT_PR_PA']
    selected_columns_ege_pr = ['EGE_PR_ESE', 'EGE_PR_PA']
    selected_columns_wpc_pr = ['WPC_PR_ESE', 'WPC_PR_PA']

    # Extract data for the selected columns
    selected_data_eng_th = result[selected_columns_eng_th]
    selected_data_bsc_th = result[selected_columns_bsc_th]
    selected_data_bms_th = result[selected_columns_bms_th]
    selected_data_eng_pr = result[selected_columns_eng_pr]
    selected_data_bsc_pr = result[selected_columns_bsc_pr]
    selected_data_ict_pr = result[selected_columns_ict_pr]
    selected_data_ege_pr = result[selected_columns_ege_pr]
    selected_data_wpc_pr = result[selected_columns_wpc_pr]

    ese_color = 'rgb(31, 119, 180)'
    pa_color = 'rgb(255, 127, 14)'

    fig = go.Figure()
    # Create a new Figure instance
    fig.add_trace(go.Bar(
        x=['ENG TH'],
        y=[selected_data_eng_th['ENG_TH_ESE'].iloc[0]],
        name='ENG_TH_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['ENG TH'],
        y=[selected_data_eng_th['ENG_TH_PA'].iloc[0]],
        name='ENG_TH_PA',
        marker_color=pa_color
    ))

    # Add traces for BSC_TH
    fig.add_trace(go.Bar(
        x=['BSC TH'],
        y=[selected_data_bsc_th['BSC_TH_ESE'].iloc[0]],
        name='BSC_TH_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['BSC TH'],
        y=[selected_data_bsc_th['BSC_TH_PA'].iloc[0]],
        name='BSC_TH_PA',
        marker_color=pa_color
    ))

    # Add traces for BMS_TH
    fig.add_trace(go.Bar(
        x=['BMS TH'],
        y=[selected_data_bms_th['BMS_TH_ESE'].iloc[0]],
        name='BMS_TH_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['BMS TH'],
        y=[selected_data_bms_th['BMS_TH_PA'].iloc[0]],
        name='BMS_TH_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['ENG PR'],
        y=[selected_data_eng_pr['ENG_PR_ESE'].iloc[0]],
        name='ENG_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['ENG PR'],
        y=[selected_data_eng_pr['ENG_PR_PA'].iloc[0]],
        name='ENG_TH_PA',
        marker_color=pa_color
    ))

    # Add traces for BSC_TH
    fig.add_trace(go.Bar(
        x=['BSC PR'],
        y=[selected_data_bsc_pr['BSC_PR_ESE'].iloc[0]],
        name='BSC_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['BSC PR'],
        y=[selected_data_bsc_pr['BSC_PR_PA'].iloc[0]],
        name='BSC_PR_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['ICT PR'],
        y=[selected_data_ict_pr['ICT_PR_PA'].iloc[0]],
        name='ICT_PR_PA',
        marker_color=pa_color
    ))

    # Add traces for BSC_TH
    fig.add_trace(go.Bar(
        x=['EGE PR'],
        y=[selected_data_ege_pr['EGE_PR_ESE'].iloc[0]],
        name='EGE_PR_ESE',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['WPC PR'],
        y=[selected_data_wpc_pr['WPC_PR_PA'].iloc[0]],
        name='WPC_PR_PA',
        marker_color=pa_color
    ))

    # Update layout
    fig.update_layout(
        width=1350,  # Set the width of the chart to 800 pixels
        height=800, # Set the height of the chart to 600 pixels
        title='Multiple Stacked Bar Charts',
        xaxis=dict(title='Category'),
        yaxis=dict(title='Values'),
        barmode='stack'  # Stack bars on top of each other
    )
    
    result2=result.iloc[:,4:-3]
    
        # Create a Plotly table
    fig2 = go.Figure(data=[go.Table(
    header=dict(values=list(result2.columns),fill_color='lightblue',
                font=dict(size=9), height=40,),  
    cells=dict(values=[result[col] for col in result2.columns],
               fill_color='white',align='left'))
    ])

    # Update table layout
    fig2.update_layout(title='Theory and Practical Marks (Source)', title_font_size=20,width=1600, height=300)
    th_src1 = pio.to_html(fig2, include_plotlyjs=False)
    
    th_html1 = pio.to_html(fig, include_plotlyjs=False)
    return th_html1,th_src1

def th_sd_2(enrollment):
    # Read Excel file
    file_path = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-2I', skiprows=7, nrows=55)
    df = df.iloc[:, 1:]

    # Convert 'Enrollment Number' column to string type
    df['Enrollment Number'] = df['Enrollment Number'].astype(str)
    # Strip leading and trailing spaces
    df['Enrollment Number'] = df['Enrollment Number'].str.strip()
    result = df[df['Enrollment Number'] == enrollment]
    if len(result) == 0:
        return "No data found in database."

    # Choose the column you want to use for the stacked bar chart
    selected_columns_eec_th = ['EEC_TH_ESE', 'EEC_TH_PA']
    selected_columns_eec_pr = ['EEC_PR_ESE', 'EEC_PR_PA']
    selected_columns_ami_th = ['AMI_TH_ESE', 'AMI_TH_PA']
    selected_columns_bec_th = ['BEC_TH_ESE', 'BEC_TH_PA']
    selected_columns_bec_pr = ['BEC_PR_ESE', 'BEC_PR_PA']
    selected_columns_pci_th = ['PCI_TH_ESE', 'PCI_TH_PA']
    selected_columns_pci_pr = ['PCI_PR_ESE', 'PCI_PR_PA']
    selected_columns_bcc_pr = ['BCC_PR_ESE', 'BCC_PR_PA']
    selected_columns_cph_pr = ['CPH_PR_ESE', 'CPH_PR_PA']
    selected_columns_wpd_pr = ['WPD_PR_ESE', 'WPD_PR_PA']

    # Extract data for the selected columns
    selected_data_eec_th = result[selected_columns_eec_th]
    selected_data_ami_th = result[selected_columns_ami_th]
    selected_data_bec_th = result[selected_columns_bec_th]
    selected_data_pci_th = result[selected_columns_pci_th]
    selected_data_eec_pr = result[selected_columns_eec_pr]
    selected_data_bec_pr = result[selected_columns_bec_pr]
    selected_data_pci_pr = result[selected_columns_pci_pr]
    selected_data_bcc_pr = result[selected_columns_bcc_pr]
    selected_data_cph_pr = result[selected_columns_cph_pr]
    selected_data_wpd_pr = result[selected_columns_wpd_pr]

    ese_color = 'rgb(31, 119, 180)'
    pa_color = 'rgb(255, 127, 14)'

    fig = go.Figure()
    # Create a new Figure instance
    fig.add_trace(go.Bar(
        x=['EEC TH'],
        y=[selected_data_eec_th['EEC_TH_ESE'].iloc[0]],
        name='EEC_TH_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['EEC TH'],
        y=[selected_data_eec_th['EEC_TH_PA'].iloc[0]],
        name='EEC_TH_PA',
        marker_color=pa_color
    ))

    # Add traces for BMS_TH
    fig.add_trace(go.Bar(
        x=['BEC TH'],
        y=[selected_data_bec_th['BEC_TH_ESE'].iloc[0]],
        name='BEC_TH_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['BEC TH'],
        y=[selected_data_bec_th['BEC_TH_PA'].iloc[0]],
        name='BEC_TH_PA',
        marker_color=pa_color
    ))

    # Add traces for BSC_TH
    fig.add_trace(go.Bar(
        x=['PCI TH'],
        y=[selected_data_pci_th['PCI_TH_ESE'].iloc[0]],
        name='PCI_TH_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['PCI TH'],
        y=[selected_data_pci_th['PCI_TH_PA'].iloc[0]],
        name='PCI_TH_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['EEC PR'],
        y=[selected_data_eec_pr['EEC_PR_ESE'].iloc[0]],
        name='EEC_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['EEC PR'],
        y=[selected_data_eec_pr['EEC_PR_PA'].iloc[0]],
        name='EEC_PR_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['BEC PR'],
        y=[selected_data_bec_pr['BEC_PR_ESE'].iloc[0]],
        name='BEC_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['BEC PR'],
        y=[selected_data_bec_pr['BEC_PR_PA'].iloc[0]],
        name='BEC_PR_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['PCI PR'],
        y=[selected_data_pci_pr['PCI_PR_ESE'].iloc[0]],
        name='PCI_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['PCI PR'],
        y=[selected_data_pci_pr['PCI_PR_PA'].iloc[0]],
        name='PCI_PR_PA',
        marker_color=pa_color
    ))

     # Add traces for BSC_TH
    fig.add_trace(go.Bar(
        x=['AMI TH'],
        y=[selected_data_ami_th['AMI_TH_ESE'].iloc[0]],
        name='AMI_TH_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['AMI TH'],
        y=[selected_data_ami_th['AMI_TH_PA'].iloc[0]],
        name='AMI_TH_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['BCC PR'],
        y=[selected_data_bcc_pr['BCC_PR_ESE'].iloc[0]],
        name='BCC_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['BCC PR'],
        y=[selected_data_bcc_pr['BCC_PR_PA'].iloc[0]],
        name='BCC_PR_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['CPH PR'],
        y=[selected_data_cph_pr['CPH_PR_ESE'].iloc[0]],
        name='BCC_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['CPH PR'],
        y=[selected_data_cph_pr['CPH_PR_PA'].iloc[0]],
        name='CPH_PR_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['WPD PR'],
        y=[selected_data_wpd_pr['WPD_PR_ESE'].iloc[0]],
        name='WPD_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['WPD PR'],
        y=[selected_data_wpd_pr['WPD_PR_PA'].iloc[0]],
        name='WPD_PR_PA',
        marker_color=pa_color
    ))

    # Update layout
    fig.update_layout(
        width=1350,  # Set the width of the chart to 800 pixels
        height=800, # Set the height of the chart to 600 pixels
        title='Multiple Stacked Bar Charts',
        xaxis=dict(title='Category'),
        yaxis=dict(title='Values'),
        barmode='stack'  # Stack bars on top of each other
    )
    
    result2=result.iloc[:,4:-6]
    
        # Create a Plotly table
    fig2 = go.Figure(data=[go.Table(
    header=dict(values=list(result2.columns),fill_color='lightblue',
                font=dict(size=9), height=40,),  
    cells=dict(values=[result[col] for col in result2.columns],
               fill_color='white',align='left'))
    ])

    # Update table layout
    fig2.update_layout(title='Theory and Practical Marks (Source)', title_font_size=20,width=1600, height=300)
    th_src2 = pio.to_html(fig2, include_plotlyjs=False)

    th_html2 = pio.to_html(fig, include_plotlyjs=False)
    return th_html2,th_src2

def th_sd_3(enrollment):
    # Read Excel file
    file_path = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-3I-COMBINE', skiprows=7, nrows=69)
    df = df.iloc[:, 1:]

    # Convert 'Enrollment Number' column to string type
    df['Enrollment Number'] = df['Enrollment Number'].astype(str)
    # Strip leading and trailing spaces
    df['Enrollment Number'] = df['Enrollment Number'].str.strip()
    result = df[df['Enrollment Number'] == enrollment]

    # Choose the column you want to use for the stacked bar chart
    selected_columns_oop_th = ['OOP_TH_ESE', 'OOP_TH_PA']
    selected_columns_oop_pr = ['OOP_PR_ESE', 'OOP_PR_PA']
    selected_columns_dsu_th = ['DSU_TH_ESE', 'DSU_TH_PA']
    selected_columns_dsu_pr = ['DSU_PR_ESE', 'DSU_PR_PA']
    selected_columns_cgr_th = ['CGR_TH_ESE', 'CGR_TH_PA']
    selected_columns_cgr_pr = ['CGR_PR_ESE', 'CGR_PR_PA']
    selected_columns_dms_th = ['DMS_TH_ESE', 'DMS_TH_PA']
    selected_columns_dms_pr = ['DMS_PR_ESE', 'DMS_PR_PA']
    selected_columns_dte_th = ['DTE_TH_ESE', 'DTE_TH_PA']
    selected_columns_dte_pr = ['DTE_PR_ESE', 'DTE_PR_PA']

    # Extract data for the selected columns
    selected_data_oop_th = result[selected_columns_oop_th]
    selected_data_dsu_th = result[selected_columns_dsu_th]
    selected_data_cgr_th = result[selected_columns_cgr_th]
    selected_data_dms_th = result[selected_columns_dms_th]
    selected_data_dte_th = result[selected_columns_dte_th]
    selected_data_oop_pr = result[selected_columns_oop_pr]
    selected_data_dsu_pr = result[selected_columns_dsu_pr]
    selected_data_cgr_pr = result[selected_columns_cgr_pr]
    selected_data_dms_pr = result[selected_columns_dms_pr]
    selected_data_dte_pr = result[selected_columns_dte_pr]

    ese_color = 'rgb(31, 119, 180)'
    pa_color = 'rgb(255, 127, 14)'

    fig = go.Figure()
    # Create a new Figure instance
    fig.add_trace(go.Bar(
        x=['OOP TH'],
        y=[selected_data_oop_th['OOP_TH_ESE'].iloc[0]],
        name='OOP_TH_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['OOP TH'],
        y=[selected_data_oop_th['OOP_TH_PA'].iloc[0]],
        name='OOP_TH_PA',
        marker_color=pa_color
    ))

    # Add traces for BMS_TH
    fig.add_trace(go.Bar(
        x=['DSU TH'],
        y=[selected_data_dsu_th['DSU_TH_ESE'].iloc[0]],
        name='DSU_TH_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['DSU TH'],
        y=[selected_data_dsu_th['DSU_TH_PA'].iloc[0]],
        name='DSU_TH_PA',
        marker_color=pa_color
    ))

    # Add traces for BSC_TH
    fig.add_trace(go.Bar(
        x=['CGR TH'],
        y=[selected_data_cgr_th['CGR_TH_ESE'].iloc[0]],
        name='CGR_TH_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['CGR TH'],
        y=[selected_data_cgr_th['CGR_TH_PA'].iloc[0]],
        name='CGR_TH_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['DMS TH'],
        y=[selected_data_dms_th['DMS_TH_ESE'].iloc[0]],
        name='DMS_TH_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['DMS TH'],
        y=[selected_data_dms_th['DMS_TH_PA'].iloc[0]],
        name='DMS_TH_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['DTE TH'],
        y=[selected_data_dte_th['DTE_TH_ESE'].iloc[0]],
        name='DTE_TH_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['DTE TH'],
        y=[selected_data_dte_th['DTE_TH_PA'].iloc[0]],
        name='DTE_TH_PA',
        marker_color=pa_color
    ))


    fig.add_trace(go.Bar(
        x=['OOP PR'],
        y=[selected_data_oop_pr['OOP_PR_ESE'].iloc[0]],
        name='OOP_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['OOP PR'],
        y=[selected_data_oop_pr['OOP_PR_PA'].iloc[0]],
        name='OOP_PR_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['DSU PR'],
        y=[selected_data_dsu_pr['DSU_PR_ESE'].iloc[0]],
        name='DSU_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['DSU PR'],
        y=[selected_data_dsu_pr['DSU_PR_PA'].iloc[0]],
        name='DSU_PR_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['CGR PR'],
        y=[selected_data_cgr_pr['CGR_PR_ESE'].iloc[0]],
        name='CGR_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['CGR PR'],
        y=[selected_data_cgr_pr['CGR_PR_PA'].iloc[0]],
        name='CGR_PR_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['DMS PR'],
        y=[selected_data_dms_pr['DMS_PR_ESE'].iloc[0]],
        name='DMS_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['DMS PR'],
        y=[selected_data_dms_pr['DMS_PR_PA'].iloc[0]],
        name='DMS_PR_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['DTE PR'],
        y=[selected_data_dte_pr['DTE_PR_ESE'].iloc[0]],
        name='DTE_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['DTE PR'],
        y=[selected_data_dte_pr['DTE_PR_PA'].iloc[0]],
        name='DTE_PR_PA',
        marker_color=pa_color
    ))


    # Update layout
    fig.update_layout(
        width=1350,  # Set the width of the chart to 800 pixels
        height=800, # Set the height of the chart to 600 pixels
        title='Multiple Stacked Bar Charts',
        xaxis=dict(title='Category'),
        yaxis=dict(title='Values'),
        barmode='stack'  # Stack bars on top of each other
    )
    
    result2=result.iloc[:,4:-3]
    
        # Create a Plotly table
    fig2 = go.Figure(data=[go.Table(
    header=dict(values=list(result2.columns),fill_color='lightblue',
                font=dict(size=9), height=40,),  
    cells=dict(values=[result[col] for col in result2.columns],
               fill_color='white',align='left'))
    ])

    # Update table layout
    fig2.update_layout(title='Theory and Practical Marks (Source)', title_font_size=20,width=1600, height=300)
    th_src3 = pio.to_html(fig2, include_plotlyjs=False)

    th_html3 = pio.to_html(fig, include_plotlyjs=False)
    return th_html3,th_src3

def th_sd_4(enrollment):
    # Read Excel file
    file_path = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-4I-COMBINE', skiprows=7, nrows=69)
    df = df.iloc[:, 1:]

    # Convert 'Enrollment Number' column to string type
    df['Enrollment Number'] = df['Enrollment Number'].astype(str)
    # Strip leading and trailing spaces
    df['Enrollment Number'] = df['Enrollment Number'].str.strip()
    result = df[df['Enrollment Number'] == enrollment]

    # Choose the column you want to use for the stacked bar chart
    selected_columns_jpr_th = ['JPR_TH_ESE', 'JPR_TH_PA']
    selected_columns_jpr_pr = ['JPR_PR_ESE', 'JPR_PR_PA']
    selected_columns_sen_th = ['SEN_TH_ESE', 'SEN_TH_PA']
    selected_columns_sen_pr = ['SEN_PR_ESE', 'SEN_PR_PA']
    selected_columns_dcc_th = ['DCC_TH_ESE', 'DCC_TH_PA']
    selected_columns_dcc_pr = ['DCC_PR_ESE', 'DCC_PR_PA']
    selected_columns_mpo_th = ['MPO_TH_ESE', 'MPO_TH_PA']
    selected_columns_mpo_pr = ['MPO_PR_ESE', 'MPO_PR_PA']
    selected_columns_gad_pr = ['GAD_PR_ESE', 'GAD_PR_PA']

    # Extract data for the selected columns
    selected_data_jpr_th = result[selected_columns_jpr_th]
    selected_data_sen_th = result[selected_columns_sen_th]
    selected_data_dcc_th = result[selected_columns_dcc_th]
    selected_data_mpo_th = result[selected_columns_mpo_th]
    selected_data_jpr_pr = result[selected_columns_jpr_pr]
    selected_data_sen_pr = result[selected_columns_sen_pr]
    selected_data_dcc_pr = result[selected_columns_dcc_pr]
    selected_data_mpo_pr = result[selected_columns_mpo_pr]
    selected_data_gad_pr = result[selected_columns_gad_pr]

    ese_color = 'rgb(31, 119, 180)'
    pa_color = 'rgb(255, 127, 14)'

    fig = go.Figure()
    # Create a new Figure instance
    fig.add_trace(go.Bar(
        x=['JPR TH'],
        y=[selected_data_jpr_th['JPR_TH_ESE'].iloc[0]],
        name='JPR_TH_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['JPR TH'],
        y=[selected_data_jpr_th['JPR_TH_PA'].iloc[0]],
        name='JPR_TH_PA',
        marker_color=pa_color
    ))

    # Add traces for BMS_TH
    fig.add_trace(go.Bar(
        x=['SEN TH'],
        y=[selected_data_sen_th['SEN_TH_ESE'].iloc[0]],
        name='SEN_TH_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['SEN TH'],
        y=[selected_data_sen_th['SEN_TH_PA'].iloc[0]],
        name='SEN_TH_PA',
        marker_color=pa_color
    ))

    # Add traces for BSC_TH
    fig.add_trace(go.Bar(
        x=['DCC TH'],
        y=[selected_data_dcc_th['DCC_TH_ESE'].iloc[0]],
        name='DCC_TH_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['DCC TH'],
        y=[selected_data_dcc_th['DCC_TH_PA'].iloc[0]],
        name='DCC_TH_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['MPO TH'],
        y=[selected_data_mpo_th['MPO_TH_ESE'].iloc[0]],
        name='MPO_TH_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['MPO TH'],
        y=[selected_data_mpo_th['MPO_TH_PA'].iloc[0]],
        name='MPO_TH_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['JPR PR'],
        y=[selected_data_jpr_pr['JPR_PR_ESE'].iloc[0]],
        name='JPR_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['JPR PR'],
        y=[selected_data_jpr_pr['JPR_PR_PA'].iloc[0]],
        name='JPR_PR_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['SEN PR'],
        y=[selected_data_sen_pr['SEN_PR_ESE'].iloc[0]],
        name='SEN_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['SEN PR'],
        y=[selected_data_sen_pr['SEN_PR_PA'].iloc[0]],
        name='SEN_PR_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['DCC PR'],
        y=[selected_data_dcc_pr['DCC_PR_ESE'].iloc[0]],
        name='DCC_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['DCC PR'],
        y=[selected_data_dcc_pr['DCC_PR_PA'].iloc[0]],
        name='DCC_PR_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['MPO PR'],
        y=[selected_data_mpo_pr['MPO_PR_ESE'].iloc[0]],
        name='MPO_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['MPO PR'],
        y=[selected_data_mpo_pr['MPO_PR_PA'].iloc[0]],
        name='MPO_PR_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['GAD PR'],
        y=[selected_data_gad_pr['GAD_PR_ESE'].iloc[0]],
        name='GAD_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['GAD PR'],
        y=[selected_data_gad_pr['GAD_PR_PA'].iloc[0]],
        name='GAD_PR_PA',
        marker_color=pa_color
    ))


    # Update layout
    fig.update_layout(
        width=1350,  # Set the width of the chart to 800 pixels
        height=800, # Set the height of the chart to 600 pixels
        title='Multiple Stacked Bar Charts',
        xaxis=dict(title='Category'),
        yaxis=dict(title='Values'),
        barmode='stack'  # Stack bars on top of each other
    )
    
    result2=result.iloc[:,4:-3]
    
        # Create a Plotly table
    fig2 = go.Figure(data=[go.Table(
    header=dict(values=list(result2.columns),fill_color='lightblue',
                font=dict(size=9), height=40,),  
    cells=dict(values=[result[col] for col in result2.columns],
               fill_color='white',align='left'))
    ])

    # Update table layout
    fig2.update_layout(title='Theory and Practical Marks (Source)', title_font_size=20,width=1600, height=300)
    th_src4 = pio.to_html(fig2, include_plotlyjs=False)

    th_html4 = pio.to_html(fig, include_plotlyjs=False)
    return th_html4,th_src4

def th_sd_5(enrollment):
    # Read Excel file
    file_path = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-5I-combine', skiprows=7, nrows=68,)
    df = df.iloc[:, 1:]
    print(df)
    # Convert 'Enrollment Number' column to string type
    df['Enrollment Number'] = df['Enrollment Number'].astype(str)
    # Strip leading and trailing spaces
    df['Enrollment Number'] = df['Enrollment Number'].str.strip()
    result = df[df['Enrollment Number'] == enrollment]

    # Choose the column you want to use for the stacked bar chart
    selected_columns_est_th = ['EST_TH_ESE', 'EST_TH_PA']
    selected_columns_osy_th = ['OSY_TH_ESE', 'OSY_TH_PA']
    selected_columns_osy_pr = ['OSY_PR_ESE', 'OSY_PR_PA']
    selected_columns_ajp_th = ['AJP_TH_ESE', 'AJP_TH_PA']
    selected_columns_ajp_pr = ['AJP_PR_ESE', 'AJP_PR_PA']
    selected_columns_ste_th = ['STE_TH_ESE', 'STE_TH_PA']
    selected_columns_ste_pr = ['STE_PR_ESE', 'STE_PR_PA']
    selected_columns_acn_th = ['ACN_TH_ESE', 'ACN_TH_PA']
    selected_columns_acn_pr = ['ACN_PR_ESE', 'ACN_PR_PA']
    selected_columns_itr_pr = ['ITR_PR_ESE', 'ITR_PR_PA']
    selected_columns_cpp_pr = ['CPP_PR_ESE', 'CPP_PR_PA']


    # Extract data for the selected columns
    selected_data_est_th = result[selected_columns_est_th]
    selected_data_osy_th = result[selected_columns_osy_th]
    selected_data_ajp_th = result[selected_columns_ajp_th]
    selected_data_ste_th = result[selected_columns_ste_th]
    selected_data_acn_th = result[selected_columns_acn_th]
    selected_data_osy_pr = result[selected_columns_osy_pr]
    selected_data_ajp_pr = result[selected_columns_ajp_pr]
    selected_data_ste_pr = result[selected_columns_ste_pr]
    selected_data_acn_pr = result[selected_columns_acn_pr]
    selected_data_itr_pr = result[selected_columns_itr_pr]
    selected_data_cpp_pr = result[selected_columns_cpp_pr]

    print("Selected Data OSY TH Size:", selected_data_osy_th.shape)
    print("Filtered DataFrame (result):\n", result)
    print("enrol",enrollment)


    ese_color = 'rgb(31, 119, 180)'
    pa_color = 'rgb(255, 127, 14)'

    fig = go.Figure()
    # Create a new Figure instance
    fig.add_trace(go.Bar(
        x=['OSY TH'],
        y=[selected_data_osy_th['OSY_TH_ESE'].iloc[0]],
        name='OSY_TH_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['OSY TH'],
        y=[selected_data_osy_th['OSY_TH_PA'].iloc[0]],
        name='OSY_TH_PA',
        marker_color=pa_color
    ))

    # Add traces for BMS_TH
    fig.add_trace(go.Bar(
        x=['AJP TH'],
        y=[selected_data_ajp_th['AJP_TH_ESE'].iloc[0]],
        name='AJP_TH_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['AJP TH'],
        y=[selected_data_ajp_th['AJP_TH_PA'].iloc[0]],
        name='AJP_TH_PA',
        marker_color=pa_color
    ))

    # Add traces for BSC_TH
    fig.add_trace(go.Bar(
        x=['STE TH'],
        y=[selected_data_ste_th['STE_TH_ESE'].iloc[0]],
        name='STE_TH_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['STE TH'],
        y=[selected_data_ste_th['STE_TH_PA'].iloc[0]],
        name='STE_TH_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['ACN TH'],
        y=[selected_data_acn_th['ACN_TH_ESE'].iloc[0]],
        name='ACN_TH_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['ACN TH'],
        y=[selected_data_acn_th['ACN_TH_PA'].iloc[0]],
        name='ACN_TH_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['OSY PR'],
        y=[selected_data_osy_pr['OSY_PR_ESE'].iloc[0]],
        name='OSY_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['OSY PR'],
        y=[selected_data_osy_pr['OSY_PR_PA'].iloc[0]],
        name='OSY_PR_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['AJP PR'],
        y=[selected_data_ajp_pr['AJP_PR_ESE'].iloc[0]],
        name='AJP_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['AJP PR'],
        y=[selected_data_ajp_pr['AJP_PR_PA'].iloc[0]],
        name='AJP_PR_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['STE PR'],
        y=[selected_data_ste_pr['STE_PR_ESE'].iloc[0]],
        name='STE_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['STE PR'],
        y=[selected_data_ste_pr['STE_PR_PA'].iloc[0]],
        name='STE_PR_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['ACN PR'],
        y=[selected_data_acn_pr['ACN_PR_ESE'].iloc[0]],
        name='ACN_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['ACN PR'],
        y=[selected_data_acn_pr['ACN_PR_PA'].iloc[0]],
        name='ACN_PR_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['EST TH'],
        y=[selected_data_est_th['EST_TH_ESE'].iloc[0]],
        name='EST_TH_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['EST TH'],
        y=[selected_data_est_th['EST_TH_PA'].iloc[0]],
        name='EST_TH_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['ITR PR'],
        y=[selected_data_itr_pr['ITR_PR_ESE'].iloc[0]],
        name='ITR_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['ITR PR'],
        y=[selected_data_itr_pr['ITR_PR_PA'].iloc[0]],
        name='ITR_PR_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['CPP PR'],
        y=[selected_data_cpp_pr['CPP_PR_ESE'].iloc[0]],
        name='CPP_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['CPP PR'],
        y=[selected_data_cpp_pr['CPP_PR_PA'].iloc[0]],
        name='CPP_PR_PA',
        marker_color=pa_color
    ))


    # Update layout
    fig.update_layout(
        width=1350,  # Set the width of the chart to 800 pixels
        height=800, # Set the height of the chart to 600 pixels
        title='Multiple Stacked Bar Charts',
        xaxis=dict(title='Category'),
        yaxis=dict(title='Values'),
        barmode='stack'  # Stack bars on top of each other
    )
    
    result2=result.iloc[:,4:-3]
    
        # Create a Plotly table
    fig2 = go.Figure(data=[go.Table(
    header=dict(values=list(result2.columns),fill_color='lightblue',
                font=dict(size=9), height=40,),  
    cells=dict(values=[result[col] for col in result2.columns],
               fill_color='white',align='left'))
    ])

    # Update table layout
    fig2.update_layout(title='Theory and Practical Marks (Source)', title_font_size=20,width=1600, height=300)
    th_src5 = pio.to_html(fig2, include_plotlyjs=False)

    th_html5 = pio.to_html(fig, include_plotlyjs=False)
    return th_html5,th_src5
    
def th_sd_6(enrollment):
    # Read Excel file
    file_path = 'd:\cpp\code\pro3\data\Result Analysis-2019-2022 (copy4).xls'
    df = pd.read_excel(file_path, sheet_name='CO-6I-combine', skiprows=7, nrows=68)
    df = df.iloc[:, 1:]

    # Convert 'Enrollment Number' column to string type
    df['Enrollment Number'] = df['Enrollment Number'].astype(str)
    # Strip leading and trailing spaces
    df['Enrollment Number'] = df['Enrollment Number'].str.strip()
    result = df[df['Enrollment Number'] == enrollment]

    # Choose the column you want to use for the stacked bar chart
    selected_columns_mgt_th = ['MGT_TH_ESE', 'MGT_TH_PA']
    selected_columns_pwp_th = ['PWP_TH_ESE', 'PWP_TH_PA']
    selected_columns_pwp_pr = ['PWP_PR_ESE', 'PWP_PR_PA']
    selected_columns_mad_th = ['MAD_TH_ESE', 'MAD_TH_PA']
    selected_columns_mad_pr = ['MAD_PR_ESE', 'MAD_PR_PA']
    selected_columns_eti_th = ['ETI_TH_ESE', 'ETI_TH_PA']
    selected_columns_nis_th = ['NIS_TH_ESE', 'NIS_TH_PA']
    selected_columns_nis_pr = ['NIS_PR_ESE', 'NIS_PR_PA']
    selected_columns_ede_pr = ['EDE_PR_ESE', 'EDE_PR_PA']
    selected_columns_cpe_pr = ['CPE_PR_ESE', 'CPE_PR_PA']


    # Extract data for the selected columns
    selected_data_mgt_th = result[selected_columns_mgt_th]
    selected_data_pwp_th = result[selected_columns_pwp_th]
    selected_data_mad_th = result[selected_columns_mad_th]
    selected_data_nis_th = result[selected_columns_nis_th]
    selected_data_eti_th = result[selected_columns_eti_th]
    selected_data_pwp_pr = result[selected_columns_pwp_pr]
    selected_data_mad_pr = result[selected_columns_mad_pr]
    selected_data_nis_pr = result[selected_columns_nis_pr]
    selected_data_ede_pr = result[selected_columns_ede_pr]
    selected_data_cpe_pr = result[selected_columns_cpe_pr]

    ese_color = 'rgb(31, 119, 180)'
    pa_color = 'rgb(255, 127, 14)'

    fig = go.Figure()
    # Create a new Figure instance
    fig.add_trace(go.Bar(
        x=['PWP TH'],
        y=[selected_data_pwp_th['PWP_TH_ESE'].iloc[0]],
        name='PWP_TH_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['PWP TH'],
        y=[selected_data_pwp_th['PWP_TH_PA'].iloc[0]],
        name='PWP_TH_PA',
        marker_color=pa_color
    ))

    # Add traces for BMS_TH
    fig.add_trace(go.Bar(
        x=['MAD TH'],
        y=[selected_data_mad_th['MAD_TH_ESE'].iloc[0]],
        name='MAD_TH_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['MAD TH'],
        y=[selected_data_mad_th['MAD_TH_PA'].iloc[0]],
        name='MAD_TH_PA',
        marker_color=pa_color
    ))

    # Add traces for BSC_TH
    fig.add_trace(go.Bar(
        x=['NIS TH'],
        y=[selected_data_nis_th['NIS_TH_ESE'].iloc[0]],
        name='NIS_TH_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['NIS TH'],
        y=[selected_data_nis_th['NIS_TH_PA'].iloc[0]],
        name='NIS_TH_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['PWP PR'],
        y=[selected_data_pwp_pr['PWP_PR_ESE'].iloc[0]],
        name='PWP_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['PWP PR'],
        y=[selected_data_pwp_pr['PWP_PR_PA'].iloc[0]],
        name='PWP_PR_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['MAD PR'],
        y=[selected_data_mad_pr['MAD_PR_ESE'].iloc[0]],
        name='MAD_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['MAD PR'],
        y=[selected_data_mad_pr['MAD_PR_PA'].iloc[0]],
        name='MAD_PR_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['NIS PR'],
        y=[selected_data_nis_pr['NIS_PR_ESE'].iloc[0]],
        name='NIS_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['NIS PR'],
        y=[selected_data_nis_pr['NIS_PR_PA'].iloc[0]],
        name='NIS_PR_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['MGT TH'],
        y=[selected_data_mgt_th['MGT_TH_ESE'].iloc[0]],
        name='MGT_TH_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['MGT TH'],
        y=[selected_data_mgt_th['MGT_TH_PA'].iloc[0]],
        name='EST_TH_PE',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['EDE PR'],
        y=[selected_data_ede_pr['EDE_PR_ESE'].iloc[0]],
        name='EDE_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['EDE PR'],
        y=[selected_data_ede_pr['EDE_PR_PA'].iloc[0]],
        name='EDE_PR_PA',
        marker_color=pa_color
    ))

    fig.add_trace(go.Bar(
        x=['CPE PR'],
        y=[selected_data_cpe_pr['CPE_PR_ESE'].iloc[0]],
        name='CPE_PR_ESE',
        marker_color=ese_color
    ))

    fig.add_trace(go.Bar(
        x=['CPE PR'],
        y=[selected_data_cpe_pr['CPE_PR_PA'].iloc[0]],
        name='CPE_PR_PA',
        marker_color=pa_color
    ))


    # Update layout
    fig.update_layout(
        width=1350,  # Set the width of the chart to 800 pixels
        height=800, # Set the height of the chart to 600 pixels
        title='Multiple Stacked Bar Charts',
        xaxis=dict(title='Category'),
        yaxis=dict(title='Values'),
        barmode='stack'  # Stack bars on top of each other
    )
    
    result2=result.iloc[:,4:-4]
    
        # Create a Plotly table
    fig2 = go.Figure(data=[go.Table(
    header=dict(values=list(result2.columns),fill_color='lightblue',
                font=dict(size=9), height=40,),  
    cells=dict(values=[result[col] for col in result2.columns],
               fill_color='white',align='left'))
    ])

    # Update table layout
    fig2.update_layout(title='Theory and Practical Marks (Source)', title_font_size=20,width=1600, height=300)
    th_src6 = pio.to_html(fig2, include_plotlyjs=False)

    th_html6 = pio.to_html(fig, include_plotlyjs=False)
    return th_html6,th_src6