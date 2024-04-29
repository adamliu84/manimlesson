from manim import *

class Updaters(Scene):
  def construct(self):
    num = MathTex("ln(2)")
    box = always_redraw(lambda:SurroundingRectangle(
      num, color = RED, fill_opacity = 0.5, fill_color=GREEN, buff=2
    ))
    name = always_redraw(lambda:Tex("Hello World").next_to(box, UP, buff=0.1))

    self.play(Create(VGroup(num,box, name)), run_time=2)
    self.play(num.animate.shift(LEFT*3), run_time=2)
    self.wait()