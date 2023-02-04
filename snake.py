import turtle
import time
from random import randint

wn = turtle.Screen()
wn.title("Kosuke")
wn.bgcolor("black")
wn.setup(width=600, height=600)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

bouffe = turtle.Turtle()
bouffe.speed(0)
bouffe.shape("circle")
bouffe.color("red")
bouffe.penup()
bouffe.goto(0,100)

segments = []

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.shape("square")
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)

score = 0
meilleur = 0


def enlevergameover():
    perdu_pen.clear()

def perdu():
    global perdu_pen
    perdu_pen = turtle.Turtle()
    perdu_pen.color("red")
    perdu_pen.hideturtle()
    perdu_pen.penup()
    perdu_pen.goto(0, -200)
    perdu_pen.pendown()
    perdu_pen.write("Game Over !", align="center", font=("Courier", 20, "bold"))
    time.sleep(1)
    perdu_pen.clear()


def update_score():
    global score, meilleur
    score += 10
    if score > meilleur:
        meilleur = score
    score_pen.clear()
    score_pen.write("Score : {}  Meilleur : {}".format(score, meilleur), align="center", font=("Courier", 20, "bold"))

def enhaut():
    if head.direction != "down":
        head.direction = "up"

def enbas():
    if head.direction != "up":
        head.direction = "down"

def gauche():
    if head.direction != "right":
        head.direction = "left"

def droite():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

wn.listen()
wn.onkeypress(enhaut, "Up")
wn.onkeypress(enbas, "Down")
wn.onkeypress(gauche, "Left")
wn.onkeypress(droite, "Right")

delay = 0.1
while True:
    wn.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        
        segments.clear()
        
        score = 0
        update_score()
        
        delay = 0.1
        perdu()
        
        head.goto(0,0)
        head.direction = "stop"


       

        
    
    if head.distance(bouffe) < 20:
        x = randint(-290, 290)
        y = randint(-290, 290)
        bouffe.goto(x, y)
        
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)
        
        delay -= 0.001
        
        update_score()
    
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    
    move()    
    
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            for segment in segments:
                segment.goto(1000, 1000)
        
            segments.clear()
            
            score = 0
            update_score()
            
            delay = 0.1
    
    time.sleep(delay)

wn.mainloop()

     