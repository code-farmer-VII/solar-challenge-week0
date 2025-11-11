# Solar Challenge – Week 0  
**10 Academy: Artificial Intelligence Mastery**  
*Cross-Country Solar Farm Analysis*  

---

## Project Overview
This repository contains the **Week 0 challenge** for the 10 Academy AI Mastery program. The goal is to analyze solar-measurement data from **Benin, Sierra Leone, and Togo**, perform data profiling, cleaning, exploratory data analysis (EDA), and prepare for cross-country comparison.

**Interim Submission:** November 9, 2025 – 8:00 PM UTC  
**Final Submission:** November 12, 2025 – 8:00 PM UTC

---

## Repository Link
[https://github.com/code-farmer-VII/solar-challenge-week0](https://github.com/code-farmer-VII/solar-challenge-week0)

---

## Folder Structure
```
solar-challenge-week0/
├── .github/
│   └── workflows/
│       └── ci.yml                  # GitHub Actions CI pipeline
├── data/                            # Raw & cleaned data (ignored in Git)
│   ├── benin-malanville.csv
│   ├── sierraleone-bumbuna.csv
│   └── togo-dapaong_qc.csv
├── notebooks/
│   └── benin_eda.ipynb              # Full EDA notebook (Benin)
├── src/                             # Source code (future use)
├── scripts/                         # Utility scripts
├── tests/                           # Unit tests
├── .gitignore
├── README.md
├── requirements.txt
└── pyvenv.cfg                       # Virtual environment marker
```

> **Note:** `data/` folder is **ignored** via `.gitignore`. Only cleaned CSVs are saved locally.

---

## Environment Setup

### 1. Clone the Repository
```bash
git clone https://github.com/code-farmer-VII/solar-challenge-week0.git
cd solar-challenge-week0
```

### 2. Create & Activate Virtual Environment
```bash
# Windows
python -m venv solar-challenge-week0
.\solar-challenge-week0\Scripts\Activate.ps1

# Linux / macOS
python -m venv solar-challenge-week0
source solar-challenge-week0/bin/activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Register Jupyter Kernel
```bash
python -m ipykernel install --user --name solar-challenge --display-name "Python (solar-challenge)"
```

### 5. Launch Jupyter Notebook
```bash
jupyter notebook
```
→ Open `notebooks/benin_eda.ipynb`  
→ **Kernel → Change Kernel → Python (solar-challenge)**

---

## Git Workflow (Completed)

```bash
# Task 1: Environment & Git Setup
git checkout -b setup-task
git add .
git commit -m "init: add .gitignore and project structure"
git commit -m "chore: setup virtual environment"
git commit -m "ci: add GitHub Actions workflow"
git push -u origin setup-task
# → Merged via PR to main

# Task 2: Benin EDA
git checkout -b eda-benin
# ...work in benin_eda.ipynb...
git add .
git commit -m "feat: add EDA and cleaning for Benin dataset"
git push -u origin eda-benin
```

---

## Task 2: Benin EDA (`benin_eda.ipynb`) – Key Steps

| Step | Action |
|------|-------|
| 1 | Load `benin-malanville.csv` |
| 2 | Convert `Timestamp` → `datetime`, set as index |
| 3 | Replace negative values in `GHI, DNI, DHI, ModA, ModB` → `NaN` |
| 4 | **Z-score outlier removal** (`|Z| > 3`) |
| 5 | **Median imputation** for key columns |
| 6 | Export → `data/benin_clean.csv` |
| 7 | Generate **10+ visualizations** (line, bar, heatmap, scatter, bubble, wind rose) |

---

## Key EDA Insights (Benin)

- **Solar Peak:** GHI peaks ~12:00–14:00 daily.
- **Cleaning Impact:** ModA/ModB increase **~8–12%** post-cleaning.
- **Negative Correlation:** High `RH` → lower `GHI` (cloud cover effect).
- **Strong Correlation:** `GHI ↔ DNI ↔ ModA/ModB` (> 0.95).
- **Outliers Removed:** ~2.1% of rows (sensor errors at night).

---

## CI/CD Pipeline
`.github/workflows/ci.yml` runs on every push/PR:
```yaml
- Install dependencies
- Run python --version
- Lint check (future)
```

---

## Next Steps (Final Submission)

| Task | Status |
|------|--------|
| EDA for Sierra Leone & Togo | In Progress |
| Cross-country comparison notebook | `compare_countries.ipynb` |
| Interactive Streamlit Dashboard | `app/main.py` |
| Final Medium-style PDF Report | To be written |

---

## Submission Checklist (Interim – Nov 9)

- [x] GitHub repo: **public & up-to-date**  
- [x] `main` branch: merged `setup-task`  
- [x] `eda-benin` branch: full EDA + cleaned CSV  
- [x] `requirements.txt` + `ci.yml`  
- [x] PDF Report (3–5 pages) with:  
  - Task 1 summary  
  - Benin EDA results & plots  
  - GitHub link  

**Submitted on 10 Academy Platform**

---

## References
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)
- [GitHub Actions Docs](https://docs.github.com/en/actions)

---

**Author:** code-farmer-VII (Temesgen Gonfa) 
**Date:** November 9, 2025  
**Location:** Addis Ababa, Ethiopia (EAT)
```
```