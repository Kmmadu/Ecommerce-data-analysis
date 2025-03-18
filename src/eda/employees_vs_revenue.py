import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/internet_companies.csv")

# Ensure numeric conversion
df["Revenue USD billions"] = pd.to_numeric(df["Revenue USD billions"], errors="coerce")
df["Employees"] = pd.to_numeric(df["Employees"], errors="coerce")

# Drop NaN values
df = df.dropna(subset=["Employees", "Revenue USD billions", "Industry"])

# Check if Industry column exists and has valid values
if df["Industry"].nunique() > 1:
    hue_var = "Industry"
else:
    hue_var = None  # Avoid using hue if there's only one unique value

# Scatter plot: Employees vs Revenue
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Employees", y="Revenue USD billions", data=df, hue=hue_var, palette="Dark2")

plt.xscale("log")  # Log scale for better visualization
plt.yscale("log")

plt.title("Relationship Between Employees and Revenue", fontsize=14, fontweight="bold")
plt.xlabel("Number of Employees (log scale)", fontsize=12)
plt.ylabel("Revenue (Billion USD, log scale)", fontsize=12)
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

# Add legend only if hue is used
if hue_var:
    plt.legend(title="Industry", bbox_to_anchor=(1.05, 1), loc="upper left")

plt.tight_layout()
plt.show()
