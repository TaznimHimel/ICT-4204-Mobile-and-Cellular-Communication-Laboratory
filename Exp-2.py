import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------
# 1. Given values
# ---------------------------------
R = 1                 # Cell radius (km)
n = 4                 # Path loss exponent
i0 = 6                # Number of interferers

N = np.array([1, 3, 4, 7, 9, 12])


# ---------------------------------
# 2. Reuse Distance and Reuse Ratio
# ---------------------------------
D = R * np.sqrt(3 * N)
Q = D / R


# ---------------------------------
# 3. Co-channel Interference
# ---------------------------------
CI = (Q ** n) / i0
CI_dB = 10 * np.log10(CI)


# ---------------------------------
# 4. Display results
# ---------------------------------
print("\n==============================================")
print("     CO-CHANNEL REUSE CALCULATION")
print("==============================================")

print("Cell Radius =", R, "km")
print("\nN\tD (km)\t\tQ\tC/I (dB)")
print("----------------------------------------------")

for i in range(len(N)):
    print(f"{N[i]}\t{D[i]:.2f}\t\t{Q[i]:.2f}\t{CI_dB[i]:.2f}")

print("\nConclusion:")
print("N increases  ->  Reuse Distance increases")
print("N increases  ->  C/I increases")
print("Higher C/I   ->  Lower co-channel interference")

print("==============================================\n")


# ---------------------------------
# 5. Plot both graphs side by side
# ---------------------------------
plt.figure(figsize=(12, 5))


# ---- Graph 1: Reuse Distance ----
plt.subplot(1, 2, 1)

plt.plot(N, D, marker='o', linewidth=2)

for x, y in zip(N, D):
    plt.text(x, y + 0.15, f"{y:.2f}", ha='center')

plt.xlabel("Cluster Size (N)")
plt.ylabel("Reuse Distance D (km)")
plt.title("Reuse Distance vs Cluster Size")
plt.grid(True)


# ---- Graph 2: C/I ----
plt.subplot(1, 2, 2)

plt.plot(N, CI_dB, marker='o', linewidth=2)

for x, y in zip(N, CI_dB):
    plt.text(x, y + 0.5, f"{y:.1f}", ha='center')

plt.xlabel("Cluster Size (N)")
plt.ylabel("C/I (dB)")
plt.title("Co-channel Interference vs Cluster Size")
plt.grid(True)


plt.tight_layout()
plt.show()