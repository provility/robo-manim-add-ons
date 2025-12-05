from graphing.geo.ui.base_ui import BaseUI
from graphing.geo.ui.ui_style_props import UIStyleProps


class BaseUI3D(BaseUI):
    def __init__(self, style_props:UIStyleProps) -> None:
        super().__init__(style_props)
        
    @property
    def z(self):
        return self.ui_part.z       