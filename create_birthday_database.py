import pickle
import os

# Pick the directory where you want to save the pkl file
os.chdir("C:\\Users\\salim\\Dropbox\\My PC (DESKTOP-F3CUOT7)\\Documents\\GitHub\\atbs")

# Create Birthday dictionary
birthdays = {}

# Enter in Birthdays
while True:
    print('Type in a name: (press Enter to quit)')
    name = input()
    if name == '':
        break
    
    # Avoid repetition
    if name in birthdays:
        print(f"{birthdays[name]} is the birthday of {name}")

    else:
        print(f"I do not have birthday information for {name}. Please enter their birthday now:")
        bday = input()
        birthdays[name] = bday
        print(f"Birthday database updated. {name}'s birthday is {bday}.")
    
# Save the database as a file to retrieve
with open('birthday_database.pkl', 'wb') as bdb:
    pickle.dump(birthdays, bdb)
    print("Your Birthday Database has been created.")
