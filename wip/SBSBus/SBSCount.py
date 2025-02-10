from manim import *
import random

class Util():
    def group_generator(bus_image, i=1):
        text_group = Group()
        text_group.add(Text(str(i)))
        image_group = Group()
        image_group.add(*[bus_image.copy() for x in range(1,i+1)])
        image_group.arrange_in_grid(cols=4)
        overall_group = Group()
        overall_group.add(text_group, image_group)
        overall_group.arrange_in_grid(cols=1)
        return overall_group

class BusAdditional(Scene):
    def construct(self):
        bus_image = ImageMobject("sbsbus.png").scale(0.3)
        MAX_RESULT = 10
        MAX_QUESTION = 3

        for i in range(1, MAX_QUESTION+1):
          question_text = Text("Question " + str(i), font_size=DEFAULT_FONT_SIZE/2)
          question_text.to_edge(UL)
          first_num = random.randint(1,MAX_RESULT-1)
          second_num = random.randint(1,MAX_RESULT-first_num)

          first_group = Util.group_generator(bus_image,first_num)
          first_group.shift(LEFT*3.5)
          self.add(first_group)
          second_group = Util.group_generator(bus_image,second_num)
          second_group.to_edge(UP + RIGHT)
          self.add(second_group)
          self.wait(1)

          self.play(second_group.animate.move_to(ORIGIN+(RIGHT*2.5)))
          self.wait(1)

          first_num_str = str(first_num)
          second_num_str = str(second_num)
          sum_num_str = str(first_num + second_num)
          answer_text = Text(str(first_num_str+"+"+second_num_str+"="+sum_num_str), color=GOLD, font_size=DEFAULT_FONT_SIZE*2)
          answer_text.shift(-2)
          self.play(Write(answer_text))
          self.wait(1)

          self.remove(question_text, first_group, second_group, answer_text)

