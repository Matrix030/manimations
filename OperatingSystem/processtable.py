from manim import *

class FDTable(Scene):
    def construct(self):
        # Headers
        headers = VGroup(
            Text("PID").scale(0.5),
            Text("FD0").scale(0.5),
            Text("FD1").scale(0.5),
            Text("FD2").scale(0.5)
        ).arrange(RIGHT, buff=1).to_edge(UP)

        # Rows
        row1 = VGroup(
            Text("101").scale(0.5),
            Text("/dev/stdin").scale(0.5),
            Text("/dev/stdout").scale(0.5),
            Text("/dev/stderr").scale(0.5)
        ).arrange(RIGHT, buff=1)

        row2 = VGroup(
            Text("102").scale(0.5),
            Text("/dev/stdin").scale(0.5),
            Text("out.log").scale(0.5),
            Text("err.log").scale(0.5)
        ).arrange(RIGHT, buff=1)

        table = VGroup(headers, row1, row2).arrange(DOWN, buff=0.7)

        self.play(Write(table))
        self.wait(1)
