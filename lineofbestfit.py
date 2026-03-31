import matplotlib.pyplot as plt
import numpy as np

# Data
years = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
rates = [0.94, 0.88, 0.97, 1.01, 1.00, 0.97, 0.91, 0.78, 0.77, 0.77, 0.77]

# Calculate Line of Best Fit (Linear Regression)
# np.polyfit(x, y, degree). Degree 1 means linear.
m, b = np.polyfit(years, rates, 1)

# Create the equation string
equation = f"y = {m:.4f}x + {abs(b):.4f}"
print(f"The equation of the line of best fit is: {equation}")

# Create the y-values for the line of best fit
line_of_best_fit = [m * x + b for x in years]
# -----------------------------------------------------------

plt.style.use("seaborn-v0_8-muted")
plt.figure(figsize=(10, 6))

# Scatter plot of array data
plt.scatter(
    years,
    rates,
    color="#db714a",
    s=100,
    label="Data Points",
    edgecolor="white",
    zorder=3,
)

# Plot the Line of Best Fit
plt.plot(
    years,
    line_of_best_fit,
    color="royalblue",
    linewidth=2,
    label=f"Line of Best Fit: {equation}",
    zorder=2,
)

plt.title(
    "Exchange Rate Trends with Line of Best Fit", fontsize=16, fontweight="bold", pad=20
)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Exchange Rate (USD/CAD)", fontsize=12)
plt.legend()  # Shows the equation on the graph
plt.grid(True, linestyle="--", alpha=0.5)
plt.xticks(years)
plt.ylim(0.7, 1.1)

plt.tight_layout()
plt.show()
