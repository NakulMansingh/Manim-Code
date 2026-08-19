# Basic axes
import numpy as np
from manim import *

class AxesMe(Scene):
    def construct(self):

        # create axes
        axes = Axes(
            x_axis = [0, 10, 1],
            y_axis = [1, -1, 0.5],
            x_length= 7,
            y_length= 3,
            axis_config={"color": WHITE}
        )

        # add labels to axes
        labels = axes.get_axis_labels(
            x_label="t",
            y_label="x(t)",
        )
        labels.scale(1)

        self.play(Create(axes), Write(labels))

        # title
        # title = Text("Sine", color=RED, run_time=3, font_size=40)
        # title.move_to(UP*3)

        sine_curve = axes.plot(
            lambda x: np.sin(x),
            color=RED
        )

        sine_label = axes.get_graph_label(
            sine_curve,
            label=r"\sin(t)",
            x_val=2,
            color=RED,
        )
        sine_label.scale(0.6)

        self.play(Create(sine_curve), run_time=3)
        self.play(Write(sine_label))
        self.wait(1)

        # cosine_curve = axes.plot(
        #     lambda x: np.cos(x),
        #     color=DARK_BLUE,
        # )

        # cosine_label = axes.get_graph_label(
        #     cosine_curve,
        #     label=r"\cos(t)",
        #     x_val=-10,
        #     color=DARK_BLUE,
        # )

        # self.play(Create(cosine_curve), run_time=2)
        # self.play(Write(cosine_label))
        # self.wait(1)

        # dot = Dot(color=YELLOW)
        # dot.move_to(axes.c2p(0, np.sin(0)))

        # self.add(dot)

        # self.play(
        #     MoveAlongPath(dot, sine_curve), run_time=3
        # )

        # manim Pr19_basic_axes.py Manim19 --renderer=opengl -p
        # manim -pqk Pr19_basic_axes.py Manim19
        