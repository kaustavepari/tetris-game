from turtle import *
import random as r

class block(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.c = (r.randint(1, 255), r.randint(1, 255), r.randint(1, 255))
        self.positions = [[0, 20], [0, -20], [-20, 0], [20, 0]]
        self.possible = {(xcor + pos[0], ycor + pos[1]) for pos in self.positions}
        visited = set()
        self.shape("square")
        self.color(self.c)
        self.penup()
        self.goto(xcor, ycor)
        self.pivotx=xcor
        self.pivoty=ycor
        self.blocks=[self]
        for _ in range(3):
            bob = Turtle()
            bob.penup()
            bob.shape("square")
            bob.color(self.c)
            self.blocks.append(bob)
            random_ind = r.choice(list(self.possible - visited))
            visited.add(random_ind)
            
            x, y = random_ind
            bob.goto(x, y)
            self.pivotx+=bob.xcor()
            self.pivoty+=bob.ycor()
            
            for pos in self.positions:
                new_pos = (pos[0] + x, pos[1] + y)
                if new_pos != (xcor, ycor):
                    self.possible.add(new_pos)
        self.pivotx=self.pivotx//4
        self.pivoty=self.pivoty//4
        

    def rotate(self):
        
        for i in self.blocks:
            i.goto(((self.pivotx + self.pivoty-i.ycor())//20)*20,((i.xcor()+self.pivoty-self.pivotx)//20)*20)
    def move_right(self):
        for i in self.blocks:
            i.goto(i.xcor()+20,i.ycor())
            
        self.pivotx+=20
    def move_left(self):
        for i in self.blocks:
            i.goto(i.xcor()-20,i.ycor())
        self.pivotx-=20                
    def move_down(self):
        for i in self.blocks:
            if 200-abs(i.ycor())<=20:
               return 0
            else:
                i.goto(i.xcor(),i.ycor()-20)
                print(i.xcor(),i.ycor())
        self.pivoty-=20
        

