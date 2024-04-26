from manim import *

class Pith(Scene):
    def construct(self):
        sq = Square(side_length=4, stroke_color = BLUE, fill_color=YELLOW, fill_opacity=0.5)
        self.play(Create(sq), run_time=3)
        self.wait()