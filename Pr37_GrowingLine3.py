from manim import *
import numpy as np

config.window_size = "default"
config.window_position = "33,959"

class GrowingLine(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 2 * PI, PI/2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=8,
            y_length=4,
            tips=False,
        )
        labels = axes.get_axis_labels("x", "y")
        self.play(Create(axes), Write(labels))
        self.wait(0.1)

            # the tracker ____________________________________________________
        tracker = ValueTracker(0)

        # Growing sine curve
        sin = always_redraw(
            lambda: axes.plot(
                lambda x: np.sin(x),
                x_range=[0, tracker.get_value() + 0.001],
                color=BLUE,
            )
        )

        # Dot at the tip
        dot = always_redraw(
            lambda: Dot(
                axes.c2p(tracker.get_value(), np.sin(tracker.get_value())),
                color=WHITE
            )
        )

        name = MathTex(r"\sin(x)", color=BLUE, font_size= 36).move_to(UP*2)

        label = always_redraw(
            lambda: MathTex(
                rf"x = {tracker.get_value():.1f}",
                color=WHITE,
                font_size=36
            ).move_to(DOWN*2)
        )

        self.add(sin, dot, name, label)
        self.play(
            tracker.animate.set_value(2*PI),
            run_time=3,
            rate_func=there_and_back
        )

        self.play(FadeOut(sin), FadeOut(dot), FadeOut(name), FadeOut(label), run_time= 0.05)

            # The tracker reset2__________________________________________________
        tracker.set_value(0)

        sin2 = always_redraw(
            lambda: axes.plot(
                lambda x: np.sin(2*x),
                x_range=[0, tracker.get_value() + 0.001],
                color=RED,
            )
        )

        dot2 = always_redraw(
            lambda: Dot(
                axes.c2p(tracker.get_value(), np.sin(2 * tracker.get_value())),
                color=WHITE
            )
        )

        name2 = MathTex(r"\sin(2x)", color=RED, font_size= 36).move_to(UP*2)

        label2 = always_redraw(
            lambda: MathTex(
                rf"x = {tracker.get_value():.1f}",
                color=WHITE,
                font_size=36,
            ).move_to(DOWN*2)
        )

        self.add(sin2, dot2, name2, label2)
        self.play(
            tracker.animate.set_value(2*PI),
            run_time=3,
            rate_func=there_and_back,
        )

        self.play(FadeOut(sin2), FadeOut(dot2), FadeOut(name2), FadeOut(label2), run_time= 0.05)

            # The tracker reset3__________________________________________________
        tracker.set_value(0)
        
        sin3 = always_redraw(
            lambda: axes.plot(
                lambda x: np.sin(3*x),
                x_range=[0, tracker.get_value() + 0.001],
                color=YELLOW_E,
            )
        )
        
        dot3 = always_redraw(
            lambda: Dot(
                axes.c2p(tracker.get_value(), np.sin(3 * tracker.get_value())),
                color=WHITE
            )
        )
        name3 = MathTex(r"\sin(3x)", color=YELLOW_A, font_size= 36).move_to(UP*2)
        
        label3 = always_redraw(
            lambda: MathTex(
                rf"x = {tracker.get_value():.1f}",
                color=WHITE,
                font_size=36,
            ).move_to(DOWN*2)
        )
        
        self.add(sin3, dot3, name3, label3)
        self.play(
            tracker.animate.set_value(2*PI),
            run_time=3,
            rate_func=there_and_back,
        )

        self.play(FadeOut(sin3), FadeOut(dot3), FadeOut(name3), FadeOut(label3), run_time= 0.05)
        
            # The tracker reset4__________________________________________________
        tracker.set_value(0)
        
        sin4 = always_redraw(
            lambda: axes.plot(
                lambda x: np.sin(4*x),
                x_range=[0, tracker.get_value() + 0.001],
                color=TEAL,
            )
        )
        
        dot4 = always_redraw(
            lambda: Dot(
                axes.c2p(tracker.get_value(), np.sin(4 * tracker.get_value())),
                color= WHITE
            )
        )
        
        name4 = MathTex(r"\sin(4x)", color=TEAL, font_size= 36).move_to(UP*2)
        
        label4 = always_redraw(
            lambda: MathTex(
                rf"x = {tracker.get_value():.1f}",
                color=WHITE,
                font_size=36,
            ).move_to(DOWN*2)
        )
        
        self.add(sin4, dot4, name4, label4)
        self.play(
            tracker.animate.set_value(2*PI),
            run_time=3,
            rate_func=there_and_back,
        )

        self.play(FadeOut(sin4), FadeOut(dot4), FadeOut(name4), FadeOut(label4), run_time= 0.05)
        
            # The tracker reset5__________________________________________________
        tracker.set_value(0)
        
        sin5 = always_redraw(
            lambda: axes.plot(
                lambda x: np.sin(5*x),
                    x_range=[0, tracker.get_value() + 0.001],
                    color=PINK,
            )
         )
        
        dot5 = always_redraw(
            lambda: Dot(
                axes.c2p(tracker.get_value(), np.sin(5 * tracker.get_value())),
                color=WHITE
            )
        )
        
        name5 = MathTex(r"\sin(5x)", color=PINK, font_size= 36).move_to(UP*2)
        
        label5 = always_redraw(
            lambda: MathTex(
                rf"x = {tracker.get_value():.1f}",
                    color=WHITE,
                font_size=36,
            ).move_to(DOWN*2)
        )
        
        self.add(sin5, dot5, name5, label5)
        self.play(
            tracker.animate.set_value(2*PI),
            run_time=3,
            rate_func=there_and_back,
        )

        self.wait(0.1)
        
        # manim Pr37_GrowingLine3.py GrowingLine --renderer=opengl -p
        # manim -pqk Pr37_GrowingLine3.py GrowingLine
        # manim -pqh Pr37_GrowingLine3.py GrowingLine
