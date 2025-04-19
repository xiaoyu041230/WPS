import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# === Step 1: Load FERI dataset ===
df = pd.read_csv("../FERI/feri_index_results.csv")  # Update with your file path

# === Step 2: Drop rows with missing values in required columns ===
df = df.dropna(subset=["FERI", "Pesticide_applied_acreage", "hired_farm_labor", "num_violations", "num_inspections"])

# === Step 3: Calculate ratio-based indicators ===
df["pesticide_per_worker"] = df["Pesticide_applied_acreage"] / df["hired_farm_labor"]
df["violations_per_inspection"] = df["num_violations"] / df["num_inspections"]

# === Step 4: Select features for clustering ===
features = ["FERI", "pesticide_per_worker", "violations_per_inspection"]
X = df[features]

# === Step 5: Standardize features ===
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# === Step 6: K-Means clustering (3 clusters) ===
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["cluster"] = kmeans.fit_predict(X_scaled)

# === Step 7: Save or preview result ===
df.to_csv("feri_clustered_results.csv", index=False)
print(df[["state", "year", "FERI", "cluster"]].sort_values("cluster"))
