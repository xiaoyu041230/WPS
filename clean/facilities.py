import pandas as pd

# Load dataset
file_path = "../originalDataFiles/cropFacilities.csv"
df_facilities = pd.read_csv(file_path)

# Step 1: Drop unnecessary columns
columns_to_drop = [
    "Week Ending", "Ag District", "Ag District Code", "County", "County ANSI",
    "Zip Code", "Region", "Watershed", "CV (%)", "watershed_code"
]
df_facilities_cleaned = df_facilities.drop(columns=columns_to_drop, errors="ignore")

# Step 2: Standardize column names
df_facilities_cleaned.columns = df_facilities_cleaned.columns.str.strip().str.lower().str.replace(" ", "_")

# Step 3: Filter data to keep only relevant records
df_facilities_cleaned = df_facilities_cleaned[df_facilities_cleaned["data_item"] == "CROP TOTALS - OPERATIONS WITH SALES"]

# Step 3: Clean "Value" column
df_facilities_cleaned["value"] = pd.to_numeric(
    df_facilities_cleaned["value"]
    .replace({r"\((D|Z|L|H)\)": None}, regex=True)  # Replace (D), (Z), (L), (H) with NaN
    .str.replace(",", ""),  # Remove commas
    errors="coerce"
)

# Step 4: Drop NaN values in "value"
df_facilities_cleaned = df_facilities_cleaned.dropna(subset=["value"])

# Step 5: Remove duplicate rows
df_facilities_cleaned = df_facilities_cleaned.drop_duplicates()

# Step 6: Standardize "State" names
df_facilities_cleaned["state"] = df_facilities_cleaned["state"].str.strip().str.upper()

# Step 8: Filter domain to avoid duplicate counting (Only keep "TOTAL")
df_facilities_cleaned = df_facilities_cleaned[df_facilities_cleaned["domain"] == "TOTAL"]

# Step 17: Save cleaned data
df_facilities_cleaned.to_csv("facilitiesTotal_cleaned.csv", index=False)

# Display summary
print(df_facilities_cleaned.info())
print(df_facilities_cleaned.head())
