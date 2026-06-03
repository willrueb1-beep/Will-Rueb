'''
Name: Will Rueb
Project 3: Python Turtle Graphics Scene Refactoring

I refactored my Project 2 hockey rink by breaking the large draw_scene function into
smaller helper functions with clearer lines, squares, circles and colors 

After refactoring,i added stands, a scoreboard, and mini players on the ice
'''

import turtle
import math


def setup_turtle():
    """Initialize turtle with standard settings"""
    t = turtle.Turtle()
    t.speed(0)
    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment")
    return t, screen


def draw_rectangle(t, width, height, fill_color=None):
    """Draw a rectangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_square(t, size, fill_color=None):
    """Draw a square with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_triangle(t, size, fill_color=None):
    """Draw an equilateral triangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()


def draw_circle(t, radius, fill_color=None):
    """Draw a circle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()


def draw_polygon(t, sides, size, fill_color=None):
    """Draw a regular polygon with given number of sides"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)
    if fill_color:
        t.end_fill()


def draw_curve(t, length, curve_factor, segments=10, fill_color=None):
    """
    Draw a curved line using small line segments
    """
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()

    segment_length = length / segments
    original_heading = t.heading()

    for i in range(segments):
        angle = curve_factor * math.sin(math.pi * i / segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle)

    t.setheading(original_heading)

    if fill_color:
        t.end_fill()


def jump_to(t, x, y):
    """Move turtle without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()


# ----------------------------
# Refactored helper functions
# ----------------------------

def prepare_turtle(t):
    """Common turtle setup for both scenes"""
    t.hideturtle()
    t.pensize(2)
    t.color("black")


def draw_rink_border(t):
    jump_to(t, -220, 120)
    t.setheading(0)
    draw_rectangle(t, 440, 240, "red")


def draw_ice_surface(t):
    jump_to(t, -210, 110)
    t.setheading(0)
    draw_rectangle(t, 420, 220, "white")


def draw_vertical_line(t, x, y, width, height, color_name):
    jump_to(t, x, y)
    t.setheading(0)
    draw_rectangle(t, width, height, color_name)


def draw_faceoff_circle(t, x, y, radius, dot_x, dot_y, dot_radius=4):
    jump_to(t, x, y)
    t.setheading(0)
    draw_circle(t, radius)
    jump_to(t, dot_x, dot_y)
    draw_circle(t, dot_radius, "red")


def draw_goal(t, x, y, width=20, height=50, color_name="firebrick"):
    jump_to(t, x, y)
    t.setheading(0)
    draw_rectangle(t, width, height, color_name)


def draw_rink_lines_and_circles(t):
    # Center red line
    draw_vertical_line(t, -5, 110, 10, 220, "red")

    # Blue lines
    draw_vertical_line(t, -110, 110, 10, 220, "blue")
    draw_vertical_line(t, 100, 110, 10, 220, "blue")

    # Center faceoff circle
    jump_to(t, 0, -40)
    t.setheading(0)
    draw_circle(t, 40)
    jump_to(t, 5, -5)
    draw_circle(t, 5, "red")

    # Corner/zone faceoff circles
    draw_faceoff_circle(t, -140, 55, 25, -135, 80)
    draw_faceoff_circle(t, -140, -105, 25, -135, -80)
    draw_faceoff_circle(t, 90, 55, 25, 95, 80)
    draw_faceoff_circle(t, 90, -105, 25, 95, -80)


def draw_rink_goals(t):
    draw_goal(t, -225, 25)
    draw_goal(t, 205, 25)


def draw_basic_rink(t):
    """This matches the original Project 2 rink scene"""
    draw_rink_border(t)
    draw_ice_surface(t)
    draw_rink_lines_and_circles(t)
    draw_rink_goals(t)


def draw_scoreboard(t):
    jump_to(t, -70, 180)
    t.setheading(0)
    draw_rectangle(t, 140, 50, "black")

    jump_to(t, -55, 145)
    t.color("white")
    t.write("HOME 3   AWAY 2", font=("Arial", 12, "bold"))

    jump_to(t, -18, 128)
    t.write("3RD", font=("Arial", 10, "bold"))
    t.color("black")


def draw_stand_section(t, x, y, rows, cols, seat_size, color_name):
    """Draw a block of crowd seats"""
    for row in range(rows):
        for col in range(cols):
            seat_x = x + col * (seat_size + 2)
            seat_y = y - row * (seat_size + 2)
            jump_to(t, seat_x, seat_y)
            t.setheading(0)
            draw_square(t, seat_size, color_name)


def draw_bench(t, x, y, width, height, color_name):
    jump_to(t, x, y)
    t.setheading(0)
    draw_rectangle(t, width, height, color_name)


def draw_player(t, x, y, jersey_color):
    """Simple composite hockey player"""
    # Head
    jump_to(t, x, y)
    t.setheading(0)
    draw_circle(t, 8, "peachpuff")

    # Body
    jump_to(t, x - 6, y - 12)
    t.setheading(0)
    draw_rectangle(t, 12, 18, jersey_color)

    # Stick
    jump_to(t, x + 8, y - 10)
    t.setheading(-60)
    t.forward(25)
    t.right(90)
    t.forward(8)

    # Skate line
    jump_to(t, x - 8, y - 31)
    t.setheading(0)
    t.forward(18)


def draw_puck(t, x, y):
    jump_to(t, x, y)
    t.setheading(0)
    draw_circle(t, 5, "black")


def draw_enhanced_hockey_scene(t):
    """More populated scene built from refactored helpers"""
    draw_basic_rink(t)

    # Scoreboard
    draw_scoreboard(t)

    # Crowd stands
    draw_stand_section(t, -210, 210, 3, 18, 10, "gray")
    draw_stand_section(t, -210, -145, 3, 18, 10, "darkgray")

    # Benches
    draw_bench(t, -70, 135, 50, 15, "gold")
    draw_bench(t, 20, 135, 50, 15, "gold")

    # Players
    draw_player(t, -60, 20, "blue")
    draw_player(t, -20, -20, "blue")
    draw_player(t, 50, 10, "red")
    draw_player(t, 90, -25, "red")

    # Pucks
    draw_puck(t, 10, 10)
    draw_puck(t, 130, 0)

    # Arena title
    jump_to(t, -80, 250)
    t.color("navy")
    t.write("HOCKEY NIGHT", font=("Arial", 16, "bold"))
    t.color("black")


def show_project2_scene(t):
    """First displayed scene must match Project 2 output"""
    screen = t.getscreen()
    screen.bgcolor("lightblue")
    prepare_turtle(t)
    draw_basic_rink(t)


def show_enhanced_scene(t):
    """Clear screen and show the enhanced version"""
    t.clear()
    screen = t.getscreen()
    screen.bgcolor("lightblue")
    prepare_turtle(t)
    draw_enhanced_hockey_scene(t)

    jump_to(t, -165, -250)
    t.color("black")
    t.write("Enhanced scene shown. Close the window when finished.",
            font=("Arial", 11, "normal"))


# YOU MUST add function calls in this draw_scene function definition
# to create your scene
def draw_scene(t):
    """
    Display the original Project 2 scene first.
    Click anywhere in the window to display the enhanced refactored scene.
    """
    show_project2_scene(t)

    screen = t.getscreen()
    jump_to(t, -180, -250)
    t.color("black")
    t.write("Click anywhere to show the enhanced refactored scene.",
            font=("Arial", 11, "normal"))

    def handle_click(x, y):
        show_enhanced_scene(t)
        screen.onclick(None)

    screen.onclick(handle_click)


def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()


if __name__ == "__main__":
    main()