from manim import *
import numpy as np

class ProjectHailMaryCentrifuge(Scene):
    def construct(self):
        # --- 1. Design the Ship Sections ---

        # Engine Section (The "Fuel/Thrust" end)
        # Using Polygon to create the tapered trapezoid look from your image
        engine_shape = Polygon(
            [-1.0, 0.8, 0], [1.0, 0.8, 0],  # Wide engine base
            [0.5, -0.8, 0], [-0.5, -0.8, 0], # Tapered neck
            color=GREY_B, fill_opacity=1
        )
        # Add the three distinct engine bells at the bottom
        bells = VGroup(*[
            Circle(radius=0.25, color=DARK_GREY, fill_opacity=1).move_to([x, 0.8, 0])
            for x in [-0.6, 0, 0.6]
        ])
        engine_section = VGroup(engine_shape, bells).rotate(PI/2).shift(LEFT * 0.5)

        # Lab Section (The "Crew/Nose" end)
        # Pointy nose and cylindrical body
        lab_shape = Polygon(
            [-0.6, 0.4, 0], [0.6, 0.4, 0],   # Rear of lab
            [0.6, -0.4, 0], [1.2, -0.8, 0],  # Nose cone point
            [-0.6, -0.4, 0],
            color=BLUE_B, fill_opacity=0.8
        )
        lab_section = VGroup(lab_shape).rotate(PI/2).next_to(engine_section, RIGHT, buff=0)

        # --- 2. Initial State: Thrust Mode ---
        mode_label = Text("THRUST MODE", font_size=32).to_edge(UP)
        gravity_arrow = Arrow(start=RIGHT, end=LEFT, color=YELLOW).next_to(mode_label, DOWN)
        gravity_text = Text("Artificial Gravity Direction", font_size=20).next_to(gravity_arrow, DOWN)

        self.add(engine_section, lab_section, mode_label, gravity_arrow, gravity_text)
        self.wait(2)

        # --- 3. Transition: Cables Extend ---
        self.play(
            FadeOut(gravity_arrow),
            FadeOut(gravity_text),
            mode_label.animate.set_text("TRANSITION: CABLES EXTEND")
        )

        # Create tether lines that "grow" as the lab moves
        tethers = always_redraw(lambda: VGroup(
            Line(engine_section.get_right() + UP*0.2, lab_section.get_left() + UP*0.2, color=WHITE, stroke_width=1.5),
            Line(engine_section.get_right() + DOWN*0.2, lab_section.get_left() + DOWN*0.2, color=WHITE, stroke_width=1.5)
        ))

        self.add(tethers)
        self.play(lab_section.animate.shift(RIGHT * 4), run_time=3)
        self.wait(1)

        # --- 4. Transition: Crew Section Rotates 180° ---
        # In the book, the lab flips so the "floor" faces away from the center of rotation
        self.play(mode_label.animate.set_text("LAB ROTATES 180°"))
        self.play(Rotate(lab_section, angle=PI), run_time=2)
        self.wait(1)

        # --- 5. Centrifuge Mode: 3 Resolutions (Rotations) ---
        self.play(mode_label.animate.set_text("CENTRIFUGE CONFIGURATION (3 Rotations)"))

        # Group everything and define the Center of Mass (COM) for the spin
        whole_ship = VGroup(engine_section, lab_section, tethers)
        center_of_mass = Dot(point=engine_section.get_right() + RIGHT*1.5, color=RED) # Anchor point

        # Perform 3 full rotations (6 * PI)
        self.play(
            Rotate(
                whole_ship,
                angle=2 * PI * 3,
                about_point=center_of_mass.get_center(),
                rate_func=linear
            ),
            run_time=8
        )

        self.wait(2)
