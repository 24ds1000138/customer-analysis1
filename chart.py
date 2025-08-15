# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style and context for presentation
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

# Create the scatterplot
plt.figure(figsize=(8, 8), dpi=64)  # Exactly 512x512 pixels
sns.scatterplot(
    data=df,
    x="Ad_Spend_USD",
    y="Conversions",
    hue="Channel",
    palette="Set2",
    s=100,
    edgecolor="black"
)

# Add title and labels
plt.title("Marketing Campaign Effectiveness", fontsize=18, fontweight='bold')
plt.xlabel("Ad Spend (USD)", fontsize=14)
plt.ylabel("Conversions", fontsize=14)

# Save chart without trimming — ensures exact size
plt.savefig("chart.png", dpi=64)
plt.close()
