import inspect
from typing import get_type_hints

def generate_class_with_signatures(cls):
    class_name = cls.__name__
    base_classes = ", ".join(base.__name__ for base in cls.__bases__)
    class_signature = f"class {class_name}({base_classes}):\n"
    
    for name, method in inspect.getmembers(cls, predicate=inspect.isfunction):
        if name.startswith("__") and name.endswith("__"):
            continue  # Skip special methods
        
        method_signature = f"    def {name}("
        signature = inspect.signature(method)
        params = []
        for param_name, param in signature.parameters.items():
            param_str = param_name
            if param.annotation is not inspect.Parameter.empty:
                param_str += f": {param.annotation.__name__}"
            if param.default is not inspect.Parameter.empty:
                param_str += f" = {param.default}"
            params.append(param_str)
        method_signature += ", ".join(params) + ")"
        
        if signature.return_annotation is not inspect.Signature.empty:
            method_signature += f" -> {signature.return_annotation.__name__}"
        
        method_signature += ":\n"
        method_signature += "        pass\n"
        
        class_signature += method_signature
    
    return class_signature

# Example usage
class BaseClass:
    def base_method(self, x: int) -> None:
        print(x)

class Example(BaseClass):
    def method1(self, a: int, b: str = "default") -> None:
        print(a, b)
    
    def method2(self, x: float) -> float:
        return x * 2

class_with_signatures = generate_class_with_signatures(Example)
print(class_with_signatures)
