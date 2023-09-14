import pyautogui as pag
import time
import pandas as pd
import os

os.chdir('C:\\users\\salim\\projects')

# Read the spreadsheet containing the form data
data = pd.read_csv('user_texts_buckup.csv')

# Loop through each row of the spreadsheet
for index, row in data.iterrows():
    pag.click(431, 320)
    time.sleep(2)
    pag.write(row.to_string(index=False))  # Write the entire row as a string
    pag.sleep(1)
    pag.hotkey('enter')
    pag.sleep(1)
    pag.keyDown('tab')
    pag.keyDown('tab')
    pag.sleep(2)
    pag.write('/snippets')
    pag.sleep(1)
    pag.click(716, 1441)
    pag.write('debit')
    pag.sleep(1)
    pag.click(716, 1441)
    pag.sleep(2)
    pag.hotkey('enter')
    time.sleep(1)
