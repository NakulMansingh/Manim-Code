    # Problem 12 — equation transformation

# This is pure 3Blue1Brown style. Create a scene called EqTransform that:

# Shows the equation F = ma in the centre
# Waits 1 second
# Uses Circumscribe to highlight F
# Transforms the equation into a = F/m using ReplacementTransform
# Uses Indicate on the new equation
# Shows the text "solving for acceleration" below it with Write

from manim import *
class EqTransfo(Scene):
    def construct(self):

        # create eqs & txs
        eq1 = MathTex(r"F=ma", color=BLUE, run_time=2.5)
        eq2 = MathTex(r"a=\frac{F}{m}}", color=GRAY_BROWN, run_time=2.5)
        tx = Text("acceleration")

            # This is LaTeX notation — the same LaTeX you'd use in a physics paper or textbook:
                # r"\frac{F}{m}"   # renders as F/m as a proper fraction
                # r"\frac{a}{b}"   # renders as a/b
                # r"x^{2}"         # renders as x²
                # r"\sqrt{2}"      # renders as √2

        # position the text
        tx.move_to(DOWN*1)

        # show 1st eq
        self.play(
            Write(eq1, run_time=2))
        self.wait(1)

        # highlight F
        self.play(Circumscribe(eq1[0][0], color=RED))
        self.wait(0.5)
            # eq1[0] accesses the first part of the MathTex object.
            # eq1[0][0] goes one level deeper to get just the first character — F.
            # This is how you highlight individual parts of an equation in Manim.
            
                #eq = MathTex(r"F = ma")
                # eq[0]      # the whole expression
                # eq[0][0]   # "F"
                # eq[0][1]   # "="
                # eq[0][2]   # "m"
                # eq[0][3]   # "a"

        # Transform 
        self.play(ReplacementTransform(eq1,eq2))
        self.wait(1)

        # # indicate new eq
        # self.play(Indicate(eq2, color=RED))
        # self.wait(0.5)

        # highlight a
        self.play(Circumscribe(eq2[0][0], Circle, color=RED))
        self.wait(0.5)

        # write tx
        # self.play(Write(tx))
        # self.wait(2)
        
        # manim Pr12_equation_transformation.py Manim12 --renderer=opengl -p
        # manim -pqk Pr12_equation_transformation.py Manim12