    # Problem 2 — next_to chain

# Create a scene called NextToChain that builds a row of four squares side by side:

# Create a white square at ORIGIN
# Place a red square to the RIGHT of it with buff=0.2
# Place a blue square to the RIGHT of the red one with buff=0.2
# Place a green square to the RIGHT of the blue one with buff=0.2

# Show them one by one with Create, each with a 0.5 second wait between.

from manim import *
class NextToChain(Scene):
    def construct(self):
        #create circle & squares

        circle = Circle(color=WHITE).scale(0.7)
        square1 = Square(color=RED).scale(0.7)
        square2 = Square(color=BLUE).scale(0.7)
        square3 = Square(color=GREY_BROWN).scale(0.7)

        #Next to them
        circle.move_to(ORIGIN)
        square1.next_to(circle, RIGHT, buff=0.2)
        square2.next_to(square1, RIGHT, buff=0.2)
        square3.next_to(square2, RIGHT, buff=0.2)

        #show them on screen 1by1
        self.play(Create(circle))
        self.wait(0.5)

        self.play(Create(square1))
        self.wait(0.5)

        self.play(Create(square2))
        self.wait(0.5)

        self.play(Create(square3))
        self.wait(0.5)
        self.interactive_embed()

        # manim Pr6_next_to_chain.py Manim6 --renderer=opengl -p
        # manim -pqk Pr6_next_to_chain.py Manim6
                  