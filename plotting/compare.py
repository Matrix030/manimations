from manim import *

class LinearFunction(Scene):
    def construct(self):
        axes = Axes(
            x_range = [-3, 3, 1],
            y_range = [-3, 3, 1],
            x_length = 5,
            y_length =  5,
            axis_config={'include_numbers': False}
        )

        function1 = axes.plot(lambda x: x*x, color=YELLOW)
        function2 = axes.plot(lambda x: x*x*x, color=RED)
        label1 = axes.get_graph_label(function1, label="x^2")
        label2 = axes.get_graph_label(function2, label ="x^3")
        self.play(Create(axes), Create(function1), Create(function2), Write(label1), Write(label2))
        self.wait()