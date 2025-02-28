import pandas as pd
import matplotlib.pyplot as plt

# Load the merged dataset
merged_data_df = pd.read_csv("../merge/merged_data_final.csv")

# Filter data for 2017 only
data_2017 = merged_data_df[merged_data_df["year"] == 2017]

# Drop NaN values to ensure proper plotting
data_2017 = data_2017.dropna(subset=["Pesticide_applied_acreage", "inspection_rate"])

# Sort states by chemical spending for better visualization
data_2017 = data_2017.sort_values(by="Pesticide_applied_acreage", ascending=False)

# Increase figure width for better readability
fig, ax1 = plt.subplots(figsize=(15, 6))  # Increased width to 15 inches

# Bar chart for chemical spending
ax1.bar(data_2017["state"], data_2017["Pesticide_applied_acreage"], alpha=0.7, label="Pesticide applied acreage", color="tab:blue")
ax1.set_ylabel("Pesticide applied acreage", color="tab:blue")
ax1.set_xlabel("State")
ax1.set_xticks(range(len(data_2017["state"])))  # Set proper x-ticks
ax1.set_xticklabels(data_2017["state"], rotation=45, ha="right")  # Rotate for readability

# Create a second y-axis for inspection rate
ax2 = ax1.twinx()
ax2.plot(data_2017["state"], data_2017["inspection_rate"], marker="o", linestyle="-", color="tab:red", label="Inspection Rate")
ax2.set_ylabel("Inspection Rate (Inspections per Facility)", color="tab:red")

# Title and Grid
plt.title("Pesticide applied acreage vs. Inspection Rate by State (2017)")
ax1.grid(axis="y", linestyle="--", alpha=0.5)

# Show the plot
plt.show()
