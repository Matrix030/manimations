from manim import *

class EquationTransform(Scene):
    def construct(self):
        start = MathTex("x^2", "+", "2x", "+", "1")
        end = MathTex("(", "x", "+", "1", ")", "^2")

        self.play(Write(start))
        self.wait(1)
        self.play(TransformMatchingTex(start, end))
        self.wait(1)