from graphing.geo.model.model_point import ModelPoint


class ModelCoordinate(ModelPoint):
    def __init__(self, x, y, z=0):
        super().__init__(x, y, z)
       

    @staticmethod
    def from_point(point:ModelPoint):
        model_coordinate = None
        
        def create():
            nonlocal model_coordinate
            model_coordinate = ModelCoordinate(point.x, point.y, point.z)
           
        def update():
            nonlocal model_coordinate
            model_coordinate.set(point.x, point.y, point.z)

        create()
        point.on_change(update)
        
        return model_coordinate
        