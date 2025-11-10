
````markdown
# Solar Challenge Week 0

## Setup Instructions

1. Clone the repo:

```bash
git clone https://github.com/code-farmer-VII/solar-challenge-week0.git
cd solar-challenge-week0
````

2. Create and activate virtual environment:

```bash
python -m venv solar-challenge-week0
# Activate
# Windows PowerShell:
.\solar-challenge-week0\Scripts\Activate.ps1
# macOS/Linux:
source solar-challenge-week0/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Folder Structure:

```
solar-challenge-week0/
├── Include/               # part of venv
├── Lib/                   # part of venv
├── Scripts/               # part of venv
├── pyvenv.cfg             # venv config
├── .github/
│   └── workflows/ci.yml
├── notebooks/
├── src/
├── tests/
├── scripts/
├── .gitignore
├── README.md
├── requirements.txt

```

````

---

## **Step 6: Create Initial Branch & Git Commands**

```bash
# Initialize repo (if not done)
git init

# Add remote (if not done)
git remote add origin https://github.com/YOUR_USERNAME/solar-challenge-week0.git

# Check status
git status

# Stage files
git add .

# Commit 1
git commit -m "init: add .gitignore and project structure"

# Create branch
git checkout -b setup-task

# Commit 2
git commit -m "chore: setup virtual environment"

# Commit 3
git commit -m "ci: add GitHub Actions workflow"

# Push branch
git push -u origin setup-task

# Create Pull Request to main
# Then merge PR
````
