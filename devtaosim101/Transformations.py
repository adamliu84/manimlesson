from manim import *


class FadeTransformExample(Scene):
    def construct(self):
        # # t1 = MathTex("e^", "\\frac{-it\\pi}{\\omega}")
        # t1 = MathTex("e^", "\\frac{-it\\pi}{\\delta}")
        # t2 = MathTex("\\frac{-it\\pi}{\\omega}")
        # VGroup(t1, t2)\
        #     .scale(3)\
        #     .arrange(DOWN, buff=2)

        # self.add(t1, t2.copy().fade(0.8))
        # self.wait(0.3)
        # self.play(
        #     ReplacementTransform(t1[-1].copy(), t2[0]),
        #     run_time=6
        # )
        # self.wait()

        # # t1 = MathTex("e^", "\\frac{-it\\pi}{\\omega}")
        t1 = MathTex("e^", "\\frac{-it\\pi}{\\delta}")
        t2 = MathTex("\\frac{-it\\pi}{\\omega}")
        VGroup(t1, t2)\
            .scale(3)\
            .arrange(DOWN, buff=2)

        self.add(t1, t2.copy().fade(0.8))
        self.wait(0.3)
        self.play(
            FadeTransformPieces(t1[-1].copy(), t2[0]),
            # FadeTransformPieces(t1, t2),
            run_time=6
        )
        self.wait()


class TransformMatchingShapesExample(Scene):
    def construct(self):
        from random import shuffle

        def get_mobs():
            mob = [Square(), Circle(), Triangle(), Text("Hello")]
            shuffle(mob)
            return mob

        grp1 = VGroup(*get_mobs()).arrange(DOWN)
        grp2 = VGroup(*get_mobs()).arrange(DOWN)
        grp3 = VGroup(*get_mobs()).arrange(DOWN)

        VGroup(grp1, grp2, grp3).arrange(RIGHT, buff=4)

        self.add(grp1, grp2, grp3)

        self.play(
            TransformMatchingShapes(
                grp1.copy(), grp2
            )
        )

        self.play(
            TransformMatchingShapes(
                grp2.copy(), grp3
            )
        )

        self.wait()


class TransformMatchingTexOneExample(Scene):
    def construct(self):
        isolate_tex = ["x", "y", "3", "="]
        t1 = MathTex("x+y=3", substrings_to_isolate=isolate_tex)
        t2 = MathTex("x=3-y", substrings_to_isolate=isolate_tex)
        VGroup(t1, t2)\
            .scale(3)
        t2.align_to(t1, LEFT)

        self.add(t1)
        self.wait()
        self.play(
            TransformMatchingTex(
                t1, t2,
                # Try removing this dict
                key_map={
                    "+": "-",
                    # "3":"y"
                }
            ),
            run_time=4
        )
        self.wait()


class TransformViaIndexesExample(Scene):
    def construct(self):

        mapping_png = ImageMobject(
            "TransformViaIndexesRef.png").scale(0.75).to_corner(UL)
        self.add(mapping_png)
        # 0 [root v]    --> 3 [root v]
        # 1 [root top]  --> 4 [root top]
        # 2 [1]         --> 0 [1]
        # 3 [fraq line] --> 1 [fraq line]
        # 4 [8]         --> 2 [2 left], 5 [2 right]

        source = MathTex("\\sqrt{\\frac{1}{8}}")[0]
        target = MathTex("\\frac{1}{2\\sqrt{2}}")[0]

        VGroup(source, target).scale(4)
        self.add(source)
        # transform_index = [
        #     [0, 1, 2, 3, 4, "r4"],
        #     # | | | | |  |
        #     # v v v v v  v
        #     [3, 4, 0, 1, 2, 5]
        # ]
        transform_index = [
            ["f0", "f1", 2, 3, 4, "r4"],
            #  |    |   | | |  |
            #  v    v   v v v  v
            [3,   4,  0, 1, 2, 5]
        ]
        self.play(
            *[
                ReplacementTransform(source[i], target[j])
                if type(i) is int else
                ReplacementTransform(source[int(i[1:])].copy(), target[j])
                if i[0] == "r" else
                FadeTransform(source[int(i[1:])], target[j])
                for i, j in zip(*transform_index)
            ],
            run_time=3
        )
        self.wait()
