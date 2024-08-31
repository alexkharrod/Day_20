# snake game Part un
import turtle
from turtle import Screen, Turtle
import time
from snake import Snake





screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

game_is_on = True

snake = Snake()
screen.update()





while game_is_on:
    screen.update()
    time.sleep(.1)



    snake.snake_move()












screen.exitonclick()
