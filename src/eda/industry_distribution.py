import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/internet_companies.csv")

# Count companies per industry
industry_counts = df["Industry"].value_counts()

# Group small industries into "Other"
threshold = 10  # Industries with less than 10 companies will be grouped
small_industries = industry_counts[industry_counts < threshold]
industry_counts_filtered = industry_counts[industry_counts >= threshold]
industry_counts_filtered["Other"] = small_industries.sum()

# Print the industries included in "Other"
print("Industries grouped under 'Other':")
for industry in small_industries.index:
    print(f"- {industry}")

# Pie chart
fig, ax = plt.subplots(figsize=(10, 8))
colors = plt.cm.Paired.colors
explode = [0.05] * len(industry_counts_filtered)

# Plot the pie chart
wedges, texts, autotexts = ax.pie(
    industry_counts_filtered,
    labels=industry_counts_filtered.index,
    autopct='%1.1f%%',
    startangle=140,
    shadow=True,
    colors=colors,
    explode=explode,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1},
    textprops={'fontsize': 12, 'fontweight': 'bold'}  # Make pie chart labels bold
)

# Improve percentage readability inside the wedges
for autotext in autotexts:
    autotext.set_fontsize(12)
    autotext.set_fontweight('bold')

# Add a legend for the industries grouped under "Other"
if not small_industries.empty:
    other_industries = [f"{industry} ({count})" for industry, count in small_industries.items()]
    ax.legend(
        other_industries,
        title="Industries in 'Other'",
        loc="center left",
        bbox_to_anchor=(1.1, 0.5),
        fontsize=10,
        title_fontsize=12,
        prop={'weight': 'bold'}  # Make legend text bold
    )

# Title and layout adjustments
ax.set_title("Industry Distribution of Internet Companies", fontsize=16, fontweight="bold")
plt.tight_layout()  # Ensure everything fits properly

# Show the plot
plt.show()
