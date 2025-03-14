import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/internet_companies.csv")

# Ensure numeric conversion
df["Revenue USD billions"] = pd.to_numeric(df["Revenue USD billions"], errors="coerce")

# Sort by Revenue
top_revenue = df.sort_values(by="Revenue USD billions", ascending=False).head(10)

# Plot
plt.figure(figsize=(10, 5))
sns.barplot(x="Revenue USD billions", y="Company", data=top_revenue, palette="viridis")
plt.title("Top 10 Internet Companies by Revenue")
plt.xlabel("Revenue (Billion USD)")
plt.ylabel("Company")
plt.grid(axis="x", linestyle="--")
plt.show()
