# Methodology

## Background

Emergency departments face three recurring operational challenges: prolonged patient stays, variable outcomes by clinical severity, and difficulty identifying admission-likely patients early enough to act. This project builds an analytics pipeline that addresses all three using a single, structured ED visit dataset.

---

## Dataset

400 synthetic ED patient visits, each representing one encounter. Variables include patient demographics (age), clinical urgency (triage level), operational metrics (LOS, tests ordered), and the binary outcome of interest (admitted vs discharged).

---

## Analytical Approach

### 1. Dataset Inspection

Before any analysis, I inspected the data structure to understand variable types — distinguishing numeric columns (age, LOS, tests) from categorical ones (triage level, insurance type). This determines which statistical methods are appropriate at each step.

### 2. Length of Stay Summary

Computed mean and median LOS to characterize the central tendency of patient flow.

- **Mean: 5.54 hours** — pulled upward by high-acuity, long-stay patients
- **Median: 4.49 hours** — more representative of the typical visit

The gap between mean and median confirms right skew, which is expected in ED data where a minority of complex cases account for disproportionate capacity.

### 3. LOS by Admission Status (Visualization)

A side-by-side boxplot comparing admitted vs discharged patients' LOS distributions. Admitted patients show both a higher median and a wider spread — consistent with longer, more complex care pathways leading to inpatient admission.

### 4. Hypothesis Testing — t-test

**Question:** Is the difference in mean LOS between admitted and discharged patients statistically significant?

**Method:** Independent samples t-test (two-group comparison of a continuous variable)

| Result | Value |
|---|---|
| T-statistic | 8.87 |
| P-value | < 0.0001 |

**Conclusion:** The difference is highly significant. Admitted patients spend substantially more time in the ED before disposition — this is an actionable finding for bed management and flow planning.

### 5. ANOVA — LOS across Triage Levels

**Question:** Does mean LOS differ across Low, Medium, and High triage categories?

**Method:** One-way ANOVA (comparing means across 3+ groups)

| Result | Value |
|---|---|
| F-statistic | 56.95 |
| P-value | < 0.0001 |

**Conclusion:** Triage level is strongly associated with LOS. Higher-severity patients stay longer — this justifies using triage level for resource pre-allocation at the start of a visit.

### 6. Logistic Regression — Admission Risk Model

**Predictors:** age, ed_los_hours, num_tests_ordered  
**Outcome:** admitted (binary)

Logistic regression was chosen as the interpretable baseline model. Coefficients indicate the direction and magnitude of each predictor's effect on admission probability.

- **Training accuracy: 70.5%**
- **ROC-AUC: 0.776** — good discriminatory ability (> 0.75 threshold)

An AUC of 0.776 means the model correctly ranks a randomly selected admitted patient above a discharged one 77.6% of the time.

### 7. Decision Tree

An unpruned decision tree was trained on the same predictors.

- **Training accuracy: 100%**

Perfect training accuracy is a red flag for overfitting. The tree has memorized the training data, including noise. Evaluated on held-out data, performance would drop substantially. A max_depth constraint or cross-validation would produce a fairer estimate.

### 8. Random Forest

A 100-tree ensemble was trained on the same predictors.

- **Training accuracy: 100%**

Same overfitting caveat as the decision tree. However, the feature importance scores from the random forest confirm that **ed_los_hours** and **num_tests_ordered** are the dominant predictors — consistent with clinical intuition.

---

## Key Findings

| Finding | Value |
|---|---|
| Mean ED LOS | 5.54 hours |
| Median ED LOS | 4.49 hours |
| LOS difference (admitted vs discharged) | Significant (p < 0.0001) |
| LOS difference across triage levels | Significant (p < 0.0001) |
| Logistic regression accuracy | 70.5% |
| ROC-AUC | 0.776 |

## Operational Conclusion

Patients with longer ED stays and more diagnostic tests are significantly more likely to be admitted. These signals are available early in the visit — before a physician formally decides on admission. Implementing a real-time scoring tool using these variables could enable earlier bed requests, better flow coordination, and reduced overall LOS for the patient population.
