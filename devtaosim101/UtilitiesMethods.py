from manim import *


class InterpolateColorExample(Scene):
    def construct(self):
        dots = VGroup(*[Dot() for _ in range(4)])\
            .set(width=3).arrange(RIGHT, buff=1)

        left_dot, center_dot, right_dot, gradient_dot = dots

        color1 = "#FF0000"
        color2 = "#0000FF"
        # color3 = interpolate_color(color1, color2, 0.5) # DO NOT SUPPORT STRING NOW
        # https://docs.manim.community/en/stable/reference/manim.utils.color.html#manim.utils.color.interpolate_color
        color3 = interpolate_color(ManimColor(color1), ManimColor(color2), 0.5)
        #                                         |
        #                                         v
        #                                  0 <= alpha <= 1
        #                               color1         color2

        print([color1, color2, color3])
        # ['#FF0000' '#0000FF' <Color #7f007f>]

        left_dot.set_color(color1)
        right_dot.set_color(color2)
        center_dot.set_color(color3)
        gradient_dot.set_color(color=[RED, YELLOW, BLUE, BLACK])

        self.add(dots)
        self.wait()


class SetPointsExample(Scene):
    def construct(self):
        sg = ScreenGrid()
        sg.fade(0.5)

        def coord(x, y):
            return np.array([x, y, 0])

        points = [
            coord(x, y)
            for x, y in [
                (-6, 3),
                (-1.5, -1),
                (0, 0),
                (2, -3),
                (3.5, 2)
            ]
        ]

        dots = VGroup(*[Dot(p) for p in points])
        polyline = VMobject(color=BLUE).set_points_as_corners(points)
        smoonthlypolyline = VMobject(color=RED).set_points_smoothly(points)

        self.add(sg, polyline, smoonthlypolyline, dots)
        self.wait()

        # Trying out MoveAlongPath
        cdot = Dot(color=YELLOW)
        sdot = Dot(color=GREY_BROWN)
        self.play(
            MoveAlongPath(cdot, polyline),
            MoveAlongPath(sdot, smoonthlypolyline),
            rate_func=linear,
            run_time=5
        )


class ScreenGrid(VGroup):
    def __init__(self, *vmobjects, **kwargs):
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


class PointFromProportionExample(Scene):
    def construct(self):
        path = Line(LEFT, RIGHT)  # We will study this below.
        path.width = config.frame_width - 2

        proportions = np.arange(0, 1.1, 0.1)
        # 0.1, 0.2, 0.3 ... 1.0

        prop_text = VGroup(*[
            VGroup(
                # The first argument to dot is the
                # coordinate where it is located,
                # so we don't need to use ".move_to"
                # in this case.
                Dot(path.point_from_proportion(p)),
                Text("%.1f" % p, height=0.3).next_to(
                    path.point_from_proportion(p), DOWN),
            ).set_color(interpolate_color(RED, BLUE, p))
            for p in proportions
        ])

        start = Text("Start").next_to(path.get_start(), UP)
        end = Text("End").next_to(path.get_end(), UP)

        self.add(path, prop_text, start, end)
        self.wait()


class ShapeFromProportionExample(Scene):
    def construct(self):
        paths = VGroup(
            Line(LEFT, RIGHT),  # We will study this below.
            Square(),
            Circle()
        ).arrange(RIGHT, buff=0.5)\
            .set(width=config.frame_width-2)

        def get_proportions(path, proportions=np.arange(0, 1.1, 0.1)):
            return VGroup(*[
                Dot(
                    # The first argument to dot is the
                    # coordinate where it is located,
                    # so we don't need to use ".move_to"
                    # in this case.
                    path.point_from_proportion(p),
                    fill_opacity=1-p+0.3,
                    color=interpolate_color(RED, BLUE, p)
                )
                for p in proportions
            ])

        def get_start_and_end(path):
            return VGroup(
                Text("START").next_to(path.get_start(), UP),
                Text("END").next_to(path.get_end(), DOWN),
            )

        vgrp_proportions = VGroup(*[
            get_proportions(path)
            for path in paths
        ])
        vgrp_start_end = VGroup(*[
            get_start_and_end(path)
            for path in paths
        ])

        # self.add(paths, vgrp_proportions, vgrp_start_end)
        self.add(paths, vgrp_start_end)
        self.wait(0.1)
        dotTempArr = []
        for vg in vgrp_proportions:
            for d in vg:
                dotTempArr.append(d)
                self.add(d)
                self.wait(0.1)
        self.wait(1)
        self.remove(paths, vgrp_start_end)
        self.remove(*[i for i in dotTempArr])
        self.wait(1)

        # Testing direction by flipping the shape at Y-axis
        mpaths = VGroup(
            Line(LEFT, RIGHT).flip(),  # We will study this below.
            Square().flip(),
            Circle().flip()
        ).arrange(RIGHT, buff=0.5)\
            .set(width=config.frame_width-2)

        mvgrp_proportions = VGroup(*[
            get_proportions(path)
            for path in mpaths
        ])
        mvgrp_start_end = VGroup(*[
            get_start_and_end(path)
            for path in mpaths
        ])

        self.add(mpaths, mvgrp_start_end)
        self.wait(0.1)
        dotTempArr = []
        for vg in mvgrp_proportions:
            for d in vg:
                dotTempArr.append(d)
                self.add(d)
                self.wait(0.1)
        self.wait(1)


class SubCurveExample(Scene):
    def construct(self):
        sg = ScreenGrid()
        sg.fade(0.5)
        self.add(sg)

        def coord(x, y):
            return np.array([x, y, 0])

        points = [
            coord(x, y)
            for x, y in [
                (-6, 3),
                (-1.5, -1),
                (0, 0),
                (2, -3),
                (3.5, 2)
            ]
        ]

        path = VMobject(color=BLUE).set_points_smoothly(points)
        partial_path = path.get_subcurve(0.1, 0.9)
        partial_path.set_style(stroke_width=10, stroke_color=RED)

        self.add(path, partial_path)
        self.wait(1)
        # Trying out MoveAlongPath
        dot = Dot(color=GREY_BROWN, radius=0.5)
        self.play(
            MoveAlongPath(dot, partial_path),
            rate_func=linear,
            run_time=3
        )


class TexColorExample(Scene):
    def construct(self):
        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
            substrings_to_isolate=["x", "+"]
        )

        equation.save_state()  # Saved state prior to coloring changes
        equation.set_color_by_tex("+", YELLOW)
        equation.set_color_by_tex("x", BLUE)
        equation.width = config.frame_width - 1
        self.add(equation)
        # equation.save_state()
        self.wait()

        text_2 = Tex("Modified")\
            .set(width=config.frame_width/1.5)\
            .set_color(ORANGE)\
            .to_corner(DL)
        self.play(Transform(equation, text_2))
        self.wait()
        self.play(Restore(equation))


class SurroundExample(Scene):
    def construct(self):
        formula = MathTex("x", "=", "y", "+", "3").scale(4)

        sm1 = Circle().surround(formula[0])  # buffer_factor=1.2) by default
        sm2 = Circle().surround(formula[1], buffer_factor=1)
        sm3 = Rectangle(color=PURPLE).surround(formula[2])
        sm4 = Rectangle(color=YELLOW).surround(
            formula[2], stretch=True)  # To fix the ratio

        self.add(
            formula,
            sm1, sm2, sm3, sm4
        )
        self.wait()

        sm1.generate_target()
        sm1.target.surround(formula[-1], buffer_factor=3)
        self.play(MoveToTarget(sm1))


class BackgroundRectangleExample(Scene):
    def construct(self):
        number_plane = NumberPlane(axis_config={"include_numbers": True})

        matrix = VGroup(*[Text(f"{i}") for i in range(27)]
                        ).arrange_in_grid(cols=6, buff=1)
        _0 = matrix[0]
        _16 = matrix[16]
        _13 = matrix[13]

        _16.add_background_rectangle()
        _0.add_background_rectangle(color=RED)
        _13.add_background_rectangle(color=YELLOW, buff=0.2)

        self.add(
            number_plane, matrix
        )
        self.wait()

        _12 = matrix[12]
        _12.add_background_rectangle(color=BLUE, buff=0.2)
        self.wait(0.5)
        _2 = matrix[2]
        _2.add_background_rectangle(color=GOLD, buff=0.2)
        self.wait(3)
        self.remove(number_plane, matrix)
        self.wait()

        # https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html
        t0 = Table(
            [["This", "is a"],
             ["simple", "Table in \n Manim."]])
        t1 = Table(
            [["This", "is a"],
             ["simple", "Table."]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        t1.add_highlighted_cell((2, 2), color=YELLOW)
        t2 = Table(
            [["This", "is a"],
             ["simple", "Table."]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")],
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": RIGHT})
        t2.add(t2.get_cell((2, 2), color=RED))
        t3 = Table(
            [["This", "is a"],
             ["simple", "Table."]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")],
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": YELLOW})
        t3.remove(*t3.get_vertical_lines())
        g = Group(
            t0, t1, t2, t3
        ).scale(0.7).arrange_in_grid(buff=1)
        self.add(g)
        self.wait()
