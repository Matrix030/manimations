from manim import *

class PositioningDemo(Scene):
    def construct(self):
        circle = Circle().set_color(RED)
        square = Square().set_color(BLUE)
        triangle = Triangle().set_color(GREEN)

        #Positioning

        square.next_to(circle, RIGHT)
        triangle.next_to(circle, LEFT)

        self.play(Create(circle), Create(square), Create(triangle))
        self.wait()

        #Group and move together

        group = VGroup(circle, square, triangle)
        self.play(group.animate.shift(LEFT * 2))
        self.wait()