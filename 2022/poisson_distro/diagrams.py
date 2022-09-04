import math
from manim import *

import numpy as np


def factorial(n):
    if n < 0:
        return 1

    if n == 0:
        return 1

    return n * factorial(n - 1)


def poisson_pr(x, lamb):
    x = math.floor(x)

    return (lamb**x) * math.exp(-lamb) / factorial(x)


def binomial_pr(x, n, p):
    x = math.floor(x)

    if n - x < 0:
        return 0

    return math.comb(n, x) * (p**x) * ((1 - p)**(n - x))


def create_value_labels(n, p) -> VGroup:
    n_label = Text("n = " + str(n))
    p_label = Text("p = {:.2f}".format(p))

    labels = VGroup(n_label, p_label)
    labels.arrange(DOWN, buff=1)
    labels.to_corner(UP + RIGHT)

    return labels


class PoissonVsBinomial(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 10.3, 1],
            y_range=[0, 1, 0.1],
            x_length=10,
            tips=False,
            axis_config={"include_numbers": True},
        )
        axes_labels = axes.get_axis_labels('x', 'Pr(X=x)')

        poisson_graph = axes.plot(lambda x: poisson_pr(x, 2),
                                  color=BLUE,
                                  x_range=(0, 20),
                                  use_smoothing=False)
        poisson_label = Text("Poisson", color=BLUE).next_to(poisson_graph, UP)

        old_graph = axes.plot(lambda x: binomial_pr(x, 2, 1),
                              color=RED,
                              use_smoothing=False)
        binomial_label = Text("Binomial", color=RED).next_to(old_graph,
                                                             UP,
                                                             buff=-1)

        plot = VGroup(poisson_graph, old_graph)
        labels = VGroup(axes_labels, poisson_label, binomial_label)
        old_value_labels = create_value_labels(2, 1)

        self.play(Write(axes))
        self.play(Write(plot), Write(labels), Write(old_value_labels))

        self.next_section()

        # This is just a temporary value until we generate something better
        new_graph = axes.plot(lambda x: poisson_pr(x, 2))
        new_value_labels = create_value_labels(2, 1)

        for n in np.logspace(2, 40, num=20, base=1.1):
            n = math.floor(n)  # Numpy numbers are scary :(
            p = 2 / n

            # n values smaller than 2 do not graph correctly
            if n <= 2:
                continue

            new_value_labels = create_value_labels(n, p)
            new_graph = axes.plot(lambda x: binomial_pr(x, n, p),
                                  color=RED,
                                  use_smoothing=False)

            self.play(ReplacementTransform(old_graph, new_graph),
                      ReplacementTransform(old_value_labels, new_value_labels),
                      run_time=0.5)

            old_graph = new_graph
            old_value_labels = new_value_labels

        self.next_section()

        self.play(Unwrite(old_graph), Unwrite(labels), Unwrite(axes),
                  Unwrite(poisson_graph), Unwrite(old_value_labels))
