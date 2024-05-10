import turtle

sc = turtle.Screen()
sc.tracer(0)
t = turtle.Turtle()

EASY = 1
MEDIUM = 3
HARD = 5



def draw_square():
    t.begin_fill()
    for _ in range(4):
        t.forward(50)
        t.right(90)
    t.end_fill()

def draw_horizontal_lines():
    t.penup()
    start_x = -200  # Starting x-coordinate
    start_y = 200   # Starting y-coordinate
    t.color('black')
    t.pensize(2)
    for i in range(9):
        t.goto(start_x, start_y - i * 50)
        t.pendown()
        t.goto(start_x + 400, start_y - i * 50)
        t.penup()

def draw_vertical_lines():
    t.penup()
    start_x = -200  # Starting x-coordinate
    start_y = 200   # Starting y-coordinate
    t.color('black')
    t.pensize(2)
    for j in range(9):
        t.goto(start_x + j * 50, start_y)
        t.pendown()
        t.goto(start_x + j * 50, start_y - 400)
        t.penup()

def draw_board():
    t.penup()
    start_x = -200  # Starting x-coordinate
    start_y = 200   # Starting y-coordinate
    for i in range(8):
        for j in range(8):
            t.goto(start_x + j * 50, start_y - i * 50)
            t.pendown()
            t.color('green')     # Set border color to black
            draw_square()
            t.penup()

    draw_vertical_lines()  # Draw vertical lines
    draw_horizontal_lines()  # Draw horizontal lines

    turtle.done()  # Move outside of the loop

draw_board()  # Call the draw_board function here