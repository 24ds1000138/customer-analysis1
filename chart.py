# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- Data Generation ---
np.random.seed(42)

# Simulate Customer Acquisition Cost (CAC) in USD
cac = np.random.normal(loc=200, scale=50, size=100)  # Average CAC = $200

# Simulate Customer Lifetime Value (CLV) in USD, generally correlated with CAC
clv = cac * np.random.uniform(3, 6, size=100) + np.random.normal(0, 200, size=100)

# Create DataFrame
df = pd.DataFrame({
    "Customer Acquisition Cost (USD)": cac,
    "Customer Lifetime Value (USD)": clv
})

# --- Visualization ---
sns.set_style("whitegrid")
sns.set_context("talk")  # Presentation-ready font sizes

plt.figure(figsize=(8, 8))  # 8 inches * 64 dpi = 512 pixels

# Scatterplot with professional styling
sns.scatterplot(
    data=df,
    x="Customer Acquisition Cost (USD)",
    y="Customer Lifetime Value (USD)",
    palette="viridis",
    hue="Customer Acquisition Cost (USD)",  # Optional: color gradient
    size="Customer Lifetime Value (USD)",
    sizes=(50, 200),
    alpha=0.8,
    edgecolor="w",
    linewidth=0.5
)

# Titles & Labels
plt.title("Customer Lifetime Value vs. Acquisition Cost", fontsize=18, fontweight='bold')
plt.xlabel("Customer Acquisition Cost (USD)", fontsize=14)
plt.ylabel("Customer Lifetime Value (USD)", fontsize=14)

# Tight layout for better spacing
plt.tight_layout()

# Save chart exactly 512x512 pixels
plt.savefig("chart.png", dpi=64, bbox_inches='tight')
plt.close()
