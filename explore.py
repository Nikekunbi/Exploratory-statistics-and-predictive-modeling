"""
explore.py
----------
Inspects the ED dataset structure and summarizes
the length of stay distribution.

Usage:
    python scripts/explore.py
"""

import pandas as pd

df = pd.read_csv("data/ed_visits.csv")

print("=== Dataset Structure ===")
print(f"Rows: {df.shape[0]}  |  Columns: {df.shape[1]}\n")
print("Column data types:")
print(df.dtypes.to_string())

print("\n=== First 5 Rows ===")
print(df.head().to_string(index=False))

print("\n=== ED Length of Stay Summary ===")
mean_los   = df["ed_los_hours"].mean()
median_los = df["ed_los_hours"].median()
print(f"Mean LOS:   {mean_los:.2f} hours")
print(f"Median LOS: {median_los:.2f} hours")
print(f"\nThe mean ({mean_los:.2f}) exceeds the median ({median_los:.2f}),")
print("indicating a right-skewed distribution — a small number of patients")
print("with very long stays pull the average upward.")

print("\n=== Admission Rate ===")
print(f"Admitted:     {df['admitted'].sum()} patients ({df['admitted'].mean():.1%})")
print(f"Not admitted: {(df['admitted']==0).sum()} patients ({(df['admitted']==0).mean():.1%})")

print("\n=== Triage Level Distribution ===")
print(df["triage_level"].value_counts().to_string())
