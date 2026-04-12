import matplotlib.pyplot as plt
import numpy as np

# Data (Updated for Maximum Heart Rate question)
age = [20, 25, 30]
heart_rate = [206, 200, 194]


# Find the R-value for part b correlation coefficient
r = np.corrcoef(age, heart_rate)[0, 1]
print(f"Correlation Coefficient (r): {r}")

# Calculate Line of Best Fit (Linear Regression)
m, b = np.polyfit(age, heart_rate, 1)

# Create the equation string
# Using 1 decimal place here as the data is clean integers
equation = f"y = {m:.1f}x + {b:.1f}"
print(f"The equation of the line of best fit is: {equation}")

# Create the y-values for the line of best fit
line_of_best_fit = [m * x + b for x in age]

plt.style.use("seaborn-v0_8-muted")
plt.figure(figsize=(10, 6))

# Scatter plot of array data
plt.scatter(
    age,
    heart_rate,
    color="#db714a",
    s=100,
    label="Data Points",
    edgecolor="white",
    zorder=3,
)

# Plot the Line of Best Fit
plt.plot(
    age,
    line_of_best_fit,
    color="royalblue",
    linewidth=2,
    label=f"Line of Best Fit: {equation}",
    zorder=2,
)

plt.title("Maximum Heart Rate vs Age", fontsize=16, fontweight="bold", pad=20)
plt.xlabel("Age (years)", fontsize=12)
plt.ylabel("Maximum Heart Rate (beats/min)", fontsize=12)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.xticks(age)
plt.ylim(190, 210)  # Adjusted for better heart rate visibility

plt.tight_layout()
plt.show()
