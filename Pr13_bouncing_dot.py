    # Problem 13 — bouncing dot

# Create a scene called BouncingDot that:

# Creates a white dot at the bottom of the screen (DOWN * 3)
# Moves it to the top (UP * 3) using rate_func=rush_into
# Moves it back to the bottom using rate_func=rush_from (slow start, fast end)
# Repeats this 3 times using a for loop
# On the final bounce, uses Flash when it hits the top

from manim import *

class BouncingDot(Scene):
    def construct(self):

        dot = Dot(radius=0.3, color=WHITE)
        dot.move_to(DOWN * 3)
        self.add(dot)

        for i in range(3):

            # move up
            self.play(
                dot.animate.move_to(UP * 3),
                rate_func=rush_into,
                run_time=0.8
            )
            self.wait(0.1)

            # flash on last bounce only
            if i == 2:
                self.play(
                    Flash(
                        dot,
                        color=YELLOW,
                        flash_radius=1.0,
                        num_lines=16,
                        line_length=0.4
                    )
                )
                self.wait(0.3)

            # move down
            self.play(
                dot.animate.move_to(DOWN * 3),
                rate_func=rush_from,
                run_time=0.8
            )
            self.wait(0.2)

        self.wait(1)


        # manim Pr13_bouncing_dot.py Manim13 --renderer=opengl -p
        # manim -pqk Pr13_bouncing_dot.py Manim13

        ## code doesn't work completely ##