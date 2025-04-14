# filepath: /Users/ankawolanska/Documents/lab_01_MLOps_intro/MLOps_intro/training.py
import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def load_data():
    """Load and return the Iris dataset."""
    data = load_iris()
    X, y = data.data, data.target
    return X, y


def train_model(X, y):
    """Train a simple classification model and return it."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    print(
        f"Model training completed. Accuracy on test set: {model.score(X_test, y_test):.2f}"
    )
    return model


def save_model(model, file_path="model.joblib"):
    """Save the trained model to a file using joblib."""
    joblib.dump(model, file_path)
    print(f"Model saved to {file_path}")


if __name__ == "__main__":
    # Example usage
    X, y = load_data()
    model = train_model(X, y)
    save_model(model)
