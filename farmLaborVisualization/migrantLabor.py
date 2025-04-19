import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files
labor_2012 = pd.read_csv("../FarmLaborData/Labor2012.csv")
labor_2017 = pd.read_csv("../FarmLaborData/Labor2017.csv")
labor_2022 = pd.read_csv("../FarmLaborData/Labor2022.csv")

# Function to clean and prepare migrant worker data
def clean_migrant(df, year):
    df = df.copy()
    df["Total migrant workers"] = pd.to_numeric(df["Total migrant workers"].str.replace(",", ""), errors="coerce")
    df["year"] = year
    return df[["state", "Total migrant workers", "year"]]

# Clean and combine the data for migrant workers
migrant_2012 = clean_migrant(labor_2012, 2012)
migrant_2017 = clean_migrant(labor_2017, 2017)
migrant_2022 = clean_migrant(labor_2022, 2022)

migrant_all = pd.concat([migrant_2012, migrant_2017, migrant_2022])

# Pivot and sort by migrant workers in 2022
migrant_pivot = migrant_all.pivot(index="state", columns="year", values="Total migrant workers")
migrant_sorted = migrant_pivot.sort_values(by=2022, ascending=False)

# Plotting migrant workers by state
plt.figure(figsize=(12, 6))
colors = {2012: 'red', 2017: 'green', 2022: 'blue'}

for year in migrant_sorted.columns:
    plt.plot(migrant_sorted.index, migrant_sorted[year], marker='o', label=str(year), color=colors[year])

plt.title("Migrant Farm Workers by State (2012, 2017, 2022) — Sorted by 2022")
plt.xlabel("State")
plt.ylabel("Number of Migrant Workers")
plt.xticks(rotation=90)
plt.legend(title="Year")
plt.grid(True)
plt.tight_layout()
plt.show()
