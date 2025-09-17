import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os
from collections import Counter
import re

st.set_page_config(page_title='CORD-19 Data Explorer', layout='wide')
st.title('CORD-19 Data Explorer')
st.write('Simple interactive explorer for the CORD-19 metadata (sample).')

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
full_path = os.path.join(DATA_DIR, 'metadata.csv')
sample_path = os.path.join(DATA_DIR, 'sample_metadata.csv')

if os.path.exists(full_path):
    df = pd.read_csv(full_path)
    st.info('Loaded full metadata.csv from data/.')
else:
    df = pd.read_csv(sample_path)
    st.info('Loaded sample_metadata.csv (included).')

# Basic cleaning
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df['abstract'] = df['abstract'].fillna('')
df['abstract_word_count'] = df['abstract'].astype(str).apply(lambda x: len(x.split()))

# Sidebar filters
st.sidebar.header('Filters')
min_year = int(df['year'].min()) if df['year'].notnull().any() else 2019
max_year = int(df['year'].max()) if df['year'].notnull().any() else 2022
year_range = st.sidebar.slider('Select year range', min_year, max_year, (min_year, max_year))

selected_journal = st.sidebar.selectbox('Journal (Top 10)', options=['All'] + df['journal'].fillna('Unknown').value_counts().head(10).index.tolist())

# Filtered dataframe
df_filtered = df.copy()
df_filtered = df_filtered[(df_filtered['year'] >= year_range[0]) & (df_filtered['year'] <= year_range[1])]
if selected_journal != 'All':
    df_filtered = df_filtered[df_filtered['journal'] == selected_journal]

st.subheader('Data sample')
st.dataframe(df_filtered[['cord_uid','title','publish_time','journal','source_x']].head(50))

# Publications over time
st.subheader('Publications by Year')
year_counts = df_filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
year_counts.plot(kind='bar', ax=ax)
ax.set_xlabel('Year')
ax.set_ylabel('Count')
st.pyplot(fig)

# Top journals
st.subheader('Top Journals')
top_j = df_filtered['journal'].value_counts().head(10)
fig2, ax2 = plt.subplots()
top_j.plot(kind='bar', ax=ax2)
ax2.set_xlabel('Journal')
ax2.set_ylabel('Count')
st.pyplot(fig2)

# Title word cloud
st.subheader('Word Cloud — Titles')
titles = df_filtered['title'].dropna().astype(str).str.lower().tolist()
wc_text = ' '.join(titles)
if wc_text.strip():
    wc = WordCloud(width=800, height=300, collocations=False).generate(wc_text)
    fig3, ax3 = plt.subplots(figsize=(10,4))
    ax3.imshow(wc, interpolation='bilinear')
    ax3.axis('off')
    st.pyplot(fig3)
else:
    st.write('No titles to display in word cloud.')

st.write('---')
st.write('Project prepared for submission. Replace `data/sample_metadata.csv` with the full `metadata.csv` for full analysis.')
