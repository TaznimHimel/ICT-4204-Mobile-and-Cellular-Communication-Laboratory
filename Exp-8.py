import numpy as np
import matplotlib.pyplot as plt

# ১. Given (দেওয়া মান)
PL0, Pmin, n = 40, -80, 3
radius = lambda Pt: 10 ** ((Pt - PL0 - Pmin) / (10 * n))   # d0 = 1 m

# ২. Calculate (হিসাব)
R = radius(35)                 # coverage radius
R2 = R / 2                     # split cell radius
cells = (R / R2) ** 2          # radius অর্ধেক -> 4টি cell
power = np.arange(20, 41, 5)

print(f"Radius: {R:.2f} m | Split radius: {R2:.2f} m | Capacity: {cells:.0f}x")

# ৩. Plot (আঁকা)
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("Cell Coverage & Cell Splitting", fontsize=16, weight="bold")

# Graph 1: Cell radius
for r, c, name in zip([R/2, R, 1.5*R], ["green", "blue", "red"], ["R/2", "R", "1.5R"]):
    ax[0].add_patch(plt.Circle((0, 0), r, fill=False, color=c, lw=2, label=name))
ax[0].plot(0, 0, "k^", ms=12)
ax[0].set(xlim=(-R*1.7, R*1.7), ylim=(-R*1.7, R*1.7), title="Effect of Cell Radius")
ax[0].set_aspect("equal"); ax[0].legend(); ax[0].grid(alpha=.3)

# Graph 2: Power vs radius
ax[1].plot(power, radius(power), "o-", c="purple", lw=2)
ax[1].set(xlabel="Transmit Power (dBm)", ylabel="Radius (m)", title="Power vs Coverage")
ax[1].grid(alpha=.3)

# Graph 3: Cell splitting
bars = ax[2].bar(["Original", "Split"], [1, cells], color=["tab:blue", "tab:green"])
ax[2].bar_label(bars, fmt="%.0f×", fontsize=13)
ax[2].set(ylabel="Relative Capacity", title="Effect of Cell Splitting")

plt.tight_layout(); plt.show()