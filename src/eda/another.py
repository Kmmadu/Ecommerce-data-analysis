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
df["Revenue per Employee"] = df["Revenue USD billions"] * 1e9 / df["Employees"]  # Convert revenue to USD
plt.figure(figsize=(10, 6))
sns.barplot(x="Company", y="Revenue per Employee", data=df.nlargest(10, "Revenue per Employee"), palette="viridis")
plt.title("Top 10 Companies by Revenue per Employee")
plt.xlabel("Company")
plt.ylabel("Revenue per Employee (USD)")
plt.xticks(rotation=45)
plt.show()

# Market Cap per Employee
df["Market Cap per Employee"] = df["Market cap. USD billions"] * 1e9 / df["Employees"]  # Convert market cap to USD
plt.figure(figsize=(10, 6))
sns.barplot(x="Company", y="Market Cap per Employee", data=df.nlargest(10, "Market Cap per Employee"), palette="coolwarm")
plt.title("Top 10 Companies by Market Cap per Employee")
plt.xlabel("Company")
plt.ylabel("Market Cap per Employee (USD)")
plt.xticks(rotation=45)
plt.show()