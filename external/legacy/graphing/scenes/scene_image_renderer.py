import os
from dotenv import load_dotenv
from manim import *
from PIL import Image
import io

class GraphRenderer:
    
      @classmethod
      def _build_image_from_dynamic_scene(self, unique_id, commands, scene_class=Scene):
           # Generate a unique class name
           class_name = f"UserScene_{unique_id.replace('-', '_')}"
            
            # Dynamically create a new scene class with the unique name
           UserScene = type(class_name, (scene_class,), {
                "construct": lambda self: self.construct_scene()
            })

                # Method to define the scene
           def construct_scene(self):
                # iterate over the commands
                for command in commands:
                    command.execute(self)
                    
               
        
            # Assign the method to the class
           UserScene.construct_scene = construct_scene
            # Render the scene
           scene = UserScene()
           scene.render()  
           frame_array = scene.renderer.get_frame()
            # Convert the numpy array to a PIL Image object
           image = Image.fromarray(frame_array)
           return image
               
            
      @classmethod
      def bootstrap(self):
        # Bootstrap the graph renderer
        load_dotenv()
        # Set up a unique output directory for this process
        user_media_dir = os.getenv("USER_MEDIA_DIR")

        # Configure the Manim media directory
        config.media_dir = user_media_dir
        config.images_dir = os.path.join(user_media_dir, "images")
        config["format"] = "png"
        config["save_last_frame"] = True
    
      @classmethod
      def render_graph(self, unique_id, commands):
            
        resultant_image = self._build_image_from_dynamic_scene(unique_id, commands)
        
        # Create a bytes buffer for the image
        img_io = io.BytesIO()
        
        # Save the image to the buffer in PNG format
        resultant_image.save(img_io, 'PNG')
        
        # Seek to the beginning of the stream
        img_io.seek(0)
        
        return img_io