from manim import *

class DotOnParabola(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-3, 3],
            y_range=[0, 9],
            x_length=7,
            y_length=5,
            axis_config={"include_numbers": True},
        )

        self.play(Create(axes))

        graph = axes.plot(lambda x: x**2, color=BLUE)
        self.play(Create(graph))

        x_tracker = ValueTracker(-3)
        dot = always_redraw(
            lambda: Dot(axes.coords_to_point(x_tracker.get_value(), x_tracker.get_value()**2), color=RED)
        )

        # Label showing dynamic (x, y)
        label = always_redraw(
            lambda: MathTex(
                f"x = {x_tracker.get_value():.2f}, y = {x_tracker.get_value()**2:.2f}"
            ).next_to(dot, UP)
        )

        self.add(dot, label)
        self.play(x_tracker.animate.set_value(3), run_time=5, rate_func=linear)
        self.wait()