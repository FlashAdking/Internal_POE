import bentoml
import numpy as np

# 1. Define the service using a class and the @bentoml.service decorator
@bentoml.service(name="iris_prediction_service")
class IrisPredictor:
    
    # 2. Declare the model dependency at the class level
    iris_model = bentoml.models.BentoModel("svc_iris_model:latest")

    def __init__(self):
        # 3. Load the model ONCE when the service starts
        # This keeps the model in memory so predictions are lightning fast
        self.model = bentoml.sklearn.load_model(self.iris_model)

    # 4. Define the endpoint using @bentoml.api
    # Notice we just use standard type hints (np.ndarray and dict) now
    @bentoml.api
    def predict(self, data: np.ndarray) -> dict:
        
        # Run the inference
        prediction = self.model.predict(data)
        
        # Return the dictionary (BentoML auto-converts this to JSON)
        return {"prediction": prediction.tolist()}