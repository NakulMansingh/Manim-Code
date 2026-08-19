from manim import *
class Einstein(Scene):
    def construct(self):

        eq1 = MathTex(r"E=mc^2", color=BLUE).scale(2)
        eq1.move_to(UP*1)
        tx1 = Text("Mass can be converted into energy?", color=BLUE, )
        tx1.move_to(DOWN*1)
        
        eq2 = MathTex(r"m=\frac{E}{c^2}", color=GRAY_BROWN).scale(2)
        eq2.move_to(UP*1)
        tx2 = Text("Mass is a manifestion of energy!", color=GRAY_BROWN)
        tx2.move_to(DOWN*1)

        self.play(
            FadeIn(eq1),
            FadeIn(tx1), run_time=1
            )
        self.wait(2)

        self.play(
            ReplacementTransform(eq1, eq2),
            ReplacementTransform(tx1, tx2),
            run_time=(3)
        )
        self.wait(2.5)

        self.play(FadeOut(eq2), FadeOut(tx2), run_time=1)

            # MathTex(r"E = mc^2")                          # E = mc²
            # MathTex(r"m = \frac{E}{c^2}")                 # m = E/c²
            # MathTex(r"v = \sqrt{\frac{2E}{m}}")           # v = √(2E/m)
            # MathTex(r"\Delta E = \frac{hc}{\lambda}")     # ΔE = hc/λ
            # MathTex(r"F = \frac{Gm_1 m_2}{r^2}")          # F = Gm₁m₂/r²
            # MathTex(r"\int_0^\infty e^{-x} dx")           # ∫₀^∞ e^(-x) dx
            # MathTex(r"\sum_{n=1}^{\infty} \frac{1}{n^2}") # Σ 1/n²

        # manim Pr34_emc2.py Manim34 --renderer=opengl -p
        # manim -pqk Pr34_emc2.py Manim34