import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load your merged dataset
df = pd.read_csv("../merge/merged_analysis_data.csv")  # Update the path if needed

# Select the columns you want to normalize
features_to_normalize = [
    "num_violations",
    "num_inspections",
    "Pesticide_applied_acreage",
    "hired_farm_labor"
]

# Create a copy to preserve the original
normalized_df = df.copy()

# Apply Z-score normalization
scaler = StandardScaler()
normalized_values = scaler.fit_transform(normalized_df[features_to_normalize])

# Create new column names
normalized_column_names = [f"{col}_zscore" for col in features_to_normalize]

# Add normalized values back to the dataframe
normalized_df[normalized_column_names] = normalized_values

# Save to CSV (optional)
normalized_df.to_csv("normalized_analysis_data.csv", index=False)

# Preview the result
print(normalized_df.head())
