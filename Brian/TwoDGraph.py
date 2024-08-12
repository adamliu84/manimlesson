from manim import *

class AxesExample(Scene):
    def construct(self):

      backg_plane = NumberPlane(x_range=[-7,7,1], y_range=[-4,4,1]).add_coordinates()

      axes = Axes(x_range = [0,5,1], y_range = [0,3,1],
      x_length = 5, y_length = 3,
      axis_config = {"include_tip": True, "numbers_to_exclude": [0]}
      ).add_coordinates()

      axes.to_edge(UR)
      axis_labels = axes.get_axis_labels(x_label = "x", y_label = "f(x)")

      graph = axes.plot(lambda x : x**0.5, x_range = [0,4], color = YELLOW)

      graphing_stuff = VGroup(axes, graph, axis_labels)

      self.play(FadeIn(backg_plane), run_time=3)
      self.play(backg_plane.animate.set_opacity(0.3))
      self.wait()
      self.play(DrawBorderThenFill(axes), Write(axis_labels), run_time = 2)
      self.wait()
      self.play(Create(graph), run_time = 2)
      self.play(graphing_stuff.animate.shift(DOWN*4), run_time = 3)
      self.wait()
      self.play(axes.animate.shift(UP*3), run_time = 3)
      self.wait()
      self.play(graph.animate.shift(UP*3), axis_labels.animate.shift(UP*3), run_time = 1)
      self.wait(1)

      # Get points from coord
      c2pCoord = (4,2,0)
      dotcoord = Dot(axes.c2p(*c2pCoord[:2]), color=RED)
      v_line = axes.get_vertical_line(axes.c2p(*c2pCoord[:2]))
      h_line = axes.get_horizontal_line(axes.c2p(*c2pCoord[:2]))
      self.play(Create(dotcoord), Create(v_line), Create(h_line))
      self.wait(3)
