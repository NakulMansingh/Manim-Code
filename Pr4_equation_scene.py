    # Problem 4 — equation scene

# Create a scene called EquationScene that shows these three equations one by one, each fading in:

# E = mc^2
# F = ma
# a^2 + b^2 = c^2

# Use MathTex for all three. Each should appear in a different color — yellow, blue, green. 
# Add a 1 second wait between each equation appearing.

# Hint: MathTex(r"E = mc^2", color=YELLOW)

from manim import *
class Equ(Scene):
    def construct(self):

        eq1 = MathTex(r"a^2 + b^2 = c^2", color = YELLOW)
        eq2 = MathTex(r"F = ma", color = BLUE)
        eq3 = MathTex(r"E = mc^2", color = RED)

        # Position them vertically
        eq1.shift(UP * 2)
        eq2.shift(ORIGIN)
        eq3.shift(DOWN * 2)

        # Fade in one by one with 1 second wait
        self.play(FadeIn(eq1), run_time = 1)
        self.wait(1)

        self.play(FadeIn(eq2), run_time = 1)
        self.wait(1)

        self.play(FadeIn(eq3), run_time = 1)
        self.wait(1)

        # manim Pr4_equation_scene.py Manim4 --renderer=opengl -p
        # manim -pqk Pr4_equation_scene.py Manim4
