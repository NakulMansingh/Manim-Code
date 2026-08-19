    # Problem 10 — shape cycle

# Create a scene called ShapeCycle that:

# Starts with a blue circle in the centre, filled with 0.3 opacity
# Transforms it into a red square
# Transforms that into a green triangle
# Transforms that into a yellow star using Star()
# After each transform, use Indicate to highlight the new shape
# Finally scale the star up by 1.5 and fade it out

from manim import *
class ShapeCycle(Scene):
    def construct(self):
        circle = Circle(color=BLUE, fill_opacity=0.3)
        square = Square(color=RED, fill_opacity=0.3)
        triangle = Triangle(color=GREEN, fill_opacity=0.3)
        star = Star(color=GOLD, fill_opacity=0.3)

        self.play(Create(circle))
        self.play(Indicate(circle), color=WHITE)
        self.wait(0.5)

        self.play(ReplacementTransform(circle, square))
        self.play(Indicate(square))
        self.wait(0.5)

        self.play(ReplacementTransform(square, triangle))
        self.play(Indicate(triangle))
        self.wait(0.5)
        self.play(ReplacementTransform(triangle, star))
        self.play(Indicate(star))
        self.wait(0.5)
        self.play(star.animate.scale(1.5))
        self.play(FadeOut(star))
        self.wait(0.5)

        # manim Pr10_shape_cycle.py Manim10 --renderer=opengl -p
        # manim -pqk Pr10_shape_cycle.py Manim10