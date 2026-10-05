import numpy as np
import matplotlib.pyplot as plt

# 1. Base Station position
BS1 = 0
BS2 = 1000

# 2. Mobile moves from Cell 1 to Cell 2
x = np.arange(1, 1000)

# 3. Distance from each Base Station
d1 = abs(x - BS1)
d2 = abs(x - BS2)

# 4. Received Signal Strength (RSS)
Pt = 40
PL0 = 40
n = 3

RSS1 = Pt - PL0 - 10 * n * np.log10(d1)
RSS2 = Pt - PL0 - 10 * n * np.log10(d2)

# 5. Find handover point
i = np.argmin(abs(RSS1 - RSS2))
handover = x[i]

# 6. Display result
print("===================================")
print("   HANDOVER SIMULATION")
print("===================================")
print("Mobile moves : Cell 1 -> Cell 2")
print("Handover Point :", handover, "meters")
print("RSS at Handover:")
print("Cell 1 :", round(RSS1[i], 2), "dBm")
print("Cell 2 :", round(RSS2[i], 2), "dBm")
print("===================================")

# 7. Plot
plt.figure(figsize=(10, 6))

plt.plot(x, RSS1, label="Cell 1 RSS", linewidth=2)
plt.plot(x, RSS2, label="Cell 2 RSS", linewidth=2)

# Mark handover point
plt.scatter(handover, RSS1[i], s=100, label="Handover Point")
plt.axvline(handover, linestyle="--", linewidth=2)

# Show Base Stations
plt.scatter(BS1, -45, s=120, marker="^", label="Base Station 1")
plt.scatter(BS2, -45, s=120, marker="^", label="Base Station 2")

# Write handover text
plt.annotate(
    f"HANDOVER\n{handover} m",
    xy=(handover, RSS1[i]),
    xytext=(handover + 80, RSS1[i] + 15),
    arrowprops=dict(arrowstyle="->"),
    fontsize=11
)

plt.xlabel("Mobile Position (meter)")
plt.ylabel("Received Signal Strength (dBm)")
plt.title("Handover Between Two Cellular Cells")

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()