from manim import *


class Dest(Scene):
    def construct(self):
        # Parties
        prect = Rectangle(width=3, height=5, color=BLUE_A,
                          fill_opacity=0.5).shift(LEFT*2.5)
        crect = Rectangle(width=3, height=5, color=ORANGE,
                          fill_opacity=0.5).shift(RIGHT*2.5)
        self.add(prect, crect)

        # Charges
        c_num = Tex("100").shift(LEFT*5).shift(UP*1.5)
        self.play(Write(c_num))
        self.play(c_num.animate.shift(RIGHT*2.5), run_time=1)
        self.wait()
        self.play(c_num.animate.shift(RIGHT*5), run_time=1)

        # Application
        a_num = Tex("20").shift(RIGHT*2).shift(DOWN*0.05)
        m_num = Tex("80").shift(RIGHT*3).shift(DOWN*0.05)
        self.play(Write(a_num), Write(m_num), FadeOut(c_num))
        self.wait()
        self.play(a_num.animate.shift(LEFT*4.5),
                  m_num.animate.shift(LEFT*0.5),
                  run_time=1)

        # Fee
        s_num = Tex("5").move_to([a_num.get_x()-0.5, a_num.get_y()-0.5, 0])
        p_num = Tex("15").move_to([a_num.get_x()+0.5, a_num.get_y()-0.5, 0])
        self.play(Write(s_num), Write(p_num), FadeOut(a_num))
        self.wait()
        self.play(s_num.animate.to_edge(LEFT, buff=0.5),
                  p_num.animate.shift(LEFT*0.5))
