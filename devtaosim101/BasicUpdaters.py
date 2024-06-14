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