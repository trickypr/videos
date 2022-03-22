from manim import *

assets_dir = os.path.dirname(os.path.abspath(__file__)) + "/assets/"


class DrawArrow(Scene):
    def construct(self):
        light_beam_text = Text("Light beam",
                               color=YELLOW,
                               font_size=DEFAULT_FONT_SIZE / 2)
        arrow = Arrow(start=5 * LEFT, end=5 * RIGHT, color=YELLOW)

        VGroup(light_beam_text, arrow).arrange(DOWN)

        self.play(Write(arrow))
        self.play(Write(light_beam_text))
        self.wait()
        self.play(Unwrite(arrow), Unwrite(light_beam_text))


class BasicDrawArrow(Scene):
    def construct(self):
        arrow = Arrow(start=6 * LEFT, end=6 * RIGHT, color=YELLOW)

        self.play(Write(arrow))
        self.wait()
        self.play(Unwrite(arrow))


class BasicDrawArrowShort(Scene):
    def construct(self):
        arrow = Arrow(start=LEFT, end=RIGHT, color=YELLOW)

        self.play(Write(arrow))
        self.wait()
        self.play(Unwrite(arrow))


class DrawSVG(Scene):
    def svg(self) -> str:
        return ""

    def construct(self):
        svg = SVGMobject(f"{assets_dir}{self.svg()}").scale(2.0)

        self.play(Write(svg))
        self.wait()
        self.play(Unwrite(svg))


class DrawShuttleDashed(DrawSVG):
    def svg(self):
        return "shuttle_dashed.svg"


class DrawShuttleSolid(DrawSVG):
    def svg(self):
        return "shuttle_solid.svg"


class LightDiagram(Scene):
    def construct(self):
        sun = Circle(radius=0.5, color=YELLOW).to_edge(RIGHT)
        earth = Circle(radius=0.2, color=GREEN).to_edge(LEFT)

        self.play(Write(sun), Write(earth))
        self.wait()
        self.play(Unwrite(sun), Unwrite(earth))