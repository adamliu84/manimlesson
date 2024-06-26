from manim import *


class BasicTheoryExample(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        self.add(circle, square)
        self.wait()

        self.play(circle.animate.to_edge(LEFT))
        self.play(square.animate.next_to(circle, UP))
        # self.play(circle.animate.to_edge(RIGHT))

        def square_updater(mob):
            mob.next_to(circle, UP)
        square.add_updater(square_updater)
        self.add(circle, square)
        self.play(circle.animate.to_edge(LEFT))
        self.play(circle.animate.to_edge(RIGHT))

        # Pause updaters: Mobject.suspend_updating()
        # Restore updaters: Mobject.resume_updating()
        # Delete all updaters: Mobject.clear_updaters()
        square.suspend_updating()
        self.play(circle.animate.to_edge(LEFT))
        square.resume_updating()
        self.wait()
        self.play(circle.animate.to_edge(RIGHT))


class BecomeExample(Scene):
    def construct(self):
        tcircle = Circle()
        bcircle = Circle()
        group = VGroup(tcircle, bcircle).arrange_in_grid(buff=1)

        tsquare = Square()
        tsquare.move_to(tcircle)
        bsquare = Square()
        bsquare.move_to(bcircle)
        bcircle.generate_target()
        bcircle.target.become(bsquare)

        self.add(group)
        self.wait()
        self.play(Transform(tcircle, tsquare), MoveToTarget(bcircle))


class BraceLineExample(Scene):
    def construct(self):
        def get_brace(mob):
            mob.become(
                Brace(line, UP)
            )
        line = Line(LEFT, RIGHT)
        brace = VMobject()
        brace.add_updater(get_brace)
        self.add(line, brace)
        self.wait(0.5)
        self.play(line.animate.scale(3))
        self.wait(0.5)
        self.play(line.animate.scale(0.8))
        self.wait(0.5)
        self.play(line.animate.scale(1.3))
        self.remove(brace)

        def get_pointsBrace(mob):
            mob.become(
                BraceBetweenPoints(line.get_end(), line.get_start())
            )
        self.add(Text("Using BraceBetweenPoints").to_corner(UL))
        pointsBrace = BraceBetweenPoints(line.get_end(), line.get_start())
        pointsBrace.add_updater(get_pointsBrace)
        self.add(pointsBrace)
        self.wait(0.5)
        self.play(line.animate.rotate(75*DEGREES))
        self.wait(0.5)
        self.play(line.animate.scale(0.6))


class PutStartEndExample(Scene):
    def construct(self):
        start_dot = Dot(LEFT, color=RED)
        end_dot = Dot(RIGHT, color=TEAL)

        def update_line(mob):
            mob.put_start_and_end_on(
                start_dot.get_center(), end_dot.get_center())

        line = Line()  # Also it works with Arrow
        line.add_updater(update_line)

        self.add(line, start_dot, end_dot)
        self.wait(0.5)
        self.play(start_dot.animate.shift(LEFT*2+UP))
        self.wait(0.5)
        self.play(end_dot.animate.shift(RIGHT+DOWN*0.5))
        self.wait(0.5)
        self.play(
            start_dot.animate.shift(RIGHT*0.5+DOWN*2),
            end_dot.animate.shift(RIGHT+UP*3).scale(5)
        )
        self.wait(0.5)
        self.play(
            start_dot.animate.shift(LEFT*3).scale(5),
            end_dot.animate.shift(DOWN*2)
        )
        self.wait(0.5)
        self.play(start_dot.animate.shift(RIGHT*10),
                  end_dot.animate.shift(LEFT*10))


class ValueTrackerExample(Scene):
    def construct(self):
        nl = NumberLine(include_numbers=True)
        selector = Triangle(fill_opacity=1).scale(0.2).rotate(PI/3)
        vt = ValueTracker(0)
        dnd = DecimalNumber(0, num_decimal_places=0).to_corner(UL)

        def update_selector(mob):
            mob.next_to(nl.n2p(vt.get_value()), UP, buff=0)
            dnd.set_value(vt.get_value())
            #                  --------------
            #  In this way we can acces to the ValueTracker value

        selector.add_updater(update_selector)

        self.add(nl, selector, dnd)
        self.wait(0.5)
        self.play(
            vt.animate.set_value(4),
            run_time=2
        )
        self.wait(0.5)
        self.play(
            vt.animate.set_value(-1),
            run_time=2
        )
        self.wait(0.5)
        self.play(
            vt.animate.set_value(-7),
            run_time=2
        )
        self.wait(0.5)
        self.play(
            vt.animate.set_value(7),
            run_time=3
        )
        self.wait(0.5)
        # To disable triangle_selector updater from updating dnd value
        selector.remove_updater(update_selector)
        self.play(ChangeDecimalToValue(dnd, -5), run_time=2)
        self.wait(0.5)


class GroupUpdatersExample(Scene):
    def construct(self):
        nl = NumberLine(include_numbers=True)
        selector = Triangle(fill_opacity=1, color=RED).scale(0.2).rotate(PI/3)
        dn = DecimalNumber(0).next_to(selector, UP, buff=0.1)

        def update_vgrp(vgrp):
            s, d = vgrp
            s.next_to(nl.n2p(dn.get_value()), UP, buff=0)
            # d.next_to(selector, UP, buff=0.1)
            nDirection = UP if d.get_value() >= 0 else DOWN
            d.next_to(s, nDirection, buff=0.2)
        update_grp = VGroup(selector, dn)
        update_grp.add_updater(update_vgrp)

        self.add(nl, update_grp)  # <-- add grp complete, not each element
        # Not use self.add(nl, selecttor, dn)
        self.wait(0.5)
        self.play(
            ChangeDecimalToValue(dn, 4),
            run_time=2
        )
        self.wait(0.5)
        self.play(
            ChangeDecimalToValue(dn, -1),
            run_time=2
        )
        self.wait(0.5)
        self.play(
            ChangeDecimalToValue(dn, -4),
            run_time=2
        )
        self.wait(0.5)
        self.play(
            ChangeDecimalToValue(dn, 7),
            run_time=3
        )
        self.wait(0.5)


class ValueTrackerAssignment(Scene):
    def construct(self):

        angleTracker = DecimalNumber(130, num_decimal_places=0).to_corner(UR)
        self.add(angleTracker)

        # Moving Line/Axis
        moveline = Line(start=[0, 0, 0], end=[1, 0, 0])
        moveline.rotate_about_origin(angleTracker.get_value()*DEGREES)

        def update_moveline(mob):
            moveline = Line(start=[0, 0, 0], end=[1, 0, 0])
            moveline.rotate_about_origin(angleTracker.get_value()*DEGREES)
            mob.become(moveline)

        moveline.add_updater(update_moveline)

        # Fix Line/Axis
        fixLine = Line(start=[0, 0, 0], end=[1, 0, 0], color=RED)

        # Angle
        displayAngle = Angle(fixLine, moveline)

        def update_displayAngle(mob):
            displayAngle = Angle(fixLine, moveline)
            mob.become(displayAngle)

        displayAngle.add_updater(update_displayAngle)

        # Text
        import math
        displayText = Text("ϑ", font_size=25).move_to(
            displayAngle.point_from_proportion(0.5))

        def update_displayText(mob):
            displayText = Text(repr(math.floor(angleTracker.get_value())), font_size=25).move_to(
                displayAngle.point_from_proportion(0.5))
            mob.become(displayText)

        displayText.add_updater(update_displayText)

        # Adding int scene
        self.add(fixLine, moveline, displayAngle, displayText)
        self.wait()

        self.play(
            ChangeDecimalToValue(angleTracker, 50),
            run_time=2
        )
        self.wait()

        self.play(
            ChangeDecimalToValue(angleTracker, 180),
            run_time=2
        )
        self.wait()

        self.play(
            ChangeDecimalToValue(angleTracker, 350),
            run_time=2
        )
        self.wait()

# Official code answer


class MovingAngle(Scene):
    def construct(self):
        rotation_center = LEFT

        theta_tracker = ValueTracker(110)
        line1 = Line(LEFT, RIGHT)
        line_moving = Line(LEFT, RIGHT)
        line_ref = line_moving.copy()
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )
        a = Angle(line1, line_moving, radius=0.5, other_angle=False)
        tex = MathTex(r"\theta").move_to(
            Angle(
                line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )

        self.add(line1, line_moving, a, tex)
        self.wait()

        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )

        a.add_updater(
            lambda x: x.become(
                Angle(line1, line_moving, radius=0.5, other_angle=False))
        )
        tex.add_updater(
            lambda x: x.move_to(
                Angle(
                    line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
                ).point_from_proportion(0.5)
            )
        )

        self.play(theta_tracker.animate.set_value(40))
        self.play(theta_tracker.animate.increment_value(140))
        self.play(tex.animate.set_color(RED), run_time=0.5)
        self.play(theta_tracker.animate.set_value(350))


class AnglesExample(Scene):
    def construct(self):
        # line1 = Line(LEFT + (1/3) * UP, RIGHT + (1/3) * DOWN)
        # line2 = Line(DOWN + (1/3) * RIGHT, UP + (1/3) * LEFT)
        # angles = [
        #     Angle(line1, line2),
        #     Angle(line1, line2, radius=0.4, quadrant=(1, -1), other_angle=True),
        #     Angle(line1, line2, radius=0.5, quadrant=(-1, 1),
        #           stroke_width=8, other_angle=True),
        #     Angle(line1, line2, radius=0.7, quadrant=(-1, -1), color=RED),
        #     Angle(line1, line2, other_angle=True),
        #     Angle(line1, line2, radius=0.4, quadrant=(1, -1)),
        #     Angle(line1, line2, radius=0.5, quadrant=(-1, 1), stroke_width=8),
        #     Angle(line1, line2, radius=0.7, quadrant=(-1, -1),
        #           color=RED, other_angle=True),
        # ]
        # plots = VGroup()
        # for angle in angles:
        #     plot = VGroup(line1.copy(), line2.copy(), angle)
        #     plots.add(VGroup(plot, SurroundingRectangle(plot, buff=0.3)))
        # plots.arrange_in_grid(rows=2, buff=1)
        # self.add(plots)
        # self.wait()

        angleTracker = DecimalNumber(0, num_decimal_places=0).to_corner(UR)
        self.add(angleTracker)

        def gen_example(rotateDeg):
            line1 = Line(LEFT + (1/3) * UP, RIGHT + (1/3) * DOWN)
            line2 = Line(DOWN + (1/3) * RIGHT, UP + (1/3) * LEFT)
            line2.rotate_about_origin(rotateDeg)
            angles = [
                Angle(line1, line2),
                Angle(line1, line2, radius=0.4,
                      quadrant=(1, -1), other_angle=True),
                Angle(line1, line2, radius=0.5, quadrant=(-1, 1),
                      stroke_width=8, other_angle=True),
                Angle(line1, line2, radius=0.7, quadrant=(-1, -1), color=RED),
                Angle(line1, line2, other_angle=True),
                Angle(line1, line2, radius=0.4, quadrant=(1, -1)),
                Angle(line1, line2, radius=0.5,
                      quadrant=(-1, 1), stroke_width=8),
                Angle(line1, line2, radius=0.7, quadrant=(-1, -1),
                      color=RED, other_angle=True),
            ]
            plots = VGroup()
            for angle in angles:
                invRect = Rectangle(
                    height=2.5, width=2.5).set_stroke(opacity=0)
                plot = VGroup(line1.copy(), line2.copy(), angle, invRect)
                plots.add(VGroup(plot, SurroundingRectangle(
                    plot, color=BLUE)))
            plots.arrange_in_grid(rows=2, buff=1)
            return plots

        def plots_updater(mob):
            plots = gen_example(angleTracker.get_value()*DEGREES)
            mob.become(plots)
        plots = gen_example(angleTracker.get_value()*DEGREES)
        plots.add_updater(plots_updater)
        self.add(plots)
        self.play(
            ChangeDecimalToValue(angleTracker, 90),
            run_time=2
        )
        self.wait()
        self.play(
            ChangeDecimalToValue(angleTracker, 180),
            run_time=2
        )
        self.wait()
        self.play(
            ChangeDecimalToValue(angleTracker, 350),
            run_time=2
        )
        self.wait()
        self.play(
            ChangeDecimalToValue(angleTracker, 0),
            run_time=2
        )
        self.wait()
