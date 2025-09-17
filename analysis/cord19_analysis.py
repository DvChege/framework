"""CORD-19 metadata analysis script

Steps:
- Load metadata.csv (or use sample_metadata.csv if metadata.csv not present)
- Basic exploration
- Cleaning: convert publish_time to datetime, extract year, compute abstract word count
- Simple analysis & visualizations saved to analysis/plots
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

sns.set(style='whitegrid', rc={'figure.figsize':(10,6)})

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
PLOT_DIR = os.path.join(os.path.dirname(__file__), 'plots')
os.makedirs(PLOT_DIR, exist_ok=True)

# Prefer full metadata if user placed it; otherwise use sample
full_path = os.path.join(DATA_DIR, 'metadata.csv')
sample_path = os.path.join(DATA_DIR, 'sample_metadata.csv')

if os.path.exists(full_path):
    df = pd.read_csv(full_path)
    print('Loaded metadata.csv (full dataset).')
else:
    df = pd.read_csv(sample_path)
    print('Loaded sample_metadata.csv.')

print('\n--- Basic Info ---')
print('Shape:', df.shape)
print(df.head(3))
print('\nData types:')
print(df.dtypes)
print('\nMissing values per column:')
print(df.isnull().sum())

# Cleaning & preparation
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df['abstract'] = df['abstract'].fillna('')
df['abstract_word_count'] = df['abstract'].astype(str).apply(lambda x: len(x.split()))

print('\nAfter cleaning:')
print(df[['cord_uid','title','publish_time','year','abstract_word_count']].head(5))

# Analysis: publications by year
year_counts = df['year'].value_counts().sort_index()
print('\nPublications by year:\n', year_counts)

# Plot publications by year
plt.figure(figsize=(8,5))
year_counts.plot(kind='bar')
plt.title('Publications by Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig(os.path.join(PLOT_DIR, 'publications_by_year.png'))
print('Saved plot:', os.path.join(PLOT_DIR, 'publications_by_year.png'))

# Top journals
top_journals = df['journal'].value_counts().head(10)
plt.figure(figsize=(8,5))
top_journals.plot(kind='bar')
plt.title('Top Publishing Journals (sample)')
plt.xlabel('Journal')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig(os.path.join(PLOT_DIR, 'top_journals.png'))
print('Saved plot:', os.path.join(PLOT_DIR, 'top_journals.png'))

# Word frequency in titles (simple)
from collections import Counter
import re
titles = df['title'].dropna().astype(str).str.lower().tolist()
words = []
for t in titles:
    words += re.findall(r"\\w+", t)
stopwords = set(['the','and','of','in','to','a','for'])
words = [w for w in words if w not in stopwords and len(w)>2]
wc = Counter(words)
common = wc.most_common(30)
print('\nTop title words:', common[:10])

# Word cloud of titles
wc_text = ' '.join(titles)
wordcloud = WordCloud(width=800, height=400, collocations=False).generate(wc_text)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(PLOT_DIR, 'title_wordcloud.png'))
print('Saved plot:', os.path.join(PLOT_DIR, 'title_wordcloud.png'))

print('\nAnalysis complete. Check the analysis/plots folder for visuals.')
