from abc import ABC, abstractmethod


class BaseCommand(ABC):
    def __init__(self,  **kwargs):
        self.kwargs = kwargs

    def execute(self, scene):
        self.pre_execute(scene)
        self.do_execute(scene)
        self.post_execute(scene)
        raise NotImplementedError
    
    def pre_execute(self, scene):
        pass
    
    def post_execute(self, scene):
        pass
    
    @abstractmethod
    def do_execute(self, scene):
        raise NotImplementedError
    
    """
    Before Adding shapes or plots, we must 
    call AddGraphSheet2DCommand. This will set the
    graph_sheet2d object in the scene.
    """
    def get_graph_sheet_2d(self, scene):
        return scene.graph_sheet2d