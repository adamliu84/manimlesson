from manim import *

class Testing(Scene):
    def construct(self):
        hwtext = Tex("Hello World").to_edge(UR, buff=0.4)
        sq = Square(side_length=0.5, fill_color=YELLOW, fill_opacity=0.5)
        tri = Triangle().scale(0.5).to_edge(DL)

        # self.play(Write(hwtext))
        # self.play(DrawBorderThenFill(sq), run_time=3)
        # self.play(Create(tri))
        self.play(Write(hwtext), DrawBorderThenFill(sq), run_time=3)
        self.play(Create(tri))
        self.wait()

        self.play(hwtext.animate.to_edge(UL), run_time=3)
        self.play(sq.animate.scale(2), tri.animate.to_edge(UL), run_time=4)