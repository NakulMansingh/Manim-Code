

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
        sin2 = always_redraw(
            lambda: axes.plot(
                lambda x: np.sin(2*x),
                x_range=[0, tracker.get_value() + 0.001],
                color=RED_D,
            )
        )

        # Dot at the tip
        dot = always_redraw(
            lambda: Dot(
                axes.c2p(tracker.get_value(), np.sin(2*tracker.get_value())),
                color=LIGHT_PINK
            )
        )

        label = always_redraw(
            lambda: MathTex(
                rf"x = {tracker.get_value():.1f}",
                color=WHITE,
                font_size=24
            ).to_edge(DOWN)
        )
        

        self.add(sin2, dot, label)

        self.play(
            tracker.animate.set_value(4 * PI),
            run_time=3,
            rate_func=smooth
        )
        self.wait(1)

        # manim Pr37_GrowingLine2.py GrowingLine --renderer=opengl -p
        # manim -pqk Pr37_GrowingLine2.py GrowingLine
        # manim -pql Pr37_GrowingLine2.py GrowingLine
