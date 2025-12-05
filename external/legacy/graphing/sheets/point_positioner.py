class PointPositioner:
    def __init__(self, scene, graph_sheet):
        self.scene = scene
        self.graph_sheet = graph_sheet
    
    """
    buffer is the distance from the point to the text
    """
    def move_to_positioner(self, point_name_or_model, buff=0.1    ):
        point_name_or_model = self.graph_sheet._point_from_input(point_name_or_model)
        ui_point = self.graph_sheet.geo_mapper.model_point_to_ui_point(point_name_or_model)
        return lambda text: text.move_to(ui_point).shift(buff)
    
    def to_corner_positioner(self, direction, buff=0.1):
        return lambda text: text.to_corner(direction, buff=buff)
    
    def to_edge_positioner(self, direction, buff=0.1):
        return lambda text: text.to_edge(direction, buff=buff)    
    
    
    
    
    