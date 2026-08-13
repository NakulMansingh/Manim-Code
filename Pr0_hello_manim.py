    #Problem 0

from manim import *

class HelloManim(Scene):
    def construct(self):
        text = Text("Hello, Manim!")
        self.play(Write(text))
        self.wait(2)

# run:
    # write in terminal: manim -pql Pr0_hello_manim HelloManim