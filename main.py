import turtle
from random import randint


drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Drawing Board with Turtle")

turtle_instance = turtle.Turtle()
turtle_instance.hideturtle()
turtle.shape("turtle")
turtle_instance.shapesize(2, 3, 1)
turtle_instance.penup()


score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()


def random_pos(a, b):
    turtle.goto(randint(-150, 0), randint(0, 150))


score = 0

def turtle_score(a, b):
    global score
    score_turtle.setpos(0, 250)
    score += 1
    score_turtle.clear()
    score_turtle.write(score, align="left", font=("Arial", 14, "normal"))

turtle.penup()
drawing_board.listen()
drawing_board.onscreenclick(random_pos, 1)
turtle.onclick(turtle_score, 1)

drawing_board.mainloop()
