import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/internet_companies.csv")

# Convert numeric columns to float
df["Revenue USD billions"] = pd.to_numeric(df["Revenue USD billions"], errors="coerce")
df["Market cap. USD billions"] = pd.to_numeric(df["Market cap. USD billions"], errors="coerce")
df["Employees"] = pd.to_numeric(df["Employees"], errors="coerce")


# Sidebar Filters
st.sidebar.header("Filters")
selected_industry = st.sidebar.selectbox("Select Industry", ["All"] + list(df["Industry"].unique()))
selected_company = st.sidebar.selectbox("Select Company", ["All"] + list(df["Company"].unique()))

# Apply Filters
if selected_industry != "All":
    df = df[df["Industry"] == selected_industry]
if selected_company != "All":
    df = df[df["Company"] == selected_company]

# Title
st.title("Internet Companies Dashboard")

# Overview
st.header("Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Total Companies", len(df))
col2.metric("Total Revenue (USD billions)", df["Revenue USD billions"].sum())
col3.metric("Total Market Cap (USD billions)", df["Market cap. USD billions"].sum())

# Industry Analysis
st.header("Industry Analysis")
industry_counts = df["Industry"].value_counts()
st.subheader("Number of Companies by Industry")
st.bar_chart(industry_counts)

industry_revenue = df.groupby("Industry")["Revenue USD billions"].sum()
st.subheader("Total Revenue by Industry")
st.bar_chart(industry_revenue)

# Geographical Analysis
st.header("Geographical Analysis")
location_counts = df["Headquarters"].value_counts().head(10)
st.subheader("Top 10 Locations by Number of Companies")
st.bar_chart(location_counts)

# Top Performers
st.header("Top Performers")
top_revenue = df.nlargest(10, "Revenue USD billions")
st.subheader("Top 10 Companies by Revenue")
st.write(top_revenue[["Company", "Revenue USD billions"]])

# Revenue and Market Cap Trends
st.header("Revenue and Market Cap Trends")
fig, ax = plt.subplots()
sns.scatterplot(x="Revenue USD billions", y="Market cap. USD billions", data=df, ax=ax)
st.pyplot(fig)

# Employee Analysis
st.header("Employee Analysis")
df["Revenue per Employee"] = df["Revenue USD billions"] * 1e9 / df["Employees"]
top_revenue_per_employee = df.nlargest(10, "Revenue per Employee")
st.subheader("Top 10 Companies by Revenue per Employee")
st.write(top_revenue_per_employee[["Company", "Revenue per Employee"]])

# Display Filtered Data
st.sidebar.header("Filtered Data")
st.write(f"Data for {selected_industry} Industry and {selected_company} Company")
st.write(df)