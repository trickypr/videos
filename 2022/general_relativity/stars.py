from random import random
from manim import *


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
