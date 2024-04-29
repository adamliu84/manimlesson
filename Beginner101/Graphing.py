from manim import *


class Graphing(Scene):
    def construct(self):

        plane = NumberPlane(
            x_range=[-5, 5, 2], x_length=10, y_range=[0, 20, 2], y_length=10).to_edge(DOWN)
        labels = plane.get_axis_labels(x_label="x", y_label="f(x)")

        # plot is the new get_graph https://stackoverflow.com/questions/74754584/manim-code-doesnt-work-gives-error-mobject-getattr-locals-getter-got-an-un
        # parab = plane.get_graph(lambda x: x**2, x_range=[-5, 5], color=BLUE)
        parab = plane.plot(lambda x: x**2, x_range=[-3, 3], color=BLUE)
        func_label = MathTex("f(x)={x}^{2}").scale(
            0.5).next_to(parab, LEFT, buff=0.4)

        area = plane.get_riemann_rectangles(
            graph=parab, x_range=[-3, 2], dx=0.1, stroke_width=0.2, stroke_color=WHITE)

        self.play(DrawBorderThenFill(plane))
        self.play(Create(VGroup(parab, labels, func_label)))
        self.wait()
        self.play(FadeIn(area))
        self.wait()
