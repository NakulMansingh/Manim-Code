import numpy as np
from manim import *

config.window_size = "default"
config.window_position = "33, 959"

class TaylorSeries(Scene):
    def construct(self):

            #axes
        axes=Axes(x_range=[-3.5,2.5], y_range=[-2.7,2.7], tips=False)
        labels=axes.get_axis_labels("x","")
        self.add(axes, labels)

        title=Text("Taylor Series", font_size=32).move_to(UP*2.5 + LEFT*4)

        eq=MathTex(r"e^x", color=WHITE)
        eq.move_to(UP*3.2)
        eq0=MathTex(r"e^x", r"\approx", r"1", color=BLUE)
        eq0.move_to(UP*3.2)
        eq1=MathTex(r"e^x", r"\approx", r"1 + x}", color=PINK)
        eq1.move_to(UP*3.2)
        eq2=MathTex(r"e^x", r"\approx", r"1 + x + \dfrac{x^2}{2!}", color=PURPLE)
        eq2.move_to(UP*3.2)
        eq3=MathTex(r"e^x", r"\approx", r"1 + x + \dfrac{x^2}{2!} + \dfrac{x^3}{3!}", color=RED)
        eq3.move_to(UP*3.2)
        eq4=MathTex(r"e^x", r"\approx", r"1 + x + \dfrac{x^2}{2!} + \dfrac{x^3}{3!} + \dfrac{x^4}{4!}",color=TEAL)
        eq4.move_to(UP*3.2)
        eq5=MathTex(r"e^x", r"\approx", r"1 + x + \dfrac{x^2}{2!} + \dfrac{x^3}{3!} + \dfrac{x^4}{4!}+ \dfrac{x^5}{5!}",color=GREEN)
        eq5.move_to(UP*3.2)
        eq6=MathTex(r"e^x", r"\approx", r"1 + x + \dfrac{x^2}{2!} + \dfrac{x^3}{3!} + \dfrac{x^4}{4!}+ \dfrac{x^5}{5!}+ \dfrac{x^6}{6!}",color=GOLD)
        eq6.move_to(UP*3.2)

            #cose
        exponetial=axes.plot(lambda x: np.exp(x), color=WHITE, x_range=[-6, 6])
        sl=axes.get_graph_label( exponetial, r"\exp(x)", x_val=4, color=WHITE, direction=UP)

            # Taylor Polynomials
        p0=axes.plot(lambda x: 1, color=BLUE, x_range=[-6, 6])

        p1=axes.plot(lambda x: 1 + x, color=PINK, x_range=[-6, 6])

        p2=axes.plot(lambda x: 1 + x + x**2/2, color=PURPLE, x_range=[-6, 6])

        p3=axes.plot(lambda x: 1 + x + x**2/2 + x**3/6, color=RED, x_range=[-6, 6])

        p4=axes.plot(lambda x: 1 + x + x**2/2 + x**3/6 + x**4/24, color=TEAL, x_range=[-6, 6])

        p5=axes.plot(lambda x: 1 + x + x**2/2 + x**3/6 + x**4/24+ x**5/120, color=GREEN, x_range=[-6, 6])

        p6=axes.plot(lambda x: 1 + x + x**2/2 + x**3/6 + x**4/24+ x**5/120+ x**6/720, color=GOLD, x_range=[-6, 6])

        # animate
        self.play(Create(exponetial), Write(eq), Write(title), run_time=1.2)
        self.wait(0.5)

        self.play(Create(p0), ReplacementTransform(eq,eq0), run_time=1.2)
        self.wait(0.5)

        self.play(ReplacementTransform(p0,p1), ReplacementTransform(eq0,eq1), run_time=1.2)
        self.wait(0.5)

        self.play(ReplacementTransform(p1,p2), ReplacementTransform(eq1,eq2), run_time=1.2)
        self.wait(0.5)

        self.play(ReplacementTransform(p2,p3), ReplacementTransform(eq2,eq3), run_time=1.2)
        self.wait(0.5)

        self.play(ReplacementTransform(p3,p4), ReplacementTransform(eq3,eq4), run_time=1.2)
        self.wait(0.5)

        self.play(ReplacementTransform(p4,p5), ReplacementTransform(eq4,eq5), run_time=1.2)
        self.wait(0.5)

        self.play(ReplacementTransform(p5,p6), ReplacementTransform(eq5,eq6), run_time=1.2)
        self.wait(1.5)

        # Add this line at the very bottom:
        # self.interactive_embed()

        # manim Pr26_exp_TaylorSeries.py Manim26 --renderer=opengl -p
        # manim -pqk Pr26_exp_TaylorSeries.py Manim26
        # manim -pqh Pr26_exp_TaylorSeries.py Manim26