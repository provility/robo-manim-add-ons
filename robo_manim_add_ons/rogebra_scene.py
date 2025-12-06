"""
RogebraScene: A Scene subclass with utility methods for common animations.
"""

from manim import MovingCameraScene, FadeIn, FadeOut, Transform, ReplacementTransform, Restore
from .text_utils import TextUtils


class RogebraScene(MovingCameraScene):
    """A MovingCameraScene subclass with convenient animation methods and camera utilities."""

    def fadeIn(self, *args):
        """
        Fade in one or more objects.
        If the last argument is a number, it's treated as run_time.

        Examples:
            self.fadeIn(obj1)
            self.fadeIn(obj1, obj2, obj3)
            self.fadeIn(obj1, obj2, 2)  # with run_time of 2 seconds
        """
        objects = list(args)
        run_time = 1  # default run_time

        # Check if last argument is a number
        if len(objects) > 0 and isinstance(objects[-1], (int, float)):
            run_time = objects.pop()

        if objects:
            self.play(*[FadeIn(obj) for obj in objects], run_time=run_time)

    def fadeOut(self, *args):
        """
        Fade out one or more objects.
        If the last argument is a number, it's treated as run_time.

        Examples:
            self.fadeOut(obj1)
            self.fadeOut(obj1, obj2, obj3)
            self.fadeOut(obj1, obj2, 2)  # with run_time of 2 seconds
        """
        objects = list(args)
        run_time = 1  # default run_time

        # Check if last argument is a number
        if len(objects) > 0 and isinstance(objects[-1], (int, float)):
            run_time = objects.pop()

        if objects:
            self.play(*[FadeOut(obj) for obj in objects], run_time=run_time)

    def amo(self, *args):
        """
        Animate move to for one or more objects.
        Format: obj1, pos1, obj2, pos2, ..., [True], [run_time]
        If True is provided, objects are copied before moving.
        If the last argument is a number, it's treated as run_time.

        Examples:
            self.amo(obj1, pos1)
            self.amo(obj1, pos1, obj2, pos2)
            self.amo(obj1, pos1, 2)  # with run_time of 2 seconds
            self.amo(obj1, pos1, True)  # copy obj1 and move to pos1
            self.amo(obj1, pos1, True, 2)  # copy with run_time
        """
        args_list = list(args)
        run_time = 1  # default run_time
        should_copy = False

        # Check if last argument is a number (run_time)
        if len(args_list) > 0 and isinstance(args_list[-1], (int, float)):
            run_time = args_list.pop()

        # Check if last argument (after removing run_time) is True (copy flag)
        if len(args_list) > 0 and args_list[-1] is True:
            should_copy = True
            args_list.pop()

        # Now we should have pairs of (object, position)
        if len(args_list) % 2 != 0:
            raise ValueError("amo requires pairs of (object, position), optionally followed by True and/or run_time")

        animations = []
        for i in range(0, len(args_list), 2):
            obj = args_list[i]
            pos = args_list[i + 1]

            # If pos is an object with get_center(), use its center
            if hasattr(pos, 'get_center'):
                pos = pos.get_center()

            if should_copy:
                # Create a copy at the original position
                obj_copy = obj.copy()
                self.add(obj_copy)
                animations.append(obj_copy.animate.move_to(pos))
            else:
                animations.append(obj.animate.move_to(pos))

        if animations:
            self.play(*animations, run_time=run_time)

    def tf(self, *args):
        """
        Transform one or more objects.
        Format: obj1, target1, obj2, target2, ..., [True], [run_time]
        If True is provided, objects are copied before transforming.
        If the last argument is a number, it's treated as run_time.

        Examples:
            self.tf(obj1, target1)
            self.tf(obj1, target1, obj2, target2)
            self.tf(obj1, target1, 2)  # with run_time of 2 seconds
            self.tf(obj1, target1, True)  # copy obj1 and transform the copy
            self.tf(obj1, target1, True, 2)  # copy with run_time
        """
        args_list = list(args)
        run_time = 1  # default run_time
        should_copy = False

        # Check if last argument is a number (run_time)
        if len(args_list) > 0 and isinstance(args_list[-1], (int, float)):
            run_time = args_list.pop()

        # Check if last argument (after removing run_time) is True (copy flag)
        if len(args_list) > 0 and args_list[-1] is True:
            should_copy = True
            args_list.pop()

        # Now we should have pairs of (source, target)
        if len(args_list) % 2 != 0:
            raise ValueError("tf requires pairs of (source, target), optionally followed by True and/or run_time")

        animations = []
        for i in range(0, len(args_list), 2):
            source = args_list[i]
            target = args_list[i + 1]

            if should_copy:
                # Create a copy of the source
                source_copy = source.copy()
                self.add(source_copy)
                animations.append(Transform(source_copy, target))
            else:
                animations.append(Transform(source, target))

        if animations:
            self.play(*animations, run_time=run_time)

    def rtf(self, *args):
        """
        ReplacementTransform one or more objects.
        Format: obj1, target1, obj2, target2, ..., [True], [run_time]
        If True is provided, objects are copied before transforming.
        If the last argument is a number, it's treated as run_time.

        Examples:
            self.rtf(obj1, target1)
            self.rtf(obj1, target1, obj2, target2)
            self.rtf(obj1, target1, 2)  # with run_time of 2 seconds
            self.rtf(obj1, target1, True)  # copy obj1 and transform the copy
            self.rtf(obj1, target1, True, 2)  # copy with run_time
        """
        args_list = list(args)
        run_time = 1  # default run_time
        should_copy = False

        # Check if last argument is a number (run_time)
        if len(args_list) > 0 and isinstance(args_list[-1], (int, float)):
            run_time = args_list.pop()

        # Check if last argument (after removing run_time) is True (copy flag)
        if len(args_list) > 0 and args_list[-1] is True:
            should_copy = True
            args_list.pop()

        # Now we should have pairs of (source, target)
        if len(args_list) % 2 != 0:
            raise ValueError("rtf requires pairs of (source, target), optionally followed by True and/or run_time")

        animations = []
        for i in range(0, len(args_list), 2):
            source = args_list[i]
            target = args_list[i + 1]

            if should_copy:
                # Create a copy of the source
                source_copy = source.copy()
                self.add(source_copy)
                animations.append(ReplacementTransform(source_copy, target))
            else:
                animations.append(ReplacementTransform(source, target))

        if animations:
            self.play(*animations, run_time=run_time)

    def zoom(self, obj, wait_time=0.3, width_factor=1.2):
        """
        Zoom to an object, wait, then restore camera.

        Args:
            obj: The object to zoom to
            wait_time: How long to wait while zoomed (default 0.3)
            width_factor: Width multiplier for zoom level (default 1.2)

        Examples:
            self.zoom(text)              # Zoom with defaults
            self.zoom(text, 1.0)         # Zoom for 1 second
            self.zoom(text, 0.5, 1.5)    # Zoom for 0.5s with 1.5x width
        """
        self.camera.frame.save_state()
        self.play(
            self.camera.frame.animate
            .set(width=obj.width * width_factor)
            .move_to(obj)
        )
        self.wait(wait_time)
        self.play(Restore(self.camera.frame))

    def text(self, mathtext, *args):
        """
        Extract a part from MathTex or create MathTex from string with flexible indexing.

        This is a pure extraction utility that doesn't modify colors or add to the scene.
        Silently fails and returns empty VMobject if indices are invalid.

        Args:
            mathtext: Either a string (creates MathTex) or existing MathTex object
            *args: Zero or more indices (int or "1:2" string slices) for extraction

        Returns:
            Extracted MathTex part or empty VMobject if extraction fails

        Examples:
            eq = self.text("x^2 + y^2")           # Create MathTex
            part = self.text("x^2 + y^2", 0)      # Extract eq[0]
            part2 = self.text("x^2 + y", 1, 2)    # Extract eq[1][2]
            part3 = self.text(eq, "1:3")          # Extract eq[1:3]
        """
        return TextUtils.text(self, mathtext, *args)

    def text2(self, mathtext, *args):
        """
        Debug utility: Extract MathTex part, color it BLUE, add to scene with ORANGE rectangle.

        This method does everything text() does, plus:
        - Colors the extracted part BLUE
        - Adds the extracted part to the scene
        - Creates an ORANGE rectangle around it
        - Adds the rectangle to the scene

        Args:
            mathtext: Either a string (creates MathTex) or existing MathTex object
            *args: Zero or more indices (int or "1:2" string slices) for extraction

        Returns:
            Extracted MathTex part or empty VMobject if extraction fails

        Examples:
            part = self.text2("x^2 + y^2", 0)     # Show eq[0] with BLUE + ORANGE box
            part2 = self.text2(eq, 1, "2:5")      # Show eq[1][2:5] with highlight
        """
        return TextUtils.text2(self, mathtext, *args)
