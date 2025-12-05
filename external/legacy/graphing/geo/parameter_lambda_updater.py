class ParameterLambdaUpdater:
    def __init__(self, source_model, source_attribute:str, target_model, target_attribute:str):
        self.source_model = source_model
        self.source_attribute = source_attribute
        self.target_model = target_model
        self.target_attribute = target_attribute
        
    def update(self):
        source_value = getattr(self.source_model, self.source_attribute)
        setattr(self.target_model, self.target_attribute, source_value)
        
  
    @staticmethod
    def from_param_change(source_model, source_attribute:str, target_model, target_attribute:str):
        parameter_lambda_updater = ParameterLambdaUpdater(source_model, source_attribute, target_model, target_attribute)   
        source_model.on_change(lambda: parameter_lambda_updater.update())
        return parameter_lambda_updater
         
        
        