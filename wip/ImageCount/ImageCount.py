from manim import *
import random

class Util():
    def group_generator(image_filename, i=1):
        text_group = Group()
        text_group.add(Text(str(i)))
        image_group = Group()
        image_group.add(*[ImageMobject(image_filename) for x in range(1,i+1)])
        image_group.arrange_in_grid(cols=5)
        overall_group = Group()
        overall_group.add(text_group, image_group)
        overall_group.arrange_in_grid(cols=1)
        return overall_group

class ImageCount(Scene):
    def construct(self):
        # Temp config file read hack (NOTE --flush_cache)
        file = open("./ImageCount.config","r")
        A_PNG = file.read()

        # Generate hacky one to ten image representative
        one_to_ten = [Util.group_generator(A_PNG, i) for i in range(1,11)]

        for num_group in one_to_ten:
          self.play(GrowFromEdge(num_group, LEFT))
          self.wait(0.5)
          self.remove(num_group)

class BasicAdditional(Scene):
      def construct(self):
        MAX_QUESTION = 10
        MAX_RESULT = 10
        # Temp config file read hack (NOTE --flush_cache)
        file = open("./ImageCount.config","r")
        A_PNG = file.read()

        for i in range(1, MAX_QUESTION+1):
          question_text = Text("Question " + str(i), font_size=DEFAULT_FONT_SIZE/2)
          question_text.to_edge(UL)
          self.add(question_text)

          first_num = random.randint(1,MAX_RESULT-1)
          second_num = random.randint(1,MAX_RESULT-first_num)
          first_num_group = Util.group_generator(A_PNG, first_num)
          second_num_group = Util.group_generator(A_PNG, second_num)
          overall_group = Group()
          overall_group.add(first_num_group, Text("+"), second_num_group)
          overall_group.arrange(aligned_edge = UP, buff = 2)
          overall_group.shift(1)
          self.play(GrowFromEdge(overall_group, LEFT))
          self.wait(0.5)
          answer_text = Text(str(first_num+second_num), color=GOLD, font_size=DEFAULT_FONT_SIZE*2)
          answer_text.shift(-1)
          self.play(Write(answer_text))
          self.wait(0.5)

          self.remove(question_text, overall_group, answer_text)
          self.wait(0.5)