# 🏥 Emergency Department Analytics: From Statistics to Predictive Models

An end-to-end data analytics project analyzing emergency department visit data to understand patient flow, length of stay patterns, and admission risk — using statistical testing, hypothesis testing, and machine learning.

---

## 🧠 Problem Statement

Emergency departments face constant pressure around three operational challenges:

- **Prolonged length of stay (LOS)** that strains capacity and affects patient experience
- **Inconsistent outcomes across triage levels** making it hard to allocate resources effectively
- **Late identification of admission-likely patients**, delaying bed planning and care coordination

This project works through the full analytics pipeline — from exploratory statistics to predictive modeling — to surface insights that can support earlier, more data-driven ED decision-making.

---

## 🗂️ Repository Structure

```
ed-analytics-project/
│
├── data/
│   └── ed_visits.csv               # 400 synthetic ED patient visits
│
├── notebooks/
│   └── ED_Analytics.ipynb          # Full end-to-end analysis notebook
│
├── scripts/
│   ├── explore.py                  # Dataset inspection & LOS summary
│   ├── statistics.py               # Hypothesis testing & ANOVA
│   ├── models.py                   # Logistic regression, decision tree, random forest
│   └── visualize.py                # LOS comparison plots
│
├── outputs/
│   └── results_summary.txt         # All key numeric results
│
├── docs/
│   └── methodology.md              # Analytical approach and findings
│
├── requirements.txt
└── README.md
```

---

## 📦 Dataset

`ed_visits.csv` — 400 synthetic emergency department patient visits

| Column | Type | Description |
|---|---|---|
| `patient_id` | str | Unique visit identifier |
| `age` | int | Patient age in years |
| `triage_level` | str | Clinical urgency: Low / Medium / High |
| `ed_los_hours` | float | ED length of stay in hours |
| `num_tests_ordered` | int | Number of diagnostic tests ordered |
| `admitted` | int | Outcome: 1 = admitted, 0 = discharged |
| `arrival_hour` | int | Hour of arrival (0–23) |
| `insurance_type` | str | Medicare / Medicaid / Private / Uninsured |

> All data is synthetically generated — no real patient information is used.

---

## 📊 Analysis Pipeline

### 1. Dataset Inspection
- 400 rows × 8 columns
- Mix of numeric (age, LOS, tests) and categorical (triage, insurance) variables

### 2. Length of Stay Summary
| Statistic | Value |
|---|---|
| Mean LOS | **5.54 hours** |
| Median LOS | **4.49 hours** |

The mean exceeds the median, indicating a right-skewed distribution — a small number of patients with very long stays pulling the average up.

### 3. LOS by Admission Status
Admitted patients have substantially longer ED stays than discharged patients, visible in both the distribution shape and summary statistics.

### 4. Hypothesis Testing (t-test)
| Result | Value |
|---|---|
| T-statistic | **8.87** |
| P-value | **< 0.0001** |

The difference in mean LOS between admitted and non-admitted patients is highly statistically significant.

### 5. ANOVA across Triage Levels
| Result | Value |
|---|---|
| F-statistic | **56.95** |
| P-value | **< 0.0001** |

Mean LOS differs significantly across Low, Medium, and High triage groups — confirming triage level is strongly associated with how long patients stay.

### 6–9. Predictive Models (Predicting Admission)

| Model | Accuracy | Notes |
|---|---|---|
| Logistic Regression | **70.5%** | Stable, interpretable baseline |
| ROC-AUC (Logistic) | **0.776** | Good discrimination ability |
| Decision Tree | **100%** | Overfitting on training data |
| Random Forest | **100%** | Overfitting on training data |

The logistic regression model, while lower in raw accuracy, provides the most honest assessment — tree-based models overfit when evaluated on the same data used for training.

### 10. Operational Conclusion
> Patients with longer ED length of stay and more diagnostic tests ordered have a measurably higher likelihood of hospital admission. These variables support early risk stratification — enabling bed planning and care coordination well before a formal admission decision is made.

---

## 🚀 Getting Started

```bash
git clone https://github.com/yourusername/ed-analytics-project.git
cd ed-analytics-project
pip install -r requirements.txt

# Run individual scripts
python scripts/explore.py
python scripts/statistics.py
python scripts/models.py

# Or open the full notebook
jupyter notebook notebooks/ED_Analytics.ipynb
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Analysis and modeling |
| pandas | Data manipulation |
| scipy | Statistical tests (t-test, ANOVA) |
| scikit-learn | Logistic regression, decision tree, random forest, ROC-AUC |
| matplotlib / seaborn | Visualizations |
| Jupyter Notebook | Interactive analysis |

---

## 💡 Key Takeaways

- **LOS and test volume** are the strongest early indicators of admission — actionable before a physician decision is made
- **High triage patients** stay significantly longer on average, supporting resource pre-allocation by triage level
- **Logistic regression** provides a clinically interpretable model for admission probability scoring
- **Tree-based models** need train/test splitting to avoid overfitting — a common pitfall in small healthcare datasets
