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

        # let's do a simple math problem
        self.play(Create(line))

        # Mary and George have some apples
        self.play(Write(text_a), Write(text_b))
        self.bring_to_back(bar_a, bar_b)
        self.play(Create(bar_a), Create(bar_b))

        self.wait()

        # they have 23 apples in total
        brace_total = Brace(bar_group, direction=RIGHT, buff=MED_LARGE_BUFF)
        brace_text = MyText("23", color=GREEN).next_to(brace_total, RIGHT)
        self.play(FadeIn(brace_total), FadeIn(brace_text))

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

        # Mary has 5 apples more than George
        self.play(Create(line_a_split), FadeIn(text_a_split))

        self.add(bar_a_2, bar_a_1)
        self.bring_to_back(bar_a_2, bar_a_1)
        self.remove(bar_a, line_a_split)

        self.wait()

        text_b_question = MyText("?").move_to(bar_b.get_center())

        # How many apples does George have?
        self.play(FadeIn(text_b_question))

        self.wait()

        self.play(FadeOut(text_b_question))

        text_a_1_part = MyText("1 part").move_to(bar_a_1.get_center())
        text_b_1_part = MyText("1 part").move_to(bar_b.get_center())

        # We start by labelling the equal parts between Mary and George
        self.play(Indicate(bar_a_1), Indicate(bar_b)) # labelling the equal parts
        # as 1 part each
        self.play(
            Write(text_a_1_part), Write(text_b_1_part)
        )

        self.wait()

        # So Mary has 1 part + 5 apples
        group_a = Group(bar_a_1, bar_a_2, text_a_1_part, text_a_split)
        self.play(Indicate(group_a)) # this might not work
        # whereas George only has 1 part
        self.play(Indicate(bar_b), Indicate(text_b_1_part))

        text_calc_1_part_1 = MyText("1 part = ")
        text_calc_1_part_2 = MyText("?").next_to(text_calc_1_part_1, RIGHT)
        text_calc_1_part_group = Group(text_calc_1_part_1, text_calc_1_part_2).next_to(
            bar_group, DOWN, buff=LARGE_BUFF
        )

        # Then we find out how many apples are in 1 part
        self.play(Write(text_calc_1_part_1))
        self.play(Write(text_calc_1_part_2))

        self.wait()

        brace_text_split = MyText("- 5", color=PURPLE).next_to(
            brace_text, RIGHT, buff=SMALL_BUFF
        )
        brace_text_result = MyText("18", color=GREEN).next_to(brace_total, RIGHT)

        # We do this by subtracting 5 apples from the total of 23
        self.play(
            FadeToColor(bar_a_2, PURPLE),
            FadeToColor(text_a_split, PURPLE),
            Write(brace_text_split),
        )

        self.wait()

        self.play(
            bar_a_2.animate.fade(1.0),
            FadeOut(text_a_split, brace_text, brace_text_split),
            FadeIn(brace_text_result),
        )

        self.wait()

        # Now, a total of 2 parts
        self.play(
            Indicate(bar_a_1),
            Indicate(bar_b),
            Indicate(brace_text_result),
        )

        self.wait()

        text_calc_2_part = MyText("2 parts = 18", t2c={"18": GREEN}).next_to(
            bar_group, DOWN, buff=LARGE_BUFF
        )

        # is equal to 18 apples
        self.play(text_calc_1_part_group.animate.shift(DOWN))
        self.play(Write(text_calc_2_part))

        self.wait()

        text_calc_1_part_3 = MyText("9", color=GREEN).move_to(
            text_calc_1_part_2.get_center()
        )

        # We divide 18 apples into 2 equal parts to get 9 apples for each part
        self.play(FadeOut(text_calc_1_part_2), FadeIn(text_calc_1_part_3, scale=2.0))

        self.wait()

        group_b = Group(bar_b, text_b, text_b_1_part)
        group_calc = Group(text_calc_1_part_1, text_calc_1_part_3)

        # Therefore, George, who has 1 part
        self.play(
            FadeOut(
                line,
                text_a,
                text_a_1_part,
                bar_a_1,
                brace_total,
                brace_text_result,
                text_calc_2_part,
            ),
        )
        # has 9 apples
        self.play(
            group_b.animate.move_to(ORIGIN),
            group_calc.animate.move_to(ORIGIN).shift(DOWN * 2),
        )

        self.wait()

        text_b_final = MyText("9", color=GREEN).move_to(text_b_1_part.get_center())

        # And the problem is solved
        self.play(FadeOut(group_calc, text_b_1_part), FadeIn(text_b_final))

        self.wait()
