import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Step 1: Load and clean data
df = pd.read_csv("../cluster/feri_clustered_results.csv")
df = df.dropna(subset=["Pesticide_applied_acreage", "hired_farm_labor", "num_inspections", "num_violations"])

# Step 2: Define features and target
X = df[["Pesticide_applied_acreage", "hired_farm_labor", "num_inspections"]]
y = df["num_violations"]

# Step 3: Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Predict and evaluate
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

# Step 6: Output results
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
print("R² Score:", r2)
print("Mean Squared Error:", mse)

# Step 7: Plot actual vs. predicted violations
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color="red", linestyle="--", linewidth=2)
plt.xlabel("Actual Violations")
plt.ylabel("Predicted Violations")
plt.title("Actual vs. Predicted WPS Violations (w/ Inspections Included)")
plt.grid(True)
plt.tight_layout()
plt.savefig("actual_vs_predicted_violations_with_inspections.png")
plt.show()
