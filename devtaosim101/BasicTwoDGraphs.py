from manim import *


class AxesExample(Scene):
    def construct(self):
        axes1 = Axes(
            #    [start,end,step]
            x_range=[-1, 4, 0.5],
            y_range=[-1, 5, 1],
            # Size of each axis
            x_length=12,
            y_length=12,
            # axis_config: the settings you make here
            # will apply to both axis, you have to use the
            # NumberLine options
            axis_config={"include_numbers": True},
            # While axis_config applies to both axis,
            # x_axis_config and y_axis_config only apply
            # to their respective axis.
            x_axis_config={
                "color": RED,
                "numbers_to_exclude": [0.5, 1],
                "decimal_number_config": {
                    "color": TEAL,
                    "unit": "\\rm m",
                    "num_decimal_places": 1
                }
            },
            y_axis_config={
                "color": YELLOW,
                "include_tip": False,
                "decimal_number_config": {
                    "color": PINK,
                    "unit": "^\\circ",
                    "num_decimal_places": 1,
                    "include_sign": True
                }
            },
        )

        axes2 = Axes(
            #    [start,end,step]
            x_range=[-1, 5, 0.5],
            y_range=[-1, 5, 1],
            # Size of each axis
            y_length=6,
            x_axis_config={
                # Instead x_lenght we can define "unit_size"
                "unit_size": 2,
                "numbers_with_elongated_ticks": list(range(-1, 4)),
                "longer_tick_multiple": 3,
                # gap between axes and numbers
                "line_to_number_buff": -1.0,
                "numbers_to_include": list(range(-1, 5)),
                "decimal_number_config": {
                    "num_decimal_places": 0,
                    "unit": "\\rm \\Omega"
                },
                "font_size": 70
            },
            y_axis_config={
                "include_numbers": True
            },
        )

        axesGroup = VGroup(axes1, axes2).scale(0.5).arrange(RIGHT, buff=1)
        self.add(axesGroup)
        self.wait()


class LineGraphExample(Scene):
    def construct(self):
        # axes = Axes(
        #     x_range=(0, 7),
        #     y_range=(0, 5),
        #     x_length=7,
        #     axis_config={"include_numbers": True},
        # )
        # axes.center()
        # line_graph = axes.plot_line_graph(
        #     x_values=[0, 1.5, 2, 3, 4, 6.3],
        #     y_values=[1, 3, 2.5, 4, 2, 1.2],
        #     line_color=BLUE,
        #     vertex_dot_style={"stroke_width": 3, "fill_color": RED},
        #     stroke_width=4,
        # )
        # self.add(axes)
        # self.play(FadeIn(line_graph))
        # self.wait()

        axes = Axes(
            x_range=(0, 7),
            y_range=(0, 5),
            x_length=7,
            axis_config={"include_numbers": True},
        )
        axes.to_edge(UL)
        x_values = [0, 1.5, 2, 3, 4, 6.3]
        y_values = [1, 3, 2.5, 4, 2, 1.2]
        coords = [axes.c2p(x, y) for x, y in zip(x_values, y_values)]
        print(coords)
        plot = VMobject(color=BLUE).set_points_as_corners(coords)

        ap_group = VGroup(axes, plot)
        self.add(ap_group)
        self.play(ap_group.animate.scale(.7))
        self.play(ap_group.animate.shift(RIGHT*2))
        self.play(plot.animate.shift(RIGHT*2))
        self.play(plot.animate.scale(2))
        self.wait()

        # Learning about Points and Coords
        coords2 = [axes.c2p(x, y) for x, y in zip(x_values, y_values)]
        print(coords2)
        plot2 = VMobject(color=BLUE).set_points_as_corners(coords2)
        self.play(ReplacementTransform(plot, plot2))
        self.wait()
