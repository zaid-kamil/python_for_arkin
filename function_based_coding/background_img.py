import pgzrun

WIDTH = 600
HEIGHT = 600

tank  = Actor('tank1', topleft = (100,200))
bg = Actor('background')
bg_move_left = True

def draw():
    screen.clear()
    bg.draw()
    tank.draw()

def update():
    global bg_move_left
    tank.x += 10
    if tank.x > WIDTH:
        tank.x = -100

pgzrun.go()