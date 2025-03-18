import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
try:
    df = pd.read_csv("data/internet_companies.csv")
    print("Data loaded successfully:")
    print(df.head())
except FileNotFoundError:
    print("Error: File not found. Check the file path.")


# Debugging: Check for NaN values after conversion
print("After numeric conversion:")
print(df["Revenue USD billions"].head())

# Drop rows with NaN values in the Revenue column
df = df.dropna(subset=["Revenue USD billions"])

# Debugging: Print the cleaned data
print("After dropping NaN values:")
print(df.head())

# Sort by Revenue and select top 10
top_revenue = df.sort_values(by="Revenue USD billions", ascending=False).head(10)

# Debugging: Print the top 10 data
print("Top 10 companies by revenue:")
print(top_revenue[["Company", "Revenue USD billions"]])

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(
    x="Revenue USD billions", 
    y="Company", 
    data=top_revenue, 
    palette="viridis"
)
plt.title("Top 10 Internet Companies by Revenue")
plt.xlabel("Revenue (Billion USD)")
plt.ylabel("Company")
plt.grid(axis="x", linestyle="--")
plt.tight_layout()
plt.show()