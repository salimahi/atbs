import re
import pyperclip
import os

# Create a regex object for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-000, (415) 555-0000, 555-000 ext 12345, ext. 12345, x12345
(
((\d{3})|(\(\d{3}\)))?          # area code (optional)
(\s|-)                              # first separator
\d{3}                # first 3 digits
-            # separator
\d{4}            # last 4 digits
((ext(\.)?\s)|x)?        # extension word-part (optional)
(\d{2,5})?     # extension number-part (optional)
)
''', re.VERBOSE)


# Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@some-thing.com

[a-zA-Z0-9_.+-]+        # name part
@        # @ symbol
[a-zA-Z0-9_.+-]+         # domain name part
''', re.VERBOSE)


# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Copy the extracted email/phone to the clipboard
# sets up new lines, can separate by comma or anything else
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)

# Create a text file and save the results in the current directory
directory = os.getcwd()
saveFile = open(directory + '\\scraped-data.txt', 'w')
saveFile.write(results)
saveFile.close()



