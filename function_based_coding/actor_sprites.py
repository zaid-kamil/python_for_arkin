import pgzrun

WIDTH = 800
HEIGHT = 600

tank1 = Actor('tank1',topleft = (0,50))

def draw():
    screen.clear()
    tank1.draw()

def update():
    
    if keyboard.right:
        tank1.x +=2
    if keyboard.left:
        tank1.x -=2

    if tank1.x > WIDTH:
        tank1.x = -50

pgzrun.go()