# MLFlow Demonstration

This directory contains a minimal demonstration of using MLFlow to track experiments, log metrics, hyperparameters, and models. It uses the Scikit-Learn `load_diabetes` dataset to train a `RandomForestRegressor`.

## How to Run the Demonstration

1. **Create and Activate a Virtual Environment:**
   ```bash
   cd ML_Flow
   python -m venv mlflow_env
   source mlflow_env/bin/activate
   ```

2. **Install the Requirements:**
   ```bash
   pip install -r req.txt
   ```

3. **Run the Training Script:**
   ```bash
   python train.py
   ```
   *You will see the metrics and Run IDs printed in your terminal. This script trains 3 different models with different hyperparameters and tracks them all in MLFlow.*

4. **View the MLFlow UI:**
   ```bash
   mlflow ui --backend-store-uri sqlite:///mlflow.db
   ```
   *After running this command, open your browser and go to http://127.0.0.1:5000. You will see the `Diabetes_Regression_Experiment` with all 3 runs. You can click on them to compare their metrics and see the stored `.pkl` models inside the artifacts section.*
