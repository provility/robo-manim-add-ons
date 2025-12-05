from graphing.geo.ui.base_ui import BaseUI


class UIPart(BaseUI):
    def __init__(self, ui_shape, graphsheet, geo_mapper, scene, style_props):
        super().__init__(style_props)
        self.ui_shape = ui_shape
        self.graphsheet = graphsheet
        self.geo_mapper = geo_mapper
        self.scene = scene
        
        
    def view(self):
        return self.ui_shape