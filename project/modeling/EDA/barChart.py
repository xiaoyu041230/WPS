import pandas as pd
import matplotlib.pyplot as plt

# Load your merged dataset
df = pd.read_csv("../merge/merged_analysis_data.csv")  # Update path if needed

# Split by year and sort by state name to align bars
df_2012 = df[df["year"] == 2012].sort_values("state")
df_2017 = df[df["year"] == 2017].sort_values("state")

# Ensure the same state order
states = df_2012["state"].tolist()

# Set bar positions and width
bar_width = 0.4
x = range(len(states))

# Create the plot
plt.figure(figsize=(16, 6))
plt.bar([i - bar_width/2 for i in x], df_2012["Pesticide_applied_acreage"], width=bar_width, label='2012')
plt.bar([i + bar_width/2 for i in x], df_2017["Pesticide_applied_acreage"], width=bar_width, label='2017')

# Labels and formatting
plt.title("Pesticide Applied Acreage by State (2012 vs 2017)")
plt.xlabel("State")
plt.ylabel("Acres Treated")
plt.xticks(ticks=x, labels=states, rotation=90)
plt.legend()
plt.tight_layout()

# Save the figure
plt.savefig("pesticide_by_state_2012_2017.png")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load your merged dataset
df = pd.read_csv("../merge/merged_analysis_data.csv")  # Adjust path if needed

# Filter and sort by state
df_2012 = df[df["year"] == 2012].sort_values("state")
df_2017 = df[df["year"] == 2017].sort_values("state")

# Ensure aligned states
states = df_2012["state"].tolist()

# Set bar positions
bar_width = 0.4
x = range(len(states))

# Plot
plt.figure(figsize=(16, 6))
plt.bar([i - bar_width/2 for i in x], df_2012["hired_farm_labor"], width=bar_width, label='2012')
plt.bar([i + bar_width/2 for i in x], df_2017["hired_farm_labor"], width=bar_width, label='2017')

# Formatting
plt.title("Hired Farm Labor by State (2012 vs 2017)")
plt.xlabel("State")
plt.ylabel("Number of Hired Farm Workers")
plt.xticks(ticks=x, labels=states, rotation=90)
plt.legend()
plt.tight_layout()

# Save the figure
plt.savefig("hired_farm_labor_by_state_2012_2017.png")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../merge/merged_analysis_data.csv")

# Create scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df["Pesticide_applied_acreage"], df["num_violations"], alpha=0.7)
plt.title("Pesticide Applied Acreage vs. WPS Violations")
plt.xlabel("Pesticide Applied Acreage")
plt.ylabel("Number of WPS Violations")
plt.grid(True)
plt.tight_layout()

# Save and/or show plot
plt.savefig("scatter_pesticide_vs_violations.png")
plt.show()
