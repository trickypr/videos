from tkinter import BOTTOM
from manim import *


class IntroduceSensors(Scene):
    def construct(self):
        self.next_section('Goals')
        title = Text('Goals', font_size=100).to_edge(UP)

        goal_1 = Text('Assist admin staff with decision making')
        goal_2 = Text('Provide UV and weather data on SchoolBox')

        VGroup(goal_1, goal_2).arrange(DOWN)

        self.play(Write(title))
        self.wait()
        self.play(FadeIn(goal_1, shift=DOWN))
        self.wait()
        self.play(FadeIn(goal_2, shift=DOWN))
        self.wait()
        self.play(Unwrite(title), FadeOut(goal_1), FadeOut(goal_2))
        self.wait()

        self.next_section('Required sensors')

        title = Text('Required Sensors', font_size=100).to_edge(UP)

        sensor_1 = Text('UV Sensor')
        sensor_2 = Text('Temperature Sensor')
        sensor_3 = Text('Pressure Sensor')
        sensor_4 = Text('Rain Gauge')
        sensor_5 = Text('Anemometer')

        VGroup(sensor_1, sensor_2, sensor_3, sensor_4, sensor_5).arrange(DOWN)

        self.play(Write(title))
        self.wait()
        self.play(FadeIn(sensor_1, shift=DOWN))
        self.wait()
        self.play(FadeIn(sensor_2, shift=DOWN))
        self.wait()
        self.play(FadeIn(sensor_3, shift=DOWN))
        self.wait()
        self.play(FadeIn(sensor_4, shift=DOWN))
        self.wait()
        self.play(FadeIn(sensor_5, shift=DOWN))
        self.wait()

        self.next_section('Highlight Sensors')

        sensor_frame_1 = SurroundingRectangle(sensor_1)
        sensor_frame_2 = SurroundingRectangle(sensor_2)
        sensor_frame_3 = SurroundingRectangle(sensor_3)
        sensor_frame_4 = SurroundingRectangle(sensor_4)
        sensor_frame_5 = SurroundingRectangle(sensor_5)

        self.play(Create(sensor_frame_1))
        self.wait()
        self.play(ReplacementTransform(sensor_frame_1, sensor_frame_2))
        self.wait()
        self.play(ReplacementTransform(sensor_frame_2, sensor_frame_3))
        self.wait()
        self.play(ReplacementTransform(sensor_frame_3, sensor_frame_4))
        self.wait()
        self.play(ReplacementTransform(sensor_frame_4, sensor_frame_5))
        self.wait()

        self.play(Unwrite(title), Uncreate(sensor_frame_5), FadeOut(sensor_1),
                  FadeOut(sensor_2), FadeOut(sensor_3), FadeOut(sensor_4),
                  FadeOut(sensor_5))
        self.wait()

        self.next_section('Additional Requirements')

        title = Text('Additional Requirements', font_size=100).to_edge(UP)

        req_1 = Text('Controlled using a Raspberry Pi')
        req_2_1 = Text('Communicate via ')
        req_2_2 = Tex(r'$I^2C$')

        req_2 = VGroup(req_2_1, req_2_2).arrange(RIGHT)

        VGroup(req_1, req_2).arrange(DOWN)

        self.play(Write(title))
        self.wait()
        self.play(FadeIn(req_1, shift=DOWN))
        self.wait()
        self.play(FadeIn(req_2, shift=DOWN))
        self.wait()
        self.play(Unwrite(title), FadeOut(req_1), FadeOut(req_2))
        self.wait()

        self.next_section('Choosing sensors')

        title = Text('Sensors', font_size=100).to_edge(UP)

        sensor_1 = Text('Temperature - DHT20')
        sensor_2 = Text('Air Pressure  - LPS22')
        sensor_3 = Text('UV  - SI1145')
        sensor_4 = Text('Rain  - All in one soln')

        VGroup(sensor_1, sensor_2, sensor_3, sensor_4).arrange(DOWN)

        self.play(Write(title))
        self.next_section()
        self.wait()
        self.next_section()
        self.play(FadeIn(sensor_1, shift=DOWN))
        self.next_section()
        self.wait()
        self.next_section()
        self.play(FadeIn(sensor_2, shift=DOWN))
        self.next_section()
        self.wait()
        self.next_section()
        self.play(FadeIn(sensor_3, shift=DOWN))
        self.next_section()
        self.wait()
        self.next_section()
        self.play(FadeIn(sensor_4, shift=DOWN))
        self.next_section()
        self.wait()
        self.next_section()
        self.play(Unwrite(title), FadeOut(sensor_1), FadeOut(sensor_2),
                  FadeOut(sensor_3), FadeOut(sensor_4))


class ResistanceEquation(Scene):
    def construct(self):
        text = Tex(r'$Z_1=\frac{V_{0} \times 10000}{5-V_{0}}$')
        self.play(Write(text))
        self.wait()
        self.play(Unwrite(text))


class ResistanceTable(Scene):
    def construct(self):
        table = Table([
            ['Direction (Degrees)', 'Resistance'],
            ['0', '33K'],
            ['22.5', '6.57K'],
            ['45', '8.2K'],
            ['67.5', '891'],
            ['90', '1K'],
            ['112.5', '688'],
            ['135', '2.2K'],
            ['157.5', '1.41K'],
            ['180', '3.9K'],
            ['202.5', '3.14K'],
            ['255', '16K'],
            ['247.5', '14.12K'],
            ['270', '120K'],
            ['292.5', '41.12K'],
            ['315', '64.9K'],
            ['337.5', '21.88K'],
        ])

        table.scale(0.25)

        self.play(Write(table))
        self.wait()
        self.play(Unwrite(table))


class Arrows(Scene):
    def construct(self):
        arrow = Arrow(LEFT, RIGHT)

        self.play(Create(arrow))
        self.next_section()
        self.wait()
        self.next_section()
        self.play(Uncreate(arrow))


class OtherText(Scene):
    def construct(self):
        vcc = Text('VCC')

        self.play(Write(vcc))
        self.next_section()
        self.wait()
        self.next_section()
        self.play(Unwrite(vcc))
        self.next_section()

        ground = Text('Ground')

        self.play(Write(ground))
        self.next_section()
        self.wait()
        self.next_section()
        self.play(Unwrite(ground))


class RainGaugeText(Scene):
    def construct(self):
        rain_gauge = Text('Rain Gauge', font_size=100, color=YELLOW)
        temp_rect = Rectangle(width=3.0,
                              height=6.0).set_stroke(opacity=0).to_edge(RIGHT)
        containing_rect = SurroundingRectangle(temp_rect).set_stroke(
            color=YELLOW, width=10.0)

        rain_gauge.next_to(temp_rect, LEFT)
        self.add(temp_rect)
        self.play(Write(rain_gauge), Write(containing_rect))
        self.wait()
        self.play(Unwrite(rain_gauge), Unwrite(containing_rect))


class WindSensorText(Scene):
    def construct(self):
        wind_sensor = Text('Wind sensor', font_size=100, color=GREEN)
        temp_rect = Rectangle(width=3.0,
                              height=6.0).set_stroke(opacity=0).to_edge(LEFT)
        containing_rect = SurroundingRectangle(
            temp_rect, color=GREEN).set_stroke(color=GREEN, width=10.0)

        wind_sensor.next_to(temp_rect, RIGHT)
        self.add(temp_rect)
        self.play(Write(wind_sensor), Write(containing_rect))
        self.wait()
        self.play(Unwrite(wind_sensor), Unwrite(containing_rect))


class WindDirectionSensorText(Scene):
    def construct(self):
        wind_sensor = Text('Wind Direction Sensor', font_size=75, color=GREEN)
        temp_rect = Rectangle(width=3.0,
                              height=6.0).set_stroke(opacity=0).to_edge(RIGHT)
        containing_rect = SurroundingRectangle(
            temp_rect, color=GREEN).set_stroke(color=GREEN, width=10.0)

        wind_sensor.next_to(temp_rect, LEFT)
        self.add(temp_rect)
        self.play(Write(wind_sensor), Write(containing_rect))
        self.wait()
        self.play(Unwrite(wind_sensor), Unwrite(containing_rect))


class ADCText(Scene):
    def construct(self):
        wind_sensor = Text('ADC', font_size=100, color=YELLOW)
        temp_rect = Rectangle(width=3.0,
                              height=5.0).set_stroke(opacity=0).to_edge(DOWN)
        containing_rect = SurroundingRectangle(
            temp_rect, color=GREEN).set_stroke(color=YELLOW, width=10.0)

        wind_sensor.next_to(temp_rect, UP)
        self.add(temp_rect)
        self.play(Write(wind_sensor), Write(containing_rect))
        self.wait()
        self.play(Unwrite(wind_sensor), Unwrite(containing_rect))


class FixedResitorText(Scene):
    def construct(self):
        wind_sensor = Text('Fixed Resistor', font_size=100, color=ORANGE)
        temp_rect = Rectangle(width=3.0,
                              height=5.0).set_stroke(opacity=0).to_edge(RIGHT)
        containing_rect = SurroundingRectangle(
            temp_rect, color=GREEN).set_stroke(color=ORANGE, width=10.0)

        wind_sensor.next_to(temp_rect, LEFT)
        self.add(temp_rect)
        self.play(Write(wind_sensor), Write(containing_rect))
        self.wait()
        self.play(Unwrite(wind_sensor), Unwrite(containing_rect))


class StevenScreenCopyright(Scene):
    def construct(self):
        text = Text('Model by RRacer, available under CC-BY', font_size=25)
        text.to_corner(DOWN + RIGHT)
        self.play(Write(text))
        self.wait()
        self.play(Unwrite(text))


class ImageNotFound(Scene):
    def construct(self):
        text = Text("image_not_found.png", font_size=100)
        self.play(Write(text))
        self.wait()
        self.play(Unwrite(text))


class PullDownNote(Scene):
    def construct(self):
        text = Text("* Pulldown resistors are enabled on most pins by default",
                    font_size=25)
        text.to_corner(DOWN + RIGHT)
        self.play(Write(text))
        self.wait()
        self.play(Unwrite(text))


class MicroclimateDefinition(Scene):
    def construct(self):
        title = Text("Microclimate", font_size=100).to_edge(LEFT)
        definition = Paragraph(
            "A small, local region having a unique pattern\nof weather or weather effects that differ from\nthe local climate"
        )
        credit = Text(
            "The American Heritage® Dictionary of the English Language, 5th Edition.",
            font_size=10,
            color=GRAY).to_edge(LEFT)

        VGroup(title, definition, credit).arrange(DOWN, center=True)

        self.play(Write(title), Write(definition), Write(credit))
        self.wait()
        self.play(Unwrite(title), Unwrite(definition), Unwrite(credit))


class TranscriptSources(Scene):
    def construct(self):
        text = Text("* Sources in transcript", font_size=25)
        text.to_corner(DOWN + RIGHT)
        self.play(Write(text))
        self.wait()
        self.play(Unwrite(text))