from manim import *

from graphing.math.function_expression_utils import FunctionUtils
class LabelBetweenArrows(VGroup):
    def __init__(self, left_extreme, right_extreme, label_text, 
                 color=BLUE,
                 gap=0.05, **kwargs):
        super().__init__(**kwargs)
        
        label = None
        
        if FunctionUtils.is_math(label_text):
            # Create the label text
            label = MathTex(label_text).set_color(color)
        else:
            label = Text(label_text).set_color(color)
        
        # Calculate the center point between the two extremes and position the label
        midpoint = (left_extreme + right_extreme) / 2
        label.move_to(midpoint)
        
        left_arrow_line = Line(start=midpoint, end=left_extreme)
        left_arrow_start = left_arrow_line.point_from_proportion(0.15)
        # Calculate the adjusted end points for the arrows based on the label width
        left_arrow_end = left_extreme  # End at the specified left extreme point


        right_arrow_line = Line(start=midpoint, end=right_extreme)
        right_arrow_start = right_arrow_line.point_from_proportion(0.15)
        right_arrow_end = right_extreme  # End at the specified right extreme point

        # Scale the label down to make the gaps between the arrows and the label smaller
        label.scale(0.7)
        
        # Create arrows pointing outward from the label with a gap
        left_arrow = Arrow(start=left_arrow_start, end=left_arrow_end, buff=gap, color=color)
        right_arrow = Arrow(start=right_arrow_start, end=right_arrow_end, buff=gap, color=color)

        # Add the arrows and label to the VGroup
        self.add(left_arrow, right_arrow, label)
        
        # Store components for animation
        self.label = label
        self.left_arrow = left_arrow
        self.right_arrow = right_arrow

    def custom_create_animation(self):
        # Fade in the label
        label_anim = FadeIn(self.label)
        
        # Create animations for drawing the arrows from start to end
        left_arrow_anim = Create(self.left_arrow)
        right_arrow_anim = Create(self.right_arrow)
        
        # Combine animations: label fades in, then arrows draw simultaneously
        return AnimationGroup(
            label_anim,
            AnimationGroup(left_arrow_anim, right_arrow_anim),
            lag_ratio=0.4  # Add a slight delay between label and arrows
        )   
