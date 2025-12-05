from manim import *
from itertools import cycle
class TextPositionRenderHelper:
    @staticmethod
    def render_subscripts(tex, color_tex=True):
        """
        Render subscripts for a given MathTex object.

        Args:
        tex (MathTex): The MathTex object for which to generate subscripts.
        color_tex (bool): Whether to apply the same colors to the MathTex content.

        Returns:
        VGroup: Group containing the original MathTex object and its subscripts.
        """
        subscripts = VGroup()
        colors = cycle([RED, TEAL, GREEN, BLUE, PURPLE])
        for j, word in enumerate(tex):
            for i, subtex in enumerate(word):
                color = next(colors)
                sub = Text(f"{j},{i}", color=color).scale(0.3)
                sub.next_to(subtex, DOWN, buff=0.05)
                subscripts.add(sub)
                if color_tex:
                    subtex.set_color(color)
        return VGroup(tex, subscripts)
    
    @staticmethod
    def render_single_mathtex(mathtex, word_index=None):
        """
        Render a single MathTex object with subscripts.

        Args:
        mathtex (MathTex): The MathTex object to render.

        Returns:
        VGroup: Group containing the MathTex object and its rendered subscripts.
        """
        if word_index is None:
            return TextPositionRenderHelper.render_subscripts(mathtex)
        else:   
            return TextPositionRenderHelper.render_subscripts(mathtex[word_index])

    @staticmethod
    def render_two_mathtex(mathtex1, mathtex2, 
                           word_index_1=None, word_index_2=None):
        """
        Render two MathTex objects side by side with subscripts.

        Args:
        mathtex1 (MathTex): The first MathTex object.
        mathtex2 (MathTex): The second MathTex object.

        Returns:
        VGroup: Group containing both MathTex objects and their rendered subscripts.
        """
        if word_index_1 is None:
            group1 = TextPositionRenderHelper.render_subscripts(mathtex1)
        else:
            group1 = TextPositionRenderHelper.render_subscripts(mathtex1[word_index_1])
        if word_index_2 is None:
            group2 = TextPositionRenderHelper.render_subscripts(mathtex2)
        else:
            group2 = TextPositionRenderHelper.render_subscripts(mathtex2[word_index_2])
        return VGroup(group1, group2).arrange(DOWN, buff=2)
