from manim import *
import numpy as np

class SineWave(Scene):
    def construct(self):
        # 1) Display the equation y = sin(x)
        equation = MathTex(r"y = \sin(x)").scale(2)
        self.play(Write(equation))
        self.wait(1)

        # 2) Set up the axes
        axes = Axes(
            x_range=[0, 2 * PI, PI/2],
            y_range=[-1.5, 1.5, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": False, "include_tip": False},
        ).scale(2)

        # 3) Create a ValueTracker to control the phase shift
        phase = ValueTracker(0)

        # 4) Define a dynamically updating sine curve: y = sin(x − phase)
        sine_curve = always_redraw(
            lambda: axes.plot(
                lambda x: np.sin(x - phase.get_value()),
                x_range=[0, 2 * PI],
                color=YELLOW
            )
        )

        # 5) Transform the equation into the sine-curve while drawing the axes
        self.play(
            Create(axes),
            ReplacementTransform(equation, sine_curve),
        )
        self.wait(0.5)

        # 6) Animate the wave “moving” by shifting its phase from 0 to 2π over 3 seconds
        self.play(phase.animate.set_value(10 * PI), run_time=3, rate_func=linear)
        self.wait()