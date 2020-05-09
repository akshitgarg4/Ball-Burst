import turtle
import time
import random
import winsound
delay=0.1
score = 0

wn=turtle.Screen()
wn.title("SNAKE GAME")
wn.bgcolor("light green")
wn.setup(width=600, height=600)
wn.tracer(0)


head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("blue")
head.penup()
head.goto(0,0)
head.direction="stop"


food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


segments = []



pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score : 0 " ,align="center",font=("Courier",24,"normal"))

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y + 20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y - 20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x - 20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x + 20)


def up():
    if head.direction !="down":
        head.direction="up"
def down():
    if head.direction !="up":
        head.direction="down"
def left():
    if head.direction !="right":
        head.direction="left"
def right():
    if head.direction !="left":
        head.direction="right"

        


wn.listen()
wn.onkeypress(up,"w")
wn.onkeypress(down,"s")
wn.onkeypress(left,"a")
wn.onkeypress(right,"d")

    


while True:
    wn.update()
    
    if head.distance(food) < 20:
        winsound.PlaySound("snakesound.wav", winsound.SND_ASYNC)
        x= random.randint(-290, 290)
        y= random.randint(-290, 290)
        food.goto(x,y)

        
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)
        
        score += 10
        pen.clear()
        pen.write("Score : {}".format(score) ,align="center",font=("Courier",24,"normal"))
        

        
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
        

    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)


    
    if head.xcor()>290 :
        y=head.ycor()
        head.goto(-290,y)
    if head.xcor()<-290 :
        y=head.ycor()
        head.goto(290,y)
    if head.ycor()>290 :
        x=head.xcor()
        head.goto(x,-290)
    if head.ycor()<-290 :
        x=head.xcor()
        head.goto(x,290)
    
    move()   
    
    
        
    for segment in segments:
        if segment.distance(head) < 20 :
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear() 
            score=0
            pen.clear()
            pen.write("Score : {}".format(score) ,align="center",font=("Courier",24,"normal"))
        

        
        
    
    

    
    time.sleep(delay)

wn.mainloop()
