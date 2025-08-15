import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set professional styling for the plot
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate realistic synthetic data
np.random.seed(42)
num_customers = 200
cac = np.random.uniform(5, 50, num_customers)
clv = 2 * cac + np.random.normal(0, 15, num_customers)
clv[clv < 0] = np.random.uniform(5, 20, np.sum(clv < 0))
campaigns = np.random.choice(['Campaign A', 'Campaign B', 'Campaign C'], num_customers)
data = pd.DataFrame({
    'customer_acquisition_cost': cac,
    'customer_lifetime_value': clv,
    'marketing_campaign': campaigns
})

# Create the scatter plot
plt.figure(figsize=(8, 8))
scatter_plot = sns.scatterplot(
    data=data,
    x='customer_acquisition_cost',
    y='customer_lifetime_value',
    hue='marketing_campaign',
    palette='viridis',
    s=100,
    edgecolor='black',
    alpha=0.8
)

# Add titles and labels for professional appearance
plt.title("Customer Lifetime Value vs. Acquisition Cost", fontsize=20, fontweight='bold', pad=20)
plt.xlabel("Customer Acquisition Cost ($)", fontsize=14)
plt.ylabel("Customer Lifetime Value ($)", fontsize=14)
plt.legend(title='Marketing Campaign')

# Add a reference line for visual insight
x_values = np.linspace(5, 50, 100)
plt.plot(x_values, 2 * x_values, 'r--', label='CLV = 2 x CAC')
plt.legend(title='Marketing Campaign', loc='upper left')

# Adjust layout to prevent clipping
plt.tight_layout()

# Save the chart as a PNG with 512x512 pixel dimensions
# Remove bbox_inches='tight' to prevent resizing
plt.savefig('chart.png', dpi=64)

# Show the plot to ensure it is finalized
plt.show()