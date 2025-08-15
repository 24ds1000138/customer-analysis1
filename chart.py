# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Example dataset
df = pd.DataFrame({
    "x": [1, 2, 3, 4, 5, 6],
    "y": [2, 4, 1, 8, 7, 3]
})

# Create seaborn scatterplot
sns.scatterplot(x="x", y="y", data=df)

# Ensure exact 512x512 pixels at 100 DPI
plt.gcf().set_size_inches(512/100, 512/100)

# Save chart
plt.savefig("chart.png", dpi=100)
