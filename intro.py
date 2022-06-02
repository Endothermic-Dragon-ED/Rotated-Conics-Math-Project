import numpy as np
from manim import *

config.max_files_cached = 10000

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
      MathTex(r"{{\left(1\right)}}{{x^2}} + {{\left(1\right)}}{{y^2}} - {{\left(2h\right)}}{{x}} - {{\left(2k\right)}}{{y}} + {{\left(h^2 + k^2 - r^2\right)}}{{ = 0}}", **eqs1_g),
      MathTex(r"{{\left(\frac{1}{a^2}\right)}}{{x^2}} + {{\left(\frac{1}{b^2}\right)}}{{y^2}} - {{\left(\frac{2h}{a^2}\right)}}{{x}} - {{\left(\frac{2k}{b^2}\right)}}{{y}} + {{\left(\frac{h^2}{a^2} + \frac{k^2}{b^2} - 1\right)}}{{ = 0}}", **eqs1_g),
      MathTex(r"{{\left(\frac{1}{b^2}\right)}}{{x^2}} + {{\left(\frac{1}{a^2}\right)}}{{y^2}} - {{\left(\frac{2h}{b^2}\right)}}{{x}} - {{\left(\frac{2k}{a^2}\right)}}{{y}} + {{\left(\frac{h^2}{b^2} + \frac{k^2}{a^2} - 1\right)}}{{ = 0}}", **eqs1_g),
      MathTex(r"{{\left(\frac{1}{a^2}\right)}}{{x^2}} - {{\left(\frac{1}{b^2}\right)}}{{y^2}} - {{\left(\frac{2h}{a^2}\right)}}{{x}} + {{\left(\frac{2k}{b^2}\right)}}{{y}} + {{\left(\frac{h^2}{a^2} - \frac{k^2}{b^2} - 1\right)}}{{ = 0}}", **eqs1_g),
      MathTex(r"{{-\left(\frac{1}{b^2}\right)}}{{x^2}} + {{\left(\frac{1}{a^2}\right)}}{{y^2}} + {{\left(\frac{2h}{b^2}\right)}}{{x}} - {{\left(\frac{2k}{a^2}\right)}}{{y}} + {{\left(-\frac{h^2}{b^2} + \frac{k^2}{a^2} - 1\right)}}{{ = 0}}", **eqs1_g)
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

    eqs6 = [eq.copy() for eq in eqs5]
    for eq in eqs6:
      eq.submobjects[0].color = RED
      eq.submobjects[1].color = BLUE
      eq.submobjects[3].color = RED
      eq.submobjects[4].color = BLUE
      eq.submobjects[6].color = RED
      eq.submobjects[7].color = BLUE
      eq.submobjects[9].color = RED
      eq.submobjects[10].color = BLUE
      eq.submobjects[12].color = RED
    
    self.play(
      TransformMatchingTex(
        Group(*eqs5),
        Group(*eqs6)
      )
    )

    self.play(
      FadeOut(Group(*eqs6), shift=DOWN)
    )
    eq = MathTex(r"{{A}}{{x^2}} + {{C}}{{y^2}} + {{D}}{{x}} + {{E}}{{y}} + {{F}} = 0")
    eq.submobjects[0].color = RED
    eq.submobjects[1].color = BLUE
    eq.submobjects[3].color = RED
    eq.submobjects[4].color = BLUE
    eq.submobjects[6].color = RED
    eq.submobjects[7].color = BLUE
    eq.submobjects[9].color = RED
    eq.submobjects[10].color = BLUE
    eq.submobjects[12].color = RED

    self.play(
      Write(eq)
    )

class DisplayRotationEquation(Scene):
  def construct(self):
    eq_old = MathTex(r"{{A}}{{x^2}} + {{C}}{{y^2}} + {{D}}{{x}} + {{E}}{{y}} + {{F}} = 0")
    eq_old.submobjects[0].color = RED
    eq_old.submobjects[1].color = BLUE
    eq_old.submobjects[3].color = RED
    eq_old.submobjects[4].color = BLUE
    eq_old.submobjects[6].color = RED
    eq_old.submobjects[7].color = BLUE
    eq_old.submobjects[9].color = RED
    eq_old.submobjects[10].color = BLUE
    eq_old.submobjects[12].color = RED

    eq2_org = MathTex(r"{{A}}{{x^2}} + {{B}}{{xy}} + {{C}}{{y^2}} + {{D}}{{x}} + {{E}}{{y}} + {{F}} = 0")
    eq2_old = eq2_org.copy()
    eq2_old.submobjects[0].color = RED
    eq2_old.submobjects[1].color = BLUE
    eq2_old.submobjects[3].color = RED
    eq2_old.submobjects[4].color = BLUE
    eq2_old.submobjects[6].color = RED
    eq2_old.submobjects[7].color = BLUE
    eq2_old.submobjects[9].color = RED
    eq2_old.submobjects[10].color = BLUE
    eq2_old.submobjects[12].color = RED
    eq2_old.submobjects[13].color = BLUE
    eq2_old.submobjects[15].color = RED

    self.add(eq_old)
    self.play(
      eq_old.animate.shift(UP*2)
    )

    ellipse = Ellipse(width=4.0, height=2.0, color=BLUE).shift(DOWN*1)
    self.play(
      Create(ellipse)
    )

    self.play(
      TransformMatchingTex(eq_old, eq2_old.shift(UP*2)),
      Rotate(ellipse, PI/5)
    )

    self.play(
      TransformMatchingTex(eq2_old, eq2_org.shift(UP*2))
    )

    self.play(
      FadeOut(ellipse, shift=DOWN)
    )

    rotationFormula = MathTex(r"\cot(2\theta) = \frac{A-C}{B}").shift(DOWN*0.5)
    domainRestriction = Tex(r"Domain: $0<\theta<\frac{\pi}{2}$").shift(DOWN*2)

    self.play(
      Write(rotationFormula)
    )

    self.play(
      Write(domainRestriction)
    )

    self.play(
      eq2_org.animate.scale(0.8).shift([-2.5,0.9,0]),
      rotationFormula.animate.scale(0.8).shift([4,3.8,0]),
      domainRestriction.animate.scale(0.8).shift([4,4.5,0])
    )

class DisplayEquations(Scene):
  def construct(self):
    eq2_org = MathTex(r"{{A}}{{x^2}} + {{B}}{{xy}} + {{C}}{{y^2}} + {{D}}{{x}} + {{E}}{{y}} + {{F}} = 0")
    rotationFormula = MathTex(r"\cot(2\theta) = \frac{A-C}{B}").shift(DOWN*0.5)
    domainRestriction = Tex(r"Domain: $0<\theta<\frac{\pi}{2}$").shift(DOWN*2)

    self.add(
      eq2_org.scale(0.8).shift([-2.5,2.9,0]),
      rotationFormula.scale(0.8).shift([4,3.8,0]),
      domainRestriction.scale(0.8).shift([4,4.5,0])
    )

    eqs1 = [
      Tex(r"These remain constant, no matter what rigid transformation\\(translation or rotation) is applied to it.").scale(0.8).shift(UP*1.6),
      MathTex(r"F = F^\prime").shift(UP*0.8).scale(0.8),
      MathTex(r"A + C = A^\prime + C^\prime").shift(UP*0.2).scale(0.8),
      MathTex(r"B^2 - 4AC = B^{\prime 2} - 4A^\prime C^\prime").shift(DOWN*0.4).scale(0.8),
      Tex(r"The expression, $B^2 - 4AC$, can also be used\\ to categorize the type of conic.").shift(DOWN*1.3).scale(0.8),
      Tex(r"Ellipse or circle: $B^2 - 4AC < 0$").shift(DOWN*2.1).scale(0.8),
      Tex(r"Parabola: $B^2 - 4AC = 0$").shift(DOWN*2.7).scale(0.8),
      Tex(r"Hyperbola: $B^2 - 4AC > 0$").shift(DOWN*3.3).scale(0.8)
    ]
    self.play(
      Write(eqs1[0])
    )
    self.play(
      Write(eqs1[1]),
      Write(eqs1[2]),
      Write(eqs1[3])
    )
    self.play(
      Write(eqs1[4])
    )
    self.play(
      Write(eqs1[5]),
      Write(eqs1[6]),
      Write(eqs1[7])
    )

class DisplayProblem(Scene):
  def construct(self):
    text = Tex(r"What type of conic section is this?")
    eq = MathTex(r"8x^2+16xy+8y^2+3x+2y+7=0")
    exp1 = [
      Tex(r"Let's use the formula $B^2-4AC$ to classify this equation."),
      MathTex(r"{{B^2-4AC}}"),
      MathTex(r"{{B^2-4AC}} = 16^2 - 4\cdot8\cdot8"),
      MathTex(r"{{B^2-4AC = 16^2 - 4\cdot8\cdot8}}"),
      MathTex(r"{{B^2-4AC = 16^2 - 4\cdot8\cdot8}} = 256 - 256"),
      MathTex(r"{{B^2-4AC = 16^2 - 4\cdot8\cdot8 = 256 - 256}}"),
      MathTex(r"{{B^2-4AC = 16^2 - 4\cdot8\cdot8 = 256 - 256}} = 0")
    ]
    text2 = Tex(r"A student applied a rotation to this equation\\about the origin, and got this equation.")
    text3 = Tex(r"However, their paper fell in some water,\\and some of the coefficients washed out.\\Find the missing values.")
    eq2 = MathTex(r"\_x^2+\_xy+5\sqrt{2}\cdot x - \frac{\sqrt{2}}{2}y + \_ = 0")
    exp2 = [
      Tex(r"First, let's use the fact that $A + C$ remains constant."),
      Tex(r"In our equation, there is no $C$ coefficient,\\which means we have $0xy$, and $C = 0$."),
      Tex(r"Before, $A+C$ was simply $8+8=16$.\\After the transformation, we get $A + 0 = 16$, so $A = 16$."),
      Tex(r"Next, we use the fact that $B^2+4AC$\\remains constant after a transformation."),
      Tex(r"Before, $B^2-4AC$ equalled $0$,\\which was how we knew it was a parabola."),
      Tex(r"Now, plugging in values for\\$B^2-4AC$, we get $B^2 - 0 = 0$. So, $B = 0$."),
      Tex(r"Finally, $F$ also remains the same\\during a transformation, so $F$ simply equals $7$.")
    ]

    self.play(
      Write(text.shift(UP*3).scale(0.9)),
      Write(eq.shift(UP*2.25).scale(0.9))
    )

    self.play(
      Write(exp1[0].scale(0.9))
    )

    self.play(
      Write(exp1[1].shift(DOWN).scale(0.9))
    )

    self.play(
      TransformMatchingTex(exp1[1], exp1[2].shift(DOWN))
    )

    self.remove(exp1[2])
    self.add(exp1[3].shift(DOWN))

    self.play(
      TransformMatchingTex(exp1[3], exp1[4].shift(DOWN))
    )

    self.remove(exp1[4])
    self.add(exp1[5].shift(DOWN))

    self.play(
      TransformMatchingTex(exp1[5], exp1[6].shift(DOWN))
    )

    self.play(
      FadeOut(Group(text, exp1[6], exp1[0]), shift=UP),
      eq.animate.shift(UP)
    )

    self.play(
      Write(text2.shift(UP*1.5).scale(0.9))
    )

    self.play(
      Write(eq2.shift(DOWN*0.25).scale(0.9))
    )

    self.play(
      Write(text3.shift(DOWN*2.5).scale(0.9))
    )

    self.play(
      FadeOut(text2, shift=DOWN),
      FadeOut(text3, shift=DOWN),
      eq2.animate.shift(UP*2)
    )

    self.play(
      Write(exp2[0].shift(UP*0.5).scale(0.9))
    )

    self.play(
      Write(exp2[1].shift(DOWN*1).scale(0.9))
    )

    self.play(
      Write(exp2[2].shift(DOWN*2.5).scale(0.9))
    )
    eq2_new = MathTex(r"{{\_}}x^2+\_xy+5\sqrt{2}\cdot x - \frac{\sqrt{2}}{2}y + \_ = 0").shift(UP*1.75)
    self.remove(eq2)
    eq2 = eq2_new
    self.add(eq2_new.scale(0.9))
    eq2_new = MathTex(r"{{16}}x^2+\_xy+5\sqrt{2}\cdot x - \frac{\sqrt{2}}{2}y + \_ = 0").shift(UP*1.75)

    self.play(
      FadeOut(Group(exp2[0], exp2[1], exp2[2]), shift=DOWN),
      TransformMatchingTex(eq2, eq2_new.scale(0.9))
    )
    eq2 = eq2_new

    self.play(
      Write(exp2[3].shift(UP*0.5).scale(0.9))
    )

    self.play(
      Write(exp2[4].shift(DOWN*1).scale(0.9))
    )

    self.play(
      Write(exp2[5].shift(DOWN*2.5).scale(0.9))
    )

    eq2_new = MathTex(r"16x^2+{{\_}}xy+5\sqrt{2}\cdot x - \frac{\sqrt{2}}{2}y + \_ = 0").shift(UP*1.75)
    self.remove(eq2)
    eq2 = eq2_new
    self.add(eq2_new.scale(0.9))
    eq2_new = MathTex(r"16x^2+{{0}}xy+5\sqrt{2}\cdot x - \frac{\sqrt{2}}{2}y + \_ = 0").shift(UP*1.75)

    self.play(
      FadeOut(Group(exp2[3], exp2[4], exp2[5]), shift=DOWN),
      TransformMatchingTex(eq2, eq2_new.scale(0.9))
    )
    eq2 = eq2_new

    eq2_new = MathTex(r"16x^2+{{0xy+}}5\sqrt{2}\cdot x - \frac{\sqrt{2}}{2}y + \_ = 0").shift(UP*1.75)
    self.remove(eq2)
    eq2 = eq2_new
    self.add(eq2_new.scale(0.9))
    eq2_new = MathTex(r"16x^2+", r"5\sqrt{2}\cdot x - \frac{\sqrt{2}}{2}y + \_ = 0").shift(UP*1.75)

    self.play(
      TransformMatchingTex(eq2, eq2_new.scale(0.9))
    )
    eq2 = eq2_new

    self.play(
      Write(exp2[6].shift(UP*0.5).scale(0.9))
    )

    eq2_new = MathTex(r"16x^2+5\sqrt{2}\cdot x - \frac{\sqrt{2}}{2}y + {{\_}} = 0").shift(UP*1.75)
    self.remove(eq2)
    eq2 = eq2_new
    self.add(eq2_new.scale(0.9))
    eq2_new = MathTex(r"16x^2+5\sqrt{2}\cdot x - \frac{\sqrt{2}}{2}y + 7 = 0").shift(UP*1.75)

    self.play(
      FadeOut(exp2[6], shift=DOWN),
      TransformMatchingTex(eq2, eq2_new.scale(0.9))
    )

class Combined(Scene):
  def construct(self):
    Intro.construct(self)
    self.wait()
    self.play(
      *[FadeOut(mob) for mob in self.mobjects]
    )
    GeneralizeConicFormulas.construct(self)
    self.wait()
    self.remove(*self.mobjects)
    DisplayRotationEquation.construct(self)
    self.wait()
    self.remove(*self.mobjects)
    DisplayEquations.construct(self)
    self.wait()
    self.play(
      *[FadeOut(mob) for mob in self.mobjects]
    )
    DisplayProblem.construct(self)

    self.wait()
    self.wait()
    self.wait()
    self.wait()