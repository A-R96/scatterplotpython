import matplotlib.pyplot as plt

# Raw Sales and Profit data
sales_raw = [195, 205, 225, 4240, 255, 300, 265, 345, 295, 335, 380, 405, 355, 390, 410]
profit_raw = [10, 15, 22, -10, 25, 39, 25, 55, 32, 37, 48, 55, 50, 48, 55]

# Sort both lists together by sales value (smallest to largest)
sorted_pairs = sorted(zip(sales_raw, profit_raw), key=lambda pair: pair[0])
sales = [pair[0] for pair in sorted_pairs]
profit = [pair[1] for pair in sorted_pairs]

# Sum of the profit column
profit_sum = sum(profit)
print(f"Sum of Profit: {profit_sum} (thousands)")

# Print the sorted table for reference
print(f"\n{'Sales ($000s)':<20} {'Profit ($000s)'}")
print("-" * 36)
for s, p in sorted_pairs:
    print(f"{s:<20} {p}")
print("-" * 36)
print(f"{'Sum:':<20} {profit_sum}")

plt.style.use("seaborn-v0_8-muted")
plt.figure(figsize=(10, 6))

plt.scatter(
    sales,
    profit,
    color="#db714a",
    s=100,
    marker="o",
    edgecolor="white",
    linewidth=1.5,
    zorder=3,
)

plt.title(
    "Sales vs. Profit",
    fontsize=16,
    fontweight="bold",
    pad=20,
)
plt.xlabel("Sales ($ thousands)", fontsize=12, fontweight="semibold")
plt.ylabel("Profit ($ thousands)", fontsize=12, fontweight="semibold")

plt.grid(True, which="major", linestyle="--", linewidth=0.5, color="gray", alpha=0.5)

plt.tight_layout()
plt.savefig("question19_scatter_plot.png", dpi=500)
plt.show()
