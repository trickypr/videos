from random import random
from manim import *
from numpy import linalg as la
import operator as op


class StarBackground(Scene):
    def construct(self):
        random_point_count = 200
        random_points = [((random() - 0.5) * config.frame_width,
                          (random() - 0.5) * config.frame_height)
                         for _ in range(random_point_count)]

        points = [
            Circle(random() * 0.05, BLACK).set_x(point[0]).set_y(
                point[1]).set_fill(GREY, 1).set_stroke(BLACK, 0)
            for point in random_points
        ]

        self.play(*[Write(point, run_time=random() * 2) for point in points])
        self.wait()


class Planet(VGroup):
    proportion: float = 0.0
    rate: float = 100

    def __init__(self, star, *mobjects, **kwargs):
        super().__init__(*mobjects, **kwargs)

        self.orbit = Circle(radius=2.0).set_fill(None,
                                                 0).set_stroke(WHITE, 0.2)
        self.planet = Circle(radius=0.2, color=GREEN).move_to(
            ORIGIN)  # TODO: Correct color for mercury
        self.planet.move_to(self.orbit.point_from_proportion(0))
        self.star = star

    def get_draw_in(self):
        return [Write(self.orbit), Write(self.planet)]

    def start_animation(self):
        self.add_updater(lambda _m, dt: self.on_update(dt))

    def on_update(self, dt: float = 0, recursive: bool = True):
        print(self.proportion)

        orbit = self.orbit
        planet = self.planet
        star = self.star

        rate = self.rate
        radius_vector = planet.get_center() - star.get_center()
        rate *= 1.0 / la.norm(radius_vector)

        prop = self.proportion
        d_prop = 0.001
        ds = la.norm(
            op.add(
                orbit.point_from_proportion((prop + d_prop) % 1),
                -orbit.point_from_proportion(prop),
            ))

        delta_prop = (d_prop / ds) * rate * dt

        self.proportion = (self.proportion + delta_prop) % 1
        planet.move_to(orbit.point_from_proportion(self.proportion))


class OrbitingPlanets(Scene):
    def construct(self):
        text = Text('(Fairly standard orbit)',
                    font_size=25).to_corner(UP + LEFT)
        sun = Circle(radius=0.5, color=YELLOW).move_to(ORIGIN)
        orbit = Circle(radius=3.0).set_fill(None, 0).set_stroke(WHITE, 0.2)
        planet = Dot(RIGHT * 3)

        self.play(Write(sun), Write(planet), Write(orbit), Write(text))

        for _ in range(0, 3):
            self.play(
                Rotating(planet,
                         about_point=ORIGIN,
                         angle=TAU,
                         run_time=TAU,
                         rate_func=linear))

        self.play(Unwrite(sun), Unwrite(planet), Unwrite(orbit), Unwrite(text))
