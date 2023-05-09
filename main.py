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


def random_pos(a, b):
    turtle.goto(randint(-150, 0), randint(0, 150))


score = 0
scoreString = f"Score: {score}"

def turtle_score(a, b):
    global score
    score += 1
    turtle_instance.clear()
    turtle_instance.write(score, align="left", font=("Arial", 14, "normal"))

turtle.penup()
drawing_board.listen()
drawing_board.onscreenclick(random_pos, 1)
turtle.onclick(turtle_score, 1)

drawing_board.mainloop()
