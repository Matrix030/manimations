from manim import *

class MemoryStackStatic(Scene):
    def construct(self):
        # 1) Title
        title = Text("Memory", font_size=20).to_edge(UP)
        self.play(Write(title))
        # 2) Block factories
        def memory_block(text, height=0.6):
            rect = Rectangle(width=4, height=height)
            label = Text(text, font_size=24).move_to(rect.get_center())
            return VGroup(rect, label)

        def gap_block(height=0.3):
            rect = Rectangle(width=4, height=height)
            return DashedVMobject(rect, num_dashes=20)

        # 3) Build & position the stack
        blocks = VGroup(
            memory_block("entry point"),
            gap_block(),
            memory_block("Instr n+1"),
            memory_block("Instr n+2"),
            gap_block(),
            memory_block("return instr."),
            gap_block(),
            memory_block("ISR entry pt."),
            gap_block(),
            memory_block("ISR instr i"),
            memory_block("ISR instr i+1"),
            gap_block(),
            memory_block("ISR ret instr"),
        ).arrange(DOWN, buff=0.1)\
         .next_to(title, DOWN, buff=0.1)\
         .scale(0.8).shift(UP * 0.6)
        
        self.play(FadeIn(blocks))
        brace1 = Brace(blocks[0:5], direction=RIGHT)
        brace_text1 = Text("A Running Program", font_size=20)
        brace_label1 = brace_text1.next_to(brace1, RIGHT)
        self.play(Create(brace1), Write(brace_label1), run_time=0.5)
        self.wait()

        brace2 = Brace(blocks[7:], direction=RIGHT)
        brace_text2 = Text("Interrupt Service Routine", font_size=20)
        brace_label2 = brace_text2.next_to(brace2, RIGHT)
        self.play(Create(brace2), Write(brace_label2), run_time=0.5)
        self.wait()

        # self.play(Create(brace), Write(brace_label))

        interrupt_text = Text("An interrupt takes place", font_size=20).next_to(blocks[2], LEFT, buff=1)

        arrow1 = Arrow(
            interrupt_text.get_right(),
            blocks[2].get_left(),
            buff=0.1
        ).set_color(RED)

        self.play(Write(interrupt_text))
        self.play(Create(arrow1), run_time=1)
        self.wait()
        
        start = blocks[2].get_left() + DOWN * 0.1
        end = blocks[7].get_left()
        arrow2 = CurvedArrow(start, end, angle=PI).set_color(RED)
        label = Text("Start Executing \n an ISR", font_size=20)
        label.next_to(blocks[7].get_left()).shift(LEFT * 3.5)
        self.play(Create(arrow2),Create(label), run_time=1)
        self.play(FadeOut(brace2), FadeOut(brace_label2),FadeOut(brace1), FadeOut(brace_label1), run_time=0.8)
        self.wait()

        start2 = blocks[12].get_right()
        end2 = blocks[3].get_right()
        arrow3 = CurvedArrow(start2, end2, angle=PI).set_color(BLUE)
        label = Text("Return to the \n previous Execution", font_size=20)
        label.next_to(blocks[3].get_right()).shift(RIGHT * 1.5)
        self.play(Create(arrow3),Create(label), run_time=1)
        self.wait()


        

