import gspread

# Initialize your gc object with service account credentials or OAuth2 credentials here
gc = gspread.service_account('xxx.json')


# Try to access a Google Sheet
try:
    # Replace 'YOUR_SPREADSHEET_ID' with the ID of a Google Sheet you have access to
    sheet = gc.open_by_key('1XAd0ERBrRe3QgxxxAFpuFGvsTdPBK0')
    worksheet = sheet.get_worksheet(4)  # You can choose a specific worksheet index here
    cell_value = worksheet.acell('A1').value  # Access a cell's value

    # If you reach this point without encountering authentication errors, your gc object is authenticated.
    print("Authentication successful!")

except gspread.exceptions.APIError as e:
    # If you encounter an authentication error, it will be captured here.
    print(f"Authentication error: {e}")

# You can continue with your code after this point
