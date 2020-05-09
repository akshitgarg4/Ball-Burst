import turtle
import random
import winsound
import time
delay=0.1


wn=turtle.Screen()
wn.bgcolor("light green")
wn.title("BALL BURST")
wn.tracer(0)
#wn.bgpic("abc.gif")


#draw border
border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range (4):
    border_pen.forward(600)
    border_pen.left(90)
border_pen.hideturtle()


score=0
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score : 0 " ,align="center",font=("Courier",24,"normal"))



#create player
player=turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
player.direction="stop"

#create players bullet
bullet=turtle.Turtle()
bullet.color("black")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
#bullet faces upward
bullet.shapesize(0.5,0.5)
#bullet is not of same size as that of player
bullet.hideturtle()
#so that bullet is hidden when game starts
bulletspeed=30



#define bullet state
#ready-ready to fire
#fire bullet is firing
bulletstate="ready"



#more enemies using lisst

enemies=[]
#add enemies to []
for i in range(5):
    #create the enemy
    enemy=turtle.Turtle()
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x=random.randint(-200,200)
    y=random.randint(100,250)
    enemy.setposition(x,y)
    enemies.append(enemy)
enemyspeed=5


#to make the player move only when we press left or right
playerspeed=15
def move_left():
    x=player.xcor()
    x-=playerspeed
    if x< -280:
        x=-280
    player.setx(x)
    
    
def move_right():
    x=player.xcor()
    x+=playerspeed
    if x > 280:
        x=280
    player.setx(x)
def fire_bullet():
    #declare bulletstate global if it needs changed
    global bulletstate


    #move the bullet to the just above the player
    if bulletstate=="ready":
        bulletstate="fire"
        x=player.xcor()
        y=player.ycor()
        bullet.setposition(x,y)
        bullet.showturtle()
        winsound.PlaySound("fire.wav", winsound.SND_ASYNC)


def iscollision(t1,t2):
    ditance=t1.distance(t2)
    if ditance < 20:
        return True
    else:
        return False
    


    
wn.listen()
wn.onkeypress(move_left,"Left")
wn.onkeypress(move_right,"Right")
wn.onkeypress(fire_bullet,"space")










while True:
    wn.update()

    for enemy in enemies: 
        x=enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)

    #boundary checking for the enemy
        if enemy.xcor() >280:
            #move all enemies down as soon as one touches the border
            for e in enemies:
                y=e.ycor()
                #enemy drops down by 20 pixels
                y-=20
                e.sety(y)
            #change direction of all enemies
            #so that it reverts its direction on touching its direction
            enemyspeed*=-1
        
        
        if enemy.xcor() <-280:
            for e in enemies:
                y=enemy.ycor()
                y-=20
                enemy.sety(y)
            enemyspeed*=-1
        #check for collision between bullet and enemy
        if (iscollision(bullet,enemy)):
            #sound
            winsound.PlaySound("burst.wav", winsound.SND_ASYNC)
            #upgrade the score
            score += 10
            pen.clear()
            pen.write("Score : {}".format(score) ,align="center",font=("Courier",24,"normal"))
            
            
            #reset the bullet
            bullet.hideturtle()
            bulletstate="ready"
            bullet.setposition(0,-400)
            #reset the enemy
            x=random.randint(-200,200)
            y=random.randint(100,250)
            enemy.setposition(x,y)
        if iscollision(player,enemy):
            player.hideturtle()
            enemy.hideturtle()
            score =0
            pen.clear()
            pen.write("Score : {}".format(score) ,align="center",font=("Courier",24,"normal"))
            print("GAMEOVER")
            break



    #move the bullet
    if bulletstate=="fire":
        y=bullet.ycor()
        y+=bulletspeed
        bullet.sety(y)


    #check to see if bullet has gone to the top
    if bullet.ycor()>275:
        bullet.hideturtle()
        bulletstate="ready"


    time.sleep(delay)

wn.mainloop()
    
