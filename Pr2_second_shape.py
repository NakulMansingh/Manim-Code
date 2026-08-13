    #Problem 2

from manim import *

class SecondShape(Scene):
    def construct(self):

        #create Mobjects
        circle = Circle(radius= 3, color= BLUE)
        text = Text("circle", color = LIGHT_BROWN)

        #animate them one by one
        self.play(Create(circle), run_time= 2)
        self.wait(0.5)
        self.play(Write(text), run_time = 1.5)
        self.wait(0.5)