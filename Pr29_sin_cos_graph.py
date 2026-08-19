    # Problem 30 — two curves

# Create a scene called SinCosGraph that:

# Creates axes with x_range=[0, 2π] and y_range=[−1.5, 1.5]
# Plots sin(x) in BLUE and cos(x) in RED
# Adds curve labels for both
# Adds a dot on the sin curve starting at x=0
# Moves the dot along the sin curve using MoveAlongPath

import numpy as np
from manim import *

class SinCos(Scene):
    def construct(self):

            # axes
        axes=Axes(x_range=[0, 2.2*PI], y_range=[-1.5,1.5])
        labels=axes.get_axis_labels("x","")

            # SineCosine
        sin = axes.plot(
            lambda x: np.sin(x),
            color=RED,
            x_range=[0, 2*PI]
        )

        cos = axes.plot(
            lambda x: np.cos(x),
            color=BLUE,
            x_range=[0, 2*PI]
        )

            #SinCos Labels
        name1 = axes.get_graph_label(sin, r"\sin(x)", color=RED, x_val=4.8, direction=DOWN)
        name2 = axes.get_graph_label(cos, r"\cos(x)", color=BLUE, x_val=3.1, direction=DOWN)

        self.add(axes, labels)
        self.play(Create(sin), run_time=2)
        self.play(Create(name1), run_time=0.5)
        self.wait(1)

        self.play(Create(cos), run_time=2)
        self.play(Create(name2), run_time=0.5)
        self.wait(1)

        # manim Pr29_sin_cos_graph.py Manim29 --renderer=opengl -p
        # manim -pqk Pr29_sin_cos_graph.py Manim29
        # manim -pqh Pr29_sin_cos_graph.py Manim29
                

        