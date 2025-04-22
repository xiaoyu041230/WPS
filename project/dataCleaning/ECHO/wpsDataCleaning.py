import pandas as pd

# List of 50 valid U.S. states
US_STATES = [
    'ALABAMA', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA', 'COLORADO', 'CONNECTICUT',
    'DELAWARE', 'FLORIDA', 'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOIS', 'INDIANA', 'IOWA',
    'KANSAS', 'KENTUCKY', 'LOUISIANA', 'MAINE', 'MARYLAND', 'MASSACHUSETTS', 'MICHIGAN',
    'MINNESOTA', 'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA',
    'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK', 'NORTH CAROLINA',
    'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON', 'PENNSYLVANIA', 'RHODE ISLAND',
    'SOUTH CAROLINA', 'SOUTH DAKOTA', 'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT',
    'VIRGINIA', 'WASHINGTON', 'WEST VIRGINIA', 'WISCONSIN', 'WYOMING'
]

def load_and_clean_wps(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)

    # Standardize state names
    df["state"] = df["state"].str.upper().str.strip()
    df = df[df["state"].isin(US_STATES)]

    # Clean column names
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    return df


def extract_inspections(df: pd.DataFrame) -> pd.DataFrame:
    # Correct column matching
    insp_cols = [col for col in df.columns if "insp-state" in col and ("2012" in col or "2017" in col)]

    df_insp = df[["state"] + insp_cols].copy()

    df_insp_long = df_insp.melt(id_vars=["state"], var_name="column", value_name="num_inspections")
    df_insp_long["year"] = df_insp_long["column"].str.extract(r'(\d{4})').astype(int)
    df_insp_long.drop(columns=["column"], inplace=True)

    return df_insp_long

def extract_violations(df: pd.DataFrame) -> pd.DataFrame:
    # Only sum columns that start with 'viol_' and are year-specific
    viol_cols_2012 = [col for col in df.columns if col.startswith("viol_") and "2012" in col]
    viol_cols_2017 = [col for col in df.columns if col.startswith("viol_") and "2017" in col]

    df_viol = df[["state"] + viol_cols_2012 + viol_cols_2017].copy()

    # Sum all violation types for each year
    df_viol["violations_2012"] = df_viol[viol_cols_2012].sum(axis=1, skipna=True)
    df_viol["violations_2017"] = df_viol[viol_cols_2017].sum(axis=1, skipna=True)

    # Reshape into long format
    df_2012 = df_viol[["state", "violations_2012"]].copy()
    df_2012["year"] = 2012
    df_2012.rename(columns={"violations_2012": "num_violations"}, inplace=True)

    df_2017 = df_viol[["state", "violations_2017"]].copy()
    df_2017["year"] = 2017
    df_2017.rename(columns={"violations_2017": "num_violations"}, inplace=True)

    return pd.concat([df_2012, df_2017], ignore_index=True)

def main():
    input_file = "../dataFiles/wps-data.csv"  # Update this path if needed

    df = load_and_clean_wps(input_file)
    inspections = extract_inspections(df)
    violations = extract_violations(df)

    # Double-check formatting
    inspections["state"] = inspections["state"].str.upper().str.strip()
    violations["state"] = violations["state"].str.upper().str.strip()
    inspections["year"] = inspections["year"].astype(int)
    violations["year"] = violations["year"].astype(int)

    # Diagnostic outer merge
    merged_debug = pd.merge(inspections, violations, on=["state", "year"], how="outer", indicator=True)
    print("\n--- Merge Status Breakdown ---")
    print(merged_debug["_merge"].value_counts())

    # Now drop missing and use inner merge for clean version
    merged_clean = merged_debug[merged_debug["_merge"] == "both"].drop(columns=["_merge"])

    # Save to CSV
    merged_clean.to_csv("cleaned_inspection_and_violation_data.csv", index=False)
    print("✅ Final saved file: 'cleaned_inspection_and_violation_data.csv'")
    print(merged_clean.head())

if __name__ == "__main__":
    main()
