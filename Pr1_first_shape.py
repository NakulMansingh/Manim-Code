    # Problem 1 — your first shape

# Create a scene called FirstShape that:

# Creates a green circle with radius 1.5
# Waits 1 second
# Fades it out

# Run with:
    # manim -pql lesson1.py FirstShape

from manim import *

class FirstShape(Scene):
    def construct(self):
        circle = Circle(radius = 1.5, color = GREEN)
        self.play(Create(circle), run_time = 0.5)
        self.wait(2)
        self.play(FadeOut(circle), run_time = 1)
        self.wait(2)