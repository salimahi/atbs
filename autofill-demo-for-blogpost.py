import pyautogui as pag
import pandas as pd
import os
from time import sleep

os.chdir('C:/Users/salim/Dropbox/My PC (DESKTOP-F3CUOT7)/Documents/GitHub/atbs/') #to read the file with the data

# Read the spreadsheet containing the form data
data = pd.read_csv('color.csv')

for index, row in data.iterrows():
    pag.click(-204,-830) #clicking into the first open box
    pag.write(row['first name']) #or whatever the column title is.
    pag.press('tab')
    pag.write(row['last name']) #or whatever the column title is.
    pag.press('tab')
    pag.write(row['favorite color']) #or whatever the column title is.
    pag.press('tab')
    pag.press('enter')
    sleep(1) #to allow for the page to load
    pag.click(-150,-1021) #to click on “submit another response”
    sleep(1) #to allow for the page to load
