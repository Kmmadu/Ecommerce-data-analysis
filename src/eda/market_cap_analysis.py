import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/internet_companies.csv")  # Ensure it's the cleaned file

# 🔍 Strip spaces from column names
df.columns = df.columns.str.strip()

# 🔍 Remove non-numeric characters from "Market cap. USD billions"
df["Market cap. USD billions"] = (
    df["Market cap. USD billions"]
    .astype(str)  # Convert to string in case of mixed types
    .str.replace(r"[^\d.]", "", regex=True)  # Keep only numbers and dots
    .replace("", None)  # Replace empty strings with None (NaN)
    .astype(float)  # Convert back to float
)

# 🔍 Check if conversion was successful
print(df["Market cap. USD billions"].describe())

# Drop rows with NaN values in "Market cap. USD billions"
df = df.dropna(subset=["Market cap. USD billions"])

# Group by Industry
industry_market_cap = df.groupby("Industry")["Market cap. USD billions"].sum().reset_index()
industry_market_cap = industry_market_cap.sort_values(by="Market cap. USD billions", ascending=False)

# 🔍 Print to verify
print(industry_market_cap.head(10))

# Ensure there are valid values before plotting
if not industry_market_cap.empty:
    # Filter to show only the top 10 industries
    top_industries = industry_market_cap.head(10)

    # Plot
    plt.figure(figsize=(12, 6))
    sns.barplot(x="Market cap. USD billions", y="Industry", 
                data=top_industries, palette="coolwarm")

    plt.title("Top 10 Industries by Total Market Capitalization")
    plt.xlabel("Market Cap (Billion USD)")
    plt.ylabel("Industry")
    plt.xticks(rotation=45)
    plt.grid(axis="x", linestyle="--")
    plt.tight_layout()  # Ensure labels fit properly
    plt.show()
else:
    print("🚨 No valid market capitalization data found. Check CSV file.")