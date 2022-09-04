from typing import Tuple
from manim import *

__dirname = os.path.dirname(os.path.realpath(__file__))


def to_valid_tex(raw: str) -> str:
    return (
        raw.replace("_", "\\_")
        .replace("|", "\\textbar ")
        .replace("<", "\\textlangle ")
        .replace(">", "\\textrangle ")
        .replace("\n", "\\leavevmode \\\\")
        .split("")
    )


raw_code = open(__dirname + "/example.py", "r").read()
raw_tokens = open(__dirname + "/tokens.txt", "r").read().split("\n")
raw_bnf = to_valid_tex(open(__dirname + "/syntax.bnf", "r").read())
raw_ast = open(__dirname + "/ast.json", "r").read()
raw_errors = open(__dirname + "/errors.txt", "r").read().split("\nNEXT\n")


def set_defaults():
    Text.set_default(font="SauceCodePro NF")
    Code.set_default(font="SauceCodePro NF")


class Slides(Scene):
    def util_title(self, title_str: str) -> Text:
        title = Text(title_str)
        title.to_corner(UP + LEFT)
        self.play(FadeIn(title))
        self.next_section()

        return title

    def slide_001_title(self):
        title = Text("Writing Macros In Python")

        self.play(FadeIn(title))
        self.next_section()
        self.play(FadeOut(title))
        self.next_section()

    def slide_002_python_code(self) -> Code:
        code = Code(code=raw_code, language="Python")

        self.play(FadeIn(code))
        self.next_section()

        return code

    def slide_003_tokens(self, code: Code) -> Code:
        tokens = Paragraph(*raw_tokens).scale(0.3)

        self.play(ReplacementTransform(code, tokens))
        self.next_section()

        return tokens

    def slide_004_bnf(self, tokens: Code) -> None:
        bnf = Tex(*raw_bnf, tex_environment="flushleft").scale(0.5)
        print(bnf)
        print(bnf[0])

        self.play(FadeOut(tokens))
        self.play(FadeIn(bnf))
        self.next_section()

        name_rect = SurroundingRectangle(bnf[0])
        pattern_rect = SurroundingRectangle(bnf[2])

        name_text = Text("Name").scale(0.3).next_to(name_rect, DOWN, buff=0.05)
        pattern_text = Text("Pattern").scale(0.3).next_to(pattern_rect, DOWN, buff=0.05)

        self.play(
            Write(name_rect),
            Write(pattern_rect),
            FadeIn(name_text),
            FadeIn(pattern_text),
        )
        self.next_section()

        or_rect = SurroundingRectangle(bnf[8])
        or_text = Text("or").scale(0.3).next_to(or_rect, DOWN, buff=0.05)

        self.play(
            ReplacementTransform(name_rect, or_rect),
            ReplacementTransform(name_text, or_text),
            FadeOut(pattern_rect),
            FadeOut(pattern_text),
        )
        self.next_section()

        loop_rect = SurroundingRectangle(bnf[6])
        loop_text = Text("Loop").scale(0.3).next_to(loop_rect, RIGHT, buff=0.05)

        self.play(
            ReplacementTransform(or_rect, loop_rect),
            ReplacementTransform(or_text, loop_text),
        )
        self.next_section()

        self.play(Unwrite(loop_rect), FadeOut(loop_text))
        self.next_section()

        name_rect = SurroundingRectangle(bnf[0])

        self.play(Write(name_rect))
        self.next_section()

        self.play(ReplacementTransform(name_rect, pattern_rect))
        self.next_section()

        self.play(FadeOut(pattern_rect))

        tokens.to_edge(LEFT)
        self.play(FadeIn(tokens), bnf.animate.to_edge(RIGHT))

        def_tokens_rect = SurroundingRectangle(tokens[1:8])
        def_rule_rect = SurroundingRectangle(bnf[4])

        self.play(Write(def_tokens_rect), Write(def_rule_rect))
        self.next_section()

        self.play(FadeOut(def_tokens_rect), FadeOut(def_rule_rect))
        self.play(FadeOut(tokens), FadeOut(bnf))

    def slide_005_ast(self):
        ast = Paragraph(raw_ast).scale(0.5)

        self.play(FadeIn(ast))
        self.next_section()

        self.play(FadeOut(ast))

    def slide_006_macros(self):
        title = self.util_title("Macros")

        definition = Text("Takes in code, splits out (different) code").scale(0.7)
        self.play(FadeIn(definition))
        self.next_section()

        step_1 = Text("1. Find the trigger token")
        step_2 = Text("2. Pass it into the macro's parser")
        step_3 = Text("3. Convert into Python code")
        step_4 = Text("4. Insert back into file")
        step_5 = Text("5. Repeat")

        group = Group(step_1, step_2, step_3, step_4, step_5)
        group.scale(0.7).arrange(DOWN, aligned_edge=LEFT)

        self.play(FadeOut(definition))
        self.play(FadeIn(step_1))
        self.next_section()

        self.play(FadeIn(step_2))
        self.next_section()

        self.play(FadeIn(step_3))
        self.next_section()

        self.play(FadeIn(step_4))
        self.play(FadeIn(step_5))
        self.next_section()

        self.play(FadeOut(group), FadeOut(title))
        self.wait()
        self.next_section()

    def slide_007_requirements(self):
        title = self.util_title("Features")

        goal_1 = Text("Parsing & translating macro files")
        goal_2 = Text("Include a couple of macros")
        goal_3 = Text("Publish to PyPI")
        goal_4 = Text("Generate docs")

        group = Group(goal_1, goal_2, goal_3, goal_4)
        group.scale(0.7).arrange(DOWN, aligned_edge=LEFT)

        self.play(FadeIn(goal_1))
        self.next_section()

        self.play(FadeIn(goal_2))
        self.next_section()

        self.play(FadeIn(goal_3))
        self.next_section()

        self.play(FadeIn(goal_4))
        self.next_section()

        # Animate each fading to green
        self.play(*[goal.animate.set_color(GREEN) for goal in group])
        self.next_section()

        self.play(FadeOut(title), FadeOut(group))

    def slide_008_user_experience(self) -> Tuple[Text, Text]:
        title = self.util_title("User Experience")

        original = Text("makros example.mpy").scale(0.7)
        trial = Text("makros run example.mpy").scale(0.7)
        back = Text("makros example.mpy").scale(0.7)

        self.play(FadeIn(original))
        self.next_section()

        self.play(ReplacementTransform(original, trial))
        self.next_section()

        self.play(ReplacementTransform(trial, back))
        self.next_section()

        return (title, back)

    def slide_009_convert_flag(self, command: Text):
        new_command = Text("makros example.mpy --convert").scale(0.7)

        self.play(ReplacementTransform(command, new_command))
        self.next_section()

        self.play(FadeOut(new_command))

    def slide_010_errors(self, title: Text):
        error = Paragraph(*(raw_errors[0]).split("\n")).scale(0.5)
        self.play(FadeIn(error))

        for error_text in raw_errors[1:]:
            new_error = Paragraph(*(error_text).split("\n")).scale(0.5)
            self.play(ReplacementTransform(error, new_error))
            error = new_error

        self.next_section()

        self.play(FadeOut(title), FadeOut(error))

    def slide_011_naming(self):
        title = self.util_title("Naming")

        self.play(FadeIn(title))
        self.next_section()

        self.play(FadeOut(title))

    def construct(self):
        set_defaults()

        self.slide_001_title()
        code = self.slide_002_python_code()
        tokens = self.slide_003_tokens(code)

        self.slide_004_bnf(tokens)
        self.slide_005_ast()
        self.slide_006_macros()

        # Example goes here

        print("Slide 7")
        self.slide_007_requirements()
        print("Slide 8")
        ux_title, command = self.slide_008_user_experience()
        print("slide 9")
        self.slide_009_convert_flag(command)
        print("slide 10")
        self.slide_010_errors(ux_title)

        self.wait()
