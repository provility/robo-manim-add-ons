"""
Demo: VectorUtils Decomposition Methods with Dynamic Updaters

Shows decompose_parallel() and decompose_perp() methods with dynamic updaters.
Demonstrates how vector decomposition changes as vectors rotate and move.
Focus on geometric relationships, not styling.
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils


class BasicDecompositionDemo(Scene):
    """Basic example: Decompose vector A into components parallel and perpendicular to vector B"""

    def construct(self):
        # Reference vector (horizontal)
        vector_b = Arrow(ORIGIN, RIGHT * 3, buff=0, color=BLUE)

        # Vector to decompose
        vector_a = Arrow(ORIGIN, RIGHT * 2 + UP * 1.5, buff=0, color=RED)

        # Show vectors
        self.play(GrowArrow(vector_b))
        self.play(GrowArrow(vector_a))
        self.wait(1)

        # Create decomposition components
        parallel = VectorUtils.decompose_parallel(vector_a, vector_b, color=GREEN)
        perp = VectorUtils.decompose_perp(vector_a, vector_b, color=ORANGE)

        # Show parallel component
        self.play(GrowArrow(parallel))
        self.wait(1)

        # Show perpendicular component
        self.play(GrowArrow(perp))
        self.wait(1)

        # Add dashed line to complete the decomposition triangle
        dashed = DashedLine(vector_a.get_end(), parallel.get_end(), color=GRAY)
        self.play(Create(dashed))
        self.wait(2)


class RotatingVectorDecomposition(Scene):
    """Demo: Decomposition updates as vector A rotates around origin"""

    def construct(self):
        # Fixed reference vector
        vector_b = Arrow(ORIGIN, RIGHT * 3, buff=0, color=BLUE)

        # Rotating vector
        vector_a = Arrow(ORIGIN, RIGHT * 2 + UP * 1, buff=0, color=RED)

        # Create dynamic decomposition with always_redraw
        parallel = always_redraw(
            lambda: VectorUtils.decompose_parallel(vector_a, vector_b, color=GREEN)
        )

        perp = always_redraw(
            lambda: VectorUtils.decompose_perp(vector_a, vector_b, color=ORANGE)
        )

        dashed = always_redraw(
            lambda: DashedLine(vector_a.get_end(), parallel.get_end(), color=GRAY, dash_length=0.1)
        )

        # Show initial state
        self.play(GrowArrow(vector_b))
        self.play(GrowArrow(vector_a))
        self.add(parallel, perp, dashed)
        self.wait(1)

        # Rotate vector_a - watch decomposition change
        self.play(
            Rotate(vector_a, angle=PI, about_point=ORIGIN),
            run_time=4,
            rate_func=linear
        )
        self.wait(1)

        # Rotate to perpendicular - parallel component becomes zero
        self.play(
            Rotate(vector_a, angle=PI/2, about_point=ORIGIN),
            run_time=2
        )
        self.wait(1)

        # Rotate to parallel - perpendicular component becomes zero
        self.play(
            Rotate(vector_a, angle=-PI/2, about_point=ORIGIN),
            run_time=2
        )
        self.wait(1)


class RotatingReferenceDecomposition(Scene):
    """Demo: Decomposition updates as reference vector B rotates"""

    def construct(self):
        # Vector to decompose (fixed)
        vector_a = Arrow(ORIGIN, RIGHT * 2.5 + UP * 1.5, buff=0, color=RED)

        # Rotating reference vector
        vector_b = Arrow(ORIGIN, RIGHT * 3, buff=0, color=BLUE)

        # Create dynamic decomposition
        parallel = always_redraw(
            lambda: VectorUtils.decompose_parallel(vector_a, vector_b, color=GREEN)
        )

        perp = always_redraw(
            lambda: VectorUtils.decompose_perp(vector_a, vector_b, color=ORANGE)
        )

        dashed = always_redraw(
            lambda: DashedLine(vector_a.get_end(), parallel.get_end(), color=GRAY, dash_length=0.1)
        )

        # Show initial state
        self.play(GrowArrow(vector_a))
        self.play(GrowArrow(vector_b))
        self.add(parallel, perp, dashed)
        self.wait(1)

        # Rotate reference vector - decomposition changes
        self.play(
            Rotate(vector_b, angle=PI/2, about_point=ORIGIN),
            run_time=3
        )
        self.wait(1)

        # Continue rotation
        self.play(
            Rotate(vector_b, angle=PI/2, about_point=ORIGIN),
            run_time=3
        )
        self.wait(1)

        # Return to start
        self.play(
            Rotate(vector_b, angle=PI, about_point=ORIGIN),
            run_time=3
        )
        self.wait(1)


class ScalingVectorDecomposition(Scene):
    """Demo: Decomposition updates as vector magnitude changes"""

    def construct(self):
        # Fixed reference vector
        vector_b = Arrow(ORIGIN, RIGHT * 3, buff=0, color=BLUE)

        # Vector that will scale
        vector_a = Arrow(ORIGIN, RIGHT * 1 + UP * 1, buff=0, color=RED)

        # Create dynamic decomposition
        parallel = always_redraw(
            lambda: VectorUtils.decompose_parallel(vector_a, vector_b, color=GREEN)
        )

        perp = always_redraw(
            lambda: VectorUtils.decompose_perp(vector_a, vector_b, color=ORANGE)
        )

        dashed = always_redraw(
            lambda: DashedLine(vector_a.get_end(), parallel.get_end(), color=GRAY, dash_length=0.1)
        )

        # Show initial state
        self.add(vector_b, vector_a, parallel, perp, dashed)
        self.wait(1)

        # Scale up - decomposition components scale proportionally
        self.play(
            vector_a.animate.put_start_and_end_on(ORIGIN, RIGHT * 2.5 + UP * 2.5),
            run_time=3
        )
        self.wait(1)

        # Scale down
        self.play(
            vector_a.animate.put_start_and_end_on(ORIGIN, RIGHT * 0.5 + UP * 0.5),
            run_time=3
        )
        self.wait(1)

        # Return to original
        self.play(
            vector_a.animate.put_start_and_end_on(ORIGIN, RIGHT * 1 + UP * 1),
            run_time=2
        )
        self.wait(1)


class InclinedPlaneForceDecomposition(Scene):
    """Practical example: Force decomposition on an inclined plane"""

    def construct(self):
        # Create inclined plane (line)
        angle = PI/6  # 30 degrees
        plane = Line(LEFT * 3, RIGHT * 3, color=GRAY).rotate(angle, about_point=ORIGIN)

        # Gravity force vector (pointing down)
        gravity = Arrow(ORIGIN, DOWN * 2, buff=0, color=RED)

        # Create slope direction (parallel to plane)
        slope_direction = Arrow(ORIGIN, RIGHT * 3, buff=0, color=BLUE).rotate(angle, about_point=ORIGIN)

        # Show plane and force
        self.play(Create(plane))
        self.wait(0.5)
        self.play(GrowArrow(gravity))
        self.wait(0.5)
        self.play(GrowArrow(slope_direction))
        self.wait(1)

        # Decompose gravity into parallel (down the slope) and perpendicular (into the plane)
        parallel_force = VectorUtils.decompose_parallel(gravity, slope_direction, color=GREEN)
        perp_force = VectorUtils.decompose_perp(gravity, slope_direction, color=ORANGE)

        # Show decomposition
        self.play(GrowArrow(parallel_force))
        self.wait(0.5)

        self.play(GrowArrow(perp_force))
        self.wait(1)

        # Add dashed line
        dashed = DashedLine(gravity.get_end(), parallel_force.get_end(), color=GRAY, dash_length=0.1)
        self.play(Create(dashed))
        self.wait(2)


class MultipleDecompositions(Scene):
    """Demo: Multiple simultaneous decompositions with updaters"""

    def construct(self):
        # Central reference vector
        ref_vector = Arrow(ORIGIN, RIGHT * 3, buff=0, color=BLUE)

        # Multiple vectors at different angles
        angles = [PI/6, PI/3, PI/2, 2*PI/3, 5*PI/6]
        vectors = VGroup()
        decompositions = VGroup()

        for i, angle in enumerate(angles):
            # Create vector at angle
            vec = Arrow(ORIGIN, RIGHT * 2, buff=0, color=RED).rotate(angle, about_point=ORIGIN)
            vectors.add(vec)

            # Create decomposition components
            parallel = always_redraw(
                lambda v=vec: VectorUtils.decompose_parallel(v, ref_vector, color=GREEN, stroke_width=2)
            )

            perp = always_redraw(
                lambda v=vec: VectorUtils.decompose_perp(v, ref_vector, color=ORANGE, stroke_width=2)
            )

            decompositions.add(VGroup(parallel, perp))

        # Show reference
        self.play(GrowArrow(ref_vector))
        self.wait(0.5)

        # Show all vectors
        self.play(LaggedStart(*[GrowArrow(v) for v in vectors], lag_ratio=0.2))
        self.wait(0.5)

        # Show all decompositions
        self.add(*decompositions)
        self.wait(2)

        # Rotate reference vector - all decompositions update
        self.play(
            Rotate(ref_vector, angle=PI/3, about_point=ORIGIN),
            run_time=4
        )
        self.wait(1)

        # Rotate back
        self.play(
            Rotate(ref_vector, angle=-PI/3, about_point=ORIGIN),
            run_time=4
        )
        self.wait(1)


class OppositeDirectionDecomposition(Scene):
    """Demo: Decomposition when vectors point in opposite directions"""

    def construct(self):
        # Reference vector (pointing right)
        vector_b = Arrow(ORIGIN, RIGHT * 3, buff=0, color=BLUE)

        # Vector pointing opposite direction (starts pointing left)
        vector_a = Arrow(ORIGIN, LEFT * 2 + UP * 0.5, buff=0, color=RED)

        # Create dynamic decomposition
        parallel = always_redraw(
            lambda: VectorUtils.decompose_parallel(vector_a, vector_b, color=GREEN)
        )

        perp = always_redraw(
            lambda: VectorUtils.decompose_perp(vector_a, vector_b, color=ORANGE)
        )

        dashed = always_redraw(
            lambda: DashedLine(vector_a.get_end(), parallel.get_end(), color=GRAY, dash_length=0.1)
        )

        # Show initial state
        self.play(GrowArrow(vector_b))
        self.play(GrowArrow(vector_a))
        self.add(parallel, perp, dashed)
        self.wait(1)

        # Rotate vector_a to show parallel component changing sign
        self.play(
            Rotate(vector_a, angle=PI, about_point=ORIGIN),
            run_time=4,
            rate_func=smooth
        )
        self.wait(1)

        # Continue rotation
        self.play(
            Rotate(vector_a, angle=PI, about_point=ORIGIN),
            run_time=4,
            rate_func=smooth
        )
        self.wait(1)
