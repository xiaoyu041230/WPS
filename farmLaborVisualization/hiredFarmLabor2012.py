import pandas as pd
import matplotlib.pyplot as plt

# === Step 1: Load data ===
df = pd.read_csv("../FarmLaborData/Labor2012.csv")

# === Step 2: Clean numeric columns ===
columns_to_clean = [
    "Hired farm labor",
    "Workers by days worked\n- 150 days or more",
    "Workers by days worked\n- Less than 150 days"
]

for col in columns_to_clean:
    df[col] = df[col].str.replace(",", "").astype(int)

# Rename for easier access
df.rename(columns={
    "Workers by days worked\n- 150 days or more": "150_days_or_more",
    "Workers by days worked\n- Less than 150 days": "less_than_150_days"
}, inplace=True)

# === Step 3: Sort for visualization ===
df_sorted = df.sort_values("Hired farm labor", ascending=False)

# === Step 4: Plot stacked bar chart ===
plt.figure(figsize=(22, 10))
bar_width = 0.8

bars1 = plt.bar(df_sorted["state"], df_sorted["150_days_or_more"], label="≥150 days", color='royalblue', width=bar_width)
bars2 = plt.bar(df_sorted["state"], df_sorted["less_than_150_days"],
                bottom=df_sorted["150_days_or_more"], label="<150 days", color='darkorange', width=bar_width)

# Adjust percentage annotations and add total Hired Farm Labor on top of each bar
for bar1, bar2, row in zip(bars1, bars2, df_sorted.itertuples(index=False)):
    if row._2 == 0:  # Hired farm labor column
        continue
    p1 = row[3] / row[2] * 100  # % of ≥150 days based on Hired farm labor
    p2 = row[4] / row[2] * 100  # % of <150 days based on Hired farm labor

    # Place percentage text slightly above the middle of each bar segment
    plt.text(bar1.get_x() + bar1.get_width()/2, bar1.get_height() * 0.55, f"{p1:.1f}%",
             ha='center', va='center', color='black', fontsize=5, fontweight='bold')

    plt.text(bar2.get_x() + bar2.get_width()/2, bar1.get_height() + (bar2.get_height() * 0.55), f"{p2:.1f}%",
             ha='center', va='center', color='black', fontsize=5, fontweight='bold')

    # Add total Hired Farm Labor on top of each bar
    total_height = bar1.get_height() + bar2.get_height()
    plt.text(bar1.get_x() + bar1.get_width()/2, total_height + 5000, f"{row[2]:,}",
             ha='center', va='bottom', color='black', fontsize=5, fontweight='bold')

# Labels
plt.title("All States by Hired Farm Labor (2012)\nStacked by Days Worked", fontsize=14)
plt.ylabel("Number of Workers", fontsize=12)
plt.xticks(rotation=90, fontsize=10)
plt.xticks(range(len(df_sorted["state"])), df_sorted["state"], ha='right')
plt.legend(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
