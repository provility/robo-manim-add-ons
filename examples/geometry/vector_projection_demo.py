"""
Demo: Vector Projection using VectorUtils

Shows dot product projection: projecting vector b onto vector a.
Uses project_onto(), projection_line(), and projection_region() from VectorUtils.
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils


class DotProductProjectionDemo(Scene):
    """Basic projection: project vector b onto vector a"""

    def construct(self):
        # Define vectors
        vector_a = Arrow(ORIGIN, RIGHT * 3.5, buff=0, color=BLUE)
        vector_b = Arrow(ORIGIN, RIGHT * 2.5 + UP * 1.5, buff=0, color=RED)

        origin = Dot(ORIGIN, color=YELLOW)

        # Show vectors
        self.add(origin)
        self.play(GrowArrow(vector_a), GrowArrow(vector_b))
        self.wait(1)

        # Calculate angle for visualization
        vec_a_dir = vector_a.get_end() - vector_a.get_start()
        vec_b_dir = vector_b.get_end() - vector_b.get_start()
        from manim.utils.space_ops import angle_between_vectors
        angle = angle_between_vectors(vec_a_dir, vec_b_dir)

        # STEP 1: Show angle sector between vectors
        angle_sector = Sector(
            radius=0.5, angle=angle, start_angle=0,
            arc_center=ORIGIN, color=YELLOW, fill_opacity=0.3
        )
        angle_label = MathTex(r"\theta", color=YELLOW).move_to(angle_sector.point_from_proportion(0.5) * 1.8)

        self.play(FadeIn(angle_sector), Write(angle_label), run_time=1.0)
        self.wait(0.5)

        # STEP 2: Show projection line using VectorUtils
        proj_line = VectorUtils.projection_line(
            vector_b, vector_a,
            color=GRAY
        )
        proj_line_dashed = DashedLine(
            proj_line.get_start(), proj_line.get_end(),
            color=GRAY, dash_length=0.05
        )

        self.play(Create(proj_line_dashed), run_time=0.8)
        self.wait(0.3)

        # STEP 3: Show right angle indicator
        proj_point = proj_line.get_start()
        right_angle = RightAngle(
            Line(proj_point, vector_a.get_end()),
            Line(proj_point, vector_b.get_end()),
            length=0.2, color=GRAY
        )

        self.play(Create(right_angle), run_time=0.6)
        self.wait(0.3)

        # STEP 4: Grow the projection vector using VectorUtils
        proj_vector = VectorUtils.project_onto(
            vector_b, vector_a,
            color="#047857", tip_length=0.2, stroke_width=5
        )

        self.play(GrowArrow(proj_vector), run_time=1.0)
        self.wait(0.5)

        # STEP 5: Show brace and label
        brace = Brace(proj_vector, direction=DOWN, color="#047857")
        brace_label = brace.get_text("proj").scale(0.6)

        self.play(GrowFromCenter(brace), Write(brace_label), run_time=0.8)
        self.wait(1)


class ProjectionWithFormula(Scene):
    """Projection with mathematical formula"""

    def construct(self):
        # Vectors
        vector_a = Arrow(ORIGIN, RIGHT * 3, buff=0, color=BLUE)
        vector_b = Arrow(ORIGIN, RIGHT * 2 + UP * 1.5, buff=0, color=RED)

        # Labels
        label_a = MathTex(r"\vec{a}", color=BLUE).next_to(vector_a, DOWN)
        label_b = MathTex(r"\vec{b}", color=RED).next_to(vector_b, LEFT)

        # Formula at top
        formula = MathTex(
            r"\text{proj}_{\vec{a}} \vec{b} = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}|^2} \vec{a}",
            font_size=32
        ).to_edge(UP)

        # Show setup
        self.play(Write(formula))
        self.play(GrowArrow(vector_a), GrowArrow(vector_b))
        self.play(Write(label_a), Write(label_b))
        self.wait(1)

        # Show projection
        proj_vector = VectorUtils.project_onto(
            vector_b, vector_a,
            color=GREEN, stroke_width=5
        )
        proj_line = DashedLine(
            proj_vector.get_end(), vector_b.get_end(),
            color=GRAY, dash_length=0.08
        )
        label_proj = MathTex(r"\text{proj}_{\vec{a}} \vec{b}", color=GREEN).next_to(proj_vector, DOWN)

        self.play(GrowArrow(proj_vector))
        self.play(Create(proj_line))
        self.play(Write(label_proj))
        self.wait(2)


class DynamicProjection(Scene):
    """Interactive: Projection updates as vectors rotate"""

    def construct(self):
        # Base vectors
        vector_a = Arrow(ORIGIN, RIGHT * 3.5, buff=0, color=BLUE)
        vector_b = Arrow(ORIGIN, RIGHT * 2 + UP * 1.5, buff=0, color=RED)

        # Dynamic projection using VectorUtils
        proj_vector = always_redraw(
            lambda: VectorUtils.project_onto(
                vector_b, vector_a,
                color=GREEN, stroke_width=5
            )
        )

        proj_line = always_redraw(
            lambda: DashedLine(
                proj_vector.get_end(), vector_b.get_end(),
                color=GRAY, dash_length=0.08
            )
        )

        # Dynamic right angle
        right_angle = always_redraw(
            lambda: RightAngle(
                Line(proj_vector.get_end(), vector_a.get_end()),
                Line(proj_vector.get_end(), vector_b.get_end()),
                length=0.15, color=GRAY
            )
        )

        # Show initial state
        self.play(GrowArrow(vector_a), GrowArrow(vector_b))
        self.add(proj_vector, proj_line, right_angle)
        self.wait(1)

        # Rotate vector b - projection updates
        self.play(
            Rotate(vector_b, angle=PI, about_point=ORIGIN),
            run_time=4,
            rate_func=linear
        )
        self.wait(1)

        # Rotate to perpendicular - projection becomes zero
        self.play(
            Rotate(vector_b, angle=PI/2, about_point=ORIGIN),
            run_time=2
        )
        self.wait(1)


class ProjectionWithRegion(Scene):
    """Projection with shaded triangular region"""

    def construct(self):
        # Vectors
        vector_a = Arrow(ORIGIN, RIGHT * 3.5, buff=0, color=BLUE)
        vector_b = Arrow(ORIGIN, RIGHT * 2.5 + UP * 1.5, buff=0, color=RED)

        # Show vectors
        self.play(GrowArrow(vector_a), GrowArrow(vector_b))
        self.wait(1)

        # Show shaded region using VectorUtils
        region = VectorUtils.projection_region(
            vector_b, vector_a,
            fill_opacity=0.3, color=YELLOW
        )
        self.play(FadeIn(region))
        self.wait(0.5)

        # Show projection vector
        proj_vector = VectorUtils.project_onto(
            vector_b, vector_a,
            color=GREEN, stroke_width=5
        )
        self.play(GrowArrow(proj_vector))
        self.wait(0.5)

        # Show perpendicular line
        proj_line = DashedLine(
            proj_vector.get_end(), vector_b.get_end(),
            color=GRAY, dash_length=0.08
        )
        self.play(Create(proj_line))
        self.wait(2)


class ProjectionCases(Scene):
    """Different projection cases: acute, right, obtuse angles"""

    def construct(self):
        # Title
        title = Text("Projection Cases", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Case 1: Acute angle (positive projection)
        case1_label = Text("Acute Angle", font_size=24).move_to(LEFT * 4 + UP * 2.5)
        vec_a1 = Arrow(LEFT * 5, LEFT * 5 + RIGHT * 2, buff=0, color=BLUE)
        vec_b1 = Arrow(LEFT * 5, LEFT * 5 + RIGHT * 1.5 + UP * 0.8, buff=0, color=RED)
        proj1 = VectorUtils.project_onto(vec_b1, vec_a1, color=GREEN, stroke_width=4)
        line1 = DashedLine(proj1.get_end(), vec_b1.get_end(), color=GRAY, dash_length=0.06)

        self.play(Write(case1_label))
        self.play(GrowArrow(vec_a1), GrowArrow(vec_b1))
        self.play(GrowArrow(proj1), Create(line1))
        self.wait(1)

        # Case 2: Right angle (zero projection)
        case2_label = Text("Right Angle", font_size=24).move_to(ORIGIN + UP * 2.5)
        vec_a2 = Arrow(LEFT * 1, LEFT * 1 + RIGHT * 2, buff=0, color=BLUE)
        vec_b2 = Arrow(LEFT * 1, LEFT * 1 + UP * 1.5, buff=0, color=RED)
        proj2 = VectorUtils.project_onto(vec_b2, vec_a2, color=GREEN, stroke_width=4)
        line2 = DashedLine(proj2.get_end(), vec_b2.get_end(), color=GRAY, dash_length=0.06)

        self.play(Write(case2_label))
        self.play(GrowArrow(vec_a2), GrowArrow(vec_b2))
        self.play(GrowArrow(proj2), Create(line2))
        self.wait(1)

        # Case 3: Obtuse angle (negative projection)
        case3_label = Text("Obtuse Angle", font_size=24).move_to(RIGHT * 4 + UP * 2.5)
        vec_a3 = Arrow(RIGHT * 3, RIGHT * 3 + RIGHT * 2, buff=0, color=BLUE)
        vec_b3 = Arrow(RIGHT * 3, RIGHT * 3 + LEFT * 0.8 + UP * 1.2, buff=0, color=RED)
        proj3 = VectorUtils.project_onto(vec_b3, vec_a3, color=GREEN, stroke_width=4)
        line3 = DashedLine(proj3.get_end(), vec_b3.get_end(), color=GRAY, dash_length=0.06)

        self.play(Write(case3_label))
        self.play(GrowArrow(vec_a3), GrowArrow(vec_b3))
        self.play(GrowArrow(proj3), Create(line3))
        self.wait(2)


class ProjectionDecomposition(Scene):
    """Decompose vector into parallel and perpendicular components"""

    def construct(self):
        # Title
        title = MathTex(r"\vec{b} = \vec{b}_\parallel + \vec{b}_\perp", font_size=36).to_edge(UP)

        # Vectors
        vector_a = Arrow(ORIGIN, RIGHT * 3.5, buff=0, color=BLUE)
        vector_b = Arrow(ORIGIN, RIGHT * 2.5 + UP * 1.8, buff=0, color=RED)

        label_a = MathTex(r"\vec{a}", color=BLUE).next_to(vector_a, DOWN)
        label_b = MathTex(r"\vec{b}", color=RED).next_to(vector_b, LEFT)

        # Show setup
        self.play(Write(title))
        self.play(GrowArrow(vector_a), GrowArrow(vector_b))
        self.play(Write(label_a), Write(label_b))
        self.wait(1)

        # Parallel component (projection)
        parallel = VectorUtils.decompose_parallel(
            vector_b, vector_a,
            color=GREEN, stroke_width=5
        )
        label_parallel = MathTex(r"\vec{b}_\parallel", color=GREEN).next_to(parallel, DOWN)

        self.play(GrowArrow(parallel))
        self.play(Write(label_parallel))
        self.wait(1)

        # Perpendicular component
        perp = VectorUtils.decompose_perp(
            vector_b, vector_a,
            color=ORANGE, stroke_width=5
        )
        label_perp = MathTex(r"\vec{b}_\perp", color=ORANGE).next_to(perp, RIGHT)

        self.play(GrowArrow(perp))
        self.play(Write(label_perp))
        self.wait(1)

        # Dashed line completing triangle
        dashed = DashedLine(vector_b.get_end(), parallel.get_end(), color=GRAY, dash_length=0.08)
        self.play(Create(dashed))
        self.wait(2)


class ProjectionScaling(Scene):
    """Projection magnitude changes with vector magnitude"""

    def construct(self):
        # Fixed target
        vector_a = Arrow(ORIGIN, RIGHT * 3.5, buff=0, color=BLUE)

        # Scaling vector
        vector_b = Arrow(ORIGIN, RIGHT * 1 + UP * 0.8, buff=0, color=RED)

        # Dynamic projection
        proj = always_redraw(
            lambda: VectorUtils.project_onto(
                vector_b, vector_a,
                color=GREEN, stroke_width=5
            )
        )

        proj_line = always_redraw(
            lambda: DashedLine(
                proj.get_end(), vector_b.get_end(),
                color=GRAY, dash_length=0.08
            )
        )

        # Show initial
        self.add(vector_a, vector_b, proj, proj_line)
        self.wait(1)

        # Scale up vector b
        self.play(
            vector_b.animate.put_start_and_end_on(ORIGIN, RIGHT * 2.5 + UP * 2),
            run_time=2
        )
        self.wait(1)

        # Scale down vector b
        self.play(
            vector_b.animate.put_start_and_end_on(ORIGIN, RIGHT * 0.5 + UP * 0.4),
            run_time=2
        )
        self.wait(1)


class DotProductVisualization(Scene):
    """Visualize dot product as projection times magnitude"""

    def construct(self):
        # Formula
        formula = MathTex(
            r"\vec{a} \cdot \vec{b} = |\vec{a}| \, |\text{proj}_{\vec{a}} \vec{b}|",
            font_size=36
        ).to_edge(UP)

        # Vectors
        vector_a = Arrow(ORIGIN, RIGHT * 3, buff=0, color=BLUE)
        vector_b = Arrow(ORIGIN, RIGHT * 2.2 + UP * 1.3, buff=0, color=RED)

        # Show setup
        self.play(Write(formula))
        self.play(GrowArrow(vector_a), GrowArrow(vector_b))
        self.wait(1)

        # Show projection
        proj = VectorUtils.project_onto(vector_b, vector_a, color=GREEN, stroke_width=5)
        proj_line = DashedLine(proj.get_end(), vector_b.get_end(), color=GRAY, dash_length=0.08)

        self.play(GrowArrow(proj))
        self.play(Create(proj_line))
        self.wait(1)

        # Highlight |a| with brace
        brace_a = Brace(vector_a, direction=DOWN, color=BLUE)
        label_a = brace_a.get_text(r"$|\vec{a}|$").scale(0.7)

        self.play(GrowFromCenter(brace_a), Write(label_a))
        self.wait(1)

        # Highlight projection with brace
        brace_proj = Brace(proj, direction=DOWN, color=GREEN)
        label_proj = brace_proj.get_text(r"$|\text{proj}|$").scale(0.7)

        self.play(GrowFromCenter(brace_proj), Write(label_proj))
        self.wait(2)
