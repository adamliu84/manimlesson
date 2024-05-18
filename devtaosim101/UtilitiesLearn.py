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
