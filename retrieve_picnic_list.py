import pickle #so we can retreive the file

## This allows you to retrieve the file
with open('picnic_data.pkl', 'rb') as f:
    picnic = pickle.load(f)

## This is the same code from 'create picnic.py' to format the list nicely
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

printPicnic(picnic, 13, 10)

## This is mostly the same code from 'create picnic.py' to allow you to edit
## the list, except the first prompt that asks you if you want to make any edits.

print(f"Do you want to add additional supplies to the list? (y/n)")
addition = input()
if addition.lower().startswith('y'):
    while True:
        print(f"Add a supply to the picnic list!(press Enter when list is complete)")
        supply = input()
        if supply == '':
            break
        if supply in picnic:
            print(f"We have {picnic[supply]} {supply} for the picnic. Do you want to update the number?")
            update = input()
            if update.lower().startswith('y'):
                print(f"Enter the new amount of {supply} now:")
                newAmount = input()
                picnic[supply] = newAmount
            else:
                 pass
        else:
            print(f"Please enter in the amount of {supply}")
            amount = input()
            picnic[supply] = amount
            print(f"Picnic List is updated.")

print(f"Here is your final picnic list:")
printPicnic(picnic, 13, 10)
