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

class AreaUnderGraphExample(Scene):
  def construct(self):
      backg_plane = NumberPlane(x_range=[-7,7,1], y_range=[-4,4,1])
      backg_plane.add_coordinates()

      my_plane = NumberPlane(x_range = [-6,6], x_length = 5, y_range = [-10,10], y_length=5)
      my_plane.add_coordinates()
      my_plane.shift(RIGHT*3)

      def sample_func(x):
        return 0.1*(x-5)*x*(x+5)

      # my_function = my_plane.plot(lambda x : 0.1*(x-5)*x*(x+5), x_range=[-6,6], color = GREEN_B)
      my_function = my_plane.plot(sample_func, x_range=[-6,6], color = GREEN_B)
      label = MathTex("f(x)=0.1x(x-5)(x+5)").next_to(my_plane, UP, buff=0.2)

      area = my_plane.get_area(graph = my_function, x_range = [-5,5], color = [BLUE,YELLOW], opacity=1)
      horiz_line = Line(
        start = my_plane.c2p(0, my_function.underlying_function(-2)),
        end = my_plane.c2p(-2, my_function.underlying_function(-2)),
        stroke_color = YELLOW, stroke_width = 10)
      # https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_horizontal_line
      horiz_line_2 = my_plane.get_horizontal_line(my_plane.c2p(5.5, my_function.underlying_function(5.5)),  line_func=Line, color=RED_A, stroke_width=10)
      # https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#getverticallineexample
      vert_line_2 = my_plane.get_vertical_line(my_plane.c2p(5.5, my_function.underlying_function(5.5)),  line_func=Line, color=RED_D, stroke_width=10)

      self.play(FadeIn(backg_plane))
      self.play(backg_plane.animate.set_opacity(0.2))
      self.wait()
      self.play(DrawBorderThenFill(my_plane))
      self.wait()
      self.play(Create(my_function), Write(label))
      self.wait()
      self.play(FadeIn(area))
      self.play(Create(horiz_line),Create(horiz_line_2), Create(vert_line_2))
      self.wait()
      self.remove(area, horiz_line, horiz_line_2, vert_line_2)
      self.wait()

      # https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.plot_antiderivative_graph
      my_afunction = my_plane.plot_antiderivative_graph(my_function, color=BLUE)
      self.play(Create(my_afunction))
      self.wait()
      self.remove(my_afunction)
      self.wait()

      # https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#getriemannrectanglesexample
      rects_left = my_plane.get_riemann_rectangles(
        my_function, x_range=[-5, -2], dx=0.15, color=YELLOW
      )
      lines_right = my_plane.get_vertical_lines_to_graph(
        my_function, x_range=[2, 5], num_lines=30, color=BLUE
      )
      self.play(Create(rects_left), Create(lines_right))
      self.wait()
      self.remove(rects_left, lines_right)
      self.wait()

