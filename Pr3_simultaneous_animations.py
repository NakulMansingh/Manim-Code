    # Problem 3 — simultaneous animations

# Create a scene called SimultaneousDemo that:

# Creates a yellow triangle and writes the text "Litte Triangle" at the same time
# Waits 1 second
# Then fades both out at the same time

# Hint: put two animations inside one self.play() to run them simultaneously.

from manim import *
class Sim(Scene):
    def construct(self):
        triangle = Triangle(color = YELLOW)
        text = Text("Little Triangle")

        self.play(Create(triangle), Write(text), run_time = 2)
        self.wait(1)

        self.play(FadeOut(triangle), FadeOut(text), run_time = 1)
        self.wait(1)

        # manim Pr3_simultaneous_animations.py Sim --renderer=opengl -p
        # manim -pqk Pr3_simultaneous_animations.py Sim