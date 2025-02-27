import pandas as pd

# Load the dataset
file_path = "../originalDataFiles/wps-data.csv"  # Update this path if necessary
df = pd.read_csv(file_path)

# Step 1: Remove non-state rows (e.g., "National", U.S. territories)
df_cleaned = df[~df["state"].str.contains("National|Total|Region|Samoa|Guam|Virgin Islands|Puerto Rico", na=False)]

# Step 2: Select relevant columns

## Agriculture-related columns
agriculture_columns = ["state", "facilities-ag", "workers-ag"]

## Inspection-related columns (Filtering based on column names containing "insp-state", "insp-tribe", "insp-epa")
inspection_columns = [col for col in df_cleaned.columns if "insp-state" in col or "insp-tribe" in col or "insp-epa" in col]

## Keep only selected columns
selected_columns = agriculture_columns + inspection_columns
df_filtered = df_cleaned[selected_columns]

# Step 3: Drop columns with excessive missing values (after filtering)
missing_threshold = 0.8  # Drop columns with more than 80% missing values
df_filtered = df_filtered.dropna(axis=1, thresh=len(df_filtered) * (1 - missing_threshold))

# Step 4: Standardize column names (lowercase and replace spaces with underscores)
df_filtered.columns = df_filtered.columns.str.lower().str.replace(" ", "_")

# Step 5: Convert all numeric columns to appropriate data types
df_filtered.iloc[:, 1:] = df_filtered.iloc[:, 1:].apply(pd.to_numeric, errors="coerce")

# Step 6: Save the cleaned and filtered dataset
df_filtered.to_csv("wps-data-cleaned-filtered.csv", index=False)

# Step 7: Display summary of the cleaned dataset
print("Filtered dataset shape:", df_filtered.shape)
print("First few rows:")
print(df_filtered.head())
df_filtered.to_csv("wps-data-cleaned-filtered.csv", index=False)
print("Filtered dataset saved as 'wps-data-cleaned-filtered.csv'")