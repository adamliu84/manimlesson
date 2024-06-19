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
