from manim import *

class WithAndWithout(Scene):
    def construct(self):

        axes = Axes(
            x_range=[0, 5],
            y_range=[-1,5, 1.5],
            x_length=8, y_length=4
        )
        self.play(Create(axes))

            # Without Updater__________________________________________________
        title1 = Text("Without Updater", color=RED, font_size= 30).to_edge(UP)
        self.play(Write(title1))

        dot1 = Dot(axes.c2p(0,0), color=RED)
        label1 = Text("x = 0", color=RED, font_size=24).next_to(dot1, UP)

        self.add(dot1, label1)
        self.wait(0.5)

        # dot moves - label stays stuck at x = 0
        self.play(dot1.animate.move_to(axes.c2p(4,0)), run_time=2, rate_func=linear)
        self.wait(1)
        # label is still sitting at the old position - wrong!

        self.play(FadeOut(dot1), FadeOut(title1), FadeOut(label1), run_time=0.5)



            # With Updater______________________________________________________
        title2 = Text("With Updater", color=BLUE, font_size=30).to_edge(UP)
        self.play(Write(title2))

        # Tracker
        tracker = ValueTracker(0)

        dot2 = always_redraw(
            lambda: Dot(axes.c2p(tracker.get_value(), 0),
            color = BLUE)
        )

        # I could've writen dot2 like this line below
        dot2 = always_redraw(
            lambda: Dot(
                axes.c2p(
                    tracker.get_value(),
                    0
                ),
                color=BLUE,
            )
        )

        label2 = always_redraw(
            lambda: Text(f"x ={tracker.get_value():.1f}",
            color=BLUE,
            font_size=24)
            .next_to(axes.c2p(tracker.get_value(), 0), UP)
        )

        self.add(dot2, label2)
        self.wait(0.5)

        self.play(tracker.animate.set_value(4),
            run_time=2,
            rate_func=linear
        )
        self.wait(1)

        self.play(FadeOut(dot2), FadeOut(title2), FadeOut(label2), run_time=0.5)

        # manim Pr32_tracker_updater.py Manim32 --renderer=opengl -p
        # manim -pqk Pr32_tracker_updater.py Manim32
        # manim -pqh Pr32_tracker_updater.py Manim32
