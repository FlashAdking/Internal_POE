# pyrefly: ignore [missing-import]
import mlflow
# pyrefly: ignore [missing-import]
import mlflow.sklearn
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import os

# Ensure the MLFlow tracking database is created locally
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("Diabetes_Regression_Experiment")

def train_model(n_estimators, max_depth):
    # 1. Load the diabetes dataset as requested
    diabetes = load_diabetes()
    X = diabetes.data
    y = diabetes.target

    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 2. Start an MLFlow run to track this specific training iteration
    with mlflow.start_run():
        print(f"Training model with n_estimators={n_estimators}, max_depth={max_depth}...")
        
        # Log Hyperparameters
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)

        # Train the model
        model = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

        # Calculate metrics
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        # Log Metrics
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("r2_score", r2)

        # Log the trained model as an artifact so it can be loaded later
        mlflow.sklearn.log_model(model, "random_forest_model")

        # Save standard pickel file locally as a demonstration
        import joblib
        joblib.dump(model, f"diabetes_model_{n_estimators}_{max_depth}.pkl")

        print(f"Metrics: MSE={mse:.2f}, R2={r2:.2f}")
        print(f"Run ID: {mlflow.active_run().info.run_id}")
        print("-" * 50)

if __name__ == "__main__":
    # Simulate a hyperparameter tuning process by running multiple experiments
    print("Starting MLFlow Experiment Tracking Demonstration...\n")
    train_model(n_estimators=50, max_depth=5)
    train_model(n_estimators=100, max_depth=10)
    train_model(n_estimators=200, max_depth=15)
    
    print("\nDemonstration complete. To view the MLFlow UI with the tracked experiments:")
    print("Run the following command in your terminal:")
    print("  mlflow ui --backend-store-uri sqlite:///mlflow.db")
    print("Then open your browser and navigate to http://127.0.0.1:5000")
