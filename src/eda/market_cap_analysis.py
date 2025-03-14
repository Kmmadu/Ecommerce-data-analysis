import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/internet_companies.csv")

# Ensure numeric conversion
df["Market cap. USD billions"] = pd.to_numeric(df["Market cap. USD billions"], errors="coerce")

# Group by Industry
industry_market_cap = df.groupby("Industry")["Market cap. USD billions"].sum().reset_index()

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(x="Market cap. USD billions", y="Industry", 
            data=industry_market_cap.sort_values(by="Market cap. USD billions", ascending=False),
            palette="coolwarm")
plt.title("Total Market Capitalization by Industry")
plt.xlabel("Market Cap (Billion USD)")
plt.ylabel("Industry")
plt.grid(axis="x", linestyle="--")
plt.show()
