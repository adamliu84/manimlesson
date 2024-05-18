from manim import *


class ScreenGrid(VGroup):
    def __init__(self, fade=0.5, *vmobjects, **kwargs):
        super().__init__(*vmobjects, **kwargs)
        # Can be draw via Rect & Lines. But trying out Numberplane
        quickGrid = NumberPlane(x_range=[-7.1, 7.1], y_range=[-4.1, 4.1])
        # Should be have better way to modify Numberplan
        y_axis_overlay = Line([0, -4.1, 0], [0, 4.1, 0], color=RED)
        x_axis_overlay = Line([-7.1, 0, 0], [7.1, 0, 0], color=RED)
        self.add(quickGrid)
        self.add(x_axis_overlay)
        self.add(y_axis_overlay)

        xRange = list(range(-6, 7))
        yRange = list(range(-3, 4))
        for n in xRange:
            t = Text(str(float(n)), font_size=25)
            t.to_edge(UP, buff=0)
            t.shift(RIGHT*n)
            t2 = t.copy()
            t2.to_edge(DOWN, buff=0)
            self.add(t)
            self.add(t2)

        for n in yRange:
            t = Text(str(float(n)), font_size=25)
            t.to_edge(LEFT, buff=0)
            t.shift(UP*n)
            t2 = t.copy()
            t2.to_edge(RIGHT, buff=0)
            self.add(t)
            self.add(t2)

        self.fade(fade)


class LineExample(Scene):
    def construct(self):
        sg = ScreenGrid(fade=0.8)

        dl1 = DashedLine(LEFT*3, RIGHT*3, dashed_ratio=0.1).shift(UP*2)
        l1 = Line(LEFT*3, RIGHT*3).shift(UP)
        l2 = Line(LEFT*3, RIGHT*3, buff=1).shift(DOWN)
        l3 = Line(LEFT*3, RIGHT*3, buff=2).shift(DOWN*2)
        self.add(sg, dl1, l1, l2, l3)
        self.wait()


class ArrowExample(Scene):
    def construct(self):
        sg = ScreenGrid(fade=0.8)
        self.add(sg)

        def get_size(s=3):
            return [LEFT*s, RIGHT*s]

        arrows = VGroup(
            Arrow(*get_size()),
            Arrow(*get_size(), buff=0),
            DoubleArrow(*get_size()),
            DoubleArrow(*get_size(), buff=0),
            # ---------------
            Arrow(*get_size(0.5)),
            Arrow(*get_size(0.5), buff=0),
            DoubleArrow(*get_size(0.5)),
            DoubleArrow(*get_size(0.5), buff=0),
        )
        arrows.arrange(DOWN, buff=0.5)

        additionalContent = VGroup(
            CurvedArrow(2*LEFT, 2*RIGHT, radius=2),
            CurvedDoubleArrow(2*LEFT, 2*RIGHT, radius=2),
            LabeledDot("ii"),
            Vector([1, 2]),
            Elbow(width=1, angle=PI/4)
        )
        additionalContent.arrange(DOWN, buff=0.5).scale(0.5)

        everything = VGroup(
            arrows, additionalContent
        ).arrange_in_grid(cols=2, buff=2)

        self.add(everything)
        self.wait()


class ArrowTipExample(Scene):
    def construct(self):
        # Special tips. IGNORE moved to Tips package
        # from manim.mobject.geometry import (
        #     ArrowTriangleFilledTip,
        #     ArrowTriangleTip
        # )
        tips_set = [
            ArrowCircleFilledTip,
            ArrowCircleTip,
            ArrowSquareFilledTip,
            ArrowSquareTip,
            ArrowTriangleFilledTip,
            ArrowTriangleTip
        ]
        normal_arrow = VGroup(*[
            Arrow(LEFT*2, RIGHT*2, tip_shape=ts)
            for ts in tips_set
        ]).arrange(DOWN, buff=0.4)

        double_arrow = VGroup(*[
            DoubleArrow(LEFT*2, RIGHT*2, tip_shape_start=ts, tip_shape_end=ts)
            for ts in tips_set
        ]).arrange(DOWN, buff=0.4)

        normal_arrow_t = Text("Arrow", font="Monospace")
        double_arrow_t = Text("DoubleArrow", font="Monospace")

        VGroup(
            VGroup(normal_arrow_t, normal_arrow).arrange(DOWN),
            VGroup(double_arrow_t, double_arrow).arrange(DOWN),
        ).arrange(RIGHT, buff=1)

        self.play(
            Write(normal_arrow_t),
            Write(double_arrow_t),
            *[
                GrowArrow(arrow)
                for arrow in [*normal_arrow, *double_arrow]
            ],
            run_time=4
        )
        self.wait(3)


class CodeSnippetExample(Scene):
    def construct(self):
        # It is important to omit the indentation
        code = '''
import Data.Char (toLower, ord)

main :: IO ()
main = do
    let input = "Hello World"
    print input
    print $ map toLower input
    print $ filter (\\a -> not $ a `elem` "aeiou") input
    print $ foldr (\\a b -> b + ord a) 0 input
'''
        rendered_code = Code(
            code=code,
            tab_width=4,
            background="window",
            language="haskell",
            font="Sans",
            style="monokai"
        )

        output = '''
"Hello World"
"hello world"
"Hll Wrld"
1052
'''
        rendered_output = Code(
            code=output,
            tab_width=4,
            background="rectangle",
            language="vim",
            font="Monospace",
            style="xcode",
            insert_line_no=False
        ).match_width(rendered_code)

        self.add(VGroup(rendered_code, rendered_output).arrange(DOWN).scale(0.5))
        self.wait()
