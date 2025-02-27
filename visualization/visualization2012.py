import pandas as pd
import matplotlib.pyplot as plt

# Load the merged dataset
merged_data_df = pd.read_csv("../merge/merged_data.csv")

# Filter data for 2012 only
data_2012 = merged_data_df[merged_data_df["year"] == 2012]

# Drop NaN values to ensure proper plotting
data_2012 = data_2012.dropna(subset=["chemical_spending", "inspection_rate"])

# Sort states by chemical spending for better visualization
data_2012 = data_2012.sort_values(by="chemical_spending", ascending=False)

# Increase figure width for better readability
fig, ax1 = plt.subplots(figsize=(15, 6))  # Increased width to 15 inches

# Bar chart for chemical spending
ax1.bar(data_2012["state"], data_2012["chemical_spending"], alpha=0.7, label="Chemical Spending ($)", color="tab:blue")
ax1.set_ylabel("Chemical Spending ($)", color="tab:blue")
ax1.set_xlabel("State")
ax1.set_xticks(range(len(data_2012["state"])))  # Set x-ticks properly
ax1.set_xticklabels(data_2012["state"], rotation=45, ha="right")  # Rotate for readability

# Create a second y-axis for inspection rate
ax2 = ax1.twinx()
ax2.plot(data_2012["state"], data_2012["inspection_rate"], marker="o", linestyle="-", color="tab:red", label="Inspection Rate")
ax2.set_ylabel("Inspection Rate (Inspections per Facility)", color="tab:red")

# Title and Grid
plt.title("Chemical Spending vs. Inspection Rate by State (2012)")
ax1.grid(axis="y", linestyle="--", alpha=0.5)

# Show the plot
plt.show()
