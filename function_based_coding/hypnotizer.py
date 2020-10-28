import pgzrun

WIDTH = 500
HEIGHT = 500
colors = ['red','white']
def draw():
    radius = WIDTH//2
    for i in range(13):
        screen.draw.filled_circle((WIDTH//2,HEIGHT//2),radius,colors[i%2])
        radius -= 20

pgzrun.go()