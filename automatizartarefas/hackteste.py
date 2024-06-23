import pyautogui as pag
from time import sleep
sleep(2)


with open('falas.txt', 'r') as arquivo:
    for i in arquivo:
       pag.write(i)
       pag.press('Enter')