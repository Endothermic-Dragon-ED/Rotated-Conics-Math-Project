import numpy as np
from manim import *

# Helpful guide: https://azarzadavila-manim.readthedocs.io/en/latest/animation.html
class Intro(Scene):
    def construct(self):
        point = Dot(point=np.array([0, 0.0, 0.0]))
        gr = VGroup(point)
        self.add(gr)
        self.wait()
        grid = NumberPlane(
            x_range=[-7, 13, 1],
            y_range=[-3, 7, 1],
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.6
            })
        self.play(
            gr.animate.shift(UP, RIGHT),
            Create(grid, run_time=2, lag_ratio=0.015)
        )
        self.wait()
        self.play(
            gr.animate(
                run_time=0.8,
                rate_func=rate_functions.ease_in_out_sine
            ).rotate(
                angle=0.4,
                about_point=[-3,-2,0],
            )
        )
        self.wait()