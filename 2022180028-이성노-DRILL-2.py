from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 402
y = 90
angle = 272
mode = 0
direction = 0
while(1):
    clear_canvas_now()
    grass.draw_now(400, 30)
    if(mode == 0 and direction == 0):
        character.draw_now(x, 90)
        update_canvas()
        x = x+2
        if(x == 780):
            direction = 1
        elif(x == 400):
            mode = 1
    elif(mode == 0 and direction == 1):
        character.draw_now(780, y)
        update_canvas()
        y = y+2
        if(y == 550):
            direction = 2
    elif(mode == 0 and direction == 2):
        character.draw_now(x, 550)
        update_canvas()
        x = x-2
        if(x == 20):
            direction = 3
    elif(mode == 0 and direction == 3):
        character.draw_now(20, y)
        update_canvas()
        y = y-2
        if(y == 90):
            direction = 0
    elif(mode == 1):#원점 = 400,345
        character.draw_now(400+225*math.cos(math.radians(angle)), 325+225*math.sin(math.radians(angle)))
        angle = angle-2
        if(angle == -90):
            x = 402
            angle = 272
            mode = 0
            direction = 0

    delay(0.01)


close_canvas()
