from manim import *

class HeaderFooter(Scene):
    def construct(self):
        header = Text("Lecture 1: Limits").to_edge(UP)
        footer = Text("Prof. Calculus").scale(0.5).to_edge(DOWN).set_opacity(0.5)

        self.play(Write(header), Write(footer))

        self.wait()

        