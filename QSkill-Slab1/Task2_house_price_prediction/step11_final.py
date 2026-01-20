import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

print(" HOUSE PRICE PREDICTION USING LINEAR REGRESSION\n")

# Load dataset
data = pd.read_csv("house_data.csv")
data = data.dropna()
data = pd.get_dummies(data, drop_first=True)

X = data.drop("price", axis=1)
y = data["price"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

#  NEW HOUSE PRICE PREDICTION (THIS WILL SHOW)
new_house = X.iloc[[0]]
new_price = model.predict(new_house)
print("\n Predicted price for a new house:", new_price[0])

# Visualization (LAST)
plt.figure()
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")
plt.show()
