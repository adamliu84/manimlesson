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
