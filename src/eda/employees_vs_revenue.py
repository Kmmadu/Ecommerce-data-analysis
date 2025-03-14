import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/internet_companies.csv")

# Ensure numeric conversion
df["Revenue USD billions"] = pd.to_numeric(df["Revenue USD billions"], errors="coerce")
df["Employees"] = pd.to_numeric(df["Employees"], errors="coerce")

# Scatter plot: Employees vs Revenue
plt.figure(figsize=(8,5))
sns.scatterplot(x="Employees", y="Revenue USD billions", data=df, hue="Industry", palette="Dark2")
plt.title("Relationship Between Employees and Revenue")
plt.xlabel("Number of Employees")
plt.ylabel("Revenue (Billion USD)")
plt.grid()
plt.show()
