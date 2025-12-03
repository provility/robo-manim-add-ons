"""
Demo: VectorUtils Projection Methods with Dynamic Updaters

Shows project_onto(), projection_line(), and projection_region() methods
with dynamic updaters. Demonstrates how projection changes as vectors move.
Focus on geometric relationships, not styling.
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils



class ProjectionDemo(Scene):
    def construct(self):
        # Fixed target vector (horizontal)
        vector_a = Arrow(ORIGIN, RIGHT * 3, buff=0, fill_opacity=0)

        # Moving vector that we'll project onto vector_a
        vector_b = Arrow(ORIGIN, RIGHT * 2 + UP * 1.5, buff=0, fill_opacity=0)

        # Create projection visualizations
        projection = VectorUtils.project_onto(vector_b, vector_a)
        proj_line = VectorUtils.projection_line(vector_b, vector_a)
        proj_region = VectorUtils.projection_region(vector_b, vector_a, fill_opacity=0.3)

        # Add updaters to make projection dynamic
        projection.add_updater(
            lambda m: m.become(VectorUtils.project_onto(vector_b, vector_a))
        )

        proj_line.add_updater(
            lambda m: m.become(VectorUtils.projection_line(vector_b, vector_a))
        )

        proj_region.add_updater(
            lambda m: m.become(VectorUtils.projection_region(vector_b, vector_a, fill_opacity=0.3))
        )

        # Show vectors
        self.play(GrowArrow(vector_a))
        self.play(GrowArrow(vector_b))
        self.wait(0.5)

        # Show projection components
        self.play(GrowArrow(projection))
        self.wait(0.5)

        self.play(Create(proj_line))
        self.wait(0.5)

        self.play(FadeIn(proj_region))
        self.wait(1)

        # Animate vector_b rotating around origin
        # This demonstrates how projection changes dynamically
        self.play(
            Rotate(vector_b, angle=PI, about_point=ORIGIN),
            run_time=4,
            rate_func=linear
        )
        self.wait(1)

        # Rotate back showing perpendicular case (projection becomes zero)
        self.play(
            Rotate(vector_b, angle=PI/2, about_point=ORIGIN),
            run_time=2
        )
        self.wait(1)

        # Show parallel case
        self.play(
            Rotate(vector_b, angle=-PI/2, about_point=ORIGIN),
            run_time=2
        )
        self.wait(1)


class ProjectionPerpDemoScene(Scene):
    """Demo showing projection behavior when vectors become perpendicular."""

    def construct(self):
        # Fixed horizontal vector
        vector_a = Arrow(ORIGIN, RIGHT * 3, buff=0, fill_opacity=0)

        # Start with diagonal vector
        vector_b = Arrow(ORIGIN, RIGHT * 2 + UP * 0.5, buff=0, fill_opacity=0)

        # Create projection visualizations with updaters
        projection = always_redraw(
            lambda: VectorUtils.project_onto(vector_b, vector_a)
        )

        proj_line = always_redraw(
            lambda: VectorUtils.projection_line(vector_b, vector_a)
        )

        proj_region = always_redraw(
            lambda: VectorUtils.projection_region(vector_b, vector_a, fill_opacity=0.3)
        )

        # Show initial state
        self.play(GrowArrow(vector_a), GrowArrow(vector_b))
        self.play(
            GrowArrow(projection),
            Create(proj_line),
            FadeIn(proj_region)
        )
        self.wait(1)

        # Rotate to perpendicular - projection collapses to point
        self.play(
            Rotate(vector_b, angle=PI/2 - np.arctan(0.5/2), about_point=ORIGIN),
            run_time=3
        )
        self.wait(1)

        # Rotate to parallel - projection equals vector_b
        self.play(
            Rotate(vector_b, angle=-PI/2, about_point=ORIGIN),
            run_time=3
        )
        self.wait(1)


class ProjectionScalingDemo(Scene):
    """Demo showing how projection changes with vector magnitude."""

    def construct(self):
        # Fixed horizontal vector
        vector_a = Arrow(ORIGIN, RIGHT * 3, buff=0, fill_opacity=0)

        # Vector that will scale
        vector_b = Arrow(ORIGIN, RIGHT * 1 + UP * 1, buff=0, fill_opacity=0)

        # Create projection visualizations with always_redraw
        projection = always_redraw(
            lambda: VectorUtils.project_onto(vector_b, vector_a)
        )

        proj_line = always_redraw(
            lambda: VectorUtils.projection_line(vector_b, vector_a)
        )

        proj_region = always_redraw(
            lambda: VectorUtils.projection_region(vector_b, vector_a, fill_opacity=0.3)
        )

        # Show initial state
        self.add(vector_a, vector_b, projection, proj_line, proj_region)
        self.wait(1)

        # Scale vector_b - watch projection scale proportionally
        new_end = RIGHT * 2.5 + UP * 2.5
        self.play(
            vector_b.animate.put_start_and_end_on(ORIGIN, new_end),
            run_time=3
        )
        self.wait(1)

        # Scale down
        new_end = RIGHT * 0.5 + UP * 0.5
        self.play(
            vector_b.animate.put_start_and_end_on(ORIGIN, new_end),
            run_time=3
        )
        self.wait(1)
