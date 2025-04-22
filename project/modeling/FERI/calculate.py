import pandas as pd

# Load your cleaned dataset
df = pd.read_csv("../merge/merged_analysis_data.csv")  # Update with your actual file path

# Make sure all numeric columns are read properly
df["num_violations"] = pd.to_numeric(df["num_violations"], errors="coerce")
df["num_inspections"] = pd.to_numeric(df["num_inspections"], errors="coerce")
df["Pesticide_applied_acreage"] = pd.to_numeric(df["Pesticide_applied_acreage"], errors="coerce")
df["hired_farm_labor"] = pd.to_numeric(df["hired_farm_labor"], errors="coerce")

# Step 1: Compute domain-specific risk metrics
df["violations_per_inspection"] = df["num_violations"] / df["num_inspections"]
df["pesticide_per_worker"] = df["Pesticide_applied_acreage"] / df["hired_farm_labor"]

# Step 2: Handle divide-by-zero or missing data
df = df.dropna(subset=["violations_per_inspection", "pesticide_per_worker"])

# Step 3: Define weights (you can adjust these if needed)
alpha = 0.5
beta = 0.5

# Step 4: Compute FERI
df["FERI"] = (alpha * df["pesticide_per_worker"]) + (beta * df["violations_per_inspection"])

# Step 5: Save to file or preview
df.to_csv("feri_index_results.csv", index=False)
print(df[["state", "year", "FERI"]].sort_values("FERI", ascending=False).head(10))
