import pandas as pd

def merge_cleaned_datasets():
    # Load updated inspection + violation data
    inspections = pd.read_csv("../dataCleaning/ECHO/cleaned_inspection_and_violation_data.csv")
    pesticides = pd.read_csv("../dataCleaning/EPAPesticide/cleaned_pesticide_data.csv")
    labor = pd.read_csv("../dataCleaning/USDALabor/cleaned_labor_data.csv")

    # Merge inspections + pesticides
    merged = pd.merge(inspections, pesticides[["state", "year", "Pesticide_applied_acreage"]],
                      on=["state", "year"], how="inner")

    # Merge in labor data
    merged = pd.merge(merged, labor, on=["state", "year"], how="inner")

    # Save to CSV
    merged.to_csv("merged_analysis_data.csv", index=False)
    print("Merged dataset saved as 'merged_analysis_data.csv'")
    print(merged.head())

if __name__ == "__main__":
    merge_cleaned_datasets()
