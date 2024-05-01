from manim import *

class UpdaterExample(Scene):
    def construct(self):
        tracker = ValueTracker(0)
        num = always_redraw(lambda: DecimalNumber().set_value(
            tracker.get_value()).to_edge(UR))
        self.add(num)

        def textUpdater(m, dt):
            rotation_value = 40*DEGREES*dt
            m.rotate(rotation_value)
            tracker.increment_value(rotation_value*180/PI)
            num.set_x(tracker.get_value()/180*PI)
        text = Text("Testing123")
        text.add_updater(textUpdater)
        self.add(text)
        self.wait(10)

class ApplyFunctionExample(Scene):
    def construct(self):
        text = Tex("Text")\
               .to_corner(DL)

        self.add(text)

        def apply_function(mob):
            mob.scale(2)
            mob.to_corner(UR)
            mob.rotate(PI/4)
            mob.set_color(RED)
            return mob

        self.play(
            ApplyFunction(
                apply_function,
                text
            )
        )

        self.wait(0.3)