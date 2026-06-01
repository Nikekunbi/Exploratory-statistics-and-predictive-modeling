"""
statistics.py
-------------
Runs hypothesis tests to evaluate whether length of stay
differs significantly across patient groups.

Tests:
  - Independent samples t-test: admitted vs non-admitted
  - One-way ANOVA: across triage severity levels (Low/Medium/High)

Usage:
    python scripts/statistics.py
"""

import pandas as pd
from scipy import stats

df = pd.read_csv("data/ed_visits.csv")

# ── T-test: admitted vs non-admitted ────────────────────────────
print("=== Hypothesis Test: LOS — Admitted vs Not Admitted ===\n")

admitted     = df[df["admitted"] == 1]["ed_los_hours"]
not_admitted = df[df["admitted"] == 0]["ed_los_hours"]

print(f"  Admitted      — mean: {admitted.mean():.2f} hrs  n={len(admitted)}")
print(f"  Not admitted  — mean: {not_admitted.mean():.2f} hrs  n={len(not_admitted)}")

t_stat, p_val = stats.ttest_ind(admitted, not_admitted)
print(f"\n  T-statistic: {t_stat:.4f}")
print(f"  P-value:     {p_val:.6f}")

if p_val < 0.05:
    print("\n  → Statistically significant difference (p < 0.05).")
    print("    Admitted patients stay considerably longer in the ED.")
else:
    print("\n  → No statistically significant difference detected.")

# ── ANOVA: across triage levels ─────────────────────────────────
print("\n=== One-Way ANOVA: LOS across Triage Levels ===\n")

for level in ["Low", "Medium", "High"]:
    grp = df[df["triage_level"] == level]["ed_los_hours"]
    print(f"  {level:<8} — mean: {grp.mean():.2f} hrs  n={len(grp)}")

groups = [g["ed_los_hours"].values for _, g in df.groupby("triage_level")]
f_stat, p_anova = stats.f_oneway(*groups)

print(f"\n  F-statistic: {f_stat:.4f}")
print(f"  P-value:     {p_anova:.6f}")

if p_anova < 0.05:
    print("\n  → Significant differences in LOS exist across triage levels (p < 0.05).")
    print("    Higher acuity patients have longer ED stays on average.")
else:
    print("\n  → No significant difference across triage levels.")
