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

class ThreeDLinesAndParamFuncExample(ThreeDScene):
  def construct(self):
    axes_3d = ThreeDAxes(
      # unit_size=1 in Z axis
      z_range=(-3,3,1),
      z_length=6,
    )
    self.set_camera_orientation(phi=70*DEGREES,theta=240*DEGREES)

    # 3D Lines
    main_line        = Line(ORIGIN,axes_3d.c2p(4,3)+2*OUT,color=RED)
    vertical_line    = DashedLine(axes_3d.c2p(4,0),axes_3d.c2p(4,3))
    horizontal_line  = DashedLine(axes_3d.c2p(0,3),axes_3d.c2p(4,3))
    fall_line        = DashedLine(axes_3d.c2p(4,3),axes_3d.c2p(4,3)+OUT*2)
    l_group = VGroup(main_line, vertical_line,horizontal_line,fall_line)

    self.add(axes_3d)
    self.add(l_group)
    self.wait(1)
    self.begin_ambient_camera_rotation(
            rate=PI/2.5, about="theta"
    )
    self.wait(5)
    # self.stop_ambient_camera_rotation(about="theta")
    self.remove(l_group)
    self.wait(1)

    # 3D Arrow
    main_arrow        = Arrow3D(ORIGIN,axes_3d.c2p(4,3)+2*OUT,color=RED, base_radius=0.3)
    vertical_arrow    = Arrow3D(axes_3d.c2p(4,0),axes_3d.c2p(4,3))
    horizontal_arrow  = Arrow3D(axes_3d.c2p(0,3),axes_3d.c2p(4,3))
    fall_arrow        = Arrow3D(axes_3d.c2p(4,3),axes_3d.c2p(4,3)+OUT*2)
    a_group = VGroup(main_arrow, vertical_arrow,horizontal_arrow,fall_arrow)
    self.play(Create(a_group))
    self.wait(5)
    self.stop_ambient_camera_rotation(about="theta")
    self.remove(a_group)
    self.wait(1)

    # 3D Parametric
    func = axes_3d.plot_parametric_curve(
        lambda t: np.array([
            2*np.cos(t),
            3*np.sin(t),
            t/3
        ]),
        t_range=(-2*PI,2*PI,0.01),
        color=RED
    )
    self.add(func)
    self.wait(1)
    self.begin_ambient_camera_rotation(
            rate=-PI/2.5, about="theta"
    )
    self.wait(2)
    self.move_camera(phi=0,run_time=1,rate_func=rush_from)
    self.wait(2)

class ThreeDSurfaceExample(ThreeDScene):
  def construct(self):
    axes_3d = ThreeDAxes(
        x_range=(-6,6,1),
        x_length=12,
        y_range=(-5,5,1),
        y_length=10,
        z_range=(-3,3,1),
        z_length=6,
    )
    self.set_camera_orientation(phi=70*DEGREES,theta=240*DEGREES)

    surface = Surface(
        lambda u, v: np.array([
            np.cos(TAU * v),
            np.sin(TAU * v),
            2 * (1 - u)
        ]),
    ).fade(0.5)

    paraboloid = Surface(
        lambda u, v: np.array([
            np.cos(v)*u,
            np.sin(v)*u,
            u**2
        ]),
        v_range=(0,TAU),
    ).fade(0.5)

    para_hyp = Surface(
        lambda u, v: np.array([
            u,
            v,
            u**2-v**2
        ]),
        u_range=(-2,2),
        v_range=(-2,2),
    ).fade(0.5)

    cone = Surface(
        lambda u, v: np.array([
            u*np.cos(v),
            u*np.sin(v),
            u
        ]),
        u_range=(-2,2),
        v_range=(0,TAU),
    )
    sphere = Surface(
        lambda u, v: np.array([
            1.5*np.cos(u)*np.cos(v),
            1.5*np.cos(u)*np.sin(v),
            1.5*np.sin(u)
        ]),
        #Resolution of the surfaces
        u_range=(-PI/2,PI/2),
        v_range=(0,TAU),
    )
    axes = ThreeDAxes(x_range=(0, 5, 1), y_range=(0, 5, 1), z_range=(-1, 1, 0.5))
    sphere.set_fill_by_value(axes=axes, colorscale=[(RED, -0.5), (YELLOW, 0), (GREEN, 0.5)], axis=2)

    self.add(
        axes_3d,surface
    )
    self.play(
        Transform(surface, paraboloid)
    )
    self.begin_3dillusion_camera_rotation(rate=2)
    self.wait(0.5)
    self.play(
        Transform(surface, para_hyp)
    )
    self.wait(0.5)
    self.play(
        Transform(surface, cone)
    )
    self.wait(0.5)
    self.play(
        Transform(surface, sphere)
    )
    self.wait(0.5)