import pandas as pd
import smtplib
import imaplib
import email
import os

# Set up IMAP server and credentials
imap_server = "imap.gmail.com"
imap_port = 993
username = #"email@email.com"
password = #"oaefganodiogjaer"

#upload the spreadsheet
os.chdir('C:\\users\\salim\\projects')
data = pd.read_csv('data.csv')

#login to gmail
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
smtp_connection.ehlo()
smtp_connection.starttls()
smtp_connection.login(username, password)

# Login to IMAP server
imap_connection = imaplib.IMAP4_SSL(imap_server, imap_port)
imap_connection.login(username, password)
imap_connection.select("INBOX")  # Select the inbox folder

#send the emails
for i in range(0, data.shape[0]):
    sender_name = #"Bleeker Admin"
    sender_email = username
    recipient_email = data.Email[i]
    subject = "Your Bleeker Connect Account Information"
    message = f"""Subject: {subject}

Dear {data.First[i]},

Here is your login information for https://google.bleekerconnect.com:

Username: {data.Email[i]}
Password: {data.Password[i]}

If you have any questions or issues, please respond to this email.

Take care,
Team Bleeker

"""
    final_message = f"From: {sender_name} <{sender_email}>\nTo: {recipient_email}\n{message}"

    # Send email using SMTP
    smtp_connection.sendmail(sender_email, recipient_email, final_message)
    
    # Move sent email to "Sent" folder using IMAP
    result, data_sent = imap_connection.search(None, "ALL")  # Search all emails
    latest_email_id = data_sent[0].split()[-1]  # Get the ID of the latest email
    imap_connection.store(latest_email_id, "+X-GM-LABELS", "\\Sent")  # Move the email to the "Sent" folder

# Logout and close the connections
smtp_connection.quit()
imap_connection.close()
imap_connection.logout()
