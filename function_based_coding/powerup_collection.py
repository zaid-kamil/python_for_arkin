import pgzrun
import random

WIDTH = HEIGHT = 500
tank = Actor('tank2_flipped',topleft =(400,400))
box = Rect((20,20),(50,50))
score = 0


def draw():
    screen.clear()
    screen.draw.filled_rect(box,'green')
    tank.draw()
    screen.draw.text(f'score:{score}',(10,470))

def update():
    global score
    if keyboard.right:
        tank.x +=2
    elif keyboard.left:
        tank.x -=2
    elif keyboard.up:
        tank.y -=2
    elif keyboard.down:
        tank.y +=2

    if tank.colliderect(box):
        box.x = random.randint(0,WIDTH)
        box.y = random.randint(0,HEIGHT)
        score += 1

pgzrun.go()

# Combine the program with the chasing enemy program,
# add a sound when power up is collected ,
# and try to make a game