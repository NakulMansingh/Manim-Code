# E=mc2 --> m=E/c2
from manim import *

class MatchingDemo(Scene):
    def construct(self):
        eq1 = MathTex(r"E", r"=", r"m", r"c^2")
        eq2 = MathTex(r"m", r"=", r"\frac{", r"E", r"}{", r"c^2", r"}")

        self.play(Write(eq1))
        self.wait(1)

        self.play(TransformMatchingTex(eq1, eq2), run_time=2)
        self.wait(1)

        # More robust SurroundingRectangle
        rect = SurroundingRectangle(
            eq2,
            color=RED,          # default, high contrast
            buff=0.15,
            stroke_width=4,        # explicit width helps OpenGL
            stroke_opacity=1,
        )
        self.play(Create(rect), run_time=1.5)
        # or safer with OpenGL:
        # self.play(FadeIn(rect), run_time=1)
        self.wait(2)

        
        # manim Pr14_Emc2_to_mEc2.py Manim14 --renderer=opengl -p
        # manim -pqk Pr14_Emc2_to_mEc2.py Manim14