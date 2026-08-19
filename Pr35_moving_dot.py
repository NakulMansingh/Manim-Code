    # Problem 35 — moving dot with label
# Create a scene called MovingDot that:
# Creates a number line using NumberLine(x_range=[0, 10])
# Creates a dot at position 0 using ValueTracker and always_redraw
# Creates a label above the dot showing the current value like "x = 0.00" — also using always_redraw
# Animates the tracker from 0 to 10 over 4 seconds

import numpy as np
from manim import *

config.window_size = "default"
config.window_position = "33, 959"

class MovingDot(Scene):
    def construct(self):

        axes = Axes(x_range=[0, 11], x_length=10, tips=False)
        self.add(axes)

        tracker = ValueTracker(0)

        # Dot
        dot = always_redraw(
            lambda: Dot(
                axes.c2p(tracker.get_value(), 0),
                color=RED,
            )
        )

        # Label
        label = always_redraw(
            lambda: MathTex(
                f"x = {tracker.get_value():.2f}",
                color=YELLOW,
                font_size=24,
            ).next_to(axes.c2p(tracker.get_value(), 0), UP)
        )

        self.add(dot, label)
        self.play(tracker.animate.set_value(10), rate_func=linear, run_time=4)
        self.wait(1)

        # manim Pr35_moving_dot.py MovingDot --renderer=opengl -p
        # manim -pqk Pr35_moving_dot.py MovingDot
        # manim -pqh Pr35_moving_dot.py MovingDot

        
        