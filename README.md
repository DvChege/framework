# Frameworks_Assignment – CORD-19 Data Exploration & Streamlit App

A beginner-friendly CORD-19 metadata analysis project. This repository contains a complete, professionally structured implementation for the assignment: data loading, cleaning, exploratory analysis, visualizations, and a Streamlit dashboard.

## Repo contents
- `data/sample_metadata.csv` — a small sample of the metadata file so the code can run without downloading the full dataset.
- `analysis/cord19_analysis.py` — a step-by-step, well-commented analysis script (load, clean, explore, visualize).
- `app.py` — Streamlit app to explore the cleaned data and visualizations interactively.
- `requirements.txt` — Python packages required.
- `README.md` — this file.
- `CONTRIBUTING.md` — contribution guide.
- `LICENSE` — MIT License.

## How to use
1. (Optional) Download the full `metadata.csv` from the CORD-19 dataset if you want to run on real data:
   https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge

   Place the file in the `data/` folder and rename to `metadata.csv`.

2. Create a virtual environment & install requirements:
```bash
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

3. Run the analysis script (produces plots saved into `analysis/`):
```bash
python analysis/cord19_analysis.py
```

4. Run the Streamlit app:
```bash
streamlit run app.py
```

## Notes
- The `data/sample_metadata.csv` is a small synthetic sample to let you run and test the code immediately.
- If you place the full `metadata.csv` into `data/` the scripts will use it automatically (it may be large; consider working with a subset).

## Author
Bashir — prepared and packaged for submission.

