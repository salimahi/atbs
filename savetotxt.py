import sys #so it can run from the command line
import pyperclip #so it can access your clipboard

text = pyperclip.paste() #saves what's in your clipboard
filename = '-'.join(sys.argv[1:]) #saves the text file as whatever you type in but replaces the spaces with -

saveFile = open('C:\\Users\\salim\\projects\\saved texts\\' + filename +'.txt','w') #creates the text file in your preset folder
saveFile.write(text) #pastes in the text from your clipboard
saveFile.close() #closes the file so it doesn't keep running

 
