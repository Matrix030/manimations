from manim import *

class BasicPlot(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range = [0, 9, 1],
            tips= False,
            x_length = 6,
            y_length = 4,
            axis_config={'color': GREY, 'include_numbers': True}
        )

        parabola = axes.plot(lambda x: x**2, color=BLUE)

        # label = axes.get_graph_label(parabola, label= "x^2")
        text = Text('x^2').to_edge(DOWN)
        self.play(Create(axes), Create(parabola), FadeIn(text))
        # self.play(FadeIn(Write(text)))
        self.wait()