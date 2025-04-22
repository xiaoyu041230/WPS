import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load clustered FERI dataset
df = pd.read_csv("feri_clustered_results.csv")

# Create a 'state_year' label for visualization
df["state_year"] = df["state"] + " (" + df["year"].astype(str) + ")"

# Split into 2012 and 2017 datasets
heatmap_2012 = df[df["year"] == 2012].copy()
heatmap_2017 = df[df["year"] == 2017].copy()

# Step 1: Sort states within each cluster by violations_per_inspection (descending)
# Cluster order: Cluster 2 (Low Risk) → Cluster 1 (Medium) → Cluster 0 (High Risk)
ordered_2012 = pd.concat([
    heatmap_2012[heatmap_2012["cluster"] == c].sort_values(by="violations_per_inspection", ascending=False)
    for c in [2, 1, 0]
])
ordered_2017 = pd.concat([
    heatmap_2017[heatmap_2017["cluster"] == c].sort_values(by="violations_per_inspection", ascending=False)
    for c in [2, 1, 0]
])

# Step 2: Create pivot tables (rows = state-year, columns = cluster, values = violations per inspection)
pivot_2012 = ordered_2012.pivot_table(
    index="state_year", columns="cluster", values="violations_per_inspection", fill_value=0
)
pivot_2012 = pivot_2012.reindex(index=ordered_2012["state_year"])
pivot_2012 = pivot_2012.reindex(columns=[0, 1, 2], fill_value=0)  # Ensure all clusters appear

pivot_2017 = ordered_2017.pivot_table(
    index="state_year", columns="cluster", values="violations_per_inspection", fill_value=0
)
pivot_2017 = pivot_2017.reindex(index=ordered_2017["state_year"])
pivot_2017 = pivot_2017.reindex(columns=[0, 1, 2], fill_value=0)

# Step 3: Plot heatmap for 2012
plt.figure(figsize=(10, 12))
sns.heatmap(pivot_2012, cmap="PuBuGn", linewidths=0.3, linecolor='gray')
plt.title("Cluster-Based Risk Grouping (2012): Violations per Inspection", fontsize=14, weight='bold')
plt.xlabel("Cluster")
plt.ylabel("State (2012)")
plt.tight_layout()
plt.savefig("viol_per_insp_heatmap_2012_cluster_emphasis.png")
plt.show()

# Step 4: Plot heatmap for 2017
plt.figure(figsize=(10, 12))
sns.heatmap(pivot_2017, cmap="PuBuGn", linewidths=0.3, linecolor='gray')
plt.title("Cluster-Based Risk Grouping (2017): Violations per Inspection", fontsize=14, weight='bold')
plt.xlabel("Cluster")
plt.ylabel("State (2017)")
plt.tight_layout()
plt.savefig("viol_per_insp_heatmap_2017_cluster_emphasis.png")
plt.show()
