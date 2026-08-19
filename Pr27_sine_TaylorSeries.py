import numpy as np
from manim import *

config.window_size = "default"
config.window_position = "33, 959"

class TaylorSeries(Scene):
    def construct(self):

            #axes
        axes=Axes(x_range=[-6,6], y_range=[-2.7,2.7], tips=False)
        labels=axes.get_axis_labels("x","")
        self.add(axes, labels)

        title=Text("Taylor Series", font_size=32).move_to(UP*2.5 + LEFT*4)

        eq=MathTex(r"sin(x)", color=WHITE)
        eq.move_to(UP*3.2)
        eq1=MathTex(r"sin(x)", r"\approx", r"x", color=RED)
        eq1.move_to(UP*3.2)
        eq3=MathTex(r"sin(x)", r"\approx", r"x - \dfrac{x^3}{3!}", color=RED)
        eq3.move_to(UP*3.2)
        eq5=MathTex(r"sin(x)", r"\approx", r"x - \dfrac{x^3}{3!} + \dfrac{x^5}{5!}", color=RED)
        eq5.move_to(UP*3.2)
        eq7=MathTex(r"sin(x)", r"\approx", r"x - \dfrac{x^3}{3!} + \dfrac{x^5}{5!} - \dfrac{x^7}{7!}", color=RED)
        eq7.move_to(UP*3.2)
        eq9=MathTex(r"sin(x)", r"\approx", r"x - \dfrac{x^3}{3!} + \dfrac{x^5}{5!} - \dfrac{x^7}{7!} + \dfrac{x^9}{9!}",color=RED)
        eq9.move_to(UP*3.2)

            #sine
        sine=axes.plot(lambda x: np.sin(x), color=WHITE, x_range=[-6, 6])
        sl=axes.get_graph_label( sine, r"\sin(x)", x_val=4, color=WHITE, direction=UP)

            # Taylor Polynomials
        p1=axes.plot(lambda x: x, color=RED, x_range=[-6, 6])

        p3=axes.plot(lambda x: x - x**3 /6, color=RED, x_range=[-6, 6])

        p5=axes.plot(lambda x: x - x**3/6 + x**5/120, color=RED, x_range=[-6, 6])

        p7=axes.plot(lambda x: x - x**3/6 + x**5/120 - x**7/5040, color=RED, x_range=[-6, 6])

        p9=axes.plot(lambda x: x - x**3/6 + x**5/120 - x**7/5040 + x**9/362880, color=RED, x_range=[-6, 6])

        # animate
        self.play(Create(sine), Write(eq), Write(title), run_time=1.2)
        self.wait(0.5)

        self.play(Create(p1), ReplacementTransform(eq,eq1), FadeOut(title), run_time=1.2)
        self.wait(0.5)

        self.play(ReplacementTransform(p1,p3), ReplacementTransform(eq1,eq3), run_time=1.2)
        self.wait(0.5)

        self.play(ReplacementTransform(p3,p5), ReplacementTransform(eq3,eq5), run_time=1.2)
        self.wait(0.5)

        self.play(ReplacementTransform(p5,p7), ReplacementTransform(eq5,eq7), run_time=1.2)
        self.wait(0.5)

        self.play(ReplacementTransform(p7,p9), ReplacementTransform(eq7,eq9), run_time=1.2)
        self.wait(1.5)

        # Add this line at the very bottom:
        # self.interactive_embed()
    

        # manim Pr27_sine_TaylorSeries.py Manim27 --renderer=opengl -p
        # manim -pqk Pr27_sine_TaylorSeries.py Manim27
        # manim -pqh Pr27_sine_TaylorSeries.py Manim27