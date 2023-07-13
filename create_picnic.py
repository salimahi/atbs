import pickle #so we can save the file 

picnic = {} #creating a blank dictionary

while True:
    print(f"Add a supply to the picnic list!(press Enter when list is complete)")
    supply = input()
    
    ## This part is to close out the program once input is complete
    if supply == '': 
        break 

    ## This part prompts you if you enter anything that is already recorded and gives you the option to update inventory amount.
    if supply in picnic:
        print(f"We have {picnic[supply]} {supply} for the picnic. Do you want to update the number?")
        update = input()
        if update.lower().startswith('y'):
            print(f"Enter the new amount of {supply} now:")
            newAmount = input()    
            picnic[supply] = newAmount
        else:
            pass 

    ## This part lets you enter in new items and the amount. 
    else:
        print(f"Please enter in the amount of {supply}")
        amount = input()
        picnic[supply] = amount
        print(f"Picnic List is updated.")
            
## This prints out the list nicely
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

printPicnic(picnic, 13, 10)

## This saves all your hard work into a file called 'picnic_data.pkl'
with open('picnic_data.pkl', 'wb') as f:
    pickle.dump(picnic, f)
    print("Picnic items saved as a file.")


