# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Fixed random seed for reproducibility
np.random.seed(0)

# Generate deterministic synthetic data
cac = np.linspace(100, 300, 100)  # evenly spaced CAC values
clv = cac * 4 + 500  # fixed linear relationship

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

# Labels and title
plt.title("Customer Lifetime Value vs. Acquisition Cost")
plt.xlabel("Customer Acquisition Cost (USD)")
plt.ylabel("Customer Lifetime Value (USD)")

# Save exactly 512x512 pixels
plt.savefig("chart.png", dpi=64)
plt.close()
