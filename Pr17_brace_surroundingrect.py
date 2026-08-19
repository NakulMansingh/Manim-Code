    # Problem 17 — Brace and SurroundingRectangle

# Create a scene called BoxedResult that:

# Writes the quadratic formula:

    # MathTex(r"x", r"=", r"\frac{", r"-b", r"\pm", r"\sqrt{b^2 - 4ac}", r"}{", r"2a", r"}")
# Puts a Brace below the fraction with the label "discriminant" pointing at \sqrt{b^2 - 4ac}
# Puts a SurroundingRectangle around the whole equation in YELLOW
# Animates: write equation → grow brace → write label → create box

from manim import *
class BoxedResult(Scene):
    def construct(self):

        # write quadratic formula
        eq = MathTex(r"x", r"=",
                     r"\frac{",
                     r"-b", r"\pm", r"\sqrt{b^2 - 4ac}",
                     r"}{",
                     r"2a",
                     r"}")

        # step1 - animate equation
        self.play(Write(eq))
        self.wait(1)

        # step2 - brace & label
        brace = Brace(eq[5], direction=UP, color=BLUE)
        label = brace.get_text("discriminant")
        label.set_color(BLUE)

        self.play(eq[5].animate.set_color(BLUE), GrowFromCenter(brace))
        self.play(Write(label))
        self.wait(1)

        # step3 - rect box around the equation
        box = SurroundingRectangle(eq, color=RED_B, buff=0.2, stroke_width=2, stroke_opacity=1)
        self.play(Create(box))
        self.wait(1)

# from manim import *

# class BoxedResult(Scene):
#     def construct(self):

#         # write the quadratic formula
#         eq = MathTex(
#             r"x", r"=", r"\frac{",
#             r"-b", r"\pm", r"\sqrt{b^2 - 4ac}",
#             r"}{", r"2a", r"}"
#         )

#         # step 1 — write equation
#         self.play(Write(eq))
#         self.wait(1)

#         # step 2 — brace under the discriminant part (index 5)
#         brace = Brace(eq[5], direction=UP, color=BLUE)
#         label = brace.get_text("discriminant")
#         label.set_color(BLUE)

#         self.play(eq[5].animate.set_color(BLUE), GrowFromCenter(brace))
#         self.play(Write(label))
#         self.wait(1)

#         # step 3 — box around whole equation
#         box = SurroundingRectangle(eq, color=RED_B, buff=0.2)
#         self.play(Create(box))
#         self.wait(2)

        # manim Pr17_brace_surroundingrect.py Manim17 --renderer=opengl -p
        # manim -pqk Pr17_brace_surroundingrect.py Manim17