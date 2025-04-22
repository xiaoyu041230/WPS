import pandas as pd

# 50 valid U.S. states
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

def clean_labor_file(file_path: str, year: int) -> pd.DataFrame:
    """Clean a labor CSV for a specific year."""
    df = pd.read_csv(file_path)

    # Standardize column names and state formatting
    df.columns = df.columns.str.lower().str.strip()
    df["state"] = df["state"].str.upper().str.strip()

    # Filter to 50 U.S. states
    df = df[df["state"].isin(US_STATES)]

    # Extract and rename the target column
    hired_col = [col for col in df.columns if "hired" in col and "labor" in col][0]
    df = df[["state", hired_col]].copy()
    df.rename(columns={hired_col: "hired_farm_labor"}, inplace=True)

    # Clean numeric values
    df["hired_farm_labor"] = (
        df["hired_farm_labor"]
        .astype(str)
        .str.replace(",", "", regex=False)
    )
    df["hired_farm_labor"] = pd.to_numeric(df["hired_farm_labor"], errors="coerce")

    # Add year column
    df["year"] = year

    return df

def main():
    # Paths to raw labor files
    file_2012 = "../dataFiles/Labor2012.csv"
    file_2017 = "../dataFiles/Labor2017.csv"

    # Clean both years
    labor_2012 = clean_labor_file(file_2012, 2012)
    labor_2017 = clean_labor_file(file_2017, 2017)

    # Combine
    combined = pd.concat([labor_2012, labor_2017], ignore_index=True)
    combined.to_csv("cleaned_labor_data.csv", index=False)
    print("✅ Cleaned labor data saved as 'cleaned_labor_data.csv'")
    print(combined.head())

if __name__ == "__main__":
    main()
