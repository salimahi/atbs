from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import os

os.chdir('C:\\users\\salim\\projects')

# Read the spreadsheet containing the form data
data = pd.read_csv('gwg_data.csv')

# Initialize Chrome driver
driver = webdriver.Chrome()

# Visit the website
driver.get('https://google.bleekerconnect.com/front/signup')

# Wait for the page to load
time.sleep(5)

# Loop through each row of the spreadsheet
for index, row in data.iterrows():
    # Wait for the element to be visible
    wait = WebDriverWait(driver, 10)
    first_name_element = wait.until(EC.visibility_of_element_located((By.NAME, 'firstName')))

    # Clear and fill out the first name input field
    first_name_element.clear()
    first_name_element.send_keys(row['First Name'])

    # Clear and fill out the last name input field
    last_name_element = driver.find_element(By.ID, 'last_name')
    last_name_element.clear()
    last_name_element.send_keys(row['Last Name'])

    # Clear and fill out the email input field
    email_element = driver.find_element(By.ID, 'email')
    email_element.clear()
    email_element.send_keys(row['Email'])

    # Clear and fill out the confirm email input field
    confirm_email_element = driver.find_element(By.ID, 'confirm-email')
    confirm_email_element.clear()
    confirm_email_element.send_keys(row['Email'])

    # Clear and fill out the password input field
    password_element = driver.find_element(By.ID, 'password')
    password_element.clear()
    password_element.send_keys(row['Password'])

    # Clear and fill out the confirm password input field
    confirm_password_element = driver.find_element(By.ID, 'confirm-pass')
    confirm_password_element.clear()
    confirm_password_element.send_keys(row['Password'])

    # Select the seniority from the dropdown menu
    seniority_dropdown = Select(driver.find_element(By.NAME, 'senioritySelect'))
    seniority_dropdown.select_by_visible_text(row['Seniority'])

    # Check the box
    checkbox_element = driver.find_element(By.ID, 'termsAndPrivacy')
    driver.execute_script("arguments[0].click();", checkbox_element)

    # Click the register button
    button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()

    # Wait for the registration process to complete (you may need to adjust the wait duration)
    time.sleep(5)

    # Go back to the registration page for the next iteration
    driver.get('https://google.bleekerconnect.com/front/signup')

# Close the browser
driver.quit()
