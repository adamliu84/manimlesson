from manim import *


class GroupsArrangeExample(Scene):
    def construct(self):
        square = Square(side_length=2)
        circle = Circle(radius=1)
        triangle = Triangle()
        rectange = Rectangle()
        # self.add(square)
        # self.add(circle)
        # self.add(triangle)
        # self.add(rectange)

        # shapeGroup = Group(square, circle, triangle, rectange)
        shapeGroup = VGroup(square, circle, triangle, rectange)
        shapeGroup.save_state()
        self.play(shapeGroup.animate.scale(0.5))
        self.play(shapeGroup.animate.arrange(DOWN, buff=0.5))
        self.play(shapeGroup.animate.arrange(
            DOWN, buff=0.5, aligned_edge=RIGHT))
        self.play(shapeGroup.animate.arrange(LEFT, buff=0.5))
        self.play(shapeGroup.animate.arrange_in_grid(col=2, flow_order="dr"))
        self.play(Restore(shapeGroup))
        self.wait()


class RainbowTextExample(Scene):
    def construct(self):
        from itertools import cycle
        colors = cycle([RED, TEAL, ORANGE, PINK])
        grp = VGroup(*[
            Text(n, color=next(colors))
            .scale(4)
            for n in "ManimCE"
        ])
        grp.arrange(RIGHT, aligned_edge=DOWN)

        self.play(Write(grp))
        self.wait()
        ce_animate_group = AnimationGroup(*[
            Indicate(grp[i], color=GOLD)
            for i in [-1, -2]
        ])
        self.play(ce_animate_group)
