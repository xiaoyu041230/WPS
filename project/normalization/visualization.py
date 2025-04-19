import pandas as pd
import matplotlib.pyplot as plt

# Load normalized data
df = pd.read_csv("normalized_analysis_data.csv")  # Adjust if needed

# Ensure proper sorting
df_2012 = df[df["year"] == 2012].sort_values("state")
df_2017 = df[df["year"] == 2017].sort_values("state")
states = df_2012["state"].tolist()

bar_width = 0.4
x = range(len(states))

# === 1. Side-by-side bar chart: Normalized Hired Farm Labor ===
plt.figure(figsize=(16, 6))
plt.bar([i - bar_width/2 for i in x], df_2012["hired_farm_labor_zscore"], width=bar_width, label='2012')
plt.bar([i + bar_width/2 for i in x], df_2017["hired_farm_labor_zscore"], width=bar_width, label='2017')
plt.title("Normalized Hired Farm Labor by State (2012 vs 2017)")
plt.xlabel("State")
plt.ylabel("Z-score (Hired Labor)")
plt.xticks(ticks=x, labels=states, rotation=90)
plt.legend()
plt.tight_layout()
plt.savefig("bar_labor_zscore_2012_2017.png")
plt.show()

# === 2. Side-by-side bar chart: Normalized Pesticide Acreage ===
plt.figure(figsize=(16, 6))
plt.bar([i - bar_width/2 for i in x], df_2012["Pesticide_applied_acreage_zscore"], width=bar_width, label='2012')
plt.bar([i + bar_width/2 for i in x], df_2017["Pesticide_applied_acreage_zscore"], width=bar_width, label='2017')
plt.title("Normalized Pesticide Applied Acreage by State (2012 vs 2017)")
plt.xlabel("State")
plt.ylabel("Z-score (Pesticide Acreage)")
plt.xticks(ticks=x, labels=states, rotation=90)
plt.legend()
plt.tight_layout()
plt.savefig("bar_pesticide_zscore_2012_2017.png")
plt.show()

# === 3. Scatter Plot: Normalized Violations vs Inspections ===
plt.figure(figsize=(8, 6))
plt.scatter(df["num_inspections_zscore"], df["num_violations_zscore"], alpha=0.7)
plt.title("Normalized WPS Violations vs. Inspections")
plt.xlabel("Inspections (Z-score)")
plt.ylabel("Violations (Z-score)")
plt.grid(True)
plt.tight_layout()
plt.savefig("scatter_violations_vs_inspections_zscore.png")
plt.show()
