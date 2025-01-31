import pandas as pd

# Load WPS data (Modify this if you're loading from a different location)
wps_data_df = pd.read_csv("wps-data-cleaned-filtered.csv")

# Melt the inspection data into long format
inspection_long_df = wps_data_df.melt(id_vars=["state"], var_name="year", value_name="num_inspections")

# Extract the year from the column names (assuming format "insp-state-YYYY" or similar)
inspection_long_df["year"] = inspection_long_df["year"].str.extract(r'(\d{4})').astype(int)

# ✅ Standardize `state` column to **UPPERCASE**
inspection_long_df["state"] = inspection_long_df["state"].str.upper()

# Add necessary columns to match facilities_df format
inspection_long_df["program"] = "WPS"
inspection_long_df["period"] = "YEAR"
inspection_long_df["geo_level"] = "STATE"
inspection_long_df["state_ansi"] = None  # No ANSI codes in the original WPS data
inspection_long_df["commodity"] = "INSPECTION TOTALS"
inspection_long_df["data_item"] = "STATE INSPECTIONS - TOTAL COUNT"
inspection_long_df["domain"] = "TOTAL"
inspection_long_df["domain_category"] = "NOT SPECIFIED"

# Rearrange columns to match the facilities_df format
inspection_cleaned_df = inspection_long_df[
    ["program", "year", "period", "geo_level", "state", "state_ansi", "commodity", "data_item", "domain", "domain_category", "num_inspections"]
]

# Print the first few rows to verify the output
print(inspection_cleaned_df.head())

# Save the cleaned inspection data as a CSV file
inspection_cleaned_df.to_csv("cleaned_inspection_data.csv", index=False)
print("Cleaned WPS Inspection Data saved as 'cleaned_inspection_data.csv'.")
