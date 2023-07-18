import webbrowser, sys, pyperclip

sys.argv #['mapit.py', '870', 'Valencia', 'St.']

# Check if command line arguments were passed

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:]) # connects everything in the list after mapit
else:
    address = pyperclip.paste()

#https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)
