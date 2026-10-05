import numpy as np
import matplotlib.pyplot as plt

# 1. Given values
c = 3e8                  # Speed of light (m/s)
fc = 900e6               # Carrier frequency (Hz)
v = 30                   # Mobile velocity (m/s)
theta = 0                # Direction angle (degree)
fd_max = 100             # Maximum Doppler frequency (Hz)

# 2. Calculate Doppler Shift
fd = (v * fc / c) * np.cos(np.radians(theta))

# 3. Calculate Maximum Mobile Velocity
v_max = (fd_max * c) / fc

# 4. Display results
print("======================================")
print("       DOPPLER SHIFT SIMULATION")
print("======================================")
print("Carrier Frequency :", fc / 1e6, "MHz")
print("Mobile Velocity   :", v, "m/s")
print("Direction Angle   :", theta, "degree")
print("--------------------------------------")
print("Doppler Frequency :", round(fd, 2), "Hz")
print("Maximum Velocity  :", round(v_max, 2), "m/s")
print("Maximum Velocity  :", round(v_max * 3.6, 2), "km/h")
print("======================================")

# 5. Effect of Carrier Frequency
frequencies = np.array([900e6, 1800e6, 2100e6, 2600e6])
doppler_fc = (v * frequencies / c) * np.cos(np.radians(theta))

# 6. Effect of Direction
angles = np.arange(0, 181, 10)
doppler_angle = (v * fc / c) * np.cos(np.radians(angles))

# 7. Plot both figures together
plt.figure(figsize=(12, 5))

# Figure 1
plt.subplot(1, 2, 1)
plt.plot(frequencies / 1e6, doppler_fc, marker='o')
plt.xlabel("Carrier Frequency (MHz)")
plt.ylabel("Doppler Frequency (Hz)")
plt.title("Effect of Carrier Frequency")
plt.grid(True)

# Figure 2
plt.subplot(1, 2, 2)
plt.plot(angles, doppler_angle, marker='o')
plt.xlabel("Direction Angle (degree)")
plt.ylabel("Doppler Frequency (Hz)")
plt.title("Effect of Movement Direction")
plt.axhline(0, linestyle='--')
plt.grid(True)

plt.tight_layout()
plt.show()