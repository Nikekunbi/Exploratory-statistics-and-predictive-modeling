"""
models.py
---------
Builds and evaluates three classification models to predict
hospital admission from ED visit data.

Models:
  - Logistic Regression  (interpretable baseline)
  - Decision Tree        (rule-based, non-linear)
  - Random Forest        (ensemble, more robust)

Predictors: age, ed_los_hours, num_tests_ordered
Outcome:    admitted (0 = discharged, 1 = admitted)

Usage:
    python scripts/models.py
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("data/ed_visits.csv")

X = df[["age", "ed_los_hours", "num_tests_ordered"]]
y = df["admitted"]

# ── Logistic Regression ──────────────────────────────────────────
print("=== Logistic Regression ===")
logistic_model = LogisticRegression(max_iter=1000, random_state=42)
logistic_model.fit(X, y)
lr_acc = logistic_model.score(X, y)
print(f"  Accuracy: {lr_acc:.4f}")

coefs = dict(zip(X.columns, logistic_model.coef_[0]))
print("  Coefficients:")
for feat, coef in coefs.items():
    print(f"    {feat:<22} {coef:+.4f}")

# ── ROC-AUC ─────────────────────────────────────────────────────
print("\n=== ROC-AUC (Logistic Regression) ===")
probs = logistic_model.predict_proba(X)[:, 1]
auc   = roc_auc_score(y, probs)
print(f"  AUC: {auc:.4f}")
print("  Interpretation: model has good discriminatory ability" if auc > 0.75
      else "  Interpretation: model has moderate discriminatory ability")

# ── Decision Tree ────────────────────────────────────────────────
print("\n=== Decision Tree ===")
decision_tree_model = DecisionTreeClassifier(random_state=42)
decision_tree_model.fit(X, y)
dt_acc = decision_tree_model.score(X, y)
print(f"  Accuracy: {dt_acc:.4f}")
if dt_acc == 1.0:
    print("  ⚠ Perfect accuracy on training data suggests overfitting.")
    print("    Use train/test split to get a fair generalization estimate.")

# ── Random Forest ────────────────────────────────────────────────
print("\n=== Random Forest ===")
random_forest_model = RandomForestClassifier(n_estimators=100, random_state=42)
random_forest_model.fit(X, y)
rf_acc = random_forest_model.score(X, y)
print(f"  Accuracy: {rf_acc:.4f}")

importances = dict(zip(X.columns, random_forest_model.feature_importances_))
print("  Feature importances:")
for feat, imp in sorted(importances.items(), key=lambda x: -x[1]):
    print(f"    {feat:<22} {imp:.4f}")

if rf_acc == 1.0:
    print("  ⚠ Perfect training accuracy — evaluate on held-out test data.")

# ── Comparison Summary ───────────────────────────────────────────
print("\n=== Model Comparison ===")
print(f"  {'Model':<25} {'Train Accuracy':>15}")
print(f"  {'-'*42}")
print(f"  {'Logistic Regression':<25} {lr_acc:>14.4f}")
print(f"  {'Decision Tree':<25} {dt_acc:>14.4f}")
print(f"  {'Random Forest':<25} {rf_acc:>14.4f}")
print(f"\n  ROC-AUC (Logistic Regression): {auc:.4f}")
print("\n  The logistic model provides the most honest baseline — tree models")
print("  need a proper train/test split to assess real generalization.")
