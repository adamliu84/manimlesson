from manim import *


class UpdaterGraphing(Scene):
    def construct(self):

        k = ValueTracker(-4)

        plane = (
            Axes(
                x_range=[-5, 5, 2], x_length=10, y_range=[0, 5, 1], y_length=5).to_edge(DOWN).add_coordinates()
        )

        # plot is the new get_graph https://stackoverflow.com/questions/74754584/manim-code-doesnt-work-gives-error-mobject-getattr-locals-getter-got-an-un
        # parab = plane.get_graph(lambda x: x**2, x_range=[-5, 5], color=BLUE)
        func = plane.plot(lambda x: x**2, x_range=[-3, 3], color=BLUE)

        slope = always_redraw(lambda:
                              plane.get_secant_slope_group(
                                  x=k.get_value(), graph=func, dx=0.02, secant_line_color=ORANGE, secant_line_length=4)
                              )

        pt = always_redraw(lambda:
                           Dot().move_to(plane.c2p(k.get_value(), func.underlying_function(k.get_value())))
                           )

        self.add(plane, func, slope, pt)
        self.wait()
        self.play(k.animate.set_value(4), run_time=4)
