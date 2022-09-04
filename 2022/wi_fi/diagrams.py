from manim import *


class EMWaves(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=[0, 10 * PI, 0.5],
                          y_range=[-2, 2, 0.5],
                          z_range=[-2, 2, 0.5],
                          y_length=5,
                          z_length=5)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-80 * DEGREES)

        electric = axes.plot(lambda x: np.sin(x)).set_color(BLUE)
        magnetic = axes.plot(lambda x: np.cos(x)).rotate(90 * DEGREES,
                                                         LEFT).set_color(RED)

        electric_label = Text("Electric field").move_to(
            electric.get_center(), UP * 2).set_color(BLUE).shift(2 * DOWN)
        magnetic_label = Text("Magnetic field").rotate(
            -90 * DEGREES, LEFT).move_to(magnetic.get_center(),
                                         LEFT * 2).set_color(RED).shift(8 * UP)

        plot = VGroup(axes, electric, magnetic)
        label = VGroup(electric_label, magnetic_label)

        self.add(plot, label)