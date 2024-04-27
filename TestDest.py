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
        ca_arrow = Line(start=c_num.get_bottom(),
                        end=a_num.get_top()).add_tip()
        cm_arrow = Line(start=c_num.get_bottom(),
                        end=m_num.get_top()).add_tip()
        self.play(FadeIn(ca_arrow, cm_arrow))
        self.play(Write(a_num), Write(m_num), FadeOut(
            c_num), FadeOut(ca_arrow), FadeOut(cm_arrow))
        self.wait()
        self.play(a_num.animate.shift(LEFT*4.5),
                  m_num.animate.shift(LEFT*0.5),
                  run_time=1)

        # Fee
        s_num = Tex("5").move_to([a_num.get_x()-0.5, a_num.get_y()-1, 0])
        p_num = Tex("15").move_to([a_num.get_x()+0.5, a_num.get_y()-1, 0])
        as_arrow = Line(start=a_num.get_bottom(),
                        end=s_num.get_top()).add_tip()
        ap_arrow = Line(start=a_num.get_bottom(),
                        end=p_num.get_top()).add_tip()
        self.play(FadeIn(as_arrow, ap_arrow))
        self.play(Write(s_num), Write(p_num), FadeOut(
            a_num), FadeOut(as_arrow), FadeOut(ap_arrow))
        self.wait()
        self.play(
            # s_num.animate.to_edge(LEFT, buff=0.5),
            # s_num.animate.next_to(prect, LEFT, buff=0.2),
            # s_num.animate.shift([-2, 0, 0])
            s_num.animate.shift(LEFT*2),
            p_num.animate.shift(LEFT*0.5)
        )

        # Payout
        self.play(m_num.animate.next_to(crect, DOWN, buff=0.2),
                  p_num.animate.next_to(prect, DOWN, buff=0.2))
        self.wait(2)
