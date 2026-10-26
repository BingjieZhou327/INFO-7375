# This module is appended *after* the entire official iso_kit.py by assemble_scenes.py.
# It assumes Manim, numpy, Iso, palette, T, finish are already defined above.
# No student claims of completed user research or software tests are made.

# Map the 22 storyboard body beats to distinct drawn concepts.
# (kind, kind, left caption, right caption, status, style)
_UX_PLANS = {
    'B00': ('interviews', 'finding', 'INTERVIEWS', 'SUMMARY', 'CONSTRUCTED', 'flow'),
    'B01': ('quotes', 'finding', 'QUOTES', 'CLAIM', 'CONSTRUCTED', 'conflict'),
    'B02': ('interviews', 'audit', 'EVIDENCE', 'VALIDATOR', 'PROPOSED', 'flow'),
    'B03': ('code', 'report', 'PYTHON', 'REPORT', 'PROPOSED', 'flow'),
    'B04': ('platforms', 'finding', 'EXISTING TOOLS', 'THEMES', 'ILLUSTRATION', 'flow'),
    'B05': ('finding', 'audit', 'CLAIM', 'AUDIT', 'PROPOSED', 'gate'),
    'B06': ('finding', 'design', 'INSIGHT', 'DESIGN RISK', 'PROPOSED', 'branch'),
    'B07': ('desk', 'interviews', 'UX RESEARCH', 'INTERVIEWS', 'PROPOSED', 'workspace'),
    'B08': ('report', 'quotes', 'REPORT', 'SOURCES', 'CONSTRUCTED', 'conflict'),
    'B09': ('interviews', 'testing', 'REPOSITORY', 'TESTS', 'PLANNED', 'flow'),
    'B10': ('interviews', 'interviews', '3 TO 5', 'INTERVIEWS', 'CONSTRUCTED', 'collection'),
    'B11': ('quotes', 'interviews', 'QUOTATION', 'SOURCE ID', 'PROPOSED', 'match'),
    'B12': ('finding', 'audit', 'FINDING', 'THREE CHECKS', 'PROPOSED', 'gate'),
    'B13': ('scope', 'scope', 'IN SCOPE', 'OUT OF SCOPE', 'PROPOSED', 'scope'),
    'B14': ('code', 'audit', 'PROMPT', 'VERIFICATION', 'PROPOSED', 'flow'),
    'B15': ('testing', 'report', 'TEST CASE', 'COMPARISON', 'PLANNED', 'branch'),
    'B16': ('finding', 'audit', 'FINDING', 'FALSE FLAG', 'HYPOTHETICAL', 'conflict'),
    'B17': ('quotes', 'desk', 'QUOTE CHECK', 'HUMAN REVIEW', 'PROPOSED', 'split'),
    'B18': ('testing', 'report', 'DETECTED', 'MISSED', 'PLANNED', 'split'),
    'B19': ('interviews', 'desk', 'UX COURSEWORK', 'RESEARCH ROLE', 'PERSONAL GOAL', 'flow'),
    'B20': ('design', 'interviews', 'TONIGHTLY', 'USER NEEDS', 'CONSTRUCTED', 'flow'),
    'B21': ('audit', 'desk', 'AI CHECKS', 'HUMAN JUDGMENT', 'PROPOSED', 'flow'),
}


def _ux_iso(kind, x, y):
    """Reusable, non-photographic isometric props centered at x,y (all constructed)."""
    iso = Iso(s=0.64)
    if kind in ('interviews', 'quotes'):
        p1 = iso.page(0, 0, 0, 2, 1.6)
        p2 = iso.page(0, 0, 0, 2, 1.6).shift(RIGHT * .22 + UP * .23)
        p3 = iso.page(0, 0, 0, 2, 1.6).shift(LEFT * .22 + DOWN * .14)
        g = VGroup(p3, p2, p1) if kind == 'interviews' else VGroup(p2, p1)
    elif kind in ('finding', 'report', 'testing'):
        frame = RoundedRectangle(corner_radius=.13, width=2.25, height=1.55,
                                 fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=4)
        lines = VGroup(*[
            Line(LEFT * .8 + UP * v, RIGHT * (.7 if n != 1 else .32) + UP * v,
                 color=BAR1 if n == 0 else BAR2, stroke_width=5)
            for n, v in enumerate((.4, .05, -.30))
        ])
        g = VGroup(frame, lines)
        if kind == 'testing':
            mark = Circle(radius=.12, color=INK, stroke_width=4).move_to(LEFT*.84 + DOWN*.47)
            g.add(mark)
        if kind == 'report':
            g.add(Dot(point=RIGHT * .76 + UP * .53, radius=.065, color=TERRA))
    elif kind in ('audit', 'code', 'design', 'scope'):
        colors = (DARK_TOP, DARK_L, DARK_R) if kind in ('audit', 'code') else (BOX_TOP, BOX_L, BOX_R)
        g = iso.box(0, 0, 0, 2.25, 1.7, .9, *colors)
        if kind == 'audit':
            g.add(Dot(point=[.65, .2, 0], radius=.13, color=TERRA))
        if kind == 'code':
            g.add(Line([-.33,-.18,0],[.28,.1,0],stroke_width=6,color=GHOST))
        if kind == 'design':
            g.add(Circle(radius=.43, color=INK,stroke_width=4).move_to([0,.1,0]))
        if kind == 'scope':
            g.add(Dot(point=[0, .25,0],radius=.17,color=BAR1))
    elif kind in ('folder', 'platforms'):
        cover = iso.box(0, 0, 0, 2.4, 1.85, .28, BOX_TOP, BOX_L, BOX_R)
        tab = Rectangle(width=.8, height=.2, fill_color=BAR1, fill_opacity=1,
                        stroke_color=INK, stroke_width=2).shift(UP*.75 + LEFT*.33)
        g = VGroup(cover, tab)
        if kind == 'platforms':
            second = cover.copy().scale(.75).shift(RIGHT*.45 + UP*.25)
            g.add(second)
    elif kind == 'desk':
        base = iso.box(0, 0, 0, 2.75, 1.95, .36, BOX_TOP, BOX_L, BOX_R)
        screen = RoundedRectangle(corner_radius=.1, width=1.4, height=.85,
            fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=4).shift(UP*.6)
        g = VGroup(base, screen)
    else:
        g = iso.page(0, 0, 0, 2, 1.6)
    return g.move_to(np.array([x,y,0]))


def _ux_caption(value, x, y):
    label = T(value, size=34, color=INK, bold=True)
    label.move_to(np.array([x, y, 0]))
    return label


def _ux_beat(scene, bid):
    leftkind, rightkind, lt, rt, status, mode = _UX_PLANS[bid]
    # All scenes share the same palette and physical objects; a paper/box motif.
    # The status is authored, not a computed experimental outcome.
    left = _ux_iso(leftkind, -3.05, .2)
    right = _ux_iso(rightkind, 3.05, .2)
    # Legible sparse visual labels outside the physical objects.
    footer = T(status, size=31, color=INK)
    footer.to_edge(DOWN, buff=.85)
    llabel = _ux_caption(lt, -3.05, -1.42)
    rlabel = _ux_caption(rt, 3.05, -1.42)
    scene.add(footer)  # Persistent caption from first frame.
    scene.play(FadeIn(left, shift=UP*.27), run_time=.55)
    scene.play(FadeIn(llabel, shift=UP*.12), run_time=.25)
    # Every beat adds a new meaningful shape *after* the initial drawing.
    # Midpoint anti-overlap: the central connector appears early and holds.
    if mode in ('flow','match','workspace','collection'):
        path = Arrow(np.array([-1.55,0.2,0]), np.array([1.45,0.2,0]),
                     buff=.06, color=INK, stroke_width=6,
                     max_tip_length_to_length_ratio=.16)
        scene.play(Create(path), run_time=.4)
    elif mode in ('conflict','split'):
        path = VGroup(
            Line([-1.45,.55,0],[1.47,.55,0],color=INK,stroke_width=5),
            Line([-1.45,-.22,0],[1.47,-.22,0],color=BAR1,stroke_width=5),
        )
        scene.play(Create(path), run_time=.45)
    elif mode in ('branch','gate'):
        path = VGroup(
            Line([-1.45,.05,0],[1.35,.05,0],color=INK,stroke_width=6),
            Circle(radius=.15,fill_color=TERRA,fill_opacity=1,stroke_width=0).move_to([0,.05,0])
        )
        scene.play(Create(path[0]), FadeIn(path[1]), run_time=.45)
    else:  # scope boundary
        path = DashedLine([-1.4,-.6,0],[1.45,.7,0], color=INK,stroke_width=6)
        scene.play(Create(path), run_time=.45)
    scene.play(FadeIn(right, shift=UP*.24), run_time=.55)
    scene.play(FadeIn(rlabel, shift=UP*.1), run_time=.25)
    # New object + motion: no static text-only slides, no test outcomes implied.
    if mode in ('match','gate','conflict'):
        seal = Circle(radius=.19, color=TERRA, stroke_width=7)
        seal.move_to([1.5, .82,0])
    elif mode == 'branch':
        seal = VGroup(
          Line([0,.08,0],[1.0,.91,0],color=INK,stroke_width=5),
          Dot([1.0,.91,0],radius=.085,color=TERRA))
    elif mode == 'scope':
        seal = Circle(radius=.24,color=INK,stroke_width=5).move_to([0,.8,0])
    else:
        seal = Dot([1.45,.18,0],radius=.085,color=TERRA)
    scene.play(FadeIn(seal), run_time=.32)
    finish(scene)


# Each literal class name matches the exact shot.manim.class in beat_sheet.json.
# The stock show-tell runner discovers these with a class-name regex.
class B00_Summary(Scene):
    def construct(self): _ux_beat(self,'B00')

class B01_Distortion(Scene):
    def construct(self): _ux_beat(self,'B01')

class B02_Validator(Scene):
    def construct(self): _ux_beat(self,'B02')

class B03_Plan(Scene):
    def construct(self): _ux_beat(self,'B03')

class B04_Alternatives(Scene):
    def construct(self): _ux_beat(self,'B04')

class B05_Claims(Scene):
    def construct(self): _ux_beat(self,'B05')

class B06_DesignRisk(Scene):
    def construct(self): _ux_beat(self,'B06')

class B07_Researcher(Scene):
    def construct(self): _ux_beat(self,'B07')

class B08_Report(Scene):
    def construct(self): _ux_beat(self,'B08')

class B09_Review(Scene):
    def construct(self): _ux_beat(self,'B09')

class B10_Synthetic(Scene):
    def construct(self): _ux_beat(self,'B10')

class B11_QuoteMatch(Scene):
    def construct(self): _ux_beat(self,'B11')

class B12_FutureChecks(Scene):
    def construct(self): _ux_beat(self,'B12')

class B13_OutOfScope(Scene):
    def construct(self): _ux_beat(self,'B13')

class B14_Skills(Scene):
    def construct(self): _ux_beat(self,'B14')

class B15_Evaluation(Scene):
    def construct(self): _ux_beat(self,'B15')

class B16_Risk(Scene):
    def construct(self): _ux_beat(self,'B16')

class B17_HumanReview(Scene):
    def construct(self): _ux_beat(self,'B17')

class B18_FailureLog(Scene):
    def construct(self): _ux_beat(self,'B18')

class B19_Motivation(Scene):
    def construct(self): _ux_beat(self,'B19')

class B20_Tonightly(Scene):
    def construct(self): _ux_beat(self,'B20')

class B21_Conclusion(Scene):
    def construct(self): _ux_beat(self,'B21')
