from manim import *
import numpy as np

class SHM(Scene):
    def construct(self):

        # create axes
        axes = Axes(
            x_range=[0, 2*PI, PI/2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=8,
            y_length=4,
            axis_config={"color":WHITE}
        )

        # axes labels
        labels = axes.get_axis_labels("t", "x(t)")

        # sine curve
        sine = axes.plot(
            lambda x: np.sin(x),
            color=BLUE
        )

        # sine label
        sine_label = axes.get_graph_label(
            sine,
            r"\sin(t)",
            color=BLUE,
            x_val=6
        )
        sine_label.scale(0.7)

        dot = Dot(color=GRAY_BROWN)
        dot.move_to(axes.c2p(0,0))

        self.play(Create(axes), Write(labels))
        self.play(Create(sine), run_time=3)
        self.play(Write(sine_label))
        self.add(dot)
        self.play(MoveAlongPath(dot,sine),run_time=3, rate_func=linear)
        self.wait(1)

        # manim Pr21_SHM.py Manim21 --renderer=opengl -p
        # manim -pqk Pr21_SHM.py Manim21