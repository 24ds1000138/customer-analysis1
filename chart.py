# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Seaborn styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic marketing campaign effectiveness data
np.random.seed(42)
n = 60
df = pd.DataFrame({
    "Ad_Spend_USD": np.random.uniform(1000, 10000, n),
    "Conversions": np.random.uniform(50, 500, n),
    "Channel": np.random.choice(["Social Media", "Search Engine", "Email"], n)
})

# Create figure exactly 512x512 px
fig, ax = plt.subplots(figsize=(8, 8), dpi=64)

# Seaborn scatterplot
sns.scatterplot(
    data=df,
    x="Ad_Spend_USD",
    y="Conversions",
    hue="Channel",
    palette="deep",
    s=100,
    ax=ax
)

# Labels & title
ax.set_title("Marketing Campaign Effectiveness", fontsize=18, fontweight='bold')
ax.set_xlabel("Ad Spend (USD)", fontsize=14)
ax.set_ylabel("Conversions", fontsize=14)

# Save WITHOUT 'tight' to keep exact size
plt.savefig("chart.png", dpi=64)
plt.close(fig)
