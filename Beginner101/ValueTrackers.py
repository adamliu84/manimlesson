from manim import *

class ValueTrackers(Scene):
  def construct(self):

    k = ValueTracker(4)
    num = always_redraw(lambda: DecimalNumber().set_value(k.get_value()))

    self.play(SpiralIn(num), run_time=2)
    self.wait()
    self.play(k.animate.set_value(2), run_time=3, rate_func=exponential_decay)
