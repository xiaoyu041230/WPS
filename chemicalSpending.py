import pandas as pd
import numpy as np

# Load dataset
file_path = "chemicalTotal.csv"
df_chemical = pd.read_csv(file_path)

# Step 1: Drop unnecessary columns
columns_to_drop = [
    "Week Ending", "Ag District", "Ag District Code", "County", "County ANSI",
    "Zip Code", "Region", "Watershed", "CV (%)", "watershed_code"
]
df_chemical_cleaned = df_chemical.drop(columns=columns_to_drop, errors="ignore")

# Step 2: Standardize column names
df_chemical_cleaned.columns = df_chemical_cleaned.columns.str.strip().str.lower().str.replace(" ", "_")

# Step 3: Filter data to keep only relevant records
df_chemical_cleaned = df_chemical_cleaned[df_chemical_cleaned["data_item"] == "CHEMICAL TOTALS - EXPENSE, MEASURED IN $"]

# Step 3: Clean "Value" column
df_chemical_cleaned["value"] = pd.to_numeric(
    df_chemical_cleaned["value"]
    .replace({r"\((D|Z|L|H)\)": None}, regex=True)  # Replace (D), (Z), (L), (H) with NaN
    .str.replace(",", ""),  # Remove commas
    errors="coerce"
)

# Step 4: Drop NaN values in "value"
df_chemical_cleaned = df_chemical_cleaned.dropna(subset=["value"])

# Step 5: Remove duplicate rows
df_chemical_cleaned = df_chemical_cleaned.drop_duplicates()

# Step 6: Standardize "State" names
df_chemical_cleaned["state"] = df_chemical_cleaned["state"].str.strip().str.upper()

# Step 8: Filter domain to avoid duplicate counting (Only keep "TOTAL")
df_chemical_cleaned = df_chemical_cleaned[df_chemical_cleaned["domain"] == "TOTAL"]

# Step 17: Save cleaned data
df_chemical_cleaned.to_csv("chemicalTotal_cleaned.csv", index=False)

# Display summary
print(df_chemical_cleaned.info())
print(df_chemical_cleaned.head())
