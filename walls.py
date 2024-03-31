from turtle import *

class Wall(Turtle):
    def __init__(self,x,y,ang):
        super().__init__()
        self.x=x
        self.y=y
        self.ang=ang
        self.up()
        self.shape("square")
        self.color("white")
        self.shapesize(13,1)
        self.right(ang)
        self.goto(x,y)
