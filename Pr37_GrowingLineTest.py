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
        self.add(axes)

        tracker = ValueTracker(0)   # start a bit higher

        # Growing sine curve
        sin = always_redraw(
            lambda: axes.plot(
                lambda x: np.sin(x),
                x_range=[0, max(tracker.get_value(), 0.05)],
                color=BLUE,
                use_smoothing=False     # ← important for OpenGL
            )
        )

        # Dot at the tip
        dot = always_redraw(
            lambda: Dot(
                axes.c2p(tracker.get_value(), np.sin(tracker.get_value())),
                color=TEAL_C
            )
        )
        label= MathTex(r"\sin(x)", color=BLUE, font_size=24).to_edge(UP)

        self.add(sin, dot)
        self.play(Write(label))

        self.play(
            tracker.animate.set_value(4 * PI),
            run_time=3,
            rate_func=there_and_back
        )
        self.wait(0.1)

        # self.play(FadeOut(sin), FadeOut(dot), FadeOut(label))

            # The tracker reset_____________________________________________
        tracker.set_value(0)

        sin2 = always_redraw(
            lambda: axes.plot(
                lambda x: np.sin(2*x),
                x_range=[0, max(tracker.get_value(), 0.05)],
                color=RED,
                use_smoothing=False,
            )
        )

        dot2 = always_redraw(
            lambda: Dot(
                axes.c2p(
                    tracker.get_value(),
                    np.sin(2 * tracker.get_value())
                ),
                color=LIGHT_PINK,
            )
        )

        label2 = MathTex(r"\sin(2x)", color=RED, font_size=24).to_edge(UP)

        self.play(ReplacementTransform(sin, sin2),
            ReplacementTransform(dot, dot2),
            ReplacementTransform(label, label2),
            run_time=1)

        # self.add(sin2, dot2)
        # self.play(Write(label2))

        self.play(
            tracker.animate.set_value(4*PI),
            run_time=3,
            rate_func=there_and_back,
        )
        self.wait(1)

        # manim Pr37_GrowingLineTest.py GrowingLine --renderer=opengl -p
        # manim -pqk Pr37_GrowingLineTest.py GrowingLine
        # manim -pqh Pr37_GrowingLineTest.py GrowingLine