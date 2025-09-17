

# 🦠 CORD-19 Data Exploration & Streamlit App

## 📌 Overview

This project provides a beginner-friendly workflow for analyzing the **CORD-19 research dataset**. It covers the entire data science pipeline — from **loading and cleaning data** to **basic analysis, visualization, and deployment of an interactive Streamlit app**.

The dataset contains metadata on COVID-19 research papers, including titles, abstracts, publication dates, journals, authors, and source information.

🔗 Dataset: [CORD-19 Research Challenge (Kaggle)](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)

---

## 🎯 Learning Objectives

By completing this project, you will:

* Load and explore a real-world dataset using **pandas**
* Apply **basic data cleaning** techniques
* Generate meaningful **visualizations** using Matplotlib/Seaborn
* Build an interactive **Streamlit web application**
* Present insights in a clear and structured way

---

## 🛠️ Tools & Technologies

* **Python 3.7+**
* **pandas** → data manipulation
* **matplotlib** & **seaborn** → data visualization
* **Streamlit** → web application framework
* **Jupyter Notebook** (optional) → exploratory analysis

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## 📂 Project Structure

```
Frameworks_Assignment/
│── data/
│   └── sample_metadata.csv        # Sample of the dataset (for demo)
│── analysis/
│   └── cord19_analysis.py         # Data loading, cleaning, visualization
│── app.py                         # Streamlit dashboard
│── requirements.txt               # Required Python packages
│── README.md                      # Project documentation
│── CONTRIBUTING.md                # Contribution guidelines
│── LICENSE                        # License file
│── .gitignore                     # Git ignore rules
│── screenshots/                   # Example charts and app previews
```

---

## 🚀 Usage

### 1️⃣ Run Analysis Script

```bash
python analysis/cord19_analysis.py
```

### 2️⃣ Launch Streamlit App

```bash
streamlit run app.py
```

---

## 📊 Example Visualizations

### 📈 Publications by Year

Shows the trend of COVID-19 related publications over time.

![Publications by Year](screenshots/publications_by_year.png)

---

### 🏛️ Top Journals Publishing COVID-19 Research

Highlights the most active journals publishing during the pandemic.

![Top Journals](screenshots/top_journals.png)

---

### ☁️ Word Cloud of Paper Titles

Displays the most common keywords in paper titles.

![Word Cloud](screenshots/wordcloud_titles.png)

---

### 📊 Distribution of Papers by Source

Breakdown of research publications by their source repositories.

![Distribution by Source](screenshots/distribution_by_source.png)

---

## 📑 Assignment Deliverables

* Python analysis script (`cord19_analysis.py`)
* Streamlit dashboard (`app.py`)
* Documentation (`README.md`)
* GitHub repo submission (`Frameworks_Assignment`)

---

## ✨ Expected Outcomes

By the end of this project, you will have:
✅ A functional analysis script with visualizations
✅ Several insights about COVID-19 research trends
✅ A working Streamlit app
✅ A polished GitHub repository

---

## 🤝 Contribution

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).


