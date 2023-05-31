from manim import *


class CreatingMobjects(Scene):
    def construct(self):
        triangle = Triangle()

        self.add(triangle)
        self.wait()
        self.remove(triangle)
        self.wait()


class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)

        self.add(circle, square, triangle)
        self.wait()


class MobjectPlacement(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle(radius=0.5)

        circle.move_to(2 * RIGHT + DOWN)
        square.next_to(circle, UP + RIGHT)
        triangle.align_to(
            circle, DOWN
        )  # align with the bottom bounding edge of the circle
        triangle.align_to(
            square, RIGHT
        )  # align with the right bounding edge of the square

        self.add(circle, square, triangle)
        self.wait()

        # hot tip
        # many methods can be chained together
        # for example
        circle = Circle().move_to(
            2 * RIGHT + DOWN
        )  # because `move_to` class method returns `self`


class MobjectStyling(Scene):
    def construct(self):
        circle = Circle().shift(1.2 * LEFT)
        square = Square().shift(0.8 * UP)
        triangle = Triangle().shift(1.5 * RIGHT)

        circle.set_stroke(color=PURPLE_B, width=20)
        square.set_fill(RED, opacity=1.0)
        triangle.set_fill(GREEN, opacity=0.8).set_stroke(TEAL, width=10)

        self.add(circle, square, triangle)
        self.wait()


class MobjectZOrder(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        circle.set_stroke(color=PURPLE_B, width=20)
        square.set_fill(RED, opacity=1.0)
        triangle.set_fill(GREEN, opacity=0.8).set_stroke(TEAL, width=10)

        self.add(triangle, square, circle)
        # order of adding mobjects to the scene matters
        # the last one added will be on top, i.e. highest z-index
        self.wait()


class SomeAnimations(Scene):
    def construct(self):
        square = Square()

        self.play(FadeIn(square))
        # start with a fully transparent square
        # end with a square with opacity 1
        # interpolation: gradually increasing the opacity

        self.play(Rotate(square, PI / 4))
        # start with a square rotated by 0 degrees
        # end with a square rotated by 45 degrees, counter-clockwise
        # interpolation: gradually increasing the angle of rotation

        self.play(FadeOut(square))


class AnimateExample(Scene):
    def construct(self):
        square = Square().set_fill(RED, opacity=1.0)
        self.add(square)

        # any property of MObject that can be changed can be animated

        self.play(square.animate.set_fill(BLUE, opacity=1.0))

        self.play(square.animate.shift(UP).rotate(PI / 3))
        # use method chaining to shift and rotate at the same time
        # don't do this
        # self.play(square.animate.shift(UP), square.animate.rotate(PI / 3))
        # because it most likely won't work
        # in fact, only rotation is observed

        self.wait()


class RunTime(Scene):
    def construct(self):
        square = Square()

        self.add(square)

        self.play(square.animate.shift(DOWN), run_time=3)
        # by default, run_time of play() is 1 second

        self.wait(1)


# custom animation
# extending the Animation class
class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs):
        # pass number as the mobject of the animation
        super().__init__(number, **kwargs)

        # set start and end properties
        self.start = start
        self.end = end

    # override interpolate_mobject method
    def interpolate_mobject(self, alpha: float) -> None:
        # set value of DecimalNumber according to alpha
        value = self.start + (self.end - self.start) * alpha
        self.mobject.set_value(value)


class CountingScene(Scene):
    def construct(self):
        # create DecimalNumber mobject
        number = DecimalNumber().set_color(WHITE).scale(3)

        # add it to the scene
        self.add(number)

        # play the custom animation
        self.play(Count(number, 0.10, 0.99), run_time=3, rate_func=linear)
        self.wait()


class MobjectExample(Scene):
    def construct(self):
        p1 = [-1, -1, 0]
        p2 = [1, -1, 0]
        p3 = [1, 1, 0]
        p4 = [-1, 1, 0]

        a = (
            Line(p1, p2)
            .append_points(Line(p2, p3).points)
            .append_points(Line(p3, p4).points)
        )

        point_start = a.get_start()
        point_end = a.get_end()
        point_center = a.get_center()

        self.add(
            Text(f"a.get_start(): {np.round(point_start, 2).tolist()}", font_size=20)
            .to_edge(UR)
            .set_color(YELLOW)
        )
        self.add(
            Text(f"a.get_end(): {np.round(point_end, 2).tolist()}", font_size=20)
            .next_to(self.mobjects[-1], DOWN)
            .set_color(BLUE)
        )
        self.add(
            Text(f"a.get_center(): {np.round(point_center, 2).tolist()}", font_size=20)
            .next_to(self.mobjects[-1], DOWN)
            .set_color(RED)
        )

        self.add(Dot(a.get_start()).set_color(YELLOW).scale(2))
        self.add(Dot(a.get_end()).set_color(RED).scale(2))
        self.add(Dot(a.get_top()).set_color(GREEN_A).scale(2))
        self.add(Dot(a.get_bottom()).set_color(GREEN_D).scale(2))
        self.add(Dot(a.get_center()).set_color(BLUE).scale(2))
        self.add(Dot(a.point_from_proportion(0.25)).set_color(PURPLE).scale(2))

        self.add(*[Dot(x) for x in a.points])

        self.add(a)


class TransformExample(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        m1 = Square().set_color(RED)
        m2 = Rectangle().set_color(BLUE).rotate(-0.2)

        self.add(m1)
        self.wait()

        self.play(Transform(m1, m2))
        # transform function maps points of m1 to points of m2
        # this might result in strange behavior
        # example: when the points in m1 and m2 are not in the same order


class ExampleRotation(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        m1a = Square().set_color(RED).shift(LEFT)
        m1b = Circle().set_color(RED).shift(LEFT)
        m2a = Square().set_color(BLUE).shift(RIGHT)
        m2b = Circle().set_color(BLUE).shift(RIGHT)

        points = m2a.points  # size: (n, 3)
        points = np.roll(points, int(len(points) / 4), axis=0)
        # roll the (,3) elements of the array by 1/4 of n
        m2a.points = points

        self.play(Transform(m1a, m1b), Transform(m2a, m2b))


class CloserTransformation(Scene):
    def construct(self):
        square = Square().set_color(RED)
        circle = Circle().set_color(BLUE)

        circle.points = np.roll(circle.points, -int(len(circle.points) / 8), axis=0)
        # roll by -1/8 of 2 Pi radians

        self.add(square)
        self.play(Transform(square, circle))
