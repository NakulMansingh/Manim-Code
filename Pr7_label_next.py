    # Problem 3 — label next to shape

# Create a scene called LabelledShapes that shows:

# A yellow circle at LEFT * 2 with the text "Circle" below it
# A blue square at RIGHT * 2 with the text "Square" below it

# Use next_to(shape, DOWN) to place each label.
# Show each shape and its label simultaneously, with a 1 second wait between the two pairs.

from manim import *
class Label(Scene):
    def construct(self):

        # create Mobjects
        circle = Circle(color=LIGHT_BROWN)
        square = Square(color=BLUE)
        ctext = Text("circle")
        stext = Text("square")

        # where the Mobjects are on the screen
        circle.move_to(LEFT*2)
        square.move_to(RIGHT*2)
        ctext.next_to(circle, DOWN)
        stext.next_to(square, DOWN)

        # show them on the screen 1by1
        self.play(
            Create(circle),
            Write(ctext)
        )
        self.wait(1)

        self.play(
            Create(square),
            Write(stext)
        )
        self.wait(1)

        # manim Pr7_label_next.py Manim7 --renderer=opengl -p
                # manim -pqk Pr7_label_next.py Manim7