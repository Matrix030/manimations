from manim import *

import numpy as np

class SineLabel(Scene):
    def construct(self):
        # Create axes with range [0, 2π]
        axes = Axes(
            x_range=[0, 2 * np.pi],
            y_range=[-1.5, 1.5],
            x_length=8,
            y_length=4,
            axis_config={"include_numbers": True},
        )


    # Plot sin(x)
        graph = axes.plot(lambda x: np.sin(x), color=BLUE)

        x_val = np.pi
        y_val = np.sin(x_val)

        dot = Dot(axes.coords_to_point(x_val, y_val), color=RED)
        label = MathTex(r"(\pi,\ 0)").next_to(dot, UP).move_to(UP)

        # Animate
        self.play(Create(axes), Create(graph))
        self.play(FadeIn(dot), Write(label))
        self.wait()