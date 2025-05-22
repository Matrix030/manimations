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

        linear_function = axes.plot(lambda x: 2*x+1, color=YELLOW)
        label = axes.get_graph_label(linear_function, label="linear Function")
        self.play(Create(axes), Create(linear_function), Write(label))
        self.wait()