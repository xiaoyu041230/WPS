import pandas as pd
import matplotlib.pyplot as plt

# Load the merged dataset
merged_data_df = pd.read_csv("../merge/merged_data_final.csv")

# Filter data for 2017 only
data_2017 = merged_data_df[merged_data_df["year"] == 2017]

# Drop NaN values to ensure proper plotting
data_2017 = data_2017.dropna(subset=["Pesticide_applied_acreage", "inspection_rate"])

# Sort states by Pesticide applied acreage for better visualization
data_2017 = data_2017.sort_values(by="Pesticide_applied_acreage", ascending=False)

# Increase figure width for better readability
fig, ax1 = plt.subplots(figsize=(15, 6))  # Increased width to 15 inches

# Bar chart for Pesticide applied acreage
ax1.bar(data_2017["state"], data_2017["Pesticide_applied_acreage"], alpha=0.7, label="Pesticide Applied Acreage", color="tab:blue")
ax1.set_ylabel("Pesticide Applied Acreage", color="tab:blue")
ax1.set_xlabel("State")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha="right")

# Create a second y-axis for inspection rate
ax2 = ax1.twinx()
ax2.plot(data_2017["state"], data_2017["inspection_rate"], marker="o", linestyle="-", color="tab:red", label="Inspection Rate")
ax2.set_ylabel("Inspection Rate (Inspections per Acreage)", color="tab:red")

# Title and Grid
plt.title("Pesticide Applied Acreage vs. Inspection Rate by State (2017)")
ax1.grid(axis="y", linestyle="--", alpha=0.5)

# Show the plot
plt.show()
