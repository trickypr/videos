from manim import *


class GravityGrid(ThreeDScene):
    def construct(self):
        resolution_fa = 42
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)

        def param_gauss(u, v):
            x = u
            y = v
            sigma, mu = 1, [0.0, 0.0]
            d = np.linalg.norm(np.array([x - mu[0], y - mu[1]]))
            z = np.exp(-(d**2 / (2.0 * sigma**2))) * 2
            return np.array([x, y, -z])

        # Create a flat plane
        gauss_plane = Surface(lambda u, v: np.array([u, v, 0]),
                              resolution=(resolution_fa, resolution_fa),
                              v_range=[-2, +2],
                              u_range=[-2, +2])

        gauss_plane.scale(2, about_point=ORIGIN)
        gauss_plane.set_style(fill_opacity=1, stroke_color=WHITE)
        gauss_plane.set_fill_by_checkerboard(GRAY, BLACK, opacity=0.1)
        axes = ThreeDAxes()
        self.play(Write(axes))
        self.play(Write(gauss_plane))

        gravity_sphere = Sphere(radius=0.5, color=BLUE)

        self.play(
            gauss_plane.animate.apply_function(
                lambda p: param_gauss(p[0], p[1])), Write(gravity_sphere))
        self.wait()

        self.play(Unwrite(gauss_plane), Unwrite(gravity_sphere), Unwrite(axes))


class Thumbnail(ThreeDScene):
    def construct(self):
        resolution_fa = 42
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)

        def param_gauss(u, v):
            x = u
            y = v
            sigma, mu = 1, [0.0, 0.0]
            d = np.linalg.norm(np.array([x - mu[0], y - mu[1]]))
            z = np.exp(-(d**2 / (2.0 * sigma**2))) * 2
            return np.array([x, y, -z])

        # Create a flat plane
        gauss_plane = Surface(lambda u, v: np.array([u, v, 0]),
                              resolution=(resolution_fa, resolution_fa),
                              v_range=[-2, +2],
                              u_range=[-2, +2])

        gauss_plane.scale(2, about_point=ORIGIN)
        gauss_plane.set_style(fill_opacity=1, stroke_color=WHITE)
        gauss_plane.set_fill_by_checkerboard(GRAY, BLACK, opacity=0.1)

        gauss_plane.apply_function(lambda p: param_gauss(p[0], p[1]))

        axes = ThreeDAxes()
        self.add(axes)
        self.add(gauss_plane)

        gravity_sphere = Sphere(radius=0.5, color=BLUE).move_to(IN * 1.5)

        self.add(gravity_sphere)

        text = Text("What even is this?",
                    font_size=75).to_corner(LEFT).rotate(90 * DEGREES).rotate(
                        90 * DEGREES, UP).shift(OUT).set_color_by_gradient(
                            "#9bf8f4", "#60efff")

        self.add(text)
