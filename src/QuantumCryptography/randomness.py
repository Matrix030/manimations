from manim import *

class RandomnessScreen(Scene):
    def construct(self):
        # 1) Title
        title = Text("Randomness", font_size=72, color=RED)
        title.to_edge(UP + LEFT)
        self.play(Write(title), run_time=1)

        # 2) Two lines of coin‐flip text
        seq1 = "HHTHTTTHHTHTHTHTTTHHHTTTHTHTHTHTTTHH"
        seq2 = "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"
        line1 = Text(seq1, font="Consolas", font_size=24, color=PURPLE)
        line2 = Text(seq2, font="Consolas", font_size=24, color=PURPLE)
        line1.next_to(title, DOWN, aligned_edge=LEFT, buff=0.5)
        line2.next_to(line1, DOWN, aligned_edge=LEFT, buff=0.2)
        self.play(Write(line1), Write(line2), run_time=1.5)

        # 3) Probability formula with split components
        prob = MathTex(
            r"\mathrm{Prob}", "[", "T", "]", "=",
            r"\mathrm{Prob}", "[", "H", "]", "=", r"\tfrac{1}{2}"
        ).scale(1.2)
        # prob.to_corner(UR)
        self.play(Write(prob[0:9]), run_time=1)

        # 5) Isolated LaTeX "H" from within the equation
        prob_H = prob[7].copy()  # this is the "H"
        prob_T = prob[2].copy()

        # Transform all 'H's in line1
        indices_of_H = [i for i, c in enumerate(seq1) if c == "H"]
        indices_of_T = [i for i, c in enumerate(seq1) if c == "T"]
        transforms_H = [
            Transform(line1.submobjects[i], prob_H.copy())
            for i in indices_of_H
        ]

        transforms_T = [
            Transform(line1.submobjects[i], prob_T.copy())
            for i in indices_of_T
        ]
        self.play(*transforms_H, *transforms_T, run_time=2)
        # 7) Animate the appearance of "\tfrac{1}{2}" after the transforms
        self.play(Write(prob[9:]), run_time=1)

        # 8) Hold final frame
        self.wait(2)
