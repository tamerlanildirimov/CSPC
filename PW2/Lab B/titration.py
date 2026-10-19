import numpy as np
import matplotlib.pyplot as plt

# Read titration.csv (volume_base, pH)
data = np.loadtxt('titration.csv', delimiter=',', skiprows=1)
V = data[:, 0]
pH = data[:, 1]

# Compute the slope with np.gradient(pH, V)
slope = np.gradient(pH, V)

# Find the volume where the slope is largest (np.argmax)
max_index = np.argmax(slope)
equivalence_volume = V[max_index]

print(f"Equivalence point volume: {equivalence_volume}")

# Make two plots side by side: the pH curve, and its slope
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(V, pH, label='pH curve', color='blue')
ax1.set_xlabel('Volume Base (mL)')
ax1.set_ylabel('pH')
ax1.set_title('Titration Curve')
ax1.legend()
ax1.grid(True)

ax2.plot(V, slope, label='Slope (dpH/dV)', color='orange')
ax2.set_xlabel('Volume Base (mL)')
ax2.set_ylabel('Slope')
ax2.set_title('pH Slope (Equivalence Point)')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig('titration.png')