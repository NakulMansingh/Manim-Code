# sine cosine exponential
import numpy as np
from manim import *

class Exp(Scene):
    def construct(self):

        # create axes
        axes = Axes(
            # x_range = [-9, 9, 1],
            x_range = [-2.5, 2.5, 4.5],
            y_range = [-5, 5, 1],
            x_length= 10,
            y_length= 5,
            axis_config={"color": WHITE}
        )

        # add labels to axes
        labels = axes.get_axis_labels(
            x_label="t",
            y_label="f(t)",
        )
        labels.scale(1)

        self.play(Create(axes), Write(labels))

        # title
        # title = Text("Sine", color=RED, run_time=3, font_size=40)
        # title.move_to(UP*3)

        # sine_curve = axes.plot(
        #     lambda x: np.sin(x),
        #     color=RED
        # )

        # cosine_curve = axes.plot(
        #     lambda x: np.cos(x),
        #     color=DARK_BLUE,
        # )

        exp_curve = axes.plot(
            lambda x: np.exp(x),
            x_range=[-2.5, 2],
            color=GRAY_BROWN
        )

        # sine_label = axes.get_graph_label(
        #     sine_curve,
        #     label=r"\sin(t)",
        #     x_val=2,
        #     color=RED,
        # )

        # cosine_label = axes.get_graph_label(
        #     cosine_curve,
        #     label=r"\cos(t)",
        #     x_val=4,
        #     color=BLUE,
        # )

        exp_label = axes.get_graph_label(
            exp_curve,
            label=r"\ e^t}",
            x_val=1,
            color=GRAY_BROWN
        )

        # sine_label.scale(0.6)

        # cosine_label.scale(0.6)

        exp_label.scale(0.8)

        # self.play(Create(sine_curve), run_time=3)
        # self.play(Write(sine_label))
        # self.wait(1)

        # self.play(Create(cosine_curve), run_time=3)
        # self.play(Write(cosine_label))
        # self.wait(1)

        self.play(Create(exp_curve), run_time=3)
        self.play(Write(exp_label))
        self.wait(1)


        # manim Pr20_sin_cos_exp.py Manim20 --renderer=opengl -p
        # manim -pqk Pr20_sin_cos_exp.py Manim20
        