import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
def load_data():
    df = pd.read_csv("data/internet_companies.csv")
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")
selected_industry = st.sidebar.selectbox("Select Industry", ["All"] + list(df["Industry"].unique()))
selected_company = st.sidebar.selectbox("Select Company", ["All"] + list(df["Company"].unique()))

# Apply Filters
if selected_industry != "All":
    df = df[df["Industry"] == selected_industry]
if selected_company != "All":
    df = df[df["Company"] == selected_company]

# Overview Metrics
st.title("📊 Internet Companies EDA Dashboard")
col1, col2, col3 = st.columns(3)
col1.metric("Total Companies", len(df))
col2.metric("Avg. Revenue (USD B)", round(df["Revenue USD billions"].mean(), 2))
col3.metric("Avg. Market Cap (USD B)", round(df["Market cap. USD billions"].mean(), 2))

# Industry Distribution
st.subheader("Number of Companies by Industry")
plt.figure(figsize=(10, 5))
sns.countplot(y=df["Industry"], order=df["Industry"].value_counts().index, palette="viridis")
st.pyplot(plt)

# Top 10 Companies by Revenue
st.subheader("Top 10 Companies by Revenue")
top_revenue = df.nlargest(10, "Revenue USD billions")
plt.figure(figsize=(10, 5))
sns.barplot(x="Revenue USD billions", y="Company", data=top_revenue, palette="coolwarm")
st.pyplot(plt)

# Revenue vs Market Cap
st.subheader("Revenue vs. Market Cap")
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["Revenue USD billions"], y=df["Market cap. USD billions"], hue=df["Industry"], palette="Set1")
st.pyplot(plt)

# Interactive Data Table
st.subheader("Company Data Table")
st.dataframe(df)
