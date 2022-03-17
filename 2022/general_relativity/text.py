from manim import *


class EquivalencePrinciple(Scene):
    def construct(self):
        text = Text("Equivalence Principle", font_size=100)
        self.play(Write(text))
        self.wait(2)


class BasicGravityFormula(Scene):
    def construct(self):
        text = Tex(r"$g=G\frac{M}{r^2}$", font_size=100)
        self.play(Write(text))
        self.wait(2)


class Conclusions(Scene):
    def construct(self):
        point_size = 40

        title = Text("Conclusions", font_size=100)
        point_1 = Text(
            "No difference between objects in free-fall and zero gravity",
            font_size=point_size)
        point_2 = Text("Space and time form the first four dimensions",
                       font_size=point_size)
        point_3 = Text(
            "Gravity is caused by bends in space time\ncreated by heavier objects",
            font_size=point_size)

        points = [point_1, point_2, point_3]

        VGroup(title, *points).arrange(DOWN)

        self.play(Write(title))

        for point in points:
            self.play(FadeIn(point, shift=DOWN))

        self.wait()
