    # Problem 1 — write and colour

# Create a scene called ColouredEquation that:

# Writes Einstein's equation split into parts: r"E", r"=", r"m", r"c^2"
# After writing, colours each part:
# E → YELLOW
# m → BLUE
# c² → RED
# Animates each colour change one by one with 0.5s wait between each

from manim import *
class ColouredEquation(Scene):
    def construct(self):

        eq = MathTex(r"E",r"=",r"m",r"c^2", font_size=72)
        self.play(Write(eq))

        self.play(eq[0].animate.set_color(TEAL))
        self.wait(0.5)
        self.play(eq[2].animate.set_color(BLUE))
        self.wait(0.5)
        self.play(eq[3].animate.set_color(GREY_BROWN))
        self.wait(0.5)

        # manim Pr15_write_and_colour.py Manim15 --renderer=opengl -p
        # manim -pqk Pr15_write_and_colour.py Manim15