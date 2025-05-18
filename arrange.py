from manim import *

class ArrangeDemo(Scene):
    def construct(self):
        a = Circle().set_color(RED)
        b = Square().set_color(BLUE)
        c = Triangle().set_color(GREEN)

        group =  VGroup(a, b, c)
        group.arrange(DOWN).to_edge(RIGHT)

        self.play(Create(group))
        self.wait()

        a2 = Circle().set_color(RED)
        b2 = Square().set_color(BLUE)
        c2 = Triangle().set_color(GREEN)

        group =  VGroup(a2, b2, c2)
        group.arrange(DOWN).to_edge(LEFT)

        self.play(Create(group))
        self.wait()