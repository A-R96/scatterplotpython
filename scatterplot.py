import matplotlib.pyplot as plt

# Data
years = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
rates = [0.94, 0.88, 0.97, 1.01, 1.00, 0.97, 0.91, 0.78, 0.77, 0.77, 0.77]

# Setting the style
plt.style.use("seaborn-v0_8-muted")

# Create the figure
plt.figure(figsize=(10, 6))


plt.scatter(
    years,
    rates,
    color="#db714a",
    s=100,
    marker="o",
    edgecolor="white",
    linewidth=1.5,
    zorder=3,
)

# Adding a line to show the trend
plt.plot(years, rates, color="#db714a", alpha=0.3, linestyle="-", linewidth=2, zorder=2)

# Add the Title and Labels
plt.title(
    "Annual Exchange Rate Trends (2008–2018)", fontsize=16, fontweight="bold", pad=20
)
plt.xlabel("Year", fontsize=12, fontweight="semibold")
plt.ylabel("Exchange Rate (USD/CAD)", fontsize=12, fontweight="semibold")


# Add Grid Background
plt.grid(True, which="major", linestyle="--", linewidth=0.5, color="gray", alpha=0.5)

# Formatting Ticks
plt.xticks(years)
plt.ylim(0.7, 1.1)

# Clean up layout and save
plt.tight_layout()
plt.savefig("styled_scatter_plot.png", dpi=500)
plt.show()
