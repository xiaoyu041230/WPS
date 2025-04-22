import pandas as pd

# Define the 50 valid U.S. states
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

def clean_pesticide_data(file_path: str, output_file: str = "cleaned_pesticide_data.csv") -> pd.DataFrame:
    # Load the dataset
    df = pd.read_csv(file_path)

    # Standardize state names
    df["state"] = df["state"].str.upper().str.strip()

    # Filter to 50 US states and years 2012 and 2017
    df = df[
        (df["state"].isin(US_STATES)) &
        (df["year"].isin([2012, 2017]))
    ].copy()

    # Replace known non-numeric strings with NaN
    non_numeric_values = ["(D)", "NA", "NaN", "N/A", "<NA>"]
    df.replace(non_numeric_values, pd.NA, inplace=True)

    # Clean and convert columns to float
    for col in df.columns[2:]:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(",", "", regex=False)
        )
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Save cleaned file
    df.to_csv(output_file, index=False)
    print(f"Cleaned pesticide data saved as '{output_file}'")
    return df

# Example usage
if __name__ == "__main__":
    clean_pesticide_data("../dataFiles/Pesticide applied acreage.csv")
