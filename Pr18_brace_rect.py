    # Problem 18 — full derivation scene

# Build a real 3Blue1Brown style scene called NewtonsSecondLaw that:

# Shows title "Deriving F = ma" at the top
# Writes r"F", r"=", r"m", r"a" in the centre
# Uses Circumscribe on F
# Transforms to: r"a", r"=", r"\frac{", r"F", r"}{", r"m", r"}"`
# Adds brace below with label "acceleration"
# Boxes the final equation with SurroundingRectangle
# Fades everything out at the end

from manim import *
class Newt2ndLaw(Scene):
    def construct(self):
        title = Text("Newton's 2nd Law", color=RED)
        title.move_to(UP*2)
    
        eq1 = MathTex(r"F", r"=", r"m", r"a", run_time=3)
        eq2 = MathTex(r"a", r"=", r"\frac{", r"F", r"}{", r"m", r"}")
    
        self.play(Write(title), run_time=2)
        self.play(Write(eq1), run_time=2)
        self.wait(1)
    
        #Circumscibe # TempBox
        self.play(Circumscribe(eq1[0]))
        self.wait(1)
    
        #Transform
        self.play(TransformMatchingShapes(eq1,eq2), run_time=2)
        self.wait(1)
    
        # brace & label
        brace = Brace(eq2[0], direction=DOWN, color=BLUE)
        label = brace.get_text("acceleration").set_color(BLUE)
        self.play(GrowFromCenter(brace), Write(label))
        # self.play(Write(label))
        self.wait(1)
    
        rectbox = SurroundingRectangle(eq2, color=GRAY_BROWN, buff=0.2)
        self.play(Create(rectbox))
        self.wait(1)
    
        # manim Pr18_brace_rect.py Manim18 --renderer=opengl -p
        # manim -pqk Pr18_brace_rect.py Manim18
