from manim import *

from diagrams import PoissonVsBinomial


class Slides(Scene):
    def construct(self):
        # Blank starting section
        self.wait()

        self.next_section()

        # Question
        question = Tex(
            "\\centering {On average, my blog will get around 168 views per week. What is the probability that I will get 0 views in a week?}"
        )
        question.scale(0.7)

        self.play(FadeIn(question))

        self.next_section()
        # Formulas

        binomial_formula = MathTex("Pr(X=x) = \\binom{n}{x} p^{x}(1-p)^{n-x}").scale(
            0.7
        )
        binomial_mean = MathTex("\\mu = n p").scale(0.7)
        e_def = MathTex(
            "e^x = \\lim_{n \\to \\infty} \\left(1 + \\frac xn\\right)^n"
        ).scale(0.7)

        formulas = VGroup(binomial_formula, binomial_mean, e_def).arrange(RIGHT, buff=1)
        formulas.next_to(question, DOWN)

        self.play(FadeIn(formulas))

        self.next_section()

        # Focus mean

        mean_box = SurroundingRectangle(binomial_mean)
        self.play(Create(mean_box))

        self.next_section()

        # Focus binomial formula

        binomial_formula_box = SurroundingRectangle(binomial_formula)
        self.play(ReplacementTransform(mean_box, binomial_formula_box))
        self.next_section()

        # Focus e_def

        e_box = SurroundingRectangle(e_def)
        self.play(ReplacementTransform(binomial_formula_box, e_box))

        self.next_section()

        # Poisson distribution formula
        self.play(FadeOut(formulas), FadeOut(question), FadeOut(e_box))

        title = Text("Poisson distribution")
        title.to_corner(UP + LEFT)

        poisson_formula = MathTex(
            "Pr(X=x) = \\frac{e^{-\\lambda} \\lambda^x}{x!}"
        ).scale(0.7)
        mean_formula = MathTex("\\mu = \\lambda").scale(0.7)
        variance_formula = MathTex("\\sigma^2 = \\lambda").scale(0.7)

        formulas = VGroup(poisson_formula, mean_formula, variance_formula)
        formulas.arrange(DOWN, buff=1)

        self.play(FadeIn(title), FadeIn(poisson_formula))
        self.next_section()

        # Show the mean formula
        self.play(FadeIn(mean_formula))
        self.next_section()

        # Show the variance formula
        self.play(FadeIn(variance_formula))
        self.next_section()

        # Clear the screen
        self.play(FadeOut(title), FadeOut(formulas))
        del title, formulas, poisson_formula, mean_formula, variance_formula
        self.next_section()

        # Black magic graph scene
        PoissonVsBinomial.construct(self)
        self.next_section()

        # Go over the derivation of the geometric distribution
        formula_1 = MathTex(r"X = \text{Number of trials to get your first success}")
        formula_2 = MathTex(r"Pr(X=x) = (1-p)^{x-1} p")
        formula_3 = MathTex(r"p = \frac{\lambda}{n}")
        formula_4 = MathTex(r"Y = \text{Amount of time to get your first success}")
        formula_5 = MathTex(
            r"Pr(Y=y) = \left(1-\frac{\lambda}{n} \right)^{yn-1} \left(\frac{\lambda}{n} \right)"
        )  # Note: yn is equivalent to x
        formula_6 = MathTex(r"p = \frac{\lambda}{n}")
        formula_7 = MathTex(
            r"\lim_{n \to \infty} \left(1-\frac{\lambda}{n} \right)^{yn-1} \left(\frac{\lambda}{n} \right)"
        )
        formula_8 = MathTex(
            r"=\left[ \lim_{n \to \infty} \left(1-\frac{\lambda}{n} \right)^n \right]^y"
        )
        formula_9 = MathTex(r"=e^{-\lambda y}")

        formulas = VGroup(
            formula_1,
            formula_2,
            formula_3,
            formula_4,
            formula_5,
            formula_6,
            formula_7,
            formula_8,
            formula_9,
        )
        formulas.arrange(DOWN)
        formulas.scale(0.7)

        self.play(FadeIn(formulas))
        self.next_section()

        self.play(FadeOut(formulas))
