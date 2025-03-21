import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Custom CSS for Center Alignment & Mobile Responsiveness
st.markdown("""
    <style>
        h1, h2, h3, h4, h5, h6 {
            text-align: center !important;
        }
        @media screen and (max-width: 768px) {
            .st-emotion-cache-1xarl3l {  /* Adjusts columns in mobile view */
                flex-direction: column !important;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Load dataset
@st.cache_data  # Cache the data loading step
def load_data():
    df = pd.read_csv("data/internet_companies.csv")
    df["Revenue USD billions"] = pd.to_numeric(df["Revenue USD billions"], errors="coerce")
    df["Market cap. USD billions"] = pd.to_numeric(df["Market cap. USD billions"], errors="coerce")
    df["Employees"] = pd.to_numeric(df["Employees"], errors="coerce")
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")
selected_industry = st.sidebar.selectbox("Select Industry", ["All"] + list(df["Industry"].unique()))
selected_company = st.sidebar.selectbox("Select Company", ["All"] + list(df["Company"].unique()))

# Apply Filters
filtered_df = df.copy()
if selected_industry != "All":
    filtered_df = filtered_df[filtered_df["Industry"] == selected_industry]
if selected_company != "All":
    filtered_df = filtered_df[filtered_df["Company"] == selected_company]

# Title
st.title("Internet Companies Dashboard")

# Key Insights
st.markdown("""
    ### Key Insights
    - The **E-commerce** industry dominates in both revenue and market capitalization.
    - **Amazon** has the highest revenue, but **Alphabet** leads in market cap.
    - Companies in **Social Media** have the highest revenue per employee.
""")

# Overview Section (Responsive Layout)
st.header("Overview")
cols = st.columns(1 if st.session_state.get("mobile_view", False) else 3)
cols[0].metric("Total Companies", len(filtered_df))
cols[1].metric("Total Revenue (USD billions)", round(filtered_df["Revenue USD billions"].sum(), 2))
cols[2].metric("Total Market Cap (USD billions)", round(filtered_df["Market cap. USD billions"].sum(), 2))

# Industry Analysis
st.header("Industry Analysis")
col4, col5 = st.columns(2)

with col4:
    st.subheader("Percentage of Companies by Industry")  # Updated title
    industry_counts = filtered_df["Industry"].value_counts()
    
    # Group smaller industries into "Other"
    threshold = 10  # Minimum number of companies to be included as a separate slice
    top_industries = industry_counts[industry_counts >= threshold]
    other_count = industry_counts[industry_counts < threshold].sum()
    top_industries["Other"] = other_count
    
    # Create pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(top_industries, labels=top_industries.index, autopct='%1.1f%%', startangle=90, explode=[0.1]*len(top_industries))
    ax1.set_ylabel('')
    st.pyplot(fig1)


with col5:
    st.subheader("Total Revenue by Industry")
    industry_revenue = filtered_df.groupby("Industry")["Revenue USD billions"].sum().nlargest(10)
    st.line_chart(industry_revenue)

# Geographical Analysis
st.header("Geographical Analysis")
st.subheader("Top 10 Locations by Number of Companies")
location_counts = filtered_df["Headquarters"].value_counts().head(10)
fig3, ax3 = plt.subplots()
sns.barplot(x=location_counts.index, y=location_counts.values, palette="magma", ax=ax3)
ax3.set_xticklabels(ax3.get_xticklabels(), rotation=45, ha="right")
st.pyplot(fig3)

# Revenue and Market Cap Trends (Heatmap)
st.header("Revenue and Market Cap Trends")
st.subheader("Heatmap of Revenue vs. Market Cap by Top 10 Industries")
heatmap_data = filtered_df.groupby("Industry")[["Revenue USD billions", "Market cap. USD billions"]].mean().nlargest(10, "Revenue USD billions")
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5, ax=ax4)
ax4.set_xlabel("Metric")
ax4.set_ylabel("Industry")
st.pyplot(fig4)

# Top Performers
st.header("Top Performers")
top_revenue = filtered_df.nlargest(10, "Revenue USD billions").reset_index(drop=True)
top_revenue.index = top_revenue.index + 1
st.subheader("Top 10 Companies by Revenue")
st.dataframe(top_revenue[["Company", "Revenue USD billions"]])

# Employee Analysis
st.header("Employee Analysis")
valid_employee_df = filtered_df.dropna(subset=["Employees"])
valid_employee_df["Revenue per Employee"] = valid_employee_df["Revenue USD billions"] * 1e9 / valid_employee_df["Employees"]
top_revenue_per_employee = valid_employee_df.nlargest(10, "Revenue per Employee").reset_index(drop=True)
top_revenue_per_employee.index = top_revenue_per_employee.index + 1
st.subheader("Top 10 Companies by Revenue per Employee")
st.dataframe(top_revenue_per_employee[["Company", "Revenue per Employee"]])

# Display Filtered Data
st.sidebar.header("Filtered Data")
st.write(f"Data for {selected_industry} Industry and {selected_company} Company")
filtered_df.index = filtered_df.index + 1
st.dataframe(filtered_df)

# Download Filtered Data
st.sidebar.download_button(
    label="Download Filtered Data as CSV",
    data=filtered_df.to_csv(index=False).encode("utf-8"),
    file_name="filtered_data.csv",
    mime="text/csv",
)

# Download Insights PDF
with open("reports/Insights.pdf", "rb") as f:
    pdf_bytes = f.read()

st.sidebar.download_button(
    label="Download Insights (PDF)",
    data=pdf_bytes,
    file_name="Insights.pdf",
    mime="application/pdf",
)
