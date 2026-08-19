from manim import *

class Positioning(Scene):
    def construct(self):

        # create three objects
        circle = Circle(color=BLUE)
        square = Square(color=LIGHT_BROWN)
        text = Text("Manim", color=WHITE)

        # position before showing
        circle.move_to(LEFT*3)
        square.move_to(ORIGIN)
        text.move_to(RIGHT*3)

        # show them all at once
        self.play(
            Create(circle),
            Create(square),
            Write(text)
        )

        # animate them moving
        self.play(
            circle.animate.move_to(ORIGIN),
            square.animate.shift(RIGHT*3),
            text.animate.shift(LEFT*6)
        )

        self.wait(1)

        # manim Pr33_positioning.py Manim33 --renderer=opengl -p
        # manim -pqk Pr33_positioning.py Manim33