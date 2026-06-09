import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\Meghana\Downloads\customer-segmentation-project\Mall_Customers.csv")

st.title("Customer Segmentation Dashboard")

st.write(df.head())

fig, ax = plt.subplots()

sns.scatterplot(
    x='Annual Income (k$)',
    y='Spending Score (1-100)',
    hue='Cluster',
    data=df,
    ax=ax
)

st.pyplot(fig)
cluster = st.selectbox(
    "Select Cluster",
    sorted(df['Cluster'].unique())
)

filtered = df[df['Cluster'] == cluster]

st.write(filtered)