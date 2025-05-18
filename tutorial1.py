from manim import *

class TrianglePlay(Scene):
    def construct(self):
        triangle = Triangle().set_color(RED)
        self.play(GrowFromCenter(triangle))
        self.wait(1)
        self.play(FadeOut(triangle))