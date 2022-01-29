
import datetime
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import turtle
s = turtle.Screen()
s.setup(width=500, height=500)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 250 or snake.head.xcor() < -250 or snake.head.ycor() > 250 or snake.head.ycor() < -250:
        food.refresh()
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            food.refresh()
            scoreboard.reset()
            snake.reset()
s.exitonclick()
