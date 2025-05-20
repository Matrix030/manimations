from manim import *

class ComplexExponentialVisualization(ThreeDScene):
    def construct(self):
        # Set background to parchment-white
        self.camera.background_color = "#FFFAF0"
        
        # Create axes - moved down by shifting the origin
        axes = ThreeDAxes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2.5, 2.5, 1],
            z_range=[0, 4, 1],
            x_length=5,
            y_length=5,
            z_length=4.5,  # Slightly shorter z-axis
            axis_config={"color": BLACK, "stroke_width": 1}
        ).shift(DOWN * 1)  # Move the entire axes system down
        
        # Create the unit circle - also shifted down
        circle = ParametricFunction(
            lambda t: np.array([np.cos(PI * t), np.sin(PI * t), 0]),
            t_range=[0, 4, 0.01],
            color=BLACK,
            stroke_width=4,
        ).shift(DOWN * 1)  # Apply the same shift as axes
        
        # Formula in the upper right
        formula = MathTex(
            r"z = e^{t\pi i}, \quad t \in [0,4]",
            color=BLACK
        ).scale(0.8).to_corner(UR)
        
        # Stage 1: 2D setup - start with head-on view
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)
        self.add_fixed_in_frame_mobjects(formula)
        
        self.play(Create(axes), run_time=1.5)
        self.play(Create(circle), run_time=2)
        self.wait()
        
        # Remove formula from fixed frame before camera moves
        self.remove_fixed_in_frame_mobjects(formula)
        self.add(formula)
        
        # Stage 2: Transform to 3D spiral - also shifted down
        spiral = ParametricFunction(
            lambda t: np.array([np.cos(PI * t), np.sin(PI * t), t]),
            t_range=[0, 4, 0.01],
            color=BLACK,
            stroke_width=4,
        ).shift(DOWN * 1)  # Apply the same shift as axes
        
        self.play(ReplacementTransform(circle, spiral), run_time=2)
        self.wait()
        
        # Stage 3: Camera animation - with adjusted viewing angle
        self.begin_ambient_camera_rotation(rate=0.1)
        # Adjust initial camera tilt to keep axes in view
        self.move_camera(phi=55 * DEGREES, frame_center=DOWN*0.5, run_time=4)
        self.wait(2)
        
        # Create projections onto the axes - also shifted down
        cos_projection = ParametricFunction(
            lambda t: np.array([np.cos(PI * t), 0, t]),
            t_range=[0, 4, 0.01],
            color=BLACK,
            stroke_width=2,
        ).shift(DOWN * 1)  # Apply the same shift as axes
        
        sin_projection = ParametricFunction(
            lambda t: np.array([0, np.sin(PI * t), t]),
            t_range=[0, 4, 0.01],
            color=BLACK,
            stroke_width=2,
        ).shift(DOWN * 1)  # Apply the same shift as axes
        
        # Add projections
        self.play(
            Create(cos_projection),
            Create(sin_projection),
            run_time=3
        )
        
        # Create dashed lines connecting spiral to projections - with adjusted positions
        num_points = 8
        dashed_lines = VGroup()
        for t in np.linspace(0, 4, num_points):
            # Base points
            base_spiral = np.array([np.cos(PI * t), np.sin(PI * t), t])
            base_cos = np.array([np.cos(PI * t), 0, t])
            base_sin = np.array([0, np.sin(PI * t), t])
            
            # Shifted points
            point_on_spiral = base_spiral + np.array([0, 0, 0]) + DOWN * 1
            point_on_cos = base_cos + np.array([0, 0, 0]) + DOWN * 1
            point_on_sin = base_sin + np.array([0, 0, 0]) + DOWN * 1
            
            line1 = DashedLine(
                point_on_spiral, point_on_cos,
                color=BLACK, stroke_width=1
            )
            line2 = DashedLine(
                point_on_spiral, point_on_sin,
                color=BLACK, stroke_width=1
            )
            dashed_lines.add(line1, line2)
        
        self.play(Create(dashed_lines), run_time=2)
        self.wait()
        
        # Stop camera rotation
        self.stop_ambient_camera_rotation()
        
        # Show the projections as sine/cosine waves - adjust frame center
        self.move_camera(phi=0, theta=0, frame_center=DOWN*0.5, run_time=4)
        self.wait()
        
        # Add labels for projections
        cos_label = MathTex(
            r"\Re(e^{i\pi t})=\cos(\pi t)",
            color=BLACK
        ).scale(0.7)
        
        sin_label = MathTex(
            r"\Im(e^{i\pi t})=\sin(\pi t)",
            color=BLACK
        ).scale(0.7)
        
        self.add_fixed_in_frame_mobjects(cos_label, sin_label)
        cos_label.next_to(axes.x_axis, DOWN)
        sin_label.to_edge(LEFT)
        
        self.play(
            Write(cos_label),
            Write(sin_label),
            run_time=2
        )
        
        # Final view to see the unfolded sine wave - with adjusted frame center
        self.move_camera(phi=80 * DEGREES, theta=0, frame_center=DOWN*0.5, run_time=3)
        self.wait(2)


if __name__ == "__main__":
    config.background_color = "#FFFAF0"  # parchment-white
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_rate = 30
    
    scene = ComplexExponentialVisualization()
    scene.render()