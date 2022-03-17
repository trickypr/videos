from manim import *


class ThreeDimensionsPlusTime(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        text3d = Text("+ time")
        self.add_fixed_in_frame_mobjects(text3d)
        text3d.to_corner(UR)
        self.play(Write(axes))
        self.wait()