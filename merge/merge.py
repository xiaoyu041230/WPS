import pandas as pd

# Load datasets
pesticide_applied_df = pd.read_csv("../cleanedDataFiles/2017Pesticide.csv")
facilities_df = pd.read_csv("../cleanedDataFiles/facilitiesTotal_cleaned.csv")
wps_data_df = pd.read_csv("../cleanedDataFiles/cleaned_inspection_data.csv")  # Already cleaned

# Select relevant columns for pesticides but keep specific categories
pesticide_applied_df = pesticide_applied_df[['state', 'year', 'Insects', 'Weeds, grass, or brush', 'Nematodes', 'Pesticide_applied_acreage']].copy()

# Convert pesticide usage columns to numeric (removing commas)
for col in ['Insects', 'Weeds, grass, or brush', 'Nematodes', 'Pesticide_applied_acreage']:
    pesticide_applied_df[col] = pesticide_applied_df[col].str.replace(",", "").astype(float)

# Ensure 'year' is integer for proper merging
pesticide_applied_df["year"] = pesticide_applied_df["year"].astype(int)

# Clean Facilities Data
facilities_df = facilities_df[['state', 'year', 'value']].rename(columns={"value": "num_facilities"})
facilities_df["num_facilities"] = facilities_df["num_facilities"].astype(int)

# Clean WPS Inspection Data
wps_data_df = wps_data_df[['state', 'year', 'num_inspections']]

# Ensure 'year' is integer
facilities_df["year"] = facilities_df["year"].astype(int)
wps_data_df["year"] = wps_data_df["year"].astype(int)

# Aggregate duplicate entries in WPS data (sum inspections per state-year)
wps_data_df = wps_data_df.groupby(["state", "year"], as_index=False).agg({"num_inspections": "sum"})

# Merge Pesticide Data with Facility Data (only using Pesticide_applied_acreage for merging)
merged_df = pd.merge(pesticide_applied_df[['state', 'year', 'Pesticide_applied_acreage']], facilities_df, on=["state", "year"], how="inner")

# Merge with WPS Inspection Data
final_df = pd.merge(merged_df, wps_data_df, on=["state", "year"], how="left")

# Compute Inspection Rate: num_inspections / num_facilities
final_df["inspection_rate"] = final_df["num_inspections"] / final_df["num_facilities"]

# Save the final merged dataset
final_df.to_csv("merged_data_final.csv", index=False)

# Save and display the pesticide dataset with selected categories
pesticide_applied_df.to_csv("cleaned_pesticide_data.csv", index=False)

# Print completion message
print("Merged data saved as 'merged_data_final.csv'.")
print("Cleaned pesticide data saved as 'cleaned_pesticide_data.csv'.")