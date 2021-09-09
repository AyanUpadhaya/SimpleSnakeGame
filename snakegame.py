#snake game in turtle module

import turtle
import random
import time

DELAY=0.1
  
class Snake:
    def __init__(self,master,color,shape,speed,width,length,position):
        self.master = master
        self.color = color
        self.shape = shape
        self.speed = speed
        self.width = width
        self.length = length
        self.position =  position
        self.segments = []

    #snake movements    

    def move_down(self):
        y = self.master.ycor()
        self.master.sety(y-20)

    def move_up(self):
        y = self.master.ycor()
        self.master.sety(y+20)

    def move_left(self):
        x = self.master.xcor()
        self.master.setx(x-20)

    def move_right(self):
        x = self.master.xcor()
        self.master.setx(x+20)

    #draw snake
    def draw(self):
        
        self.master.color(self.color)
        self.master.shape(self.shape)
        self.master.shapesize(stretch_wid=self.width,stretch_len = self.length)
        self.master.speed(self.speed)
        self.master.dx = 1
        self.master.dy = 1
        self.master.penup()
        self.master.goto(self.position[0],self.position[1])
        return self.master
        




class Food(Snake):
    def move_at_random_place(self):
        x = random.randint(-290,290)
        y = random.randint(-290,290)

        self.master.goto(x,y)


class Pen:
    def __init__(self):
        self.pen = turtle.Turtle()
        self.color = 'white'
        self.pen.hideturtle()
        self.pen.color(self.color)

    def WriteText(self,text,x,y):
        self.pen.clear()
        self.pen.speed(0)#speed of animation
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(x,y)
        self.pen.write('{}'.format(text),align='center',font=('Courier',18,'bold'))
        

class Game:
    def __init__(self,title,bg,width,height):
        self.window = turtle.Screen()
        self.title = title
        self.bg = bg
        self.width = width
        self.height = height
        self.snake = Snake(turtle.Turtle(),'yellow','square',0,1,1,[-250,100])
        self.food = Food(turtle.Turtle(),'red','circle',0,.7,.7,[0,0])
        self.snake.draw()
        self.food.draw()
        self.direction = 'stop'
        self.score = 0
        self.life = 4
        self.scoreWriter = Pen()
        self.lifeWriter = Pen()
        self.gameOver = Pen()
        self.running =True

    #change direction

    def to_down(self):
        self.direction = 'down'
        return self.direction

    def to_up(self):
        self.direction = 'up'
        return self.direction

    def to_left(self):
        self.direction = 'left'
        return self.direction

    def to_right(self):
        self.direction = 'right'
        return self.direction

    #class walk method to move the snake
    def walk(self):
        if self.direction == 'down':
            self.snake.move_down()
        if self.direction == 'up':
            self.snake.move_up()
        if self.direction == 'left':
            self.snake.move_left()
        if self.direction == 'right':
            self.snake.move_right()
        

    #play 
    def play(self):
        self.scoreWriter.WriteText(f'Score:{self.score}',-190,260)
        self.lifeWriter.WriteText(f'Life:{self.life}',190,260)

        #check collision with border

        if self.snake.master.xcor()>290 or self.snake.master.xcor()<-290 or self.snake.master.ycor()>290 or self.snake.master.ycor()<-290:
            time.sleep(1)
            self.snake.master.goto(0,0)
            self.life-=1
            self.lifeWriter.WriteText(f'Life:{self.life}',190,260)
            self.direction = 'stop'

            for segment in self.snake.segments:
                segment.goto(1000,1000)
            self.snake.segments.clear()

        #check collision with food
        if self.snake.master.distance(self.food.master)<20:
            self.food.move_at_random_place()
            self.score+=1
            self.scoreWriter.WriteText(f'Score:{self.score}',-180,260)
            new_segment = Snake(turtle.Turtle(),'white','square',0,1,1,[0,0])
            self.snake.segments.append(new_segment.draw()) #add new segment to snake body
            # ~ playsound('sounds/ding.wav')

        #move last segment first in reverse order
        for index in range(len(self.snake.segments)-1,0,-1):
            x = self.snake.segments[index-1].xcor()
            y = self.snake.segments[index-1].ycor()
            self.snake.segments[index].goto(x,y)

        #Move 0 segment where the head is
        if len(self.snake.segments)>0:
            x = self.snake.master.xcor()
            y = self.snake.master.ycor()
            self.snake.segments[0].goto(x,y)
        #if game over
        if self.life==0:
            self.running =False
            self.window.clear()
            self.window.bgcolor('black')
            self.gameOver.WriteText(f'Game Over, score: {self.score}',0,260)
            # ~ playsound('sounds/crash.wav')

                

        self.walk()
        

    def run(self):
        #configure window
        self.window.title(self.title)
        self.window.bgcolor(self.bg)
        self.window.setup(self.width,self.height)
        self.window.tracer(0)

        #lets create event listener
        self.window.listen()
        self.window.onkeypress(self.to_down,'Down')
        self.window.onkeypress(self.to_up,'Up')
        self.window.onkeypress(self.to_right,'Right')
        self.window.onkeypress(self.to_left,'Left')



        #gameloop
        while self.running:
            self.window.update()
            self.play()

            #coliding with body itself
            for segment in self.snake.segments:
                if segment.distance(self.snake.master)<20:
                    time.sleep(1)
                    self.snake.master.goto(0,0)
                    self.life-=1
                    self.lifeWriter.WriteText(f'Life:{self.life}',190,260)
                    self.direction = 'stop'
                    for segment in self.snake.segments:
                        segment.goto(1000,1000)
                    self.snake.segments.clear()
            time.sleep(DELAY)
            
        self.window.mainloop()


if __name__=='__main__':
    app =Game('Snake Game','black',600,600)
    app.run()
    
