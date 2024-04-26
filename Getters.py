from manim import *

class Getters(Scene):
    def construct(self):
      rect = Rectangle(color=RED, height=4, width=5)
      circle = Circle().to_edge(UP)
      # arrow  = Line(start=rect.get_left(), end=circle.get_bottom(), buff=0.5).add_tip()
      arrow = always_redraw(
        lambda: Line(start=rect.get_left(), end=circle.get_bottom(), buff=0.5).add_tip()
      )

      self.play(Create(VGroup(rect, circle, arrow)))
      self.wait()
      self.play(rect.animate.to_edge(UR), circle.animate.to_edge(DL))