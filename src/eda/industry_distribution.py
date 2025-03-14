import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/internet_companies.csv")

# Count companies per industry
industry_counts = df["Industry"].value_counts()

# Pie chart
plt.figure(figsize=(8, 8))
industry_counts.plot.pie(autopct='%1.1f%%', cmap='coolwarm', startangle=90, shadow=True)
plt.title("Industry Distribution of Internet Companies")
plt.axis("equal")  # Ensure it's a circle
plt.ylabel("")  # Remove label
plt.show()
