import time
import pyautogui as gui

#récupération des coordonées des points de récoltes
"""
k=0
while k != 1:
    gui.keyDown('y')
    time.sleep(1)
    x, y = gui.position()
    print(x,",",y)
gui.keyUp('y')
"""

#tableaux avec les coordonées : les 0 séparent les zone (-1,-5 puis -1,-6)
x = [0,-452,-374,-540,-480,-407,-448,-524,-589,-747,-851,-1012,-1121,-1209,-945,0,-717,-789,-892,-898,-864,-968,-890,-846,-979]
y = [0,738,700,612,582,586,496,502,414,393,414,753,721,748,25,0,767,749,770,634,566,570,513,209,914]
q = 0
while q != 1:
    for i in range(24):
        if x[i] ==0:
            time.sleep(20)
        else:
            gui.keyDown('shift')
            gui.moveTo(x[i],y[i],0.1)
            print(x[i],",",y[i])
            gui.click()
            gui.keyUp('shift')
#"""