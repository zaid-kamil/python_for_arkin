import pgzrun

WIDTH = 600
HEIGHT = 600

tank  = Actor('tank1', topleft = (100,200))
box = Rect((500,200),(20,60))

def draw():
    screen.clear()
    screen.draw.filled_rect(box,'blue')
    tank.draw()

def update():
    if tank.colliderect(box):
        tank.image = 'tank_explosion3'
    else:
        tank.x += 2
    if tank.x > WIDTH:
        tank.x = -100

pgzrun.go()

# make the box do vertical movement