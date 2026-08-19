        # Problem 23 — basic graph

# Create a scene called ParabolaGraph that:

# Creates axes with x_range=[−3, 3] and y_range=[0, 9]
# Plots f(x) = x² in RED
# Adds axis labels "x" and "f(x)"
# Adds a curve label r"x^2" at x=2
# Animates: axes appear → curve draws itself → label writes

import numpy as np
from manim import *

class Powers(Scene):
    def construct(self):

        axes=Axes(
            x_range=[-4,4],
            y_range=[-6,6],
        )

        labels=axes.get_axis_labels("x","f(x)")

            # constant
        constant=axes.plot(lambda x: 3, color=YELLOW_A, )
        #l0=axes.get_graph_label(constant, r"\ c", color=YELLOW_A, x_val=3,)

            # straight-
        straight=axes.plot(lambda x: x, color=RED, )
        l1=axes.get_graph_label(straight, r"\ x", color=RED, x_val=4,)

            # parabola
        parabola=axes.plot(lambda x: x**2, color=BLUE,)
        l2=axes.get_graph_label(parabola, r"\ x^2", color=BLUE, x_val=3,)

            # cube
        cube=axes.plot(lambda x: x**3, color=GRAY_BROWN, )
        l3=axes.get_graph_label(cube, r"\ x^3", color=GRAY_BROWN, x_val=3,)

            # 4th power
        power4=axes.plot(lambda x: x**4, color=GREEN, x_range=[-2.7,2.7])
        l4=axes.get_graph_label(power4, r"\ x^4", color=GREEN, x_val=3,)

            # 5th power
        power5=axes.plot(lambda x: x**5, color=TEAL, x_range=[-2.7,2.7])
        l5=axes.get_graph_label(power5, r"\ x^5", color=TEAL, x_val=3,)

        power6=axes.plot(lambda x: x**6, color=PINK, x_range=[-2.7,2.7])
        l6=axes.get_graph_label(power6, r"\ x^6", color=PINK, x_val=3,)

        power7=axes.plot(lambda x: x**7, color=GOLD, x_range=[-2.7,2.7])
        l7=axes.get_graph_label(power7, r"\ x^7", color=GOLD, x_val=3,)


        self.add(axes, labels)

        #self.play(Create(constant), Write(l0), run_time=1.2)
        self.play(Create(constant), run_time=1.2)
        self.wait(0.5)
        # self.play(ReplacementTransform(constant, straight), ReplacementTransform(l0,l1), run_time=1.2)
        self.play(ReplacementTransform(constant, straight), Write(l1), run_time=1.2)
        self.wait(0.5)
        self.play(ReplacementTransform(straight, parabola), ReplacementTransform(l1,l2), run_time=1.2)
        self.wait(0.5)
        self.play(ReplacementTransform(parabola, cube), ReplacementTransform(l2,l3), run_time=1.2)
        self.wait(0.5)
        self.play(ReplacementTransform(cube, power4), ReplacementTransform(l3,l4), run_time=1.2)
        self.wait(0.5)
        self.play(ReplacementTransform(power4, power5), ReplacementTransform(l4,l5), run_time=1.2)
        self.wait(0.5)
        self.play(ReplacementTransform(power5, power6), ReplacementTransform(l5,l6), run_time=1.2)
        self.wait(0.5)
        self.play(ReplacementTransform(power6, power7), ReplacementTransform(l6,l7), run_time=1.2)
        self.wait(1)

        # manim Pr23_powers_dancing.py Manim23 --renderer=opengl -p
        # manim -pqk Pr23_powers_dancing.py Manim23
        # manim -pqh Pr23_powers_dancing.py Manim23