from manim import *


class TextFuncExample(Scene):
    def construct(self):
        grp = VGroup(
            # Text to color
            Text("Hello", t2c={"[1:-1]": BLUE}),
            Text("World", t2c={"rl": RED}),
            # Text to font
            Text("Manim", t2f={"an": "Open Sans"}),
            Text("Manim", t2f={"[2:-1]": "Open Sans"}),
            # Text to gradient
            Text("Hello", t2g={"[1:-1]": (RED, GREEN)}),
            Text("World", t2g={"World": (RED, BLUE)}),
            # Text to slant
            Text("Manim", t2s={"an": ITALIC}),
            Text("Manim", t2s={"[2:-1]": ITALIC}),
            # Text to weight
            Text("Manim", t2w={"an": THIN}, font="Open Sans"),
            Text("Manim", t2w={"[2:]": HEAVY}, font="Open Sans"),
            # Ligature
            Text("fl ligature", font_size=40),
            Text("fl ligature", disable_ligatures=True, font_size=40),
        ).arrange_in_grid(cols=2).scale(1.4)

        self.add(grp)
        self.wait()


class TexExample(Scene):
    def construct(self):
        t = Tex(
            "Hello my ", "world",
            tex_to_color_map={
                "Hello": RED,
                "wor": ORANGE
            }
        )
        t[1][1].set_color(BLUE)
        print(t)
        self.add(t)
        self.wait()
