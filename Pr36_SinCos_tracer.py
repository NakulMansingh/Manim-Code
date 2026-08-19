    # Problem 36 — sine and cosine together

# Create a scene called SinCosTracer that:

# Creates axes with x_range=[0, 2π], y_range=[−1.5, 1.5]
# Plots both sin(x) in BLUE and cos(x) in RED
# Creates TWO dots using always_redraw — one on sin, one on cos
# Creates two labels showing their current y values
# Animates both dots moving together using one tracker.animate.set_value(2*PI)

import numpy as np
from manim import *

config.window_size = "default"
config.window_position = "33, 959"

class SinCosTracer(Scene):
    def construct(self):

        axes = Axes(
            x_range=[0, 2.05*PI],
            y_range=[-1.5, 1.5],
            x_length=10,
            y_length=5,
            tips=False,
        )

        self.add(axes)

        sin = axes.plot(
            lambda x: np.sin(x),
            color=BLUE,
            x_range=[0, 2*PI]
        )

        cos = axes.plot(
            lambda x: np.cos(x),
            color=RED,
            x_range=[0, 2*PI]
        )

        self.add(sin,cos)
        self.wait(0.5)

        tracker = ValueTracker(0)

        # Dot on sine
        dot1 = always_redraw(
            lambda: Dot(
                axes.c2p(
                    tracker.get_value(),
                    np.sin(tracker.get_value())
                ),
                color = TEAL
            )
        )

        label1 = always_redraw(
            lambda: Text(
                f"sin = {np.sin(tracker.get_value()):.1f}",
                color = TEAL,
                font_size=24,
            ).next_to(axes.c2p(tracker.get_value(),np.sin(tracker.get_value())), UP),
        )

        # Dot on cosine
        dot2 = always_redraw(
            lambda: Dot(
                axes.c2p(
                    tracker.get_value(),
                    np.cos(tracker.get_value()),
                ),
                color = LIGHT_PINK
            )
        )

        label2 = always_redraw(
            lambda: Text(
                f"cos = {np.cos(tracker.get_value()):.1f}",
                color = LIGHT_PINK,
                font_size=24,
            ).next_to(axes.c2p(tracker.get_value(), np.cos(tracker.get_value())), UP)
        )

        self.add(dot1, dot2, label1, label2)
        self.wait(0.5)

        self.play(tracker.animate.set_value(2*PI), run_time=5, rate_func=linear)
        self.wait(1)

        self.play(FadeOut(dot1), FadeOut(dot2), FadeOut(label1), FadeOut(label2))

        # manim Pr36_SinCos_tracer.py SinCosTracer --renderer=opengl -p
        # manim -pqk Pr36_SinCos_tracer.py SinCosTracer
        # manim -pqh Pr36_SinCos_tracer.py SinCosTracer