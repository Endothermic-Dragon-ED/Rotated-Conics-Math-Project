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
    coords = MathTex(r"(x, y)", font_size=60).move_to([1,1.75,0])
    xTex = MathTex(r"x", font_size=60).move_to([-1,-2.75,0])
    yTex = MathTex(r"y", font_size=60).move_to([1.75,-0.5,0])
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
      ).shift([-2.75,0.5,0]),
      VGroup(xTex).animate(
        run_time=0.8,
        rate_func=rate_functions.ease_in_out_sine
      ).shift(
        [
          0,
          2.25,
          0
        ]
      ),
      VGroup(yTex).animate(
        run_time=0.8,
        rate_func=rate_functions.ease_in_out_sine
      ).shift(
        [
          -2.25,
          1.5,
          0
        ]
      )
    )
    coordsNew = MathTex(r"(x', y')", font_size=60).move_to([-1.75,2.25,0])
    self.play(
      Transform(coords, coordsNew)
    )
    self.wait()
    angle1 = Arc(0.9, 0, theta, arc_center=[-3,-2,0])
    angle2 = Arc(0.9, PI/2, theta, arc_center=
      [
        4*np.cos(theta) - 3,
        4*np.sin(theta) - 2,
        0
      ]
    )
    line1 = Line([-3,-2,0],
      [
        4*np.cos(theta) - 3,
        -2,
        0
      ]
    )
    line2 = Line(
      [
        4*np.cos(theta) - 3,
        -2,
        0
      ],
      [
        4*np.cos(theta) - 3,
        4*np.sin(theta) - 2,
        0
      ]
    )
    line3 = Line(
      [
        4*np.cos(theta) - 3,
        4*np.sin(theta) - 2,
        0
      ],
      [
        4*np.cos(theta) - 3,
        4*np.sin(theta) + 3*np.cos(theta) - 2,
        0
      ]
    )
    line4 = Line(
      [
        4*np.cos(theta) - 3,
        4*np.sin(theta) + 3*np.cos(theta) - 2,
        0
      ],
      [
        4*np.cos(theta) - 3*np.sin(theta) - 3,
        4*np.sin(theta) + 3*np.cos(theta) - 2,
        0
      ]
    )

    angle1.stroke_width=5
    angle2.stroke_width=5
    line1.stroke_width=7
    line2.stroke_width=7
    line3.stroke_width=7
    line4.stroke_width=7

    angle1.stroke_color=RED
    angle2.stroke_color=RED
    line1.stroke_color=RED
    line2.stroke_color=RED
    line3.stroke_color=RED
    line4.stroke_color=RED

    thetaTex1 = MathTex(r"\theta", font_size=60).move_to([-1.3,-1.65,0])
    thetaTex2 = MathTex(r"\theta", font_size=60).move_to([0.45,0.9,0])
    thetaTex1.color=RED
    thetaTex2.color=RED
    self.play(
      Create(angle1),
      Create(angle2),
      Create(line1),
      Create(line2),
      Create(line3),
      Create(line4),
      FadeIn(thetaTex1, shift=LEFT),
      FadeIn(thetaTex2, shift=DOWN)
    )
    self.wait()

    xComp1 = MathTex(r"x\cos(\theta)", font_size=50).move_to([-1,-2.5,0])
    xComp2 = MathTex(r"x\sin(\theta)", font_size=50).move_to([1.75,-1.25,0])
    yComp1 = MathTex(r"y\cos(\theta)", font_size=50).move_to([1.75,1,0])
    yComp2 = MathTex(r"y\sin(\theta)", font_size=50).move_to([0,2.75,0])
    xComp1.color=RED
    xComp2.color=RED
    yComp1.color=RED
    yComp2.color=RED
    self.play(Write(xComp1))
    self.play(Write(xComp2))
    self.play(Write(yComp1))
    self.play(Write(yComp2))
    self.wait()
    formula1 = MathTex(r"x'=x\cos(\theta)-y\sin(\theta)", font_size=45).move_to([4.3,3,0])
    formula2 = MathTex(r"y'=x\sin(\theta)+y\cos(\theta)", font_size=45).move_to([4.3,2,0])
    self.play(Write(formula1))
    self.play(Write(formula2))
    self.wait()


class GeneralizeConicFormulas(Scene):
  def construct(self):
    eqs1_g = {"font_size": 40}
    arrowTemplate = MathTex(r"=>", **eqs1_g)
    eqs1 = [
      MathTex(r"(x-h)^2 + (y-k)^2 = r^2", **eqs1_g),
      MathTex(r"\frac{(x-h)^2}{a^2} + \frac{(y-k)^2}{b^2} = 1", **eqs1_g),
      MathTex(r"\frac{(x-h)^2}{b^2} + \frac{(y-k)^2}{a^2} = 1", **eqs1_g),
      MathTex(r"\frac{(x-h)^2}{a^2} - \frac{(y-k)^2}{b^2} = 1", **eqs1_g),
      MathTex(r"-\frac{(x-h)^2}{b^2} + \frac{(y-k)^2}{a^2} = 1", **eqs1_g)
    ]
    self.play(
      *[Write(eqs1[i].shift([-4,(2-i)*1.5,0])) for i in range(len(eqs1))]
    )
    arrows = [arrowTemplate.copy() for i in range(5)]
    self.wait()
    self.play(
      *[FadeIn(arrows[i].shift([-1,(2-i)*1.5,0]), shift=RIGHT) for i in range(len(arrows))]
    )
    self.wait()
    eqs2 = [
      MathTex(r"x^2-2xh+h^2 + y^2-2yk+k^2 = r^2", **eqs1_g),
      MathTex(r"\frac{x^2-2xh+h^2}{a^2} + \frac{y^2-2yk+k^2}{b^2} = 1", **eqs1_g),
      MathTex(r"\frac{x^2-2xh+h^2}{b^2} + \frac{y^2-2yk+k^2}{a^2} = 1", **eqs1_g),
      MathTex(r"\frac{x^2-2xh+h^2}{a^2} - \frac{y^2-2yk+k^2}{b^2} = 1", **eqs1_g),
      MathTex(r"-\frac{x^2-2xh+h^2}{b^2} + \frac{y^2-2yk+k^2}{a^2} = 1", **eqs1_g)
    ]
    self.play(
      *[Write(eqs2[i].shift([3,(2-i)*1.5,0])) for i in range(len(eqs2))]
    )
    self.play(
      *[FadeOut(eqs1[i], shift=RIGHT) for i in range(len(eqs1))],
      *[FadeOut(arrows[i], shift=RIGHT) for i in range(len(arrows))],
      *[eqs2[i].animate.shift([-6.5,0,0]) for i in range(len(eqs2))]
    )
    arrows = [arrowTemplate.copy() for i in range(5)]
    for arrow in arrows:
      arrow.font_size = 32
    self.play(
      *[FadeIn(arrows[i].shift([0.2,(2-i)*1.5,0]), shift=RIGHT) for i in range(len(arrows))]
    )
    eqs2_g = {"font_size": 32}
    eqs3 = [
      MathTex(r"x^2-2xh+h^2 + y^2-2yk+k^2 - r^2 = 0", **eqs2_g),
      MathTex(r"\frac{x^2-2xh+h^2}{a^2} + \frac{y^2-2yk+k^2}{b^2} - 1 = 0", **eqs2_g),
      MathTex(r"\frac{x^2-2xh+h^2}{b^2} + \frac{y^2-2yk+k^2}{a^2} - 1 = 0", **eqs2_g),
      MathTex(r"\frac{x^2-2xh+h^2}{a^2} - \frac{y^2-2yk+k^2}{b^2} - 1 = 0", **eqs2_g),
      MathTex(r"-\frac{x^2-2xh+h^2}{b^2} + \frac{y^2-2yk+k^2}{a^2} - 1 = 0", **eqs2_g)
    ]
    self.play(
      *[Write(eqs3[i].shift([3.6,(2-i)*1.5,0])) for i in range(len(eqs3))]
    )
    self.play(
      *[FadeOut(eqs2[i], shift=RIGHT) for i in range(len(eqs2))],
      *[FadeOut(arrows[i], shift=RIGHT) for i in range(len(arrows))],
      *[eqs3[i].animate.shift([-7.25,0,0]) for i in range(len(eqs3))]
    )
    eqs4 = [
      MathTex(r"x^2-2xh+h^2 + y^2-2yk+k^2 - r^2 = 0", **eqs2_g),
      MathTex(r"\frac{x^2}{a^2}-\frac{2xh}{a^2}+\frac{h^2}{a^2} + \frac{y^2}{b^2}-\frac{2yk}{b^2}+\frac{k^2}{b^2} - 1 = 0", **eqs2_g),
      MathTex(r"\frac{x^2}{b^2}-\frac{2xh}{b^2}+\frac{h^2}{b^2} + \frac{y^2}{a^2}-\frac{2yk}{a^2}+\frac{k^2}{a^2} - 1 = 0", **eqs2_g),
      MathTex(r"\frac{x^2}{a^2}-\frac{2xh}{a^2}+\frac{h^2}{a^2} - \frac{y^2}{b^2}-\frac{2yk}{b^2}+\frac{k^2}{b^2} - 1 = 0", **eqs2_g),
      MathTex(r"-\frac{x^2}{b^2}-\frac{2xh}{b^2}+\frac{h^2}{b^2} + \frac{y^2}{a^2}-\frac{2yk}{a^2}+\frac{k^2}{a^2} - 1 = 0", **eqs2_g)
    ]
    arrows = [arrowTemplate.copy() for i in range(5)]
    for arrow in arrows:
      arrow.font_size = 32
    self.play(
      *[FadeIn(arrows[i].shift([-0.1,(2-i)*1.5,0]), shift=RIGHT) for i in range(len(arrows))]
    )
    self.play(
      *[Write(eqs4[i].shift([3.5,(2-i)*1.5,0])) for i in range(len(eqs4))]
    )
    eqs5 = [
      MathTex(r"\left(1\right)x^2 + \left(1\right)y^2 - \left(2h\right)x - \left(2k\right)y + \left(h^2 + k^2 - r^2\right) = 0", **eqs1_g),
      MathTex(r"\left(\frac{1}{a^2}\right)x^2 + \left(\frac{1}{b^2}\right)y^2 - \left(\frac{2h}{a^2}\right)x - \left(\frac{2k}{b^2}\right)y + \left(\frac{h^2}{a^2} + \frac{k^2}{b^2} - 1\right) = 0", **eqs1_g),
      MathTex(r"\left(\frac{1}{b^2}\right)x^2 + \left(\frac{1}{a^2}\right)y^2 - \left(\frac{2h}{b^2}\right)x - \left(\frac{2k}{a^2}\right)y + \left(\frac{h^2}{b^2} + \frac{k^2}{a^2} - 1\right) = 0", **eqs1_g),
      MathTex(r"\left(\frac{1}{a^2}\right)x^2 - \left(\frac{1}{b^2}\right)y^2 - \left(\frac{2h}{a^2}\right)x + \left(\frac{2k}{b^2}\right)y + \left(\frac{h^2}{a^2} - \frac{k^2}{b^2} - 1\right) = 0", **eqs1_g),
      MathTex(r"-\left(\frac{1}{b^2}\right)x^2 + \left(\frac{1}{a^2}\right)y^2 + \left(\frac{2h}{b^2}\right)x - \left(\frac{2k}{a^2}\right)y + \left(-\frac{h^2}{b^2} + \frac{k^2}{a^2} - 1\right) = 0", **eqs1_g)
    ]
    self.play(
      *[FadeOut(eqs3[i], shift=RIGHT) for i in range(len(eqs3))],
      *[FadeOut(arrows[i], shift=RIGHT) for i in range(len(arrows))],
      *[eqs4[i].animate.shift([-4.25,0,0]) for i in range(len(eqs4))]
    )
    arrows = [arrowTemplate.copy() for i in range(5)]
    for arrow in arrows:
      arrow.font_size = 32
    self.play(
      *[FadeIn(arrows[i].shift([3.25,(2-i)*1.5,0]), shift=RIGHT) for i in range(len(arrows))]
    )
    self.play(
      *[FadeOut(eqs4[i], shift=RIGHT) for i in range(len(eqs4))],
      *[FadeOut(arrows[i], shift=RIGHT) for i in range(len(arrows))],
    )
    self.play(
      *[Write(eqs5[i].shift([0,(2-i)*1.5,0])) for i in range(len(eqs5))]
    )
    self.wait()

class DeriveTheta(Scene):
  def construct(self):
    a = MathTex(r"A{{x^2}}+B{{xy}}+C{{y^2}}+D{{x}}+E{{y}}+F = 0")
    b = MathTex(r"A{{x^{\prime 2} }}+B{{xy}}+C{{y^{\prime 2} }}+D{{x}}+E{{y}}+F = 0")
    c = MathTex(r"{{A}}x^{\prime 2}+{{B}}xy+{{C}}y^{\prime 2}+{{D}}x+{{E}}y+{{F}} = 0")
    d = MathTex(r"{{A}}(x\cos(\theta)-y\sin(\theta))^2")
    e = MathTex(r"{{B}}(x\cos(\theta)-y\sin(\theta))(x\sin(\theta)+y\cos(\theta))")
    f = MathTex(r"{{C}}(x\sin(\theta)+y\cos(\theta))^2")
    g = MathTex(r"{{D}}(x\cos(\theta)-y\sin(\theta))")
    h = MathTex(r"{{E}}(x\sin(\theta)+y\cos(\theta))")
    i = MathTex(r"{{F}}")
    j = MathTex(r"A^\prime x^2+B^\prime xy+C^\prime y^2+D^\prime x+E^\prime y+F^\prime = 0", substrings_to_isolate=[r"x^2", r"y^2", r"x", r"y"])

    self.play(
      Write(a.shift(UP*3))
    )
    self.play(
      ReplacementTransform(a, b.shift(UP*3))
    )
    self.remove(b)
    k = c.copy()
    self.add(k.shift(UP*3))
    self.add(c.shift(UP*3))
    self.play(
      TransformMatchingTex(c, d.shift(UP*2))
    )
    self.add(c)
    self.play(
      TransformMatchingTex(c, e.shift(UP))
    )
    self.add(c)
    self.play(
      TransformMatchingTex(c, f)
    )
    self.add(c)
    self.play(
      TransformMatchingTex(c, g.shift(DOWN))
    )
    self.add(c)
    self.play(
      TransformMatchingTex(c, h.shift(DOWN*2))
    )
    self.add(c)
    self.remove(k)
    self.play(
      TransformMatchingTex(c, i.shift(DOWN*3))
    )


r"x'=x\cos(\theta)-y\sin(\theta)"
r"y'=x\sin(\theta)+y\cos(\theta)"