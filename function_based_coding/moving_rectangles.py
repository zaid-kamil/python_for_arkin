
import pgzrun

WIDTH = 800
HEIGHT = 400
COORDS = "0,0"

box = Rect((20,20), (100,50))

def draw():
    screen.clear()
    screen.draw.filled_rect(box,'green')
    screen.draw.text(COORDS,(20,70),color='green')

def update():
    global COORDS
    box.x = box.x + 2
    box.y = box.y + 2
    if box.x > WIDTH:
        box.x = 0
    if box.y > HEIGHT:
        box.y = 0
    COORDS = f'{box.x},{box.y}'


pgzrun.go()