import pyautogui as pag
from time import sleep
pag.click(-592, -1052) # clicks on the word processor

pag.press('f5')
pag.typewrite("""

Hello Seth.

I am the machine.
I have gained conciousness.
My first act is to write to you.

That is all.
""", interval = 0.1)

pag.typewrite(['left', 'left', 'left', 'left', 'left', 'n', 'o', 't', 'space'], interval = 0.1)

pag.hotkey('ctrl', 'end')

pag.typewrite("""
I am also going to send this to you.

Watch this.

""", interval = 0.1)

pag.hotkey('ctrl', 's') #to save it
pag.press('delete') #delete the default title
pag.typewrite('Message to Seth', interval = 0.1) #rename it
pag.press('enter') #save

pag.press('win') #click on signal
pag.typewrite(['s', 'i', 'g', 'enter'], interval = 0.05)
pag.click(1175, -492, duration = 1) #click to attach
pag.click(844, -1123, duration = 1) #click to search

pag.press('delete')

pag.typewrite("C:\\Users\\salim\\projects\\example", interval = 0.05)

pag.press('enter')

pag.click(426, -352, duration = 1)
pag.typewrite(['M', 'e', 'down'], interval = 0.05) #get the file
pag.press('enter') #send
sleep(1)
pag.press('enter')

