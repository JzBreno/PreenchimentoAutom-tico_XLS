import pyautogui as pg
import time 
import mouse


def BuscarQacademico():
    pg.PAUSE = 1
    pg.press('win')
    pg.write('chrome')
    time.sleep(2)
    pg.press('enter')
    time.sleep(2)
    pg.moveTo(695, 507)
    pg.click()
    pg.moveTo(1368, 293)
    pg.click()
    time.sleep(1)
    pg.moveTo(639, 65)
    pg.click()
    pg.write('https://antigo.qacademico.ifce.edu.br/')
    pg.moveTo(572, 103)
    pg.click()
    pg.press('enter131099')
    pg.moveTo(695, 252)
    pg.click()
    pg.moveTo(731, 303)
    pg.click()
    pg.moveTo(922, 546)
    pg.click()
    pg.write('131099')
    pg.moveTo(873, 258)
    pg.click()

BuscarQacademico()