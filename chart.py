# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Fixed random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
cac = np.random.normal(loc=200, scale=50, size=100)
clv = cac * 4 + np.random.normal(0, 200, size=100)  # simple linear relationship

df = pd.DataFrame({
    "Customer Acquisition Cost (USD)": cac,
    "Customer Lifetime Value (USD)": clv
})

# Seaborn styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Create figure exactly 512x512 pixels
plt.figure(figsize=(8, 8))

# Simple scatterplot
sns.scatterplot(
    data=df,
    x="Customer Acquisition Cost (USD)",
    y="Customer Lifetime Value (USD)"
)

# Titles and labels
plt.title("Customer Lifetime Value vs. Acquisition Cost")
plt.xlabel("Customer Acquisition Cost (USD)")
plt.ylabel("Customer Lifetime Value (USD)")

# Save without bbox_inches to preserve size
plt.savefig("chart.png", dpi=64)
plt.close()
