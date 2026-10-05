import numpy as np
import matplotlib.pyplot as plt

# 1. Given values
d0 = 1                  # Reference distance (m)
PL0 = 40                # Path loss at 1 m (dB)
Pr_min = -80            # Minimum received power (dBm)
n = 3                   # Path loss exponent
Pt = 35                 # Transmit power (dBm)

# 2. Calculate coverage radius
R = d0 * 10 ** ((Pt - PL0 - Pr_min) / (10 * n))

# Different cell radii
radii = [R / 2, R, R * 1.5]

# 3. Calculate effect of transmit power
power = np.arange(20, 41, 5)

radius_power = d0 * 10 ** (
    (power - PL0 - Pr_min) / (10 * n)
)

# 4. Cell splitting
R_original = R
R_split = R_original / 2

area_original = np.pi * R_original ** 2
area_split = np.pi * R_split ** 2

number_of_cells = area_original / area_split
capacity_increase = number_of_cells

# 5. Display results
print("======================================")
print("   CELL COVERAGE & CELL SPLITTING")
print("======================================")
print("Transmit Power        :", Pt, "dBm")
print("Original Radius       :", round(R_original, 2), "m")
print("Split Cell Radius     :", round(R_split, 2), "m")
print("Original Coverage     :", round(area_original, 2), "m^2")
print("Split Cell Coverage   :", round(area_split, 2), "m^2")
print("Number of Split Cells :", round(number_of_cells, 2))
print("Capacity Increase     :", round(capacity_increase, 2), "times")
print("======================================")

# 6. Plot all results together
plt.figure(figsize=(15, 5))

# --- Figure 1: Effect of Cell Radius ---
plt.subplot(1, 3, 1)

for r in radii:
    circle = plt.Circle((0, 0), r, fill=False, linewidth=2)
    plt.gca().add_patch(circle)

plt.scatter(0, 0, marker="^", s=100)
plt.text(0, 20, "Base Station", ha="center")

plt.xlim(-R * 1.7, R * 1.7)
plt.ylim(-R * 1.7, R * 1.7)
plt.xlabel("Distance (m)")
plt.ylabel("Distance (m)")
plt.title("Effect of Cell Radius")
plt.gca().set_aspect("equal")
plt.grid(True)

# --- Figure 2: Effect of Transmit Power ---
plt.subplot(1, 3, 2)

plt.plot(power, radius_power, marker="o", linewidth=2)

plt.xlabel("Transmit Power (dBm)")
plt.ylabel("Coverage Radius (m)")
plt.title("Transmit Power vs Coverage")
plt.grid(True)

# --- Figure 3: Effect of Cell Splitting ---
plt.subplot(1, 3, 3)

cells = ["Original Cell", "Split Cells"]
capacity = [1, capacity_increase]

plt.bar(cells, capacity)

plt.ylabel("Relative Capacity")
plt.title("Effect of Cell Splitting")

plt.text(
    0, 1.05,
    "1×",
    ha="center"
)

plt.text(
    1, capacity_increase + 0.1,
    f"{capacity_increase:.0f}×",
    ha="center"
)

plt.grid(axis="y")

plt.tight_layout()
plt.show()