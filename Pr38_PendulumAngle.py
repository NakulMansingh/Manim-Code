    # Problem 38 — pendulum angle

# Create a scene called PendulumAngle that shows a pendulum swinging using updaters:

# Create a ValueTracker for the angle θ, starting at π/4
# Use always_redraw to draw:
# A line from ORIGIN to the bob position: [sin(θ), -cos(θ), 0] scaled by 2
# A dot at the bob position
# A label showing f"θ = {theta:.2f} rad"
# Animate the tracker from π/4 to −π/4 and back using there_and_back, run_time=3
# Repeat 3 times using a for loop# 

import numpy as np
from manim import *

config.window_size = "default"
config.window_position = "33,959"

class PendulumAngle(Scene):
    def construct(self):

        pivot = Dot(ORIGIN, color=WHITE)
        self.add(pivot)

            # tracker ________________________________________________________
        theta = ValueTracker(PI/4)        # tracker starts from pi/4

        string = always_redraw(
            lambda: Line(
                ORIGIN,
                np.array([
                    2 * np.sin(theta.get_value()),
                   -2 * np.cos(theta.get_value()),
                    0
                ]),
                color=WHITE,
                stroke_width=4
            )
        )

        bob = always_redraw(
            lambda: Dot(
                np.array([
                    2*np.sin(theta.get_value()),
                   -2*np.cos(theta.get_value()),
                    0
                ]),
                color=BLUE,
                radius=0.2
            )
        )

        label = always_redraw(
            lambda: MathTex(
                rf"\theta = {theta.get_value():.1f}",
                color=WHITE,
                font_size=36,
            ).to_edge(UP)
        )

        self.add(bob, string, label)
        self.wait(0.5)

        for i in range(3):
            self.play(
                theta.animate.set_value(-PI/4),
                run_time=2,
                rate_func=there_and_back
            )
            self.wait(0.2)

        self.play(1)



        # manim Pr38_PendulumAngle.py PendulumAngle --renderer=opengl -p
        # manim -pqk Pr38_PendulumAngle.py PendulumAngle
        # manim -pqh Pr38_PendulumAngle.py PendulumAngle

