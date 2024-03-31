from turtle import *
from walls import Wall
from blocks import block
import time

screen=Screen()
screen.setup(600,800)
screen.bgcolor("black")
screen.tracer(0)
screen.colormode(255)
b=block(0,100)
w1=Wall(0,-200,90)
w2=Wall(140,-80,0)
w3=Wall(-140,-80,0)

blocked=[]

    
screen.listen()
screen.onkey(b.move_down,"Down")
screen.onkey(b.move_right,"Right")
screen.onkey(b.move_left,"Left")
screen.onkey(b.rotate,"r")

game_is_on = True

def row_fill_check():
    temp=[]
    d={}
    col=-1
    for i in blocked:
        for j in i:
            d[j.ycor()]=d.get(j.ycor(),0)+1
            if d[j.ycor()]==13:
                col=j.ycor()
                            
    if col!=-1:
        for i in blocked:
            for j in i:
                if j.ycor()==col:
                    del j
                    break
                if j.xcor()>col:
                    j.goto(j.xcor(),j.ycor()-20)
        col=-1
        d={}                



while game_is_on:
    collision = False
    
    
    for j in blocked:
        for k in j:
            for i in b.blocks:           
                if abs(i.xcor() - k.xcor()) == 0 and abs(i.ycor() - k.ycor()) <= 20:
                    collision = True
                    break
           
            if collision:
                break  
        
        if collision:
            break

    
    if collision:
        blocked.append(list(b.blocks))
        b = block(0, 100)
        screen.onkey(b.move_down, "Down")
        screen.onkey(b.rotate, "r")
        screen.onkey(b.move_left, "Left")
        screen.onkey(b.move_right, "Right")

    for i in b.blocks:
        if abs(w1.ycor() - i.ycor()) <= 20:

            blocked.append(list(b.blocks))
            b = block(0, 100)
            screen.onkey(b.move_down, "Down")
            screen.onkey(b.rotate, "r")
            screen.onkey(b.move_left, "Left")
            screen.onkey(b.move_right, "Right")
            break
    row_fill_check()


                    


    screen.update()
    time.sleep(0.1)
print("Game Over")
screen.exitonclick()



