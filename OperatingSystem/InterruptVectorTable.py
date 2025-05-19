from manim import *

class MemoryStack(Scene):
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
         .next_to(title, DOWN, buff=0.4)\
         .scale(0.8)

        self.play(FadeIn(blocks))

        # 4) "Interrupt takes place" arrow
        interrupt_text = Text("An interrupt takes place", font_size=20)\
                            .next_to(blocks[2], LEFT, buff=1)
        arrow1 = Arrow(
            interrupt_text.get_right(),
            blocks[2].get_left(),
            buff=0.1
        ).set_color(BLUE)

        self.play(Write(interrupt_text))
        self.play(Create(arrow1), run_time=2)
        self.wait()
        
        # 5) Curved L-shaped blue arrow with smaller arrowhead
        # Define key points
        start_point = blocks[2].get_left()  # Start at left edge of "Instr n+1"
        left_point = start_point + LEFT * 1  # Far left point
        left_mid = start_point + LEFT * 1  # Midpoint for curve
        down_point = left_point + DOWN * (blocks[7].get_y() - blocks[2].get_y())  # Bottom left corner
        down_mid = down_point + DOWN * 4  # Midpoint for vertical curve
        end_point = blocks[7].get_left()  # End at "ISR entry pt."
        
        # Create a path with points for smooth curve
        path = VMobject()
        path.set_points_smoothly([
            start_point,
            down_mid,
            end_point
        ])
        path.set_color(BLUE)
        
        # Create a small arrowhead
        arrow_tip = Arrow(
            end_point + LEFT * 0.15,  # Smaller offset for smaller arrow
            end_point,
            buff=0,
            max_tip_length_to_length_ratio=0.2,  # Smaller tip
            max_stroke_width_to_length_ratio=1.5
        ).set_color(BLUE)
        
        # Animate the curved L-arrow
        self.play(Create(path), run_time=2)
        self.play(Create(arrow_tip), run_time=0.5)
        
        self.wait(2)