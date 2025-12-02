"""
Vector utilities for Manim objects.

Provides helper class for vector operations like forward projection.
"""

import numpy as np
from manim import Mobject


class VectorUtils:
    """Utility class for vector operations on Manim objects."""

    @staticmethod
    def forward(source: Mobject, distance: float) -> Mobject:
        """
        Create a copy of a vector shifted forward along its direction.

        This method takes a vector (Line, Arrow, or any Mobject with start/end points)
        and creates a copy shifted forward by the specified distance along the
        vector's direction.

        Args:
            source: The source Mobject (typically a Line or Arrow) to copy and shift
            distance: The distance to shift the copy forward along the vector's direction

        Returns:
            A new Mobject that is a copy of the source, shifted forward by the distance

        Example:
            >>> from manim import *
            >>> from robo_manim_add_ons.vector_utils import VectorUtils
            >>>
            >>> source_vector = Arrow(ORIGIN, RIGHT * 2, color=BLUE)
            >>> shifted_vector = VectorUtils.forward(source_vector, 1.5)
            >>> # Creates a copy of the arrow shifted 1.5 units to the right
        """
        # Calculate shift direction
        direction = source.get_end() - source.get_start()
        direction_unit = direction / np.linalg.norm(direction)
        shift_vector = direction_unit * distance
        shifted_vector = source.copy()
        shifted_vector.shift(shift_vector)

        return shifted_vector

    @staticmethod
    def backward(source: Mobject, distance: float) -> Mobject:
        """
        Create a copy of a vector shifted backward (opposite to its direction).

        This method takes a vector (Line, Arrow, or any Mobject with start/end points)
        and creates a copy shifted backward by the specified distance, opposite to the
        vector's direction.

        Args:
            source: The source Mobject (typically a Line or Arrow) to copy and shift
            distance: The distance to shift the copy backward (opposite to vector direction)

        Returns:
            A new Mobject that is a copy of the source, shifted backward by the distance

        Example:
            >>> from manim import *
            >>> from robo_manim_add_ons.vector_utils import VectorUtils
            >>>
            >>> source_vector = Arrow(ORIGIN, RIGHT * 2, color=BLUE)
            >>> shifted_vector = VectorUtils.backward(source_vector, 1.5)
            >>> # Creates a copy of the arrow shifted 1.5 units to the left
        """
        # Calculate shift direction
        direction = source.get_end() - source.get_start()
        direction_unit = direction / np.linalg.norm(direction)
        shift_vector = direction_unit * -distance
        shifted_vector = source.copy()
        shifted_vector.shift(shift_vector)

        return shifted_vector

    @staticmethod
    def perpMove(source: Mobject, distance: float) -> Mobject:
        """
        Create a copy of a vector shifted perpendicular to its direction.

        This method takes a vector (Line, Arrow, or any Mobject with start/end points)
        and creates a copy shifted perpendicular by the specified distance. The
        perpendicular direction is 90° counterclockwise from the vector's direction.

        Args:
            source: The source Mobject (typically a Line or Arrow) to copy and shift
            distance: The distance to shift the copy perpendicular to vector direction
                     (positive = counterclockwise, negative = clockwise)

        Returns:
            A new Mobject that is a copy of the source, shifted perpendicular by the distance

        Example:
            >>> from manim import *
            >>> from robo_manim_add_ons.vector_utils import VectorUtils
            >>>
            >>> source_vector = Arrow(ORIGIN, RIGHT * 2, color=BLUE)
            >>> shifted_vector = VectorUtils.perpMove(source_vector, 1.5)
            >>> # Creates a copy of the arrow shifted 1.5 units upward (perpendicular)
        """
        # Calculate shift direction
        direction = source.get_end() - source.get_start()
        direction_unit = direction / np.linalg.norm(direction)
        # Perpendicular: rotate direction by 90° counterclockwise: (x,y) -> (-y,x)
        perp_direction = np.array([-direction_unit[1], direction_unit[0], 0])
        shift_vector = perp_direction * distance
        shifted_vector = source.copy()
        shifted_vector.shift(shift_vector)

        return shifted_vector

    @staticmethod
    def tailAtTip(vector_a: Mobject, vector_b: Mobject) -> Mobject:
        """
        Create a copy of vector B positioned so its tail starts at vector A's tip.

        This method is useful for vector addition visualization (tip-to-tail method),
        where you want to place one vector starting at the end of another vector.

        Args:
            vector_a: The first vector (Mobject with start/end points)
            vector_b: The second vector to position at vector_a's tip

        Returns:
            A new Mobject that is a copy of vector_b, positioned with its tail at vector_a's tip

        Example:
            >>> from manim import *
            >>> from robo_manim_add_ons.vector_utils import VectorUtils
            >>>
            >>> vector_a = Arrow(ORIGIN, RIGHT * 2, color=BLUE)
            >>> vector_b = Arrow(ORIGIN, UP * 1.5, color=RED)
            >>> vector_b_shifted = VectorUtils.tailAtTip(vector_a, vector_b)
            >>> # Creates a copy of vector_b starting at the tip of vector_a
        """
        # Calculate direction of vector B
        vec_b_direction = vector_b.get_end() - vector_b.get_start()

        # Create a copy of vector_b positioned at tip of vector_a
        shifted_vector = vector_b.copy()

        # Calculate the shift needed: from vector_b's current start to vector_a's tip
        shift_amount = vector_a.get_end() - vector_b.get_start()
        shifted_vector.shift(shift_amount)

        return shifted_vector

    @staticmethod
    def shiftAmount(vector_target: Mobject, vector_source: Mobject) -> np.ndarray:
        """
        Calculate the shift vector needed to move vector_source's tail to vector_target's tip.

        This method returns a numpy array representing the displacement needed to position
        vector_source so that its start point aligns with vector_target's end point.
        Useful for animating vectors with .animate.shift().

        Args:
            vector_target: The target vector whose tip will be the destination
            vector_source: The source vector to be shifted

        Returns:
            numpy.ndarray: The shift vector to apply to vector_source

        Example:
            >>> from manim import *
            >>> from robo_manim_add_ons.vector_utils import VectorUtils
            >>>
            >>> vector_a = Arrow(ORIGIN, RIGHT * 2, color=BLUE, buff=0)
            >>> vector_b = Arrow(LEFT, LEFT + UP, color=RED, buff=0)
            >>> shift_vector = VectorUtils.shiftAmount(vector_a, vector_b)
            >>> # In animation: self.play(vector_b.animate.shift(shift_vector))
        """
        # Calculate shift needed: from source's start to target's end
        shift_vector = vector_target.get_end() - vector_source.get_start()
        return shift_vector
