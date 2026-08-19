import numpy as np
from manim import *

config.window_size = "default"
config.window_position = "33, 959"
# config.window_position = "ORIGIN"

class TaylorSeries(Scene):
    def construct(self):

            #axes
        axes=Axes(x_range=[-6,6], y_range=[-2.7,2.7], tips=False)
        labels=axes.get_axis_labels("x","")
        self.add(axes, labels)

        title=Text("Taylor Series", font_size=32).move_to(UP*2.5 + LEFT*4)

        eq=MathTex(r"cos(x)", color=WHITE)
        eq.move_to(UP*3.2)
        eq1=MathTex(r"cos(x)", r"\approx", r"1", color=BLUE)
        eq1.move_to(UP*3.2)
        eq3=MathTex(r"cos(x)", r"\approx", r"1 - \dfrac{x^2}{2!}", color=BLUE)
        eq3.move_to(UP*3.2)
        eq5=MathTex(r"cos(x)", r"\approx", r"1 - \dfrac{x^2}{2!} + \dfrac{x^4}{4!}", color=BLUE)
        eq5.move_to(UP*3.2)
        eq7=MathTex(r"cos(x)", r"\approx", r"1 - \dfrac{x^2}{2!} + \dfrac{x^4}{4!} - \dfrac{x^6}{6!}", color=BLUE)
        eq7.move_to(UP*3.2)
        eq9=MathTex(r"cos(x)", r"\approx", r"1 - \dfrac{x^2}{2!} + \dfrac{x^4}{4!} - \dfrac{x^6}{6!} + \dfrac{x^8}{8!}",color=BLUE)
        eq9.move_to(UP*3.2)
        eq11=MathTex(r"cos(x)", r"\approx", r"1 - \dfrac{x^2}{2!} + \dfrac{x^4}{4!} - \dfrac{x^6}{6!} + \dfrac{x^8}{8!} - \dfrac{x^{10}}{10!}",color=BLUE)
        eq11.move_to(UP*3.2)
        

            #cose
        cose=axes.plot(lambda x: np.cos(x), color=WHITE, x_range=[-6, 6])
        sl=axes.get_graph_label( cose, r"\cos(x)", x_val=4, color=WHITE, direction=UP)

            # Taylor Polynomials
        p1=axes.plot(lambda x: 1, color=BLUE, x_range=[-6, 6])

        p3=axes.plot(lambda x: 1 - x**2/2, color=BLUE, x_range=[-6, 6])

        p5=axes.plot(lambda x: 1 - x**2/2 + x**4/24, color=BLUE, x_range=[-6, 6])

        p7=axes.plot(lambda x: 1 - x**2/2 + x**4/24 - x**6/720, color=BLUE, x_range=[-6, 6])

        p9=axes.plot(lambda x: 1 - x**2/2 + x**4/24 - x**6/720 + x**8/40320, color=BLUE, x_range=[-6, 6])

        p11=axes.plot(lambda x: 1 - x**2/2 + x**4/24 - x**6/720 + x**8/40320 - x**10/3628800, color=BLUE, x_range=[-6, 6])

        # animate
        self.play(Create(cose), Write(eq), Write(title), run_time=1.2)
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
        self.wait(0.5)

        self.play(ReplacementTransform(p9,p11), ReplacementTransform(eq9,eq11), run_time=1.2)
        self.wait(1.5)

        # Add this line at the very bottom:
        # self.interactive_embed()

        # manim Pr28_cosine_TaylorSeries.py Manim28 --renderer=opengl -p
        # manim -pqk Pr28_cosine_TaylorSeries.py Manim28
        # manim -pqh Pr28_cosine_TaylorSeries.py Manim28
        
        # manim Pr28_cosine_TaylorSeries.py TaylorSeries --renderer=opengl -p