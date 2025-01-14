from manim import *

class ImageCount(Scene):
    def construct(self):
        # Temp config file read hack (NOTE --flush_cache)
        file = open("./ImageCount.config","r")
        A_PNG = file.read()

        # Generate hacky one to ten image representative
        one_to_ten = [ImageCount.group_generator(A_PNG, i) for i in range(1,11)]

        for num_group in one_to_ten:
          self.play(GrowFromEdge(num_group, LEFT))
          self.wait(0.5)
          self.remove(num_group)

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




