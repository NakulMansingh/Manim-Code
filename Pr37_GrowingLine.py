    # Problem 37 — growing line

# Create a scene called GrowingLine that:
# Creates axes with x_range=[0, 4π]
# Uses a ValueTracker starting at 0
# Uses always_redraw to draw a partial sine curve from 0 to the tracker value:
    # axes.plot(np.sin, x_range=[0, tracker.get_value()+0.001])

# Animates the tracker from 0 to 4π over 5 seconds — the curve draws itself in real time
# Adds a dot at the leading edge of the curve

# This is the most satisfying animation — the curve grows as if being drawn by hand.

from manim import *
import numpy as np

config.window_size = "default"
config.window_position = "33,959"

class GrowingLine(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 4 * PI, PI/2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=8,
            y_length=4,
            tips=False,
        )
        labels = axes.get_axis_labels("x", "y")
        self.play(Create(axes), Write(labels))
        self.wait(0.1)
        
        tracker = ValueTracker(0)

        # Growing sine curve
        sin = always_redraw(
            lambda: axes.plot(
                np.sin,
                x_range=[0, tracker.get_value() + 0.001],
                color=BLUE,
            )
        )

        # Dot at the tip
        dot = always_redraw(
            lambda: Dot(
                axes.c2p(tracker.get_value(), np.sin(tracker.get_value())),
                color=TEAL
            )
        )

        label = always_redraw(
            lambda: MathTex(
                rf"x = {tracker.get_value():.1f}",
                color=WHITE,
                font_size=24
            ).to_edge(DOWN)
        )
        

        self.add(sin, dot, label)

        self.play(
            tracker.animate.set_value(4 * PI),
            run_time=3,
            rate_func=smooth
        )
        self.wait(1)

        # manim Pr37_GrowingLine.py GrowingLine --renderer=opengl -p
        # manim -pqk Pr37_GrowingLine.py GrowingLine
        # manim -pql Pr37_GrowingLine.py GrowingLine
