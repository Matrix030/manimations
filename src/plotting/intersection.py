from manim import *
from scipy.optimize import fsolve

class AutoIntersection(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1, 3],
            y_range=[-1, 3],
            axis_config={"include_numbers": True},
        )

        f1 = lambda x: x*x*x
        f2 = lambda x: -x + 2

        # Find x where f1(x) == f2(x)
        x_intersect = fsolve(lambda x: f1(x) - f2(x), 0)[0]
        y_intersect = f1(x_intersect)

        # Convert to scene point
        dot = Dot(axes.coords_to_point(x_intersect, y_intersect), color=RED)
        label = MathTex(f"({x_intersect:.1f},\ {y_intersect:.1f})").next_to(dot, UP).move_to(LEFT).scale(0.5)

        graph1 = axes.plot(f1, color=BLUE)
        graph2 = axes.plot(f2, color=GREEN)

        self.play(Create(axes), Create(graph1), Create(graph2))
        self.play(FadeIn(dot), Write(label))
        self.wait()
