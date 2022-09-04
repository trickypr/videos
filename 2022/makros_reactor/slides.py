import enum
from manim import *

__dirname = os.path.dirname(os.path.realpath(__file__))

tokens_str = open(__dirname + "/tokens.txt", "r").read()
tokens_ast = open(__dirname + "/ast.json", "r").read()
converted_str = open(__dirname + "/converted.py", "r").read()
out_str = open(__dirname + "/out.py", "r").read()

def set_defaults():
    Text.set_default(font="SauceCodePro NF")

class SceneHelper(Scene):
    def pause_section(self):
        self.next_section()
        self.wait()
        self.next_section()

class Slides(Scene):
    def construct(self):
        set_defaults()

        tokens = Text(tokens_str).scale(0.4)
        output = Text(tokens_ast).scale(0.3)

        group = VGroup(tokens, output).arrange(RIGHT, buff=1)

        token_copy = tokens.copy()

        self.play(FadeIn(tokens))
        self.next_section()
        self.wait()
        self.next_section()
        self.add(token_copy)
        self.play(ReplacementTransform(tokens, output))
        self.remove(tokens)
        self.next_section()
        self.wait()
        self.next_section()

        self.play(FadeOut(token_copy), output.animate.to_edge(LEFT))

        del tokens, group, token_copy

        self.next_section()
        self.wait()
        self.next_section()

        converted = Text(converted_str).scale(0.3)
        group = VGroup(output, converted).arrange(RIGHT, buff=1)

        output_copy = output.copy()

        self.add(output_copy)
        self.play(Transform(output, converted))
        self.next_section()
        self.wait()
        self.next_section()
        self.remove(output)

        self.play(FadeOut(output_copy), FadeOut(group))
        self.wait()

class Mixins(Scene):
    def construct(self):
        set_defaults()

        enum_token_text = Text("NAME      'enum'", color="black").scale(0.4)
        token_rect = SurroundingRectangle(enum_token_text)

        self.add(enum_token_text)

        self.play(Write(token_rect))
        self.next_section()
        self.wait()
        self.next_section()
        self.play(Unwrite(token_rect))
        self.remove(enum_token_text)

        del enum_token_text, token_rect

        self.next_section()

        ast_name_text = Text("\"name\": \"Animals\",", color="black").scale(0.3)
        ast_rect = SurroundingRectangle(ast_name_text)

        self.add(ast_name_text)
        
        self.play(Write(ast_rect))
        self.next_section()
        self.wait()
        self.next_section()
        self.play(Unwrite(ast_rect))
        self.remove(ast_name_text)

        del ast_name_text, ast_rect
        self.next_section()

        attr_text = Text('"options": [\n    { "case": "Cat", "arguments": [] },\n    { "case": "Dog", "arguments": [] },\n    {\n      "case": "Other",\n      "arguments": [{ "name": "name", "type": "str" }]\n    }\n')
        attr_text.scale(0.3)
        attr_rect = SurroundingRectangle(attr_text)

        self.play(Write(attr_rect))
        self.next_section()
        self.wait()
        self.next_section()
        self.play(Unwrite(attr_rect))

        del attr_rect, attr_text

        self.next_section()

class TitleSlides(SceneHelper):
    def construct(self):
        title = Text("Extending Python With Macros")

        self.play(FadeIn(title))
        self.pause_section()
        self.play(FadeOut(title))

class BootstrappingSlides(SceneHelper):
    def construct(self):
        set_defaults()

        title = Text("Bootstrapping", weight=BOLD)
        title.to_edge(UP)

        self.play(FadeIn(title))
        self.pause_section()

        step_1 = Text("Write a compiler in a different language")
        step_2 = Text("Add more features using your new language")
        step_3 = Text("Use the new features to add more complex features")

        group = VGroup(step_1, step_2, step_3)
        group.arrange(DOWN, buff=1).scale(0.5)

        self.play(FadeIn(step_1))
        self.pause_section()
        self.play(FadeIn(step_2))
        self.pause_section()
        self.play(FadeIn(step_3))
        self.pause_section()

        self.play(FadeOut(group), FadeOut(title))

class EndSlides(Scene):
    def construct(self):
        set_defaults()

        repo = Text("https://github.com/trickypr/makros")
        install = Text("pip3 install makros")

        group = VGroup(repo, install).arrange(DOWN, buff=1)

        self.play(FadeIn(group))
        self.next_section()
        self.wait()
        self.next_section()
        self.play(FadeOut(group))

