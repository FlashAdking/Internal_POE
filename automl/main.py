import joblib
from flaml import AutoML
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split

# 1. Prepare the Dataset
# We use the breast cancer dataset (binary classification) as a robust example
data = load_breast_cancer()
X = data.data
y = data.target

# Split into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 2. Initialize and Configure FLAML AutoML
automl = AutoML()

automl_settings = {
    "time_budget": 60,                # Total time limit in seconds
    "metric": "accuracy",             # Optimization metric ('auto', 'accuracy', 'f1', 'roc_auc', etc.)
    "task": "classification",         # Type of ML task
    "estimator_list": ["lgbm", "xgboost", "rf", "extra_tree"], # Algorithms to try
    "log_file_name": "flaml_training.log", # Saves progression details
    "seed": 42,                       # Ensures reproducibility
}

# 3. Run the AutoML Optimization
print("Starting FLAML optimization (Budget: 60 seconds)...")
automl.fit(X_train=X_train, y_train=y_train, **automl_settings)

# 4. Extract and Inspect the Best Model
print("\n=== Optimization Complete ===")
print(f"Best ML Algorithm found: {automl.best_estimator}")
print(f"Best Hyperparameters: {automl.best_config}")
print(f"Best Validation Accuracy: {1 - automl.best_loss:.4f}")

# 5. Evaluate on the Testing Set
# The automl instance automatically acts as the best trained estimator
y_pred = automl.predict(X_test)
test_accuracy = accuracy_score(y_test, y_pred)

print(f"\nOut-of-Sample Test Accuracy: {test_accuracy:.4f}")
print("\nDetailed Classification Report:")
print(classification_report(y_test, y_pred, target_names=data.target_names))

# 6. Save the Final Optimized Pipeline
output_path = "flaml_optimized_model.joblib"
joblib.dump(automl, output_path)
print(f"\nSuccessfully serialized and saved model to '{output_path}'")