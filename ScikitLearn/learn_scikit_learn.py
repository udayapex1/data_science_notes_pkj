

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.preprocessing import StandardScaler
import numpy as np

print("===== 1. Load Dataset =====")
data = load_iris()
X = data.data
y = data.target

print("Features shape:", X.shape)
print("Target shape:", y.shape)


print("\n===== 2. Train-Test Split =====")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Train size:", X_train.shape)
print("Test size:", X_test.shape)


print("\n===== 3. Feature Scaling =====")
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


print("\n===== 4. Logistic Regression (Classification) =====")
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))


print("\n===== 5. Linear Regression (Regression Example) =====")
# simple synthetic data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

reg = LinearRegression()
reg.fit(X, y)

pred = reg.predict([[6]])
print("Prediction for 6:", pred)

print("MSE:", mean_squared_error(y, reg.predict(X)))


print("\n===== DONE =====")