import pgzrun
import os
print('-'*30)
print(os.getcwd())
print(os.listdir())
print('-'*30)

TILE_SIZE = 64
# a map with 10x10 grid 
WIDTH = TILE_SIZE * 10
HEIGHT = TILE_SIZE * 10

tiles = ['road','wall','goal','key']
maze = [
    [1 ,1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1 ,0, 1, 3, 0, 0, 0, 0, 0, 1],
    [1 ,0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1 ,0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1 ,1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1 ,1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1 ,1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1 ,0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1 ,0, 1, 1, 0, 0, 0, 1, 2, 1],
    [1 ,1, 1, 1, 1, 1, 1, 1, 1, 1],
]

player = Actor('little_hero',topleft=(1*TILE_SIZE,1*TILE_SIZE))
enemy1 = Actor('zombie',topleft=(1* TILE_SIZE, 7*TILE_SIZE))
moveForward = True
playerDead = False
unlock = 0
msg = ""


def draw():
    screen.clear()
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            x= col * TILE_SIZE
            y = row * TILE_SIZE
            img = tiles[maze[row][col]]
            screen.blit(img, (x,y))
    player.draw()
    enemy1.draw()
    screen.draw.text(msg, (4*TILE_SIZE,4*TILE_SIZE),color='red',fontsize= 100,fontname='arial')

def on_key_down(key):
    global unlock
    global msg
    row = int(player.y// TILE_SIZE)
    col = int(player.x// TILE_SIZE)
    if key == keys.UP:
        row -= 1
    if key == keys.DOWN:
        row += 1
    if key == keys.LEFT:
        col -= 1
    if key == keys.RIGHT:
        col += 1
    print(row,col)
    tile = tiles[maze[row][col]]
    if tile =='road' and not playerDead:
       move_player(row,col)
    if tile == 'key' and not playerDead :
        unlock +=1
        maze[row][col] = 0
        move_player(row,col)
    if tile =='goal' and unlock > 0:
        msg = 'You win'
        move_player(row,col)

def move_player(row,col):
    x = col*TILE_SIZE
    y = row*TILE_SIZE
    animate(player,topleft=(x,y),duration=.2)

def update():
    global moveForward
    global msg
    row = int(enemy1.y// TILE_SIZE)
    col = int(enemy1.x// TILE_SIZE)
    if moveForward:
        col += 1
    else:
        col -= 1
    tile = tiles[maze[row][col]]
    if not tile =='wall':
        x = col*TILE_SIZE
        y = row*TILE_SIZE
        animate(enemy1,topleft=(x,y),duration=.3)
    else:
        moveForward = not moveForward
    
    if enemy1.colliderect(player):
        msg = "GAME OVER"
        clock.schedule_unique(gameover,.1)

def gameover():
    global playerDead
    player.image = 'tank_destroyed'
    playerDead = True

pgzrun.go() 