from manim import *
from manim.opengl import *

class OpenGLIntro(Scene):
    def construct(self):
        hello_world = Tex("Hello World")
        self.play(Write(hello_world))
        self.play(
            self.camera.animate.set_euler_angles(
                theta=-10 * DEGREES,
                phi=50*DEGREES
            )
        )

        self.play(FadeOut(hello_world))