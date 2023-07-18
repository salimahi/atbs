import pyautogui as pag
from random import randint

pag.click() #start from where the mouse is placed
distance = 500
while distance > 0:
    pag.dragRel(distance, randint(0, 10), duration = 1) #move to the right
    distance = distance - randint(0, 50)
    pag.dragRel(randint(0, 10), distance, duration = 1) #move down
    distance = distance - randint(0, 50)
    pag.dragRel(-distance, randint(0, 10), duration = 1) #move left
    distance = distance - randint(0, 50)
    pag.dragRel(randint(0, 10), -distance, duration = 1) #move up
    distance = distance - randint(0, 50)
    
