import turtle
import time
import random


screen = turtle.Screen()
screen.title("Snake Game")


screen.bgcolor("white")
screen.setup(width=600,height=600)
screen.tracer(0)


class Sprite():
    def __init__(self, shape='square', color='black'):
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape(shape)
        self.pen.color(color)
        self.pen.penup()
        self.pen.hideturtle()
        self.x = 0
        self.y = 0


    def goto(self, x, y):
        self.x = x
        self.y = y
        self.pen.goto(x, y)


    def sety(self, y):
        self.pen.sety(y)


    def setx(self, x):
        self.pen.setx(x)


    def ycor(self):
        return self.pen.ycor()


    def xcor(self):
        return self.pen.xcor()


    def clear(self):
        self.pen.clear()


    def distance(self, other):
        return self.pen.distance(other.pen)




    def draw(self):
        self.pen.clear()
        self.pen.stamp()
        


class Food(Sprite):
    def __init__(self):
        super().__init__('circle', 'red')


    def draw(self):
        self.clear()
        x = self.xcor()
        y = self.ycor()
        self.pen.setheading(0)


        self.pen.fillcolor('red')
        self.pen.begin_fill()


        self.pen.circle(10)
        self.pen.end_fill()


        self.goto(x, y+20)


        self.pen.fillcolor('green')
        self.pen.begin_fill()
        self.pen.left(-20)
        self.pen.forward(10)
        self.pen.left(50)
        self.pen.forward(10)
        self.pen.left(130)
        self.pen.forward(10)
        self.pen.left(50)
        self.pen.forward(10)


        self.pen.end_fill()
        self.goto(x, y)






head = Sprite(color = 'green')
head.goto(0,0)
head.direction = "stop"


food = Food()
food.goto(0,100)


score = 0
high_score = 0


pen = turtle.Turtle()
pen.speed(0)
pen.shape('circle')
pen.color('black')
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
pen.write(f'Score: {score} High Score: {high_score}', align = 'center', font = ('Courlier', 24, 'normal'))


# Make four functions go_left, go_right, go_up and go_down, which change the direction the head is facing. 
# Don't forget: the snake cannot turn 180 degrees, i.e. if the snake is going up we cannot suddenly 
# change the direction to down. Add this constraint to your functions.


def go_up():
    if head.direction != 'down':
        head.direction = 'up'


def go_down():
    if head.direction != 'up':
        head.direction = 'down'


def go_left():
    if head.direction != 'right':
        head.direction = 'left'


def go_right():
    if head.direction != 'left':
        head.direction = 'right'


#-------------------------------------------------------------------------------------------------------


# Here we tell the program to "listen" for keypresses w,a,s,d. We assign on of the functions you've designed 
# above to be called when the corresponding key is pressed.
screen.listen()
screen.onkeypress(go_up,"w")
screen.onkeypress(go_down,"s")
screen.onkeypress(go_left,"a")
screen.onkeypress(go_right,"d")


#-------------------------------------------------------------------------------------------------------
# Step 2: Move the snake
# We told the snake to face a certain direction when we press a key, but now we need the snake to move in
# that direction. 
# Create a function 'move' which checks the direction the snake is facing, and moves it accordingly. 


def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)


    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)


#-------------------------------------------------------------------------------------------------------


# Game Loop
# It is extremely common for games to have a "while True:" loop which we call the game loop. We use this
# to repeatedly move the snake and check for the game logic i.e. collisions with fruit/walls/snake.
segments = []
while True:
    screen.update()     # This clears and redraws the screen, usually turtle will call this automatically after our
                        # code is run but, since we want things to be drawn while our code is still running, we
                        # need to manually write it.


    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'


        for seg in segments:
            seg.goto(10000, 10000)
            seg.clear()


        segments.clear()
        score = 0
        pen.clear()
        pen.write(f'Score: {score} High Score: {high_score}', align = 'center', font = ('Courlier', 24, 'normal'))


    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)




        seg = Sprite(color = 'light green', shape = 'square')
        
        segments.append(seg)


        score += 10
        pen.clear()
        pen.write(f'Score: {score} High Score: {high_score}', align = 'center', font = ('Courlier', 24, 'normal'))


    for i in range (len(segments) - 1, 0 , -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)


    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)        


    move()              # Move the snake.


    for seg in segments:
        if head.distance(seg) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'


            for seg in segments:
                seg.goto(10000, 10000)
                seg.clear()
            segments.clear()
        
        
    food.draw()
    head.draw()
    for seg in segments:
        seg.draw()




    time.sleep(0.1)
