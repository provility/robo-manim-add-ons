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
        vector_a = VectorUtils.create_vector(ORIGIN, RIGHT * 3.5, color=BLUE)
        vector_b = VectorUtils.create_vector(ORIGIN, RIGHT * 2.5 + UP * 1.5, color=RED)

        origin = Dot(ORIGIN, color=YELLOW)

        # Show vectors
        self.add(origin)
        self.play(Create(vector_a), Create(vector_b))
        self.wait(1)

        # Calculate angle for visualization
        vec_a_dir = vector_a.get_end() - vector_a.get_start()
        vec_b_dir = vector_b.get_end() - vector_b.get_start()
        from manim.utils.space_ops import angle_between_vectors
        angle = angle_between_vectors(vec_a_dir, vec_b_dir)

        # STEP 1: Show angle sector between vectors
        angle_sector = Sector(
            radius=0.5, angle=angle, start_angle=0, color=YELLOW)
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

        self.play(Create(proj_vector), run_time=1.0)
        self.wait(0.5)

        # STEP 5: Show brace and label
        brace = Brace(proj_vector, direction=DOWN, color="#047857")
        brace_label = brace.get_text("proj").scale(0.6)

        self.play(GrowFromCenter(brace), Write(brace_label), run_time=0.8)
        self.wait(1)


class DynamicProjection(Scene):
    """Interactive: Projection updates as vectors rotate"""

    def construct(self):
        # Base vectors
        vector_a = VectorUtils.create_vector(ORIGIN, RIGHT * 3.5, color=BLUE)
        vector_b = VectorUtils.create_vector(ORIGIN, RIGHT * 2 + UP * 1.5, color=RED)

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
        self.play(Create(vector_a), Create(vector_b))
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
