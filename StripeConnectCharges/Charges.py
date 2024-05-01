from manim import *


class Util():
    AMOUNT_FONT_SIZE = 25

    def GenHourGlass():
        upTriange = Triangle(fill_opacity=1).rotate(180*DEGREES).scale(0.25)
        downTriange = Triangle(fill_opacity=1).scale(0.25).next_to(upTriange, DOWN, buff=-0.05)
        tri_group = VGroup(upTriange, downTriange)
        return tri_group


class Dest(Scene):

    def construct(self):
        # Parties
        platformAccountRect = Rectangle(width=3, height=5, color=BLUE_A,
                                        fill_opacity=0.5).shift(LEFT*2.5)
        platformAccountText = Text("Platform Account", font_size=18, weight=HEAVY).next_to(
            platformAccountRect, UP, buff=-0.5)
        platformAccountVGroup = VGroup(
            platformAccountRect, platformAccountText)
        connectAccountRect = Rectangle(width=3, height=5, color=ORANGE,
                                       fill_opacity=0.5).shift(RIGHT*2.5)
        connectAccountText = Text("Connected Account", font_size=18, weight=HEAVY).next_to(
            connectAccountRect, UP, buff=-0.5)
        connectAccountVGroup = VGroup(
            connectAccountRect, connectAccountText)
        self.play(GrowFromPoint(platformAccountVGroup, ORIGIN))
        self.play(GrowFromPoint(connectAccountVGroup, ORIGIN))
        self.wait()

        # Charges
        charge_amount = Text("100", font_size=Util.AMOUNT_FONT_SIZE).next_to(
            platformAccountVGroup, LEFT, buff=1).shift(UP*1.5)
        self.play(Write(charge_amount))
        self.play(charge_amount.animate.shift(RIGHT*2.75), run_time=1)
        self.wait()
        self.play(charge_amount.animate.shift(RIGHT*5), run_time=1)

        # Charge Fee Split
        application_amount = Text("20", font_size=Util.AMOUNT_FONT_SIZE).next_to(
            charge_amount, DOWN, buff=0.75).shift(LEFT*0.75)
        merchant_amount = Text("80", font_size=Util.AMOUNT_FONT_SIZE).next_to(
            charge_amount, DOWN, buff=0.75).shift(RIGHT*0.75)
        charge_application_arrow = Line(start=charge_amount.get_bottom(),
                                        end=application_amount.get_top()).add_tip()
        charge_merchant_arrow = Line(start=charge_amount.get_bottom(),
                                     end=merchant_amount.get_top()).add_tip()
        self.play(FadeIn(charge_application_arrow),
                  FadeIn(charge_merchant_arrow))
        self.play(Write(application_amount), Write(merchant_amount),
                  FadeOut(charge_amount), FadeOut(charge_application_arrow), FadeOut(charge_merchant_arrow))
        self.play(application_amount.animate.move_to(
            [platformAccountVGroup.get_x(), application_amount.get_y(), 0]),
            merchant_amount.animate.move_to(
            [connectAccountVGroup.get_x(), merchant_amount.get_y(), 0])
        )

        # Application Fee Split
        stripe_amount = Text("3", font_size=Util.AMOUNT_FONT_SIZE).next_to(
            application_amount, DOWN, buff=0.75).shift(LEFT*0.75)
        platform_amount = Text("17", font_size=Util.AMOUNT_FONT_SIZE).next_to(
            application_amount, DOWN, buff=0.75).shift(RIGHT*0.75)
        application_stripe_arrow = Line(start=application_amount.get_bottom(),
                                        end=stripe_amount.get_top()).add_tip()
        application_platform_arrow = Line(start=application_amount.get_bottom(),
                                          end=platform_amount.get_top()).add_tip()
        self.play(FadeIn(application_stripe_arrow),
                  FadeIn(application_platform_arrow))
        self.play(Write(stripe_amount), Write(platform_amount),
                  FadeOut(application_amount), FadeOut(application_stripe_arrow), FadeOut(application_platform_arrow))
        self.play(stripe_amount.animate.shift(LEFT*2),
                  platform_amount.animate.move_to(
            [platformAccountVGroup.get_x(), platform_amount.get_y(), 0])
        )

        # Platform & CA Payout
        platform_payout_arrow = Line(start=platform_amount.get_bottom(
        ), end=platformAccountVGroup.get_bottom()+[0, -0.5, 0], color=RED).add_tip()
        merchant_payout_arrow = Line(start=merchant_amount.get_bottom(
        ), end=connectAccountVGroup.get_bottom()+[0, -0.5, 0], color=RED).add_tip()
        self.play(FadeIn(platform_payout_arrow), FadeIn(merchant_payout_arrow))
        self.play(platform_amount.animate.next_to(platformAccountVGroup, DOWN, buff=0.2),
                  merchant_amount.animate.next_to(
                      connectAccountVGroup, DOWN, buff=0.2),
                  FadeOut(platform_payout_arrow), FadeOut(
                      merchant_payout_arrow)
                  )
        self.wait(2)


class SCT(Scene):

    def construct(self):
        # Parties
        platformAccountRect = Rectangle(width=3, height=5, color=BLUE_A,
                                        fill_opacity=0.5).shift(LEFT*2.5)
        platformAccountText = Text("Platform Account", font_size=18, weight=HEAVY).next_to(
            platformAccountRect, UP, buff=-0.5)
        platformAccountVGroup = VGroup(
            platformAccountRect, platformAccountText)
        connectAccountRect = Rectangle(width=3, height=5, color=ORANGE,
                                       fill_opacity=0.5).shift(RIGHT*2.5)
        connectAccountText = Text("Connected Account", font_size=18, weight=HEAVY).next_to(
            connectAccountRect, UP, buff=-0.5)
        connectAccountVGroup = VGroup(
            connectAccountRect, connectAccountText)
        self.play(GrowFromPoint(platformAccountVGroup, ORIGIN))
        self.play(GrowFromPoint(connectAccountVGroup, ORIGIN))
        self.wait()

        # Charges
        charge_amount = Text("100", font_size=Util.AMOUNT_FONT_SIZE).next_to(
            platformAccountVGroup, LEFT, buff=1).shift(UP*1.5)
        self.play(Write(charge_amount))
        self.play(charge_amount.animate.shift(RIGHT*2.75), run_time=1)
        self.wait()

        # Holding fund
        self.play(charge_amount.animate.shift(DOWN*0.5))
        holding_amount = Text(
            "97", font_size=Util.AMOUNT_FONT_SIZE).move_to(charge_amount)
        stripe_amount = Text(
            "3", font_size=Util.AMOUNT_FONT_SIZE).move_to(charge_amount)
        self.play(ReplacementTransform(charge_amount, holding_amount),
                  stripe_amount.animate.shift(LEFT*2))
        self.wait(0.25)
        hourGlass = Util.GenHourGlass()
        hourGlass.next_to(platformAccountVGroup, RIGHT, buff=-0.4)
        self.add(hourGlass)
        self.play(Rotate(hourGlass, angle=10*PI,
                  rate_func=slow_into), run_time=2)
        self.wait()

        # Fee Split
        self.play(holding_amount.animate.shift(DOWN*0.5))
        platform_amount = Text(
            "17", font_size=Util.AMOUNT_FONT_SIZE).move_to(holding_amount)
        merchant_amount = Text(
            "80", font_size=Util.AMOUNT_FONT_SIZE).move_to(holding_amount)
        self.remove(hourGlass)
        self.play(ReplacementTransform(holding_amount, platform_amount),
                  merchant_amount.animate.move_to([connectAccountVGroup.get_x(), holding_amount.get_y(), 0]))
        self.wait()

        # Platform & CA Payout
        platform_payout_arrow = Line(start=platform_amount.get_bottom(
        ), end=platformAccountVGroup.get_bottom()+[0, -0.5, 0], color=RED).add_tip()
        merchant_payout_arrow = Line(start=merchant_amount.get_bottom(
        ), end=connectAccountVGroup.get_bottom()+[0, -0.5, 0], color=RED).add_tip()
        self.play(FadeIn(platform_payout_arrow), FadeIn(merchant_payout_arrow))
        self.play(platform_amount.animate.next_to(platformAccountVGroup, DOWN, buff=0.2),
                  merchant_amount.animate.next_to(
                      connectAccountVGroup, DOWN, buff=0.2),
                  FadeOut(platform_payout_arrow), FadeOut(
                      merchant_payout_arrow)
                  )
        self.wait(2)

class SCTM(Scene):

    AMOUNT_FONT_SIZE = 25

    def construct(self):
        # Parties
        platformAccountRect = Rectangle(width=3, height=5, color=BLUE_A,
                                        fill_opacity=0.5).shift(LEFT*2.5)
        platformAccountText = Text("Platform Account", font_size=18, weight=HEAVY).next_to(
            platformAccountRect, UP, buff=-0.5)
        platformAccountVGroup = VGroup(
            platformAccountRect, platformAccountText)
        connectAccountRect = Rectangle(width=1, height=5, color=ORANGE,
                                       fill_opacity=0.5).shift(RIGHT*1.5)
        connectAccountText = Text("CA1", font_size=18, weight=HEAVY).next_to(
            connectAccountRect, UP, buff=-0.5)
        connectAccountRect2 = Rectangle(width=1, height=5, color=GREY,
                                        fill_opacity=0.5).shift(RIGHT*3.5)
        connectAccountText2 = Text("CA2", font_size=18, weight=HEAVY).next_to(
            connectAccountRect2, UP, buff=-0.5)
        connectAccountVGroup = VGroup(
            connectAccountRect, connectAccountText)
        connectAccount2VGroup = VGroup(
            connectAccountRect2, connectAccountText2)
        self.play(GrowFromPoint(platformAccountVGroup, ORIGIN))
        self.play(GrowFromPoint(connectAccountVGroup, ORIGIN),
                  GrowFromPoint(connectAccount2VGroup, ORIGIN))
        self.wait()

        # Charges
        charge_amount = Text("100", font_size=Util.AMOUNT_FONT_SIZE).next_to(
            platformAccountVGroup, LEFT, buff=1).shift(UP*1.5)
        self.play(Write(charge_amount))
        self.play(charge_amount.animate.shift(RIGHT*2.75), run_time=1)
        self.wait()

        # Holding fund
        self.play(charge_amount.animate.shift(DOWN*0.5))
        holding_amount = Text(
            "97", font_size=Util.AMOUNT_FONT_SIZE).move_to(charge_amount)
        stripe_amount = Text(
            "3", font_size=Util.AMOUNT_FONT_SIZE).move_to(charge_amount)
        self.play(ReplacementTransform(charge_amount, holding_amount),
                  stripe_amount.animate.shift(LEFT*2))
        self.wait(0.25)
        hourGlass = Util.GenHourGlass()
        hourGlass.next_to(platformAccountVGroup, RIGHT, buff=-0.4)
        self.add(hourGlass)
        self.play(Rotate(hourGlass, angle=10*PI,
                  rate_func=slow_into), run_time=2)
        self.wait()

        # Fee Split
        self.play(holding_amount.animate.shift(DOWN*0.5))
        platform_amount = Text(
            "17", font_size=Util.AMOUNT_FONT_SIZE).move_to(holding_amount)
        merchant_amount = Text(
            "50", font_size=Util.AMOUNT_FONT_SIZE).move_to(holding_amount)
        merchant2_amount = Text(
            "30", font_size=Util.AMOUNT_FONT_SIZE).move_to(holding_amount)
        self.remove(hourGlass)
        self.play(ReplacementTransform(holding_amount, platform_amount),
                  merchant_amount.animate.move_to(
                      [connectAccountVGroup.get_x(), holding_amount.get_y(), 0]),
                  merchant2_amount.animate.move_to([connectAccount2VGroup.get_x(), holding_amount.get_y(), 0]))
        self.wait()

        # Platform & CA Payout
        platform_payout_arrow = Line(start=platform_amount.get_bottom(
        ), end=platformAccountVGroup.get_bottom()+[0, -0.5, 0], color=RED).add_tip()
        merchant_payout_arrow = Line(start=merchant_amount.get_bottom(
        ), end=connectAccountVGroup.get_bottom()+[0, -0.5, 0], color=RED).add_tip()
        merchant2_payout_arrow = Line(start=merchant2_amount.get_bottom(
        ), end=connectAccount2VGroup.get_bottom()+[0, -0.5, 0], color=RED).add_tip()
        self.play(FadeIn(platform_payout_arrow), FadeIn(
            merchant_payout_arrow), FadeIn(merchant2_payout_arrow))
        self.play(platform_amount.animate.next_to(platformAccountVGroup, DOWN, buff=0.2),
                  merchant_amount.animate.next_to(
                      connectAccountVGroup, DOWN, buff=0.2),
                  merchant2_amount.animate.next_to(
                      connectAccount2VGroup, DOWN, buff=0.2),
                  FadeOut(platform_payout_arrow), FadeOut(
                      merchant_payout_arrow), FadeOut(merchant2_payout_arrow)
                  )
        self.wait(2)