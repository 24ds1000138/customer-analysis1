# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Seaborn style and context
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate realistic synthetic marketing data
np.random.seed(42)
n = 60
df = pd.DataFrame({
    "Ad_Spend_USD": np.random.uniform(1000, 10000, n),
    "Conversions": np.random.uniform(50, 500, n),
    "Channel": np.random.choice(["Social Media", "Search Engine", "Email"], n)
})

# Create a 512x512 figure
fig, ax = plt.subplots(figsize=(8, 8), dpi=64)

# Seaborn scatterplot
sns.scatterplot(
    x="Ad_Spend_USD",
    y="Conversions",
    hue="Channel",
    palette="deep",
    data=df,
    s=100,
    ax=ax
)

# Titles and labels
ax.set_title("Marketing Campaign Effectiveness", fontsize=18, fontweight="bold")
ax.set_xlabel("Ad Spend (USD)", fontsize=14)
ax.set_ylabel("Conversions", fontsize=14)

# Save exactly 512x512 pixels without altering the figure
fig.savefig("chart.png", dpi=64)
plt.close(fig)
