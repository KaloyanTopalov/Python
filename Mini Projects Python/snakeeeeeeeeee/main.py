import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import  Scoreboard

screen = Screen()
screen.setup(width=620, height=600)
screen.bgcolor("black")
screen.title("Python is chasing you!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right,"d")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() >300 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()


    for segment in snake.segment:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()