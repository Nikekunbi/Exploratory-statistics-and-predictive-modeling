"""
visualize.py
------------
Generates plots comparing ED length of stay across patient groups.

Plots:
  - Boxplot: LOS by admission status
  - Boxplot: LOS by triage level

Usage:
    python scripts/visualize.py
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/ed_visits.csv")
df["Admission Status"] = df["admitted"].map({1: "Admitted", 0: "Discharged"})

sns.set_style("whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# ── Plot 1: LOS by admission status ─────────────────────────────
sns.boxplot(
    data=df, x="Admission Status", y="ed_los_hours",
    palette={"Admitted": "#E05C5C", "Discharged": "#5C9BE0"},
    ax=axes[0]
)
axes[0].set_title("ED Length of Stay by Admission Status", fontsize=13, fontweight="bold")
axes[0].set_xlabel("Admission Status")
axes[0].set_ylabel("LOS (hours)")

for status, color in zip(["Admitted", "Discharged"], ["#E05C5C", "#5C9BE0"]):
    med = df[df["Admission Status"] == status]["ed_los_hours"].median()
    axes[0].annotate(f"Median: {med:.1f}h",
                     xy=(0.5, 0.95), xycoords="axes fraction",
                     ha="center", fontsize=9, color="gray")
    break

# ── Plot 2: LOS by triage level ─────────────────────────────────
order = ["Low", "Medium", "High"]
palette = {"Low": "#5CB85C", "Medium": "#F0AD4E", "High": "#D9534F"}

sns.boxplot(
    data=df, x="triage_level", y="ed_los_hours",
    order=order, palette=palette, ax=axes[1]
)
axes[1].set_title("ED Length of Stay by Triage Level", fontsize=13, fontweight="bold")
axes[1].set_xlabel("Triage Level")
axes[1].set_ylabel("LOS (hours)")

plt.suptitle("Emergency Department — Length of Stay Analysis", fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig("outputs/los_comparison.png", dpi=150, bbox_inches="tight")
plt.show()
print("Plot saved to outputs/los_comparison.png")
