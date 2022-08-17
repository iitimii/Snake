import random
import turtle
import time

delay = 0.15

score = 0
high_score =0

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f'Score: {score}  High Score: {high_score}', align='center', font=('Courier', 24, 'bold'))

win = turtle.Screen()
win.title('Snake')
win.bgcolor('black')
win.setup(600,600)
win.tracer(0)


head = turtle.Turtle()
head.shape('square')
head.color('green')
head.goto(0,0)
head.penup()
head.speed(0)
head.direction = 'stop'

food = turtle.Turtle()
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)
food.speed(0)

segment = []


def go_up():
    head.direction = 'up'
def go_down():
    head.direction = 'down'
def go_left():
    head.direction = 'left'
def go_right():
    head.direction = 'right'
def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+20)

win.listen()
win.onkeypress(go_up,'Up')
win.onkeypress(go_down,'Down')
win.onkeypress(go_left,'Left')
win.onkeypress(go_right,'Right')


while True:
    win.update()

    
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'
        
        for segments in segment:
            segments.goto(1000,1000)
        segment.clear()
        score=0
        delay = 0.15
        pen.clear()
        pen.write(f'Score: {score}  High Score: {high_score}', align='center', font=('Courier', 24, 'bold'))


    if head.distance(food)<20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        score+=10
        if score>high_score:
            high_score = score
        pen.clear()
        pen.write(f'Score: {score}  High Score: {high_score}', align='center', font=('Courier', 24, 'bold'))


        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('green')
        new_segment.penup()
        segment.append(new_segment)

        delay-=0.001
    
    for index in range(len(segment)-1,0,-1):
        x = segment[index-1].xcor()
        y = segment[index-1].ycor()
        segment[index].goto(x,y)
    if len(segment)>0:
        x = head.xcor()
        y= head.ycor()
        segment[0].goto(x,y)
    
        
        


    move()

    for segments in segment:
        ''' if head.xcor() == segments.xcor() and  head.ycor() == segments.ycor(): ''' 
        if segments.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'
            for segments in segment:
                segments.goto(1000,1000)
            segment.clear()
            score=0
            delay = 0.15
            pen.clear()
            pen.write(f'Score: {score}  High Score: {high_score}', align='center', font=('Courier', 24, 'bold'))


    time.sleep(delay)


