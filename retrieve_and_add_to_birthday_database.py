import pickle

import os

# Pick the directory where you want to retrieve the pkl file
os.chdir("C:\\Users\\salim\\Dropbox\\My PC (DESKTOP-F3CUOT7)\\Documents\\GitHub\\atbs")

with open('birthday_database.pkl', 'rb') as bdb:
    birthdays = pickle.load(bdb)

# Format the database
def printBirthdays(itemsDict, leftWidth, rightWidth):
    print('Birthday Database'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth) + v.ljust(rightWidth))

printBirthdays(birthdays, 20, 10)

# Add new entries to the database
while True:
    print(f"Do you want to add more birthdays to your database? (y/n)")
    addition = input()
    if addition.lower().startswith('n'):
        break
    else:
        print('Type in a name: (press Enter to quit)')
        name = input()
        if name == '':
            break
        if name in birthdays:
            print(f"{birthdays[name]} is {name}'s Birthday. Do you want to correct it?")
            correction = input()
            if correction.lower().startswith('y'):
                print(f"Enter {name}'s new birthday now:")
                newBirth = input()
                birthdays[name] = newBirth
            else:
                pass
        else:
            print(f"I do not have birthday information for {name}. Please enter their birthday now:")
            bday = input()
            birthdays[name] = bday
            print(f"Birthday database updated. {name}'s birthday is {bday}.")
    
# Print the final list
print(f"Here is your final birthday list:")
printBirthdays(birthdays, 20, 10)
