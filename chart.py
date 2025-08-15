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

# Create a 512x512 figure
fig, ax = plt.subplots(figsize=(8, 8), dpi=64)

# Seaborn scatterplot
sns.scatterplot(
    data=df,
    x="Ad_Spend_USD",
    y="Conversions",
    hue="Channel",
    palette="deep",  # standard seaborn palette
    s=100
)

# Labels & title
plt.title("Marketing Campaign Effectiveness", fontsize=18, fontweight='bold')
plt.xlabel("Ad Spend (USD)", fontsize=14)
plt.ylabel("Conversions", fontsize=14)

# Force figure size
fig.set_size_inches(8, 8, forward=True)

# Save EXACT 512×512 image
plt.savefig("chart.png", dpi=64, pad_inches=0)
plt.close(fig)
