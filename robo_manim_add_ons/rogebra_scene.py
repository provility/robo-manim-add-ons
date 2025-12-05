"""
RogebraScene: A Scene subclass with utility methods for common animations.
"""

from manim import Scene, FadeIn, FadeOut, Transform, ReplacementTransform


class RogebraScene(Scene):
    """A Scene subclass with convenient animation methods."""

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
