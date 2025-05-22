from manim import *

class HelloWorld(Scene):
    def construct(self):
        circle = Circle()
        text = Text("Hello World", font_size=72)
        text.to_edge(UP)

        self.play(Write(text), run_time=1)

        # Get index of first "H"
        index_of_H = text.text.find("H")
        letter_H = text.submobjects[index_of_H]

        self.play(Transform(letter_H, circle))
