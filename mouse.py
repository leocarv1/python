import pyautogui as pg
import time
# print(pg.size())

# pg.moveRel(0, 50, duration=2)
# pg.click()
# pg.typewrite("Hello world!")
# print(pg.position())
# pg.press('winleft')
# pg.write('bloco')
# pg.press('enter')
# time.sleep(2)
# pg.write('Testando', interval=0.25)
# pg.hotkey('alt','f4')
# pg.hotkey('winleft', 'd')

# faz um desenho em espiral
def draw():
    pg.press('winleft')
    pg.write('paint')
    pg.press('enter')
    time.sleep(2)
    distance = 100
    pg.click()
    while distance > 0:
        pg.drag(distance, 0)   # move right
        distance -= 5
        pg.drag(0, distance)   # move down
        pg.drag(-distance, 0)  # move left
        distance -= 5
        pg.drag(0, -distance)  # move up
    
    pg.hotkey('alt', 'f4')
    pg.press('right')
    pg.press('enter')

def criaArquivo():
    # minimiza tudo
    pg.hotkey('winleft', 'd')

    # cria uma nova pasta
    pg.click(button='right')
    pg.press('down', presses=10)
    pg.press('enter', presses=2)
    time.sleep(1)
    pg.write('Python Auto')
    pg.press('enter', presses=2)
    time.sleep(2)

    # cria arquivo dentro da pasta
    pg.click(button='right')
    pg.press('down', presses=13)
    pg.press('enter')
    pg.press('down', presses=10)
    pg.press('enter')


criaArquivo()