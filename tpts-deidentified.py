import gspread
import pandas as pd
from time import sleep
import os
os.chdir('C:\\Users\\salim\\projects')

gc = gspread.service_account(#get the .json file)

#Access the spreadsheet where the report will go - AKA "Report Spreadsheet"
REPORT = 'redacted' #pulled from the google sheet URL
report_sheet = gc.open_by_key(REPORT)
report_worksheet = report_sheet.get_worksheet(0)

sheet_id_list = [record['id'] for record in gc.list_spreadsheet_files() if record['name'].startswith('TPTS')]

#Creating a function that will pull the information I need from the TPTS spreadsheets and append them to the Report spreadsheet.
def extract_worksheet(sheet_id,worksheet_id):
    spreadsheet = gc.open_by_key(sheet_id)
    worksheet = spreadsheet.get_worksheet_by_id(worksheet_id)
    rows = worksheet.get_all_values()

    df = pd.DataFrame(rows)
    col_Names = df.iloc[8,1:]

    df = df.iloc[9:,1:]
    df.columns = col_Names
    df = df.drop('Duration', errors='ignore', axis=1)
    
    etp_report = df[(df['Type of work'] == 'Client facing: Thinking Partner session (TPs)') & (df['TP session held?'] == 'Yes')]

    num_rows_appended = len(etp_report)

    report_worksheet.append_rows(etp_report.values.tolist())

    print(f"{spreadsheet.title}, {worksheet.title}: {num_rows_appended} rows appended")

    sleep(10)
    
def get_worksheet_id_list(sheet_id):
    sheet = gc.open_by_key(sheet_id)
    return [record.id for record in sheet.worksheets() if record.title != 'Lists']
    

for sheet_id in sheet_id_list:
    worksheet_id_list = get_worksheet_id_list(sheet_id)
    for worksheet_id in worksheet_id_list:
        extract_worksheet(sheet_id, worksheet_id)



