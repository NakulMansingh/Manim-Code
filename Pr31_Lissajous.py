    # Problem 4 — parametric curve

# Create a scene called LissajousScene that plots three Lissajous figures one after another using plot_parametric_curve:

# Figure 1: x=sin(t), y=sin(2t) — BLUE
# Figure 2: x=sin(2t), y=sin(3t) — RED
# Figure 3: x=sin(3t), y=sin(4t) — GREEN

# Each uses t_range=[0, 2π]. Show them one by one with Create, each taking 2 seconds. Add the title "Lissajous Figures" at the top.

import numpy as np
from manim import *

class Lissajous(Scene):
    def construct(self):

        axes = Axes(
            x_range=[-1.5,1.5],
            y_range=[-1.5,1.5],
        )
        title = Text("Lissajous Figures", font_size=32).next_to(axes, UP, buff=0.5)

        curve1 = axes.plot_parametric_curve(
            lambda t: np.array([np.sin(t), np.sin(2*t), 0]),
            t_range= [0, 2*PI],
            color=BLUE
        )

        curve2 = axes.plot_parametric_curve(
            lambda t: np.array([np.sin(2*t), np.sin(3*t), 0]),
            t_range= [0, 2*PI],
            color=RED
        )

        curve3 = axes.plot_parametric_curve(
            lambda t: np.array([np.sin(3*t), np.sin(4*t), 0]),
            t_range= [0, 2*PI],
            color=GREEN
        )

        self.add(axes, title)
        self.play(Create(curve1), rate_func=linear, run_time=2)
        self.wait(0.7)
        self.play(FadeOut(curve1), run_time=0.5)

        self.play(Create(curve2), rate_func=linear, run_time=2)
        self.wait(0.7)
        self.play(FadeOut(curve2), run_time=0.5)

        self.play(Create(curve3), rate_func=linear, run_time=2)
        self.wait(1)

        # manim Pr31_Lissajous.py Manim31 --renderer=opengl -p
        # manim -pqk Pr31_Lissajous.py Manim31
        # manim -pqh Pr31_Lissajous.py Manim31