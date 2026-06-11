import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.title(" Insights & Visualizations")
# Load Dataset
df = pd.read_csv("heart-checkpoint.csv")
st.subheader("Dataset Preview")
st.dataframe(df.head())
# Heart Disease Count
st.subheader("Heart Disease Distribution")
fig, ax = plt.subplots()
sns.countplot(x='HeartDisease', data=df, ax=ax)
st.pyplot(fig)
# Age Distribution
st.subheader("Age Distribution")
fig, ax = plt.subplots()
sns.histplot(df['Age'], kde=True, ax=ax)
3
st.pyplot(fig)
# Correlation Heatmap
st.subheader("Correlation Heatmap")
fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(df.select_dtypes(include=['int64','float64']).corr(),
annot=True,
cmap='coolwarm',
ax=ax)
st.pyplot(fig)
# Boxplots
st.subheader("Numerical Feature Boxplots")
num_cols = ['Age', 'RestingBP', 'Cholesterol',
'MaxHR', 'Oldpeak']
fig, axes = plt.subplots(2,3, figsize=(15,8))
axes = axes.flatten()

for i, col in enumerate(num_cols):
    sns.boxplot(x=df[col], ax=axes[i])
    axes[i].set_title(col)

plt.tight_layout()
st.pyplot(fig)

