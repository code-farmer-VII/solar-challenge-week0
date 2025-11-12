# app/main.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide", page_title="Solar Comparison")
st.title("Solar Data — Cross Country Comparison")

# Load cleaned csvs (local)
@st.cache_data
def load_data():
    ben = pd.read_csv("data/benin_clean.csv")
    sierra = pd.read_csv("data/sierraleone_clean.csv")
    togo = pd.read_csv("data/togo_clean.csv")
    ben['country'] = 'Benin'; sierra['country']='SierraLeone'; togo['country']='Togo'
    df = pd.concat([ben,sierra,togo], ignore_index=True)
    return df

df = load_data()
countries = df['country'].unique().tolist()
sel = st.multiselect("Select countries", countries, default=countries)

metric = st.selectbox("Select metric", ["GHI","DNI","DHI"])
filtered = df[df['country'].isin(sel)]

# -------------------------------------------------
#  RESPONSIVE MEDIUM-SIZED BOXPLOT
# -------------------------------------------------
st.subheader(f"{metric} comparison")

col1, col2 = st.columns([3, 1])
with col1:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x="country", y=metric, data=filtered, ax=ax, palette="Set2")
    ax.set_title(f"{metric} distribution by country", fontsize=14, pad=12)
    ax.set_xlabel("Country", fontsize=12)
    ax.set_ylabel(metric, fontsize=12)
    sns.despine(trim=True)
    st.pyplot(fig, use_container_width=True)

with col2:
    st.caption("**Quick stats**")
    summary = filtered.groupby("country")[[metric]].agg(["mean", "median", "std"]).round(2)
    st.dataframe(summary, use_container_width=True)

# -------------------------------------------------
#  (Original) Summary table – you can keep it below if you prefer
# -------------------------------------------------
st.subheader("Full summary table")
summary = filtered.groupby('country')[[metric]].agg(['mean','median','std']).round(2)
st.dataframe(summary)