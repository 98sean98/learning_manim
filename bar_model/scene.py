from abc import ABC

from manim import *


class MyText(Text, ABC):
    def __init__(self, text: str, **kwargs):
        kwargs = {"text": text, "font": "Helvetica Neue", "font_size": 32, **kwargs}
        super().__init__(**kwargs)


class BarModelScene(Scene):
    def construct(self):
        height = 1
        width_ratio = 0.3

        line = Line(start=[-2.5, 2, 0], end=[-2.5, -2, 0], color=WHITE)

        bar_a = (
            Rectangle(height=height, width=width_ratio * 14, color=BLUE)
            .shift(UP)
            .align_to(line, LEFT)
        )
        bar_b = (
            Rectangle(height=height, width=width_ratio * 9, color=RED)
            .shift(DOWN)
            .align_to(line, LEFT)
        )

        text_a = (
            MyText("Mary")
            .move_to(bar_a.get_center())
            .align_to(line, RIGHT)
            .shift(LEFT * 0.2)
        )
        text_b = (
            MyText("George")
            .move_to(bar_b.get_center())
            .align_to(line, RIGHT)
            .shift(LEFT * 0.2)
        )

        bar_group = Group(line, bar_a, bar_b, text_a, text_b)

        self.play(Create(line))
        self.bring_to_back(bar_a, bar_b)
        self.play(Create(bar_a), Create(bar_b))
        self.play(AddTextLetterByLetter(text_a), AddTextLetterByLetter(text_b))

        self.wait()

        self.play(Indicate(bar_a, color=bar_a.get_color()))

        self.wait()

        brace_total = Brace(bar_group, direction=RIGHT, buff=MED_LARGE_BUFF)
        self.play(FadeIn(brace_total))

        self.wait()

        brace_text = MyText("23", color=GREEN).next_to(brace_total, RIGHT)
        self.play(FadeIn(brace_text))
        self.play(
            Indicate(brace_text, color=GREEN),
            Indicate(bar_a, color=bar_a.get_color()),
            Indicate(bar_b, color=bar_b.get_color()),
        )

        self.wait()

        x_coord = bar_b.get_right()[0]
        line_a_split = Line(
            start=[x_coord, 1, 0], end=[x_coord, 0, 0], color=BLUE
        ).align_to(bar_a, UP)

        bar_a_1 = (
            Rectangle(height=height, width=width_ratio * 9, color=BLUE)
            .align_to(bar_a, LEFT)
            .align_to(bar_a, UP)
        )
        bar_a_2 = Rectangle(
            height=height, width=width_ratio * (14 - 9), color=BLUE
        ).next_to(bar_a_1, RIGHT, buff=0)

        text_a_split = MyText("5", color=GREEN).move_to(bar_a_2.get_center())

        self.play(Create(line_a_split), FadeIn(text_a_split))

        self.add(bar_a_2, bar_a_1)
        self.bring_to_back(bar_a_2, bar_a_1)
        self.remove(bar_a, line_a_split)

        self.wait()

        text_a_1_part = MyText("1 part").move_to(bar_a_1.get_center())
        text_b_1_part = MyText("1 part").move_to(bar_b.get_center())

        self.play(
            AddTextLetterByLetter(text_a_1_part), AddTextLetterByLetter(text_b_1_part)
        )

        self.wait()

        text_calc_1_part_1 = MyText("1 part = ")
        text_calc_1_part_2 = MyText("?").next_to(text_calc_1_part_1, RIGHT)
        text_calc_1_part_group = Group(text_calc_1_part_1, text_calc_1_part_2).next_to(
            bar_group, DOWN, buff=LARGE_BUFF
        )

        self.play(AddTextLetterByLetter(text_calc_1_part_1))
        self.play(AddTextLetterByLetter(text_calc_1_part_2))

        self.wait()

        brace_text_split = MyText("- 5", color=YELLOW).next_to(
            brace_text, RIGHT, buff=SMALL_BUFF
        )
        brace_text_result = MyText("18", color=GREEN).next_to(brace_total, RIGHT)

        self.play(
            FadeToColor(bar_a_2, YELLOW),
            FadeToColor(text_a_split, YELLOW),
            AddTextLetterByLetter(brace_text_split),
        )

        self.wait()

        self.play(
            bar_a_2.animate.fade(1.0),
            FadeOut(text_a_split, brace_text, brace_text_split),
            FadeIn(brace_text_result),
        )

        self.wait()

        self.play(
            Indicate(bar_a_1, color=bar_a_1.get_color()),
            Indicate(bar_b, color=bar_b.get_color()),
            Indicate(brace_text_result, color=GREEN),
        )

        self.wait()

        text_calc_2_part = MyText("2 parts = 18", t2c={"18": GREEN}).next_to(
            bar_group, DOWN, buff=LARGE_BUFF
        )

        self.play(text_calc_1_part_group.animate.shift(DOWN))

        self.play(AddTextLetterByLetter(text_calc_2_part))

        self.wait()

        text_calc_1_part_3 = MyText("9", color=GREEN).move_to(
            text_calc_1_part_2.get_center()
        )

        self.play(FadeOut(text_calc_1_part_2), FadeIn(text_calc_1_part_3))

        self.wait()

        self.play(
            FadeOut(
                line,
                text_a,
                text_a_1_part,
                bar_a_1,
                brace_total,
                brace_text_result,
                text_calc_2_part,
            )
        )

        self.wait()

        group_b = Group(bar_b, text_b, text_b_1_part)
        group_calc = Group(text_calc_1_part_1, text_calc_1_part_3)

        self.play(
            group_b.animate.move_to(ORIGIN),
            group_calc.animate.move_to(ORIGIN).shift(DOWN * 2),
        )

        self.wait()

        text_b_final = MyText("9", color=GREEN).move_to(text_b_1_part.get_center())

        self.play(FadeOut(group_calc, text_b_1_part), FadeIn(text_b_final))

        self.wait()
