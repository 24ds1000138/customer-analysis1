# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Seaborn style
sns.set_style("whitegrid")

# Synthetic data
np.random.seed(42)
df = pd.DataFrame({
    "Ad_Spend_USD": np.random.uniform(1000, 10000, 50),
    "Conversions": np.random.uniform(50, 500, 50)
})

# Create figure 512x512 px
fig, ax = plt.subplots(figsize=(8, 8), dpi=64)

# Simple scatterplot (no hue, default palette)
sns.scatterplot(x="Ad_Spend_USD", y="Conversions", data=df, ax=ax)

# Titles and labels
ax.set_title("Marketing Campaign Effectiveness")
ax.set_xlabel("Ad Spend (USD)")
ax.set_ylabel("Conversions")

# Save exact 512x512 image
fig.savefig("chart.png", dpi=64)
plt.close(fig)
