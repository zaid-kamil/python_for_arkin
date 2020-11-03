from random import randint
import pgzrun
import random

WIDTH = 600
HEIGHT = 600

hero  = Actor('hero', topleft = (100,200))
cursor  = Actor('dot')
score = 0

def draw():
    screen.clear()
    hero.draw()
    screen.draw.text(f'score:{score}',(10,10))
    cursor.draw()


    

def on_mouse_down(pos, button):
    global score
    if button == mouse.LEFT and hero.colliderect(cursor):
        hero.image = 'tank_destroyed'
        sounds.collision.play()
        score +=1
        clock.schedule_unique(jump, .3)

def on_mouse_move(pos):
    cursor.pos = pos

def jump():
    newpos = random.randint(0, WIDTH), random.randint(0,HEIGHT)
    animate(hero, pos=newpos,duration=1)
    hero.image = 'hero'

clock.schedule_interval(jump, .3)
pgzrun.go()