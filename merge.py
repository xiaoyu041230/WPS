import pandas as pd

# Load datasets
pesticide_applied_df = pd.read_csv("2017Pesticide.csv")
facilities_df = pd.read_csv("facilitiesTotal_cleaned.csv")
wps_data_df = pd.read_csv("cleaned_inspection_data.csv")  # Already cleaned

# Rename relevant columns for clarity before merging
pesticide_applied_df = pesticide_applied_df.rename(columns={"value": "Pesticide_applied_acreage"})
facilities_df = facilities_df.rename(columns={"value": "num_facilities"})

# Ensure `year` column is integer for proper merging
pesticide_applied_df["year"] = pesticide_applied_df["year"].astype(int)
facilities_df["year"] = facilities_df["year"].astype(int)
wps_data_df["year"] = wps_data_df["year"].astype(int)

# Merge chemical spending with facility data
merged_df = pd.merge(pesticide_applied_df, facilities_df, on=["state", "year"], how="inner")

# Merge with the WPS inspection data (without melting)
final_df = pd.merge(merged_df, wps_data_df, on=["state", "year"], how="left")

# Compute Inspection Rate: num_inspections / num_facilities
final_df["inspection_rate"] = final_df["num_inspections"] / final_df["num_facilities"]

# Print first few rows and save output
print(final_df.head())
final_df.to_csv("merged_data.csv", index=False)
print("Merged data saved as 'merged_data.csv'.")
