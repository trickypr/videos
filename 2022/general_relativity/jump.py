from random import random
from manim import *
from manim_physics import *


class CircleJump(SpaceScene):
    def construct(self):
        circle_size = config.frame_width / 16 / 1.61803

        objects = [
            Square(color=RED).move_to(UP).shift(UP * 3).shift(
                UP * 6 * random()).shift(RIGHT * 6 * (random() - 0.5)).rotate(
                    random() * 2 * PI).scale(circle_size) for _ in range(10)
        ]

        self.play(*[Write(obj) for obj in objects])

        self.make_rigid_body(*objects)

        self.wait(5)
