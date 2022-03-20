from tkinter import BOTTOM
from manim import *


class BasicCitation(Scene):
    def number(self) -> str:
        return ""

    def construct(self):
        number = self.number()
        text = Text(f"({number})", font_size=50).to_corner(DOWN + RIGHT)

        self.play(Write(text))
        self.wait(2)
        self.play(Unwrite(text, reverse=False))


class CitationIntro(BasicCitation):
    def number(self) -> str:
        return "Citations in description"


class Citation1(BasicCitation):
    def number(self) -> str:
        return "1"


class Citation2(BasicCitation):
    def number(self) -> str:
        return "2"


class Citation3(BasicCitation):
    def number(self) -> str:
        return "3"


class Citation4(BasicCitation):
    def number(self) -> str:
        return "4"


class Citation5(BasicCitation):
    def number(self) -> str:
        return "5"


class Citation6(BasicCitation):
    def number(self) -> str:
        return "6"


class Citation7(BasicCitation):
    def number(self) -> str:
        return "7"