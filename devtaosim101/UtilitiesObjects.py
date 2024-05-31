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


class BracesExample(Scene):
    def construct(self):
        start = Dot([-2, -1, 0])
        end = Dot([2,  1, 0])
        line = Line(start.get_center(), end.get_center(), color=ORANGE)
        down_brace = Brace(line)
        left_brace = Brace(line, LEFT, buff=2)
        right_brace = Brace(line, RIGHT)
        down_brace_tex = down_brace.get_text("Down brace")
        left_brace_tex = left_brace.get_text("Left brace")

        # normal_brace = Brace(line, direction=rotate_vector(
        #     line.get_unit_vector(), 90*DEGREES))
        normal_brace = always_redraw(
            lambda:
                Brace(line, direction=rotate_vector(
                    line.get_unit_vector(), 90*DEGREES))
        )
        #                                   --------------------------------------------------
        #                                                   normal vector
        # rotate_vector is a function that, as the name suggests, rotates a vector.
        # normal_brace_tex = normal_brace.get_tex("x-x_1")
        normal_brace_tex = always_redraw(lambda: normal_brace.get_tex("x-x_1"))
        self.add(
            line, start, end,
            down_brace, down_brace_tex,
            left_brace, left_brace_tex,
            right_brace,
            normal_brace, normal_brace_tex,
        )
        self.play(line.animate.put_start_and_end_on([-2, 1, 0], [1, 0, 0]))
        self.wait()


class DecimalNumberExample(Scene):
    def construct(self):
        dgrp = VGroup(
            DecimalNumber(0),
            DecimalNumber(1, include_sign=True),
            DecimalNumber(1, unit="\\rm m"),
            DecimalNumber(13.41364, unit="\\rm m", num_decimal_places=3),
            DecimalNumber(133414.41364, unit="\\rm m", num_decimal_places=3),
            DecimalNumber(133414.41364, unit="\\rm m",
                          num_decimal_places=3, group_with_commas=False),
        ).scale(2.5).arrange(DOWN)
        self.add(dgrp)
        self.wait()


class NumberLineExample(Scene):
    def construct(self):

        vt = ValueTracker(2)

        l0 = NumberLine(
            #        min max step
            x_range=[-10, 10, 1],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
            font_size=20,
        )

        l1 = NumberLine(
            x_range=[-10, 10, 2],
            unit_size=0.5,
            numbers_with_elongated_ticks=[-2, 4],
            include_numbers=True,
            font_size=24,
        )
        [num6] = [num for num in l1.numbers if num.number == 6]
        num6.set_color(RED)
        l1.add(num6)

        l2 = NumberLine(
            x_range=[-2.5, 2.5 + 0.5, 0.5],
            length=12,
            # Here they are modifying the parameters of the numbers,
            # the number of decimal places.
            decimal_number_config={
                "num_decimal_places": 1,
                "unit": "\\rm m",
                "color": TEAL
            },
            include_numbers=True,
            font_size=30,
        )

        l3 = NumberLine(
            x_range=[-5, 5 + 1, 1],
            length=6,
            include_tip=True,
            include_numbers=True,
            rotation=10 * DEGREES,
        )

        line_group = VGroup(l0, l1, l2, l3).arrange(DOWN, buff=1)

        pink_dot = Dot(l0.n2p(-3), color=PINK)
        moving_white_dot = always_redraw(
            lambda: Dot(l1.n2p(vt.get_value()), color=WHITE))
        orange_dot = Dot(l3.n2p(1.5), color=ORANGE)
        moving_gold_dot = always_redraw(
            lambda: Dot(l3.n2p(vt.get_value()), color=GOLD))

        self.add(line_group, pink_dot, orange_dot)
        self.add(moving_white_dot, moving_gold_dot)
        self.play(vt.animate.set_value(10), run_time=2)
        self.play(vt.animate.set_value(-6), run_time=2)
        self.wait()


class MatrixExample(Scene):
    def construct(self):
        m0 = Matrix([
            ["\\pi", 0],
            [-1,     1]
        ])
        m1 = Matrix([
            ["π", "0"],
            ["-1", "1"]
        ],
            element_to_mobject=Text,
            element_to_mobject_config={"font": "Arial"}
        )
        m2 = IntegerMatrix([
            [1.5, 0.],
            [12, -1.3]
        ],
            left_bracket="(",
            right_bracket=")"
        )
        m3 = DecimalMatrix(
            [[3.456, 2.122], [33.2244, 12.33]],
            element_to_mobject_config={"num_decimal_places": 2},
            left_bracket="\\{",
            right_bracket="\\}")
        m4 = MobjectMatrix([
            [Circle().scale(0.3),      Square().scale(0.3)],
            [MathTex("\\pi").scale(2), Star().scale(0.3)]
        ],
            left_bracket="\\langle",
            right_bracket="\\rangle"
        )
        g = Group(m0, m1, m2, m3).arrange_in_grid(buff=1).to_edge(UP)
        m4.next_to(g, DOWN, buff=1)
        g.add(m4)
        self.add(g)
        self.wait()

        m4c = m4.copy().move_to(m1)
        self.play(ReplacementTransform(m1, m4c))
        self.wait()


class TableExample(Scene):
    def construct(self):
        # Table -------------------------------------------------
        t0 = Table([
            ["First", "Second"],
            ["Third", "Fourth"]
        ],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")],
            top_left_entry=Text("TOP"))
        #                     (row,col) not start from 0, 1 instead
        t0.add_highlighted_cell((2, 3), color=GREEN)
        # DecimalTable ------------------------------------------
        x_vals = np.linspace(-2, 2, 5)
        y_vals = np.exp(x_vals)
        t1 = DecimalTable(
            [x_vals, y_vals],
            row_labels=[MathTex("x"), MathTex("f(x)")],
            include_outer_lines=True)
        t1.add(t1.get_cell((2, 2), color=RED))
        # MathTable ---------------------------------------------
        t2 = MathTable(
            [["+", 0, 5, 10],
             [0, 0, 5, 10],
             [2, 2, 7, 12],
             [4, 4, 9, 14]],
            include_outer_lines=True)
        t2.get_horizontal_lines()[:3].set_color(ORANGE)
        t2.get_vertical_lines()[:3].set_color(ORANGE)
        t2.get_vertical_lines()[3].set_color(PINK)
        t2.get_vertical_lines()[4].set_color(YELLOW)
        t2.get_horizontal_lines()[:3].set_z_index(1)
        # MobjectTable ------------------------------------------
        cross = VGroup(
            Line(UP + LEFT, DOWN + RIGHT),
            Line(UP + RIGHT, DOWN + LEFT)
        ).set_color(BLUE).scale(0.5)
        a = Circle().set_color(RED).scale(0.5)
        b = cross
        t3 = MobjectTable([
            [a.copy(), b.copy(), a.copy()],
            [b.copy(), a.copy(), a.copy()],
            [a.copy(), b.copy(), b.copy()]
        ])
        t3.add(Line(
            t3.get_corner(DL), t3.get_corner(UR)
        ).set_color(RED))
        vals = np.arange(1, 21).reshape(5, 4)
        t4 = IntegerTable(
            vals,
            include_outer_lines=True
        )
        grp = Group(
            Group(t0, t1)    .scale(0.5).arrange(buff=1).to_edge(UP, buff=1),
            Group(t2, t3, t4).scale(0.5).arrange(buff=1).to_edge(DOWN, buff=1)
        )
        self.add(grp)
        self.wait()

        # Un-highlight cell https://www.reddit.com/r/manim/comments/10fnanm/manim_undo_highlighting_cell_in_table/
        self.play(t0[0].animate.set_opacity(0))
        self.wait()


class AngleExample(Scene):
    def construct(self):
        number_plane = NumberPlane(axis_config={"include_numbers": True})
        number_plane.set_opacity(0.3)

        # 【Arc】
        # start_angle, increment angle
        movingArc = Arc(2, 20*DEGREES, 80*DEGREES, color=GOLD)
        arcs = VGroup(
            Arc(radius=1),
            # ---------------------------
            Circle(radius=2, stroke_opacity=0.4),
            movingArc,
            # ---------------------------
            Circle(radius=3, stroke_opacity=0.4, color=BLUE),
            Arc(3, 300*DEGREES, (60+90)*DEGREES),
            # ---------------------------
            Circle(radius=1.5, stroke_opacity=0.4,
                   color=YELLOW, arc_center=[2, 2, 0]),
            Arc(1.5, -30*DEGREES, 60*DEGREES, arc_center=[2, 2, 0]),
        )

        dot = Dot(arcs[-1].get_arc_center(), color=YELLOW)
        self.add(number_plane, arcs, dot)
        # Moving Arc #1 move
        self.play(movingArc.animate.rotate_about_origin(90*DEGREES))
        self.wait()
        # Moving Arc #2 move
        # Cheap way of moving & rotating arc. Should be using add_updater instead?
        # Also not using rotate_about_origin to try out rotate
        for i in range(1, 10):
            # self.play(movingArc.animate.rotate_about_origin(
            #     10*DEGREES), run_time=0.05)
            self.play(movingArc.animate.rotate(
                10*DEGREES,
                about_point=movingArc.get_arc_center()
            ), run_time=0.05)
        self.wait()
        # Moving Arc #3 move
        movingArcDest = Arc(2, 280*DEGREES, 80*DEGREES, color=PURPLE)
        self.play(ReplacementTransform(movingArc, movingArcDest))
        self.wait()

        # 【ArcBetweenPoints】
        non_origin_circle = arcs[5]
        start = Dot(non_origin_circle.point_at_angle(
            135*DEGREES), color=ORANGE)
        end = Dot(non_origin_circle.point_at_angle(225*DEGREES), color=PINK)
        arcbp = ArcBetweenPoints(
            start.get_center(),
            end.get_center(),
            # 225 - 135 = 90
            angle=90*DEGREES
        )
        self.add(number_plane, arcbp, start, end)
        self.wait()
        movingArcPointSq = Square(
            side_length=0.3, fill_color=BLUE, fill_opacity=1).move_to(start)
        movingArcPointSq.set_stroke(width=0)
        self.add(movingArcPointSq)
        self.play(MoveAlongPath(movingArcPointSq, arcbp), run_time=3)
        self.wait()


class ArcPolygonsExample(Scene):
    def construct(self):
        # https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.ArcPolygon.html
        a = [0, 0, 0]
        b = [2, 0, 0]
        c = [0, 2, 0]
        ap1 = ArcPolygon(a, b, c, radius=2)
        ap2 = ArcPolygon(a, b, c, angle=45*DEGREES)
        ap3 = ArcPolygon(a, b, c, arc_config={'radius': 1.7, 'color': RED})
        ap4 = ArcPolygon(a, b, c, color=RED, fill_opacity=1,
                         arc_config=[{'radius': 1.7, 'color': RED},
                                     {'angle': 20*DEGREES, 'color': BLUE},
                                     {'radius': 1}])
        ap_group = VGroup(ap1, ap2, ap3, ap4).arrange()
        self.play(*[Create(ap) for ap in [ap1, ap2, ap3, ap4]])
        self.wait()

        movingArcPointSq = Square(
            side_length=0.3, fill_color=BLUE, fill_opacity=1).move_to(ap2.get_all_points()[0])
        self.add(movingArcPointSq)
        self.play(MoveAlongPath(movingArcPointSq, ap2), run_time=3)
        self.wait()


class CutoutExample(Scene):
    def construct(self):
        # 【Cutout】Triangle seem to have problem
        holes = VGroup(*[
            vm.scale(0.5)
            for vm in [Triangle(), Circle(), RegularPolygon(6), Star(5)]
        ]).arrange_in_grid(cols=2, buff=0.5)
        vmob_to_cut = Square().scale(2)
        c = Cutout(vmob_to_cut, *holes, fill_opacity=1,
                   color=BLUE, stroke_color=RED)
        c.scale(1.5)
        self.play(DrawBorderThenFill(c), run_time=4)
        self.wait()
        self.remove(c)
        self.wait()

        # 【_BooleanOps】
        boolop_circle = Circle(
            fill_color=RED, fill_opacity=1).scale(0.65)
        boolop_triange = Triangle(fill_color=RED, fill_opacity=1)

        intersection_result = Intersection(
            boolop_triange, boolop_circle, fill_color=RED, fill_opacity=1)
        self.add(intersection_result)
        self.wait(2)
        self.remove(intersection_result)
        self.wait()

        exclusion_result = Exclusion(
            boolop_triange, boolop_circle, fill_color=RED, fill_opacity=1)
        self.add(exclusion_result)
        self.wait()
        movingArcPointSq = Square(
            side_length=0.3, fill_color=BLUE, fill_opacity=1).move_to(exclusion_result.get_all_points()[0])
        self.add(movingArcPointSq)
        self.play(MoveAlongPath(movingArcPointSq,
                  exclusion_result), run_time=2)
        self.wait()
