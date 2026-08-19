    # Problem 1 — basic positioning

# Create a scene called BasicPositioning with three circles:

# A red circle at LEFT * 3
# A green circle at ORIGIN
# A blue circle at RIGHT * 3

# Show all three at the same time with Create.
# Wait 1 second, then move all three up by 2 units simultaneously using .animate.shift().

from manim import *
class BasicPositioning(Scene):
    def construct(self):

        # create circles
        c1 = Circle(color=BLUE)
        c2 = Circle(color=WHITE, )
        c3 = Circle(color=LIGHT_BROWN,)

        # shift them before moving
        c1.move_to(LEFT*3)
        c2.move_to(ORIGIN)
        c3.move_to(RIGHT*3)

        # show them all at screen % wait for 1 sec
        self.play(
            Create(c1),
            Create(c2),
            Create(c3)
        )

        self.wait(1)

        # animate them moving
        self.play(
            c1.animate.shift(UP*2),
            c2.animate.shift(UP*2),
            c3.animate.shift(UP*2)
        )
        
        self.wait(1)
        

        # manim Pr5_basic_positioning.py Manim5 --renderer=opengl -p
        # manim -pqk Pr5_basic_positioning.py Manim5
        