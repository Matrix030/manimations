from manim import *

class SineWave(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 2*PI, PI/2],
            y_range=[-1.5, 3, 1],
            x_length=2,
            y_length=6,
            axis_config={"include_numbers": False},
        )

        sine = axes.plot(lambda x: np.sin(x), color=YELLOW)
        label = axes.get_graph_label(sine, label="\\sin x")

        self.play(Create(axes), Create(sine), Write(label))
        self.wait()