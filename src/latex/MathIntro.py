from manim import *

class MathIntro(Scene):
    def construct(self):
        eq1 = MathTex(r"E = mc^2")
        eq2 = MathTex(r"\lim_{x \to 0} \frac{\sin x}{x} = 1")
        eq3 = MathTex(r"\int_0^1 x^2 dx")
        eq4 = MathTex(r"a^2", "+", r"b^2", "=", r"c^2")
        eq4.set_color_by_tex("a^2", RED)
        eq4.set_color_by_tex("b^2", GREEN)
        eq4.set_color_by_tex("c^2", BLUE)
        eq2.next_to(eq1, DOWN)
        eq3.next_to(eq2, DOWN)
        eq4.next_to(eq3, DOWN)
        group = VGroup(eq1, eq2, eq3, eq4)
        group.move_to(ORIGIN)

        self.play(Write(group))
        self.wait()

