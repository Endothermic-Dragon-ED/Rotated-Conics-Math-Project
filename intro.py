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
      x_range=[-6.6, 4.6, 1],
      y_range=[-3, 7, 1],
      background_line_style={
        "stroke_color": TEAL,
        "stroke_width": 4,
        "stroke_opacity": 0.6
      }).shift([-4,0,0])
    self.play(
      gr.animate.shift(UP, RIGHT),
      Create(grid, run_time=2, lag_ratio=0.015)
    )
    self.wait()
    coords = Tex(r"(x, y)", font_size=60).move_to([1,1.75,0])
    xTex = Tex(r"x", font_size=60).move_to([-1,-2.75,0])
    yTex = Tex(r"y", font_size=60).move_to([1.75,-0.5,0])
    xLine = Line((-3,-2,0),(1,-2,0))
    yLine = Line((1,-2,0),(1,1,0))
    xLine.stroke_width=10
    yLine.stroke_width=10
    self.play(
      FadeIn(coords, shift=DOWN),
      FadeIn(xTex, shift=UP),
      FadeIn(yTex, shift=LEFT),
      Create(xLine),
      Create(yLine)
    )
    self.wait()
    gr += xLine
    gr += yLine
    # Label coordinate
    # Label x and y
    # Add x and y labels to group gr
    # Transform coordinate label from (x,y) to (x', y')
    theta = 0.4
    self.play(
      gr.animate(
        run_time=0.8,
        rate_func=rate_functions.ease_in_out_sine
      ).rotate(
        angle=theta,
        about_point=[-3,-2,0]
      ),
      VGroup(coords).animate(
        run_time=0.8,
        rate_func=rate_functions.ease_in_out_sine
      ).shift(
        [
          4*np.cos(theta) - 3*np.sin(theta) - 4,
          4*np.sin(theta) + 3*np.cos(theta) - 3,
          0
        ]
      ),
      VGroup(xTex).animate(
        run_time=0.8,
        rate_func=rate_functions.ease_in_out_sine
      ).shift(
        [
          2*np.cos(theta) - 2,
          2*np.sin(theta),
          0
        ]
      ),
      VGroup(yTex).animate(
        run_time=0.8,
        rate_func=rate_functions.ease_in_out_sine
      ).shift(
        [
          4*np.cos(theta) - 1.5*np.sin(theta) - 4,
          4*np.sin(theta) + 1.5*np.cos(theta) - 1.5,
          0
        ]
      )
    )
    coordsNew = Tex(r"(x', y')", font_size=60).move_to([1,1.75,0]).shift(
      [
        4*np.cos(theta) - 3*np.sin(theta) - 4,
        4*np.sin(theta) + 3*np.cos(theta) - 3,
        0
      ]
    )
    self.play(
      Transform(coords, coordsNew)
    )
    # Draw sub-legs and theta
    # Label lengths of sub-legs
    # Write equations on the side
    self.wait()