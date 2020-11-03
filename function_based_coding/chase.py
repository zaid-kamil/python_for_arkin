import pgzrun

WIDTH = 600
HEIGHT = 600

herotank  = Actor('tank1', topleft = (100,200))
enemy  = Actor('tank2_flipped', topleft = (600,500))
bg = Actor('background')
is_hero_destroyed = False

def draw():
    screen.clear()
    bg.draw()
    herotank.draw()
    enemy.draw()

def update():
    global is_hero_destroyed

    if not is_hero_destroyed:
        if keyboard.right:
            herotank.x +=2
        elif keyboard.left:
            herotank.x -=2
        elif keyboard.up:
            herotank.y -=2
        elif keyboard.down:
            herotank.y +=2
    if enemy.x < herotank.x:
        enemy.x += 1
    if enemy.x > herotank.x:
        enemy.x -= 1
    if enemy.y < herotank.y:
        enemy.y += 1
    if enemy.y > herotank.y:
        enemy.y -= 1

    if enemy.colliderect(herotank) and not is_hero_destroyed:
        herotank.image = 'tank_destroyed'
        is_hero_destroyed=True
        sounds.collision.play()

pgzrun.go()

