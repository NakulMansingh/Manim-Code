    # Problem 4 — equation layout

# This one is closer to real 3Blue1Brown style. Create a scene called EquationLayout that:

# Shows the title "Newton's Second Law" at the TOP of the screen
# Shows the equation F = ma in the centre
# Shows three labels below the equation, side by side:
# "F = Force" on the left
# "m = mass" in the centre
# "a = acceleration" on the right
# Animate them appearing in this order: title → equation → three labels together

# Use MathTex for the equation and Text for everything else. Use move_to, next_to, and shift appropriately.

from manim import*
class EquationLayout(Scene):
    def construct(self):

        # create texts
        t1 = Text("Newton's Second Law", color=BLUE)
        t2 = MathTex(r"F = ma").scale(2)
        t3 = Text("m = mass",color=DARK_BROWN).scale(0.7)
        t4 = Text("F = Force",color=DARK_BROWN).scale(0.7)
        t5 = Text("a = acceleration",color=DARK_BROWN).scale(0.7)

        # where texts are on the screen
        t1.move_to(UP*2)
        t2.move_to(ORIGIN)
        t3.next_to(t2, DOWN, buff = 1.5)
        t4.next_to(t3, LEFT, buff = 2.0)
        t5.next_to(t3, RIGHT, buff = 2.0)

        # show them on the screen
        self.play(Write(t1))
        self.wait(1)

        self.play(Write(t2))
        self.wait(1)

        self.play(
            Write(t3),
            Write(t4),
            Write(t5)
        )
        self.wait(1)

        # manim Pr8_equation_layout.py Manim8 --renderer=opengl -p
        # manim -pqk Pr8_equation_layout.py Manim8