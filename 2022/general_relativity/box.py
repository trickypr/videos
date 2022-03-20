from manim import *


class FloatingBox(Scene):
    def construct(self):
        box_size = config.frame_height / 2
        circle_size = box_size / 6

        box = Rectangle(height=box_size, width=box_size * 1.61803, color=BLUE)
        box.move_to(ORIGIN)

        contents = Circle(radius=circle_size, color=RED)

        self.play(Write(box), Write(contents))
        self.wait()
        self.play(Unwrite(box), Unwrite(contents))
