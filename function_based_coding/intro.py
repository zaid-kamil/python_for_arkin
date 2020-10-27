import pgzrun

WIDTH = 500
HEIGHT = 500

def draw():
    screen.clear()
    screen.draw.text("welcome to functions",(10,10),color='red')
    screen.draw.text("this is pygamezero ",(10,30),color='green')
    screen.draw.circle((250,250),50,'white')
    screen.draw.filled_circle((250,250),30,'red')
    screen.draw.filled_circle((250,250),10,'white')
pgzrun.go()