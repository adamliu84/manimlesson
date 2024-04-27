from manim import *

SG_SVG = "./Singapore.svg"
SG_PNG = "./Singapore.png"


class SVGs(Scene):
    def construct(self):

        sg_svg = SVGMobject(SG_SVG).shift(LEFT*3)
        # self.play(DrawBorderThenFill(sg_svg))

        sg_png = ImageMobject(SG_PNG).shift(RIGHT*3).scale(0.45)
        # self.play(FadeIn(sg_png))

        self.play(DrawBorderThenFill(sg_svg),
                  GrowFromEdge(sg_png, LEFT)
                  )
