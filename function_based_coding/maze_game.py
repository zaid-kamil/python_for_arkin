import pgzrun

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

def draw():
    screen.clear()
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            x= col * TILE_SIZE
            y = row * TILE_SIZE
            img = tiles[maze[row][col]]
            screen.blit(img, (x,y))
    player.draw()

def on_key_down(key):
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
    tile = tiles[maze[row][col]]
    if tile =='road':
        x = col*TILE_SIZE
        y = row*TILE_SIZE
        animate(player,topleft=(x,y),duration=.3)
    print(row,col)

pgzrun.go()