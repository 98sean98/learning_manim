from manim import *


class BarModelScene(Scene):
    def construct(self):
        height = 1
        width_ratio = 0.3

        line = Line(start=[-2.5, -2, 0], end=[-2.5, 2, 0], color=WHITE)

        bar_a = Rectangle(height=height, width=width_ratio * 14, color=BLUE).shift(UP).align_to(line, LEFT)
        bar_b = Rectangle(height=height, width=width_ratio * 9, color=RED).shift(DOWN).align_to(line, LEFT)

        text_a = Text("Mary", font_size=32).move_to(bar_a.get_center()).align_to(line, RIGHT).shift(LEFT * 0.2)
        text_b = Text("George", font_size=32).move_to(bar_b.get_center()).align_to(line, RIGHT).shift(LEFT * 0.2)

        self.play(Create(line))
        self.bring_to_back(bar_a, bar_b)
        self.play(Create(bar_a), Create(bar_b))
        self.play(Create(text_a), Create(text_b))

        self.wait()

        x_coord = bar_b.get_right()[0]
        line_a_split = Line(start=[x_coord, 1, 0], end=[x_coord, 0, 0], color=BLUE).align_to(bar_a, UP)

        bar_a_1 = Rectangle(height=height, width=width_ratio * 9, color=BLUE).align_to(bar_a, LEFT).align_to(bar_a, UP)
        bar_a_2 = Rectangle(height=height, width=width_ratio * (14 - 9), color=BLUE).next_to(bar_a_1, RIGHT, buff=0)

        text_a_split = Text("5", font_size=32).move_to(bar_a_2.get_center())

        self.play(Create(line_a_split), Create(text_a_split))

        self.add(bar_a_1, bar_a_2)
        self.bring_to_back(bar_a_1, bar_a_2)
        self.remove(bar_a)

        self.wait()
