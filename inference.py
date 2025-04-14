# filepath: /Users/ankawolanska/Documents/lab_01_MLOps_intro/MLOps_intro/inference.py
import joblib
from sklearn.datasets import load_iris


def load_model(file_path="model.joblib"):
    """Load the trained model from a file."""
    try:
        model = joblib.load(file_path)
        print(f"Model loaded from {file_path}")
        return model
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Model file '{file_path}' not found. Train and save the model first."
        )


def predict(model, input_data):
    """Use the model to make predictions and return the predicted class as a string."""
    iris = load_iris()
    class_names = iris.target_names
    prediction = model.predict([input_data])
    predicted_class = class_names[prediction[0]]
    return predicted_class


if __name__ == "__main__":
    # Example usage
    model = load_model("model.joblib")
    sample_input = [1.3, 7.5, 7.4, 4.2]
    predicted_class = predict(model, sample_input)
    print(f"Predicted class: {predicted_class}")
