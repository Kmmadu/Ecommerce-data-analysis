import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/internet_companies.csv")


# Employee Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df["Employees"], bins=20, kde=True)
plt.title("Distribution of Employees")
plt.xlabel("Number of Employees")
plt.ylabel("Frequency")
plt.show()

# Revenue per Employee
df["Revenue per Employee"] = df["Revenue USD billions"] * 1e9 / df["Employees"]
plt.figure(figsize=(10, 6))
sns.barplot(x="Company", y="Revenue per Employee", data=df.nlargest(10, "Revenue per Employee"), palette="viridis")
plt.title("Top 10 Companies by Revenue per Employee")
plt.xlabel("Company")
plt.ylabel("Revenue per Employee (USD)")
plt.xticks(rotation=45)
plt.show()

# Market Cap per Employee
df["Market Cap per Employee"] = df["Market cap. USD billions"] * 1e9 / df["Employees"]
plt.figure(figsize=(10, 6))
sns.barplot(x="Company", y="Market Cap per Employee", data=df.nlargest(10, "Market Cap per Employee"), palette="coolwarm")
plt.title("Top 10 Companies by Market Cap per Employee")
plt.xlabel("Company")
plt.ylabel("Market Cap per Employee (USD)")
plt.xticks(rotation=45)
plt.show()

# Industry Distribution
industry_counts = df["Industry"].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=industry_counts.index, y=industry_counts.values, palette="viridis")
plt.title("Number of Companies by Industry")
plt.xlabel("Industry")
plt.ylabel("Number of Companies")
plt.xticks(rotation=45)
plt.show()

# Revenue by Industry
industry_revenue = df.groupby("Industry")["Revenue USD billions"].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=industry_revenue.index, y=industry_revenue.values, palette="coolwarm")
plt.title("Total Revenue by Industry")
plt.xlabel("Industry")
plt.ylabel("Total Revenue (USD billions)")
plt.xticks(rotation=45)
plt.show()

# Headquarters Location Distribution
location_counts = df["Headquarters"].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=location_counts.index, y=location_counts.values, palette="viridis")
plt.title("Top 10 Locations by Number of Companies")
plt.xlabel("Location")
plt.ylabel("Number of Companies")
plt.xticks(rotation=45)
plt.show()

# Revenue vs. Market Cap
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Revenue USD billions", y="Market cap. USD billions", data=df, hue="Industry", palette="Dark2")
plt.title("Revenue vs. Market Cap")
plt.xlabel("Revenue (USD billions)")
plt.ylabel("Market Cap (USD billions)")
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.show()

print("Data analysis complete!")
