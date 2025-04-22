import pandas as pd
from sqlalchemy import create_engine

# MySQL connection settings
username = "root"             # Placeholder MySQL username
password = "mypassword"     # Placeholder MySQL password
host = "localhost"            # Host where MySQL is running
port = 3306                   # Default MySQL port
database = "wps_db"           # Name of the database you want to use or create

# Create SQLAlchemy connection string
engine = create_engine("mysql+pymysql://root:@localhost:3306/wps_db")

# Load your cleaned datasets
df_inspections = pd.read_csv("../dataCleaning/ECHO/cleaned_inspection_and_violation_data.csv")  # ECHO enforcement data
df_pesticide = pd.read_csv("../dataCleaning/EPAPesticide/cleaned_pesticide_data.csv")           # Pesticide application data
df_labor = pd.read_csv("../dataCleaning/USDALabor/cleaned_labor_data.csv")                      # Farm labor statistics

# Replicate your merge logic
df_merged = pd.merge(df_inspections, 
                     df_pesticide[["state", "year", "Pesticide_applied_acreage"]], 
                     on=["state", "year"], how="inner")

df_merged = pd.merge(df_merged, df_labor, on=["state", "year"], how="inner")

# Upload each table to MySQL
df_inspections.to_sql("inspections", con=engine, if_exists="replace", index=False)
df_pesticide.to_sql("pesticide_applied", con=engine, if_exists="replace", index=False)
df_labor.to_sql("farm_labor", con=engine, if_exists="replace", index=False)
df_merged.to_sql("merged_analysis_data", con=engine, if_exists="replace", index=False)

print("All tables uploaded to MySQL (including merged_analysis_data).")
