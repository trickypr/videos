from tkinter import BOTTOM
from manim import *

assets_dir = os.path.dirname(os.path.abspath(__file__)) + "/assets/"


class WaterbottleQuestion(Scene):
    def construct(self):
        question_text = Text(
            "Which best explains a bottle of water in freefall?",
            font_size=50).to_edge(UP)

        image_a = ImageMobject(f"{assets_dir}water_down.png").scale(0.25)
        image_b = ImageMobject(f"{assets_dir}water_straight.png").scale(0.25)
        image_c = ImageMobject(f"{assets_dir}water_up.png").scale(0.25)
        image_d = ImageMobject(f"{assets_dir}water_none.png").scale(0.25)

        group = Group(
            Group(image_c, image_d).arrange(),
            Group(image_a,
                  image_b).arrange()).arrange(UP).scale(0.75).to_edge(DOWN)

        self.play(Write(question_text))
        self.play(FadeIn(group))

        self.wait(2)

        frame_a = SurroundingRectangle(image_a)
        frame_b = SurroundingRectangle(image_b)
        frame_c = SurroundingRectangle(image_c)
        frame_d = SurroundingRectangle(image_d)
        frame_d_secondary = SurroundingRectangle(image_d, color=GREEN)

        self.play(Create(frame_a))
        self.wait(2)
        self.play(ReplacementTransform(frame_a, frame_b))
        self.wait(2)
        self.play(ReplacementTransform(frame_b, frame_c))
        self.wait(2)
        self.play(ReplacementTransform(frame_c, frame_d))
        self.wait(2)
        self.play(Uncreate(frame_d))
        self.wait(2)
        self.play(Create(frame_d_secondary))
        self.wait(2)
        self.play(Uncreate(frame_d_secondary))
        self.play(FadeOut(group), Unwrite(question_text))


class Placeholder(Scene):
    def construct(self):
        text = Text("Placeholder", font_size=100)
        self.play(Write(text))
        self.wait(2)
        self.play(Unwrite(text))


class Gravity(Scene):
    def construct(self):
        text = Text("Gravity", font_size=100)
        self.play(Write(text))
        self.wait(2)
        self.play(Unwrite(text))


class EquivalencePrinciple(Scene):
    def construct(self):
        text = Text("Equivalence Principle", font_size=100)
        self.play(Write(text))
        self.wait(2)
        self.play(Unwrite(text))


class BasicGravityFormula(Scene):
    def construct(self):
        text = Tex(r"$g=G\frac{M}{r^2}$", font_size=100)
        self.play(Write(text))
        self.wait(2)
        self.play(Unwrite(text))


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

        self.play(FadeOut(title), FadeOut(point_1), FadeOut(point_2),
                  FadeOut(point_3))


class Endscreen(Scene):
    def construct(self):
        text = Text("Youtube thinks you will like:",
                    font_size=100).to_edge(UP, 5.0)
        self.play(Write(text))
        self.wait(20)
        self.play(Unwrite(text))
