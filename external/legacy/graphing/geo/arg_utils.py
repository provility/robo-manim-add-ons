import numpy as np

class ArgUtils:
    
    @staticmethod
    def extract_num_py_point(tuple_or_numpy_array):
        if isinstance(tuple_or_numpy_array, np.ndarray):
            return tuple_or_numpy_array
        
        if hasattr(tuple_or_numpy_array, '__getitem__'):
            if hasattr(tuple_or_numpy_array, '__len__') and len(tuple_or_numpy_array) == 2:
                return np.array([tuple_or_numpy_array[0], tuple_or_numpy_array[1]])
            
        if hasattr(tuple_or_numpy_array, 'x') and hasattr(tuple_or_numpy_array, 'y'):
            return np.array([tuple_or_numpy_array.x, tuple_or_numpy_array.y])
       
        raise ValueError("Input must be a tuple with 2 elements or a numpy array")