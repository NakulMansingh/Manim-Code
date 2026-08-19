import numpy as np
from manim import *

class HiCircle(Scene):
    def construct(self):

        # parametric curve
        axes = Axes(
            x_range=[-2,2,1],
            y_range=[-2,2,1],
            x_length=7,
            y_length=7,
        )

        circlepath = axes.plot_parametric_curve(
            lambda t: np.array([np.cos(t), np.sin(t), 0]),
            t_range=[0, 2*PI], color=TEAL
        )

        self.play(Create(axes))
        self.play(Create(circlepath), color=TEAL, run_time=3)
        self.wait(1)

        # manim Pr22_circle.py Manim22 --renderer=opengl -p
        # manim -pqk Pr22_circle.py Manim22