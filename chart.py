import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set Seaborn style and context for a professional look
sns.set_theme(style="whitegrid", palette="pastel")
sns.set_context("notebook", font_scale=1.2)

# --- Data Generation ---
# Create synthetic data for customer acquisition cost and lifetime value
np.random.seed(42)  # for reproducibility
num_campaigns = 50

# Generate acquisition costs
acquisition_cost = np.random.uniform(5, 50, num_campaigns)

# Generate lifetime values
# Lifetime value is generally higher for campaigns with lower acquisition costs, but with noise
lifetime_value = 150 - 2 * acquisition_cost + np.random.normal(0, 20, num_campaigns)

# Ensure lifetime values are positive
lifetime_value = np.maximum(5, lifetime_value)

# Create a DataFrame
data = pd.DataFrame({
    'Customer Acquisition Cost': acquisition_cost,
    'Customer Lifetime Value': lifetime_value
})

# --- Visualization ---
# Create a figure with a specific size for the desired output dimensions
plt.figure(figsize=(8, 8))

# Create the scatterplot
ax = sns.scatterplot(
    data=data,
    x='Customer Acquisition Cost',
    y='Customer Lifetime Value',
    s=150,  # Size of the markers
    edgecolor='w',
    linewidth=1.5,
    alpha=0.8
)

# Add a title and labels
plt.title(
    'Customer Acquisition Cost vs. Lifetime Value',
    fontsize=16,
    fontweight='bold',
    pad=20
)
plt.xlabel('Customer Acquisition Cost ($)', fontsize=12)
plt.ylabel('Customer Lifetime Value ($)', fontsize=12)

# Add a line showing a hypothetical break-even point or trend line
# This adds a critical business insight
x_vals = np.array(ax.get_xlim())
y_vals = x_vals
plt.plot(x_vals, y_vals, color='red', linestyle='--', linewidth=2, label='Break-Even Point (LTV = CAC)')
plt.legend()

# Add a subtle grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Improve layout
plt.tight_layout()

# --- Export the chart ---
# Save the figure as a PNG with 512x512 pixel dimensions
# The `dpi=64` and `figsize=(8, 8)` combination achieves the target size (8 * 64 = 512)
plt.savefig('chart.png', dpi=64)

print("Chart successfully created and saved as chart.png")