"""Draws a scene of a tree in front of grass on a starry night with low-lying clouds.

Notes:
line 59: setworldcoordinates - used to help me map out my space with the bottom-left corner being (0,0).
line 213: xcor - used to return the x-coordinate of where the turtle was so that the turtle could 
come back to that location when drawing my tree.
line 214: ycor - used to return the y-coordinate of where the turtle was so that the turtle could 
come back to that location when drawing my tree.
line 60: tracer / line 72: update - used to update my scene at the end so as to speed up rendering.
line 105: heading - used to return the direction (angle) the turtle was pointed at so as to determine 
appropriate directions to place branches.
line 106: setheading - used to set the direction of the turtle to where I wanted it to face.
line 131: circle - used to draw circles.
lines 106, 127, 147, 163, 166, 309, 387: randint - used to put items in random places, generate random
colors, and randomize how many branches grew from each node in the tree and at what angle they grew.
lines 186-236: the wood function iterates over every node created in a tree to grow new branches until the
tree has branched out the number of times specified by the levels variable. It does so by using the string 
made by the nodes function (lines 289-303) to keep track of how many nodes should be on the tree and at what 
level they should be on, the string made by branch_len_list (lines 239-246) to find how long branches should be, 
and using the functions commas (lines 329-342), remove (lines 345-359), and access value (lines 362-382) to 
store and access coordinates the turtle had to return to when making the tree. Lengths of the branches 
(lines 163-164) are based off of the Fibonacci sequence in that the branch lengths are directly proportionate 
to lengths given by the Fibonacci sequence for how much branching occurs; for example, a tree 3 units tall 
that branches out 3 times should have branches of length 2 at the first branching and length 1 at the second 
and third branchings. Similarly, a tree 300 units tall that branches out 3 times should have branches of length 
200 at the first branching and length 100 at the second and third branchings.
"""

from turtle import Turtle, colormode, setworldcoordinates, tracer, heading, update, done
from random import randint
"""
The function randint is used in lines 106, 127, 147, 163, 166, 309, 387 (see documentation above).
"""

__author__: str = "730411523"


MAX_SPEED: int = 0
FIRST_NUMBER_FIB_SEQ: int = 0
SECOND_NUMBER_FIB_SEQ: int = 1
SMALLEST_BRANCH_LENGTH: int = 30
MIN_BRANCHES_PER_NODE: int = 2
MAX_BRANCHES_PER_NODE: int = 3
BRANCH_ANGLE_RANGE: int = 90
RGBRANGE: int = 50  # For most instances where a range of RGB values is needed.
RGBRANGECIR: int = 20
RGBRANGEGRASS: int = 40
BRANCHINGS: int = 3


# Note: BRANCHINGS must be less than or equal to 6 branchings to simplify branch_len_list
# by ensuring that each branch length can be accessed by using one index of a string;
# BRANCHINGS must also be greater than or equal to 3 to load without errors.


def main() -> None:
    """The entrypoint of my scene."""
    colormode(255)
    setworldcoordinates(0, 0, 1000, 1000)
    tracer(0, 0)
    ito: Turtle = Turtle()
    ito.speed(MAX_SPEED)
    major_rectangle(ito, 0, 200, 1000, 800, 65, 107, 165)  # sky
    stars(ito, 100, 10, 40, 0, 200, 1000, 800, 230, 229, 234)  # stars
    cir(ito, 500, 0, 200, 1000, 75, 28, 174, 192, 212)  # darkest clouds
    cir(ito, 500, 0, 275, 1000, 75, 28, 209, 216, 224)  # darker clouds
    cir(ito, 500, 0, 350, 1000, 100, 28, 211, 224, 239)  # light clouds
    major_rectangle(ito, 0, 0, 1000, 200, 91, 102, 42)  # ground
    lines(ito, 4000, 10, 20, 0, 0, 1000, 200, 135, 151, 62)  # grass
    leaves(ito, 800, 500, 800, 100, 325, 40, 94, 109, 75)  # leaves
    wood(ito, 325, 50, 520, 0, 69, 68, 65, 65, 63, 56)  # tree
    update()
    done()


def major_rectangle(ito: Turtle, x: float, y: float, w: int, h: int, r: int, g: int, b: int) -> None:
    """Draws a rectangle with dimensions (w*h) starting from the bottom-left corner (x, y) with a color (r, g, b)."""
    i: int = 0
    ito.color(r, g, b)
    ito.penup()
    ito.goto(x, y)
    ito.pendown()
    ito.begin_fill()
    while i < 2:
        ito.forward(w)
        ito.left(90)
        ito.forward(h)
        ito.left(90)
        i += 1
    ito.end_fill()


def rect(ito: Turtle, x: float, y: float, w: int, h: int, r: int, g: int, b: int, rl: int, gl: int, bl: int) -> None:
    """Draws rectangles as branches.
    
    Does so at tilts of (direction the turtle is heading + / - BRANCH_ANGLE_RANGE with dimensions (w*h) 
    starting from the bottom-left corner (x, y) with fill color (r, g, b) and outline length color (rl, gl, bl).
    """
    i: int = 0
    ito.fillcolor(r, g, b)
    ito.penup()
    ito.goto(x, y)
    ito.pendown()
    ito.begin_fill()
    angle: int = int(heading())
    ito.setheading(float(randint((angle - BRANCH_ANGLE_RANGE), (angle + BRANCH_ANGLE_RANGE))))
    while i < 2:
        ito.pencolor(r, g, b)
        ito.forward(w)
        ito.left(90)
        ito.pencolor(rl, gl, bl)
        ito.forward(h)
        ito.left(90)
        i += 1
    ito.end_fill()


def cir(ito: Turtle, n: int, x: float, y: float, w: int, h: int, s: int, r: int, g: int, b: int) -> None:
    """Draws n circles.
    
    Does so at random points within a specified rectangle of dimensions (w*h) starting at (x, y) 
    in shades varying by a specified + / - range (RGBRANGECIR) from the rgb values of a color (r, g, b).
    """
    i: int = 0
    while i < n:
        ito.penup()
        ito.goto(randint(int(x), int(x + w)), randint(int(y), int(y + h)))
        ito.pendown()
        ito.begin_fill()
        ito.color(actual_rgb(r, RGBRANGECIR), actual_rgb(g, RGBRANGECIR), actual_rgb(b, RGBRANGECIR))
        ito.circle(s)
        ito.end_fill()
        i = i + 1


def lines(ito: Turtle, n: int, l1: int, l2: int, x: float, y: float, w: int, h: int, r: int, g: int, b: int) -> None:
    """Draws n lines.
    
    Does so in a range of lengths [l1,l2] within a specified rectangle of dimensions (w*h) starting at (x, y) 
    in shades varying by a specified + / - color range (RGBRANGEGRASS) from the rgb values of a color (r, g, b).
    """
    i: int = 0
    ito.left(90)
    while i < n:
        ito.color(actual_rgb(r, RGBRANGEGRASS), actual_rgb(g, RGBRANGEGRASS), actual_rgb(b, RGBRANGEGRASS))
        ito.penup()
        ito.goto(randint(int(x), int(x + w)), randint(int(y), int(y + h)))
        ito.pendown()
        ito.forward(randint(l1, l2))
        i += 1


def stars(ito: Turtle, n: int, l1: int, l2: int, x: float, y: float, w: int, h: int, r: int, g: int, b: int) -> None:
    """Draws n stars of color (r, g, b).

    Does so in a range of lengths [l1, l2] within a specified rectangle of dimensions (w*h) 
    starting at (x, y) in shades varying by + / - RGBRANGE (color range) from a specified (r, g, b).
    """
    number_stars: int = 0
    while number_stars < n:
        ito.color(actual_rgb(r, RGBRANGE), actual_rgb(g, RGBRANGE), actual_rgb(b, RGBRANGE))
        ito.penup()
        ito.goto(randint(int(x), int(x + w)), randint(int(y), int(y + h)))
        ito.pendown()
        ito.begin_fill()
        side_length = randint(l1, l2)
        i: int = 0
        while i < 9:
            ito.forward(side_length)
            ito.left(160)
            i += 1
        ito.end_fill()
        number_stars += 1


def leaves(ito: Turtle, n: int, h: int, w: int, x: float, y: float, size: int, r: int, g: int, b: int) -> None:
    """Draws the specified number of leaves for a tree.
    
    Does so given dimensions of the area (h*w), the starting point (x, y), base leaf color (r,g,b), and size.
    """
    cir(ito, int(n / 2), int(x + w / 4), y, int(w / 2), h, size, r, g, b)  # middle
    cir(ito, int(n / 4), int(x), int(y), int(w / 4), int(h / 2), size, r, g, b)  # left
    cir(ito, int(n / 4), int(x + w * 0.75), int(y), int(w / 4), int(h / 2), size, r, g, b)  # right


def wood(ito: Turtle, h: int, w: int, x: float, y: float, r: int, g: int, b: int, rl: int, gl: int, bl: int) -> None:
    """Draws the wood of a tree.
    
    Does so in fill color (r, g, b) and outline length color (rl, gl, bl),
    given the trunk's dimensions (w*h) and the starting point (x,y).
    """
    major_rectangle(ito, x, y, h, w, r, g, b)
    branch_lengths: str = branch_len_list(h)
    node_list: str = nodes(branch_lengths)
    levels: int = int(len(branch_lengths))
    scale_unit: float = h / int(branch_lengths[levels - 1])
    x = int(x - (w / 2))
    y = int(y + (h) - (w / 2))
    height: float = 0
    width: float = 0
    store_x: str = (str(x) + ",")
    store_y: str = (str(y) + ",")
    i: int = 0
    while i < len(node_list): 
        old_x: float = x
        old_y: float = y
        height = scale_unit * int(branch_lengths[levels - int(node_list[i])])
        width = w * (height / h)
        rect(ito, int(x), int(y), int(width), int(height), r, g, b, rl, gl, bl)
        ito.forward(width / 2)
        ito.left(90)
        ito.forward(height - (width / 2))
        new_x: float = ito.xcor()
        new_y: float = ito.ycor()
        if i - 2 > 0:
            level_jump: int = int(node_list[i - 1]) - int(node_list[i])
            if level_jump > 0:
                x = new_x
                y = new_y
                store_x += (str(old_x) + ",")
                store_y += (str(old_y) + ",")
            else:
                if level_jump == 0:
                    x = old_x
                    y = old_y
                else:  # level_jump < 0
                    old_commas: int = commas(store_x)   # = commas(store_y)
                    desired_commas: int = int(old_commas + level_jump + 2)
                    store_x = remove(store_x, desired_commas)
                    store_y = remove(store_y, desired_commas)
                    x = access_value(store_x, commas(store_x) - 1)
                    y = access_value(store_y, commas(store_y) - 1)
        else:
            x = new_x
            y = new_y
        i += 1


def branch_len_list(h: int) -> str:
    """Given the trunk height (h), returns a string of the lengths of the tree's branches."""
    i: int = 0
    branch_lengths: str = ""
    while i < branchings(h, SMALLEST_BRANCH_LENGTH):
        branch_lengths += str(fibonacci(i + 1))
        i += 1
    return branch_lengths


def branchings(h: int, smallest_len: int) -> int:
    """Returns how many branchings the tree can have.

    Does so given the height of the trunk (h) and the smallest length of a branch (smallest_len).
    """
    branchings: int = 1  # have at least one for the trunk
    scale_unit: float = h / fibonacci(branchings)
    while scale_unit > smallest_len:
        branchings += 1
        scale_unit = h / fibonacci(branchings)
    if branchings > BRANCHINGS:
        branchings = BRANCHINGS
    else: 
        branchings = branchings
    return branchings


def fibonacci(position: int) -> int:
    """Returns the number at a desired position (where the first number has position 0) in the Fibonacci sequence.

    In the Fibonacci sequence, the current number and the previous number are added to obtain the next number.
    """
    number1: int = FIRST_NUMBER_FIB_SEQ 
    number2: int = SECOND_NUMBER_FIB_SEQ
    number3: int = 0 
    if position < 1:
        return number1
    else:
        if position < 2:
            return number2
        else:
            i: int = 1
            while i < position:
                number3 = number1 + number2
                number1 = number2
                number2 = number3
                i = i + 1
            return number3


def nodes(branch_lengths: str) -> str:
    """Given a string of branch lengths, creates a string to keep track of randomly generated nodes in a tree."""
    levels: int = int(len(branch_lengths))
    nodes: str = "1"
    current_level: int = 1
    while current_level <= levels:   # repeat until the tree has branched out the specified number of levels
        node_position: int = 0
        length_nodes: int = len(nodes)
        while node_position < length_nodes:   # add a random number of characters of value str(i_1+1) after every i_1
            working_value: int = int(nodes[node_position])
            nodes = insert_values(working_value, current_level, node_position, nodes)
            length_nodes = len(nodes)
            node_position += 1
        current_level += 1
    return nodes


def insert_values(working_value: int, current_level: int, node_position: int, nodes: str) -> str:
    """Helper function to the nodes function that adds nodes in the desired order."""
    if working_value == current_level:
        branches_needed: int = randint(MIN_BRANCHES_PER_NODE, MAX_BRANCHES_PER_NODE)
        branches_added: int = 0
        while branches_added < branches_needed:
            store_nodes: str = ""
            position: int = int(node_position + branches_added)
            i: int = 0
            while i <= position:  # this ensures the values are inserted in the right places
                store_nodes += nodes[i]
                i += 1
            store_nodes += str(current_level + 1)
            while i < len(nodes):
                store_nodes += nodes[i]
                i += 1
            nodes = store_nodes
            branches_added += 1
    else:
        nodes = nodes
    return nodes


def commas(string: str) -> int:
    """Given a comma-separated string of branch lengths, returns the number of commas in the string.
    
    The number of commas equals the number of elements in the string.
    """
    i: int = 0
    count: int = 0
    while i < len(string):
        if string[i] == ",":
            count += 1
        else:
            count = count
        i += 1
    return count


def remove(csv_string: str, trim_to: int) -> str:
    """Trims the string.
    
    Does so given a string of comma-separated values (csv_string) and the number of elements to trim_to.
    """
    i: int = 0
    re_store_string: str = ""
    while i < len(csv_string):
        if commas(csv_string) <= trim_to:
            re_store_string += csv_string[i]
        else:
            re_store_string = re_store_string
        i += 1
    csv_string = re_store_string
    return csv_string


def access_value(numbers: str, position: int) -> int:
    """This returns the value at the specified position in a comma-separated string of numbers.
    
    Note that there is a comma at the end, and the starting position is 1.
    """
    i: int = 0
    working_value: str = ""
    working_lengths: str = ""
    while i < len(numbers):
        working_lengths += numbers[i]
        number_commas: int = commas(working_lengths)
        if number_commas == int(position): 
            if working_lengths[i] == ",":
                working_value = working_value
            else:
                working_value += working_lengths[i]
        else:
            working_value = working_value
        i += 1
    value: int = int(working_value)
    return value


def actual_rgb(base_color: int, RGBRANGE: int) -> float:
    """Checks that RGB values generated randomly do not exceed 255 and adjusts values as necessary."""
    actual_color: int = base_color + randint(-RGBRANGE, RGBRANGE)
    if actual_color > 255:
        return 255 - (actual_color % 255)
    else:
        return actual_color


if __name__ == "__main__":
    main()
else: 
    print(__name__)