# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Seaborn style & context
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic marketing campaign effectiveness data
np.random.seed(42)
n = 50
df = pd.DataFrame({
    "Ad_Spend_USD": np.random.uniform(1000, 10000, n),
    "Conversions": np.random.uniform(50, 500, n) + np.random.normal(0, 20, n),
    "Channel": np.random.choice(["Social Media", "Search Engine", "Email"], n)
})

# Create figure & scatterplot
fig, ax = plt.subplots(figsize=(8, 8), dpi=64)  # 8 in × 64 dpi = 512 px
sns.scatterplot(
    data=df,
    x="Ad_Spend_USD",
    y="Conversions",
    hue="Channel",
    palette="Set2",
    s=100,
    edgecolor="black",
    ax=ax
)

# Labels & title
ax.set_title("Marketing Campaign Effectiveness", fontsize=18, fontweight='bold')
ax.set_xlabel("Ad Spend (USD)", fontsize=14)
ax.set_ylabel("Conversions", fontsize=14)

# Force figure size before saving
fig.set_size_inches(8, 8, forward=True)

# Save EXACT 512×512 image
fig.savefig("chart.png", dpi=64, pad_inches=0)  # no bbox_inches, no tight layout
plt.close(fig)
