# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data Generation
np.random.seed(42)
cac = np.random.normal(loc=200, scale=50, size=100)
clv = cac * np.random.uniform(3, 6, size=100) + np.random.normal(0, 200, size=100)

df = pd.DataFrame({
    "Customer Acquisition Cost (USD)": cac,
    "Customer Lifetime Value (USD)": clv
})

# Seaborn Styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Figure Size = 512x512 pixels
plt.figure(figsize=(8, 8))

# Basic Seaborn scatterplot
sns.scatterplot(
    data=df,
    x="Customer Acquisition Cost (USD)",
    y="Customer Lifetime Value (USD)"
)

# Labels and title
plt.title("Customer Lifetime Value vs. Acquisition Cost")
plt.xlabel("Customer Acquisition Cost (USD)")
plt.ylabel("Customer Lifetime Value (USD)")

# Save exactly 512x512 pixels
plt.savefig("chart.png", dpi=64)
plt.close()
