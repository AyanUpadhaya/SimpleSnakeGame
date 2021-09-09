# Simple snake game in python
import turtle
import random
import time

run = True
segments = []
score = 0
#screen

wn = turtle.Screen()
wn.title('Snake Game')
wn.bgcolor('black')
wn.setup(600,600)
wn.tracer(0)

#head

head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('yellow')
head.shapesize(stretch_wid=1,stretch_len=1)
head.penup()
head.goto(-250,250)
head.direction = 'down'
#food

food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.shapesize(stretch_wid=.9,stretch_len=.9)
food.penup()
food.goto(0,0)

def to_up():
    if head.direction!='down':
        head.direction='up'

def to_down():
    if head.direction!='up':
        head.direction='down'

def to_left():
    if head.direction!='right':
        head.direction='left'

def to_right():
    if head.direction!='left':
        head.direction='right'



def play():
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'

        for segment in segments:
            segment.goto(1000,1000)

        segments.clear()
        
    if head.distance(food)<20:
        food.goto(random.randint(-290,290),random.randint(-290,290))
        global score
        score+=1
        pen.clear()
        pen.goto(-250,250)
        pen.write(f"Score:{score}",align="left",font=('Courier',16,'normal'))

        new_segment = turtle.Turtle()
        new_segment.color('white')
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.shapesize(stretch_wid=1,stretch_len=1)
        new_segment.penup()
        segments.append(new_segment)

    for i in range(len(segments)-1,0,-1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)

    if len(segments)>0:
        x= head.xcor()
        y= head.ycor()
        segments[0].goto(x,y)


#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(-250,250)
pen.write(f"Score:{score}",align="left",font=('Courier',16,'normal'))

#event listener

wn.listen()
wn.onkeypress(to_up,'Up')
wn.onkeypress(to_down,'Down')
wn.onkeypress(to_left,'Left')
wn.onkeypress(to_right,'Right')

def move():
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20)
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+20)
#game loop

while run:
    play()
    move()
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'

            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
    time.sleep(0.1)
    wn.update()



wn.mainloop()
