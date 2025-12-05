
from manim import *

class GraphSheetArrangement:
    def __init__(self, graph_sheets):
        self.graph_sheets = graph_sheets

    def fit_graphsheets_in_columns(self, num_columns:int=2):
        graph_sheets = self.graph_sheets
        num_sheets = len(graph_sheets)
        num_rows = (num_sheets + num_columns - 1) // num_columns  # Ceiling division

        # Create a 2D list to hold the graph sheets
        grid = [[] for _ in range(num_rows)]
        for i, sheet in enumerate(graph_sheets):
            grid[i // num_columns].append(sheet)

        # Create VGroups for each row
        rows = [VGroup(*row).arrange(RIGHT, buff=0.5) for row in grid]
        
        # Arrange the rows vertically
        vgroup = VGroup(*rows).arrange(DOWN, buff=0.5)
        
        vgroup.scale_to_fit_width(config.frame_width - 1)
        vgroup.center()
        return vgroup
    
    def fit_graphsheets_in_rows(self, num_rows:int=2):
        graph_sheets = self.graph_sheets
        num_sheets = len(graph_sheets)
        num_columns = (num_sheets + num_rows - 1) // num_rows  # Ceiling division

        # Create a 2D list to hold the graph sheets
        grid = [[] for _ in range(num_rows)]
        for i, sheet in enumerate(graph_sheets):
            grid[i % num_rows].append(sheet)

        # Create VGroups for each column
        columns = [VGroup(*column).arrange(DOWN, buff=0.5) for column in grid]
        
        # Arrange the columns horizontally
        vgroup = VGroup(*columns).arrange(RIGHT, buff=0.5)
        
        vgroup.scale_to_fit_height(config.frame_height - 1)
        vgroup.center()
        return vgroup
        
    def fit_graphsheets_in_grid(self,  num_rows:int=2, num_columns:int=2):
        graph_sheets = self.graph_sheets
        num_sheets = len(graph_sheets)
        num_rows = (num_sheets + num_columns - 1) // num_columns  # Ceiling division

        # Create a 2D list to hold the graph sheets
        grid = [[] for _ in range(num_rows)]
        for i, sheet in enumerate(graph_sheets):
            grid[i // num_columns].append(sheet)

        # Create VGroups for each row
        rows = [VGroup(*row).arrange(RIGHT, buff=0.5) for row in grid]
        
        # Arrange the rows vertically
        vgroup = VGroup(*rows).arrange(DOWN, buff=0.5)
        
        vgroup.scale_to_fit_width(config.frame_width - 1)   
        vgroup.scale_to_fit_height(config.frame_height - 1)
        vgroup.center()
        return vgroup
    
    def fit_by_config(self, config: dict, arrangement_direction='top_to_bottom'):
        if not config or not isinstance(config, dict):
            raise ValueError("Invalid configuration for graph sheet arrangement")

        vgroup = VGroup()
        total_width = 0
        total_height = 0

        for sheet_name, sheet_config in config.items():
            if sheet_name not in self.graph_sheets:
                raise ValueError(f"Graph sheet '{sheet_name}' not found")
            
            graph_sheet = self.graph_sheets[sheet_name]
            
            if 'width' not in sheet_config or 'height' not in sheet_config:
                raise ValueError(f"Missing width or height in configuration for graph sheet '{sheet_name}'")
            
            # Convert percentage to actual size
            width = sheet_config['width'] / 100 * config.frame_width
            height = sheet_config['height'] / 100 * config.frame_height
            
            # Scale the graph sheet to fit the specified dimensions
            graph_sheet.scale_to_fit_width(width)
            graph_sheet.scale_to_fit_height(height)
            
            vgroup.add(graph_sheet)
            total_width = max(total_width, width)
            total_height += height

        # Arrange the scaled graph sheets based on arrangement_direction
        if arrangement_direction == 'top_to_bottom':
            vgroup.arrange(DOWN, buff=0)
        elif arrangement_direction == 'bottom_to_top':
            vgroup.arrange(UP, buff=0)
        elif arrangement_direction == 'left_to_right':
            vgroup.arrange(RIGHT, buff=0)
        elif arrangement_direction == 'right_to_left':
            vgroup.arrange(LEFT, buff=0)
        else:
            raise ValueError("Invalid arrangement_direction. Choose 'top_to_bottom', 'bottom_to_top', 'left_to_right', or 'right_to_left'")
        
        # Scale the entire group if it exceeds frame dimensions
        if arrangement_direction in ['top_to_bottom', 'bottom_to_top']:
            if total_height > config.frame_height:
                vgroup.scale_to_fit_height(config.frame_height)
        else:
            if total_width > config.frame_width:
                vgroup.scale_to_fit_width(config.frame_width)
        
        # Center the entire group
        vgroup.center()
        
        return vgroup
   
    def fit_graphsheets_using_proportions(self, proportions:list[float], arrangement_direction:str='top_to_bottom'):
        graph_sheets = self.graph_sheets
        if len(proportions) != len(graph_sheets):
            raise ValueError("The number of proportions must match the number of graph sheets")
        
   
        
        # Create a VGroup to hold the graph sheets
        vgroup = VGroup()
        
        
        for i, graph_sheet in enumerate(graph_sheets):
            vgroup.add(graph_sheet)
        
        # Arrange the graph sheets based on the arrangement direction
        if arrangement_direction == 'left_to_right':
            vgroup.arrange(RIGHT, buff=0)
        elif arrangement_direction == 'top_to_bottom':
            vgroup.arrange(DOWN, buff=0)
        
        return vgroup
