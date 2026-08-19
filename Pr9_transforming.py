from manim import *
class TransformIt(Scene):
    def construct(self):

        circle = Circle(color=BLUE, fill_opacity=0.3)
        square = Square(color=RED, fill_opacity=0.3)
        triangle = Triangle(color=DARK_BROWN, fill_opacity=0.3)
        circle2 = Circle(color=WHITE, fill_opacity=0.3)
        label = Text("Transform", color=WHITE)
        label.next_to(circle, DOWN)

        self.play(GrowFromCenter(circle))
        self.play(Write(label))
        self.wait(0.5)

        self.play(
            ReplacementTransform(circle, square), FadeOut(label)
        )
        self.wait(0.5)

        self.play(ReplacementTransform(square, triangle))
        self.play(Indicate(triangle))
        self.play(triangle.animate.rotate(PI/4), run_time=2)
        self.wait(1)

        self.play(ReplacementTransform(triangle, circle2))
        self.play(ShrinkToCenter(circle2))
        self.play(0.5)

        # manim Pr9_transforming.py Manim9 --renderer=opengl -p
        # manim -pqk Pr9_transforming.py Manim9