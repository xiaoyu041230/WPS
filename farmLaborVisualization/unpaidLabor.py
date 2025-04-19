import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files
labor_2012 = pd.read_csv("../FarmLaborData/Labor2012.csv")
labor_2017 = pd.read_csv("../FarmLaborData/Labor2017.csv")
labor_2022 = pd.read_csv("../FarmLaborData/Labor2022.csv")

# Function to clean and prepare unpaid worker data
def clean_unpaid(df, year):
    df = df.copy()
    df["Unpaid workers"] = pd.to_numeric(df["Unpaid workers"].str.replace(",", ""), errors="coerce")
    df["year"] = year
    return df[["state", "Unpaid workers", "year"]]

# Clean and combine the data
unpaid_2012 = clean_unpaid(labor_2012, 2012)
unpaid_2017 = clean_unpaid(labor_2017, 2017)
unpaid_2022 = clean_unpaid(labor_2022, 2022)

unpaid_all = pd.concat([unpaid_2012, unpaid_2017, unpaid_2022])

# Pivot and sort by unpaid workers in 2022
unpaid_pivot = unpaid_all.pivot(index="state", columns="year", values="Unpaid workers")
unpaid_sorted = unpaid_pivot.sort_values(by=2022, ascending=False)

# Plotting with identifiable colors
plt.figure(figsize=(12, 6))
colors = {2012: 'red', 2017: 'green', 2022: 'blue'}

for year in unpaid_sorted.columns:
    plt.plot(unpaid_sorted.index, unpaid_sorted[year], marker='o', label=str(year), color=colors[year])

plt.title("Unpaid Farm Workers by State (2012, 2017, 2022) — Sorted by 2022")
plt.xlabel("State")
plt.ylabel("Number of Unpaid Workers")
plt.xticks(rotation=90)
plt.legend(title="Year")
plt.grid(True)
plt.tight_layout()
plt.show()
