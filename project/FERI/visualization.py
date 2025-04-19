import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import us

# === Step 1: Load your FERI dataset ===
feri_df = pd.read_csv("feri_index_results.csv")
feri_df["state"] = feri_df["state"].str.upper()  # Ensure uppercase matching

# === Step 2: Load US states shapefile ===
states_gdf = gpd.read_file("us-states1.json")  # Replace with your actual GeoJSON or Shapefile path
states_gdf["name"] = states_gdf["name"].str.upper()

# === Step 3: Generate FERI maps for each year ===
for year in [2012, 2017]:
    # Filter FERI data for that year
    feri_year = feri_df[feri_df["year"] == year]

    # Merge shapefile with FERI data
    merged = states_gdf.merge(feri_year, left_on="name", right_on="state", how="left")

    # Add state abbreviations (e.g., "CA", "NY")
    merged["state_abbr"] = merged["state"].apply(
        lambda x: us.states.lookup(str(x)).abbr if pd.notnull(x) and us.states.lookup(str(x)) else ""
    )

    # === Plot map ===
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    merged.plot(column="FERI", cmap="OrRd", linewidth=0.8, ax=ax, edgecolor="0.8", legend=True)

    ax.set_title(f"FERI Index by State ({year})", fontsize=14)
    ax.axis("off")
    ax.set_xlim(-130, -65)   # Zoom into continental U.S.
    ax.set_ylim(23, 50)

    # Add state abbreviation labels
    for idx, row in merged.iterrows():
        if row["geometry"].centroid.is_empty or pd.isna(row["FERI"]):
            continue
        x, y = row["geometry"].centroid.x, row["geometry"].centroid.y
        ax.text(x, y, row["state_abbr"], fontsize=8, ha='center', va='center', color='black')

    # Save and show the map
    plt.savefig(f"feri_heatmap_{year}_abbr_labeled.png", dpi=300)
    plt.show()
