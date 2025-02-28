import pandas as pd

# Define file paths
pesticide_applied_path = "../cleanedDataFiles/2017Pesticide.csv"
facilities_path = "../cleanedDataFiles/facilitiesTotal_cleaned.csv"
wps_data_path = "../cleanedDataFiles/cleaned_inspection_data.csv"

# Load the datasets
pesticide_applied_df = pd.read_csv(pesticide_applied_path)
facilities_df = pd.read_csv(facilities_path)
wps_data_df = pd.read_csv(wps_data_path)

# Select relevant columns for pesticides but keep specific categories
pesticide_applied_df = pesticide_applied_df[['state', 'year', 'Insects', 'Weeds, grass, or brush', 'Nematodes', 'Pesticide_applied_acreage']].copy()

# Convert pesticide usage columns to numeric (removing commas, handling errors)
for col in ['Insects', 'Weeds, grass, or brush', 'Nematodes', 'Pesticide_applied_acreage']:
    pesticide_applied_df[col] = pd.to_numeric(pesticide_applied_df[col].astype(str).str.replace(",", ""), errors='coerce')

# Ensure 'year' is integer for proper merging
pesticide_applied_df["year"] = pesticide_applied_df["year"].astype(int)

# Clean Facilities Data (rename value column to Facility_Total)
facilities_df = facilities_df[['state', 'year', 'value']].rename(columns={"value": "Facility_Total"})
facilities_df["Facility_Total"] = pd.to_numeric(facilities_df["Facility_Total"], errors='coerce')
facilities_df["year"] = facilities_df["year"].astype(int)

# Clean WPS Inspection Data
wps_data_df = wps_data_df[['state', 'year', 'num_inspections']]
wps_data_df["year"] = wps_data_df["year"].astype(int)

# Aggregate duplicate entries in WPS data (sum inspections per state-year)
wps_data_df = wps_data_df.groupby(["state", "year"], as_index=False).agg({"num_inspections": "sum"})

# Merge Pesticide Data with WPS Inspection Data
merged_df = pd.merge(pesticide_applied_df, wps_data_df, on=["state", "year"], how="outer")

# Merge the facilities data
merged_df = pd.merge(merged_df, facilities_df, on=["state", "year"], how="left")

# Keep only 2012 and 2017 data
merged_df = merged_df[merged_df['year'].isin([2012, 2017])]

# Compute Inspection Rate: num_inspections / Facility_Total
merged_df["inspection_rate"] = merged_df["num_inspections"] / merged_df["Facility_Total"]

# List of entities to remove
entities_to_remove = [
    "AK-CHIN INDIAN COMMUNITY", "ARIZONA", "CHEYENNE RIVER SIOUX TRIBE", "COCOPAH INDIAN TRIBE",
    "COEUR D'ALENE TRIBE", "COLORADO RIVER INDIAN COMMUNITY", "CONFEDERATED SALISH AND KOOTENAI TRIBES",
    "DISTRICT OF COLUMBIA", "FORT PECK ASSINIBOINE AND SIOUX TRIBE", "GILA RIVER INDIAN COMMUNITY",
    "INTER TRIBAL COUNCIL OF ARIZONA", "MASSACHUSETTS", "NAVAJO NATION", "NORTHERN MARIANA ISLANDS",
    "NOT A CURRENT GRANTEE", "OGLALA LAKOTA NATION", "OREGON", "QUECHAN TRIBE",
    "SALT RIVER PIMA MARICOPA INDIAN COMMUNITY", "SHOSHONE PAIUTE OF THE DUCK VALLEY",
    "STANDING ROCK SIOUX TRIBE", "THREE AFFILIATED TRIBES", "WHITE EARTH NATION", "YAKAMA NATION"
]

# Remove specified entities (case-insensitive, stripping whitespace)
merged_df = merged_df[~merged_df['state'].str.strip().str.upper().isin([e.upper() for e in entities_to_remove])]

# Save the final merged dataset
merged_data_path = "../merge/merged_data_final.csv"
merged_df.to_csv(merged_data_path, index=False)

# Save and display the pesticide dataset with selected categories
cleaned_pesticide_path = "../merge/cleaned_pesticide_data.csv"
pesticide_applied_df.to_csv(cleaned_pesticide_path, index=False)

# Print completion message
print(f"Merged data saved as '{merged_data_path}'.")
print(f"Cleaned pesticide data saved as '{cleaned_pesticide_path}'.")
