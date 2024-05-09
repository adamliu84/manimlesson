from manim import *


class TargetExample(Scene):
    def construct(self):
        source_left = Dot()
        source_right = source_left.copy()

        VGroup(source_left, source_right).arrange(RIGHT, buff=3)
        source_left.save_state()

        # Left side - MoveToTarget ----------------
        source_left.generate_target()
        # Manupulate the .target attr
        source_left.target.set_style(
            fill_color=TEAL,
            stroke_width=10,
            stroke_color=ORANGE
        )
        source_left.target.scale(7)
        source_left.target.to_edge(UP)
        # # Right side - Manually ----------------
        # source_right_target = source_right.copy()
        # source_right_target.set_style(
        #     fill_color=TEAL,
        #     stroke_width=10,
        #     stroke_color=ORANGE
        # )
        # source_right_target.scale(7)
        # source_right_target.to_edge(UP)

        # Animations
        self.add(source_left, source_right)
        self.play(
            MoveToTarget(source_left),
            # Transform(source_right, source_right_target),
            run_time=3
        )
        self.wait()
        self.play(Restore(source_left))


class ApplyFunctionExample(Scene):
    def construct(self):
        import random
        def getScaleRandom(): return random.randint(1, 5)
        source = VGroup(Dot(), Square(), Circle(), Text("A"))\
            .arrange(RIGHT, buff=2)

        self.add(source)

        self.play(
            ApplyFunction(self.custom_method(
                scale=getScaleRandom(), edge=DOWN), source[0]),  # Dot
            ApplyFunction(self.custom_method(
                scale=getScaleRandom(),
                fill_color=PURPLE), source[1]),  # Square
            ApplyFunction(self.custom_method(
                scale=getScaleRandom(),
                fill_opacity=0),    source[2]),  # Circle
            ApplyFunction(self.custom_method(
                scale=getScaleRandom(),
                edge=LEFT),
                source[3]),  # Text("A")
            run_time=3
        )
        self.wait()

    def custom_method(self,
                      fill_color=TEAL,
                      fill_opacity=1,
                      stroke_width=10,
                      stroke_color=ORANGE,
                      scale=3,
                      edge=UP,
                      ):
        def custom_func(mob):
            mob.set_style(
                fill_color=fill_color,
                fill_opacity=fill_opacity,
                stroke_width=stroke_width,
                stroke_color=stroke_color,
            )
            mob.scale(scale)
            mob.to_edge(edge)
            # Don't forget return mob
            return mob
        # Don't forget return the func
        return custom_func


class ApplyFunctionVGroupExample(Scene):
    def construct(self):
        source = VGroup(Dot(), Square(), Circle(), Text("A"))\
            .arrange(RIGHT, buff=2)

        self.add(source)

        self.play(
            ApplyFunction(self.custom_method(), source),
            run_time=3
        )
        self.wait()

    def custom_method(self,
                      fill_color=TEAL,
                      fill_opacity=1,
                      stroke_width=10,
                      stroke_color=ORANGE,
                      scale=3,
                      edge=UP,
                      ):

        def vgroup_func(vgrp):
            import random
            def getScaleRandom(): return random.randint(1, 10)
            d, s, *other = vgrp
            vgrp.set_style(
                fill_color=fill_color,
                fill_opacity=fill_opacity,
                stroke_width=stroke_width,
                stroke_color=stroke_color,
            )
            d.scale(getScaleRandom())
            s.scale(getScaleRandom()/10)
            s.set_color(PINK)
            VGroup(*other).set_color(WHITE)
            # Don't forget return mob
            return vgrp
        # Don't forget return the func
        return vgroup_func


class AnimateVGroupExample(Scene):
    def construct(self):
        square = Square(side_length=2)
        circle = Circle(radius=1)
        triangle = Triangle()
        rectange = Rectangle()

        shapeGroup = VGroup(square, circle, triangle, rectange)
        shapeGroup.save_state()
        self.play(shapeGroup.animate
                  .scale(2)
                  .arrange_in_grid(col=2, flow_order="dr")
                  .set_style(fill_opacity=1, fill_color=PINK, stroke_color=WHITE),)
        self.wait()
        self.play(Restore(shapeGroup))
        self.wait()


class RotationExample(Scene):

    def generateTipTriangleGroup(self):
        wholeTriangle = Triangle()
        triangleTip = Triangle(
            fill_color=GOLD, fill_opacity=1, stroke_opacity=0).scale(0.2)
        triangleTip.align_to(wholeTriangle, UP)
        return VGroup(wholeTriangle, triangleTip)

    def construct(self):
        angles = [10, 30, 60, 90, 120, 180]
        # mobs = VGroup(*[
        #     VGroup(MathTex(f"{angle}^\\circ"), Square())
        #     .arrange(DOWN, buff=1)
        #     for angle in angles
        # ]).arrange(RIGHT, buff=0.7)
        mobs = VGroup(*[
            VGroup(MathTex(f"{angle}^\\circ"), self.generateTipTriangleGroup())
            .arrange(DOWN, buff=1)
            for angle in angles
        ]).arrange(RIGHT, buff=0.7)
        mobs.save_state()
        self.add(mobs)

        '''
        You can see that the greater the angle, the more deformed the rotation.
        This is because, what happens in reality,
        is that the squares are transformed to another square already rotated,
        that is, the rotations are not continuous,
        but it is a simple transformation between two states.
        To solve this we can use Rotating:
        '''
        self.play(
            *[
                # mob[0] is the MathTex and
                # mob[1] is the Square()
                mob[1].animate.rotate(angle*PI/180)
                for mob, angle in zip(mobs, angles)
            ],
            run_time=3
        )
        self.wait()

        # RESTORE without animation
        self.next_section(skip_animations=True)  # Halt animation
        self.play(Restore(mobs))
        self.next_section()  # "Force" Re-Render
        self.wait()

        # Using Rotating class
        self.play(
            *[
                # mob[0] is the MathTex and
                # mob[1] is the Square()
                Rotating(mob[1], radians=angle*PI/180)
                for mob, angle in zip(mobs, angles)
            ],
            run_time=3
        )
        self.wait()
