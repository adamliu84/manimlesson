from manim import *

class FirstThreeDExample(ThreeDScene):
  def construct(self):

    def func_billboardText(val, removeObj=None):
      self.remove(removeObj)
      textObj = Text(val, font_size=50).to_corner(UL)
      self.add_fixed_orientation_mobjects(textObj)
      self.add_fixed_in_frame_mobjects(textObj)
      self.play(Write(textObj))
      return textObj

    og_text = func_billboardText("OG")
    axes_3d = ThreeDAxes()
    self.add(axes_3d)
    self.play(Write(Text("Hello World")))
    self.wait(2)

    co_text = func_billboardText("Camera Orientation", og_text)
    self.set_camera_orientation(phi=20*DEGREES)
    self.wait(2)
    self.set_camera_orientation(theta=20*DEGREES)
    self.wait(2)

    acr_text = func_billboardText("Ambient Camera Rotation", co_text)
    self.begin_ambient_camera_rotation(
            rate=PI / 10, about="theta"
    )
    self.wait(2)
    self.begin_ambient_camera_rotation(
            rate=PI / 10, about="phi"
    )
    self.wait(4)
    self.stop_ambient_camera_rotation(about="theta")
    self.stop_ambient_camera_rotation(about="phi")
    self.wait(2)

    mcr_text = func_billboardText("Move Camera", acr_text)
    self.move_camera(phi=0*DEGREES, run_time=2)
    self.wait(2)
    self.move_camera(theta=-90*DEGREES, run_time=2)
    self.wait(2)
    self.move_camera(gamma=135*DEGREES, run_time=2, added_anims=[Write(Text("Z 135").move_to(UR*0.5))])
    self.wait(2)