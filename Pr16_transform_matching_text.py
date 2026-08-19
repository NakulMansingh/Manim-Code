    # Problem 16 — TransformMatchingTex

# Create a scene called KineticEnergyDerivation that shows:

# Step 1 — write: r"W", r"=", r"F", r"s"

# Step 2 — transform to: r"W", r"=", r"m", r"a", r"s"

# Step 3 — transform to: r"W", r"=", r"\frac{1}{2}", r"m", r"v^2"

# Each step uses TransformMatchingTex. Add 1 second wait between steps.

from manim import *
class KEDerivation(Scene):
    def construct(self):

        eq1 = MathTex(r"W", r"=", r"F", r"s")
        eq2 = MathTex(r"W", r"=", r"m", r"a", r"s")
        eq3 = MathTex(r"W", r"=", r"\frac{1}{2}", r"m", r"v^2")

        self.play(Write(eq1))
        self.wait(1)

        self.play(TransformMatchingShapes(eq1, eq2))
        self.wait(1)

        self.play(TransformMatchingShapes(eq2, eq3))
        self.wait(1)

        # manim Pr16_transform_matching_text.py Manim16 --renderer=opengl -p
        # manim -pqk Pr16_transform_matching_text.py Manim16
