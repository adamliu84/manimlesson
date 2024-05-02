from manim import *


class GetCoordExample(Scene):
    def construct(self):
        r = Rectangle()
        self.add(r)

        center = r.get_center()
        right = r.get_right()
        left = r.get_left()
        top = r.get_top()
        bottom = r.get_bottom()
        center_of_mass = r.get_center_of_mass()

        up_right = r.get_corner(UR)
        up_left = r.get_corner(UL)
        down_right = r.get_corner(DR)
        down_left = r.get_corner(DL)

        for n, p in zip(
            ["C", "R", "L", "T", "B", "UR", "UL", "DR", "DL", "CM"],
            [center, right, left, top, bottom, up_right,
                up_left, down_right, down_left, center_of_mass]
        ):
            t = Text(f"{n}", color=RED)
            t.move_to(p)
            self.add(t)
            self.wait()


class NextToExample(Scene):
    def construct(self):
        # Reference Mobject:
        rm = Rectangle()
        # Mobjects that we want to move:
        red_dot = Dot(color=RED)
        blue_dot = Dot(color=BLUE)
        green_dot = Dot(color=GREEN)
        t = Text("Some text")
        # Set positions
        red_dot.next_to(rm, LEFT)

        blue_dot.next_to(rm, LEFT, buff=0)

        green_dot.next_to(rm, DR, buff=0)

        # t.next_to(rm, DOWN, aligned_edge=LEFT)
        t.next_to(rm, DOWN, aligned_edge=RIGHT)
        #                   -----------------
        #               Delete this parameter and see what
        #               happens, then change LEFT to RIGHT

        self.add(
            rm,
            red_dot,
            blue_dot,
            green_dot,
            t
        )
        self.wait()


class StretchExample(Scene):
    def construct(self):
        c = Circle()
        t = Triangle()
        r = Rectangle()

        t.stretch_to_fit_height(c.height)
        r.stretch_to_fit_width(c.width)

        t.move_to(c.get_center())  # What happend if you remove this line

        self.add(c, t, r)
        self.wait()


class ExerciseGridExample(Scene):
    def construct(self):
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


class ExerciseYinYangExample(Scene):
    def construct(self):
        full_white_circle = Circle(
            radius=3,
            stroke_color=GREY,
            fill_color=WHITE,
            fill_opacity=1.0
        )
        self.add(full_white_circle)

        full_black_circle = Circle(
            radius=3,
            stroke_color=GREY,
            fill_color=BLACK,
            fill_opacity=1.0
        )
        sq = Square(color=RED, fill_opacity=1, side_length=6).shift(LEFT*3)
        half_black_circle = Difference(
            full_black_circle, sq, color=BLACK, fill_opacity=1, stroke_color=GREY,)
        self.add(half_black_circle)

        balance_white_circle = Circle(
            radius=1.5,
            stroke_opacity=0,
            fill_color=WHITE,
            fill_opacity=1.0
        ).shift(DOWN*1.5)
        self.add(balance_white_circle)

        balance_black_circle = Circle(
            radius=1.5,
            stroke_opacity=0,
            fill_color=BLACK,
            fill_opacity=1.0
        ).shift(UP*1.5)
        self.add(balance_black_circle)

        dot_black_circle = Circle(
            radius=0.5,
            stroke_opacity=0,
            fill_color=BLACK,
            fill_opacity=1.0
        ).move_to(balance_white_circle.get_center())
        self.add(dot_black_circle)

        dot_white_circle = Circle(
            radius=0.5,
            stroke_opacity=0,
            fill_color=RED,
            # fill_color=WHITE,
            fill_opacity=1.0
        ).move_to(balance_black_circle.get_center())
        self.add(dot_white_circle)


class ExerciseVueExample(Scene):
    def construct(self):
        t3 = Triangle(fill_color=GREEN, fill_opacity=1,
                      stroke_opacity=0).scale(3)
        t2 = Triangle(fill_color=GREY, fill_opacity=1,
                      stroke_opacity=0).scale(2)
        t2.align_to(t3, DOWN)
        t1 = Triangle(fill_color=WHITE, fill_opacity=1,
                      stroke_opacity=0).scale(1)
        t1.align_to(t2, DOWN)
        t_group = VGroup(t3, t2, t1)
        t_group.rotate(PI)
        self.add(t_group)
