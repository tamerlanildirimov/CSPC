import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
# (hint: np.loadtxt with a comma delimiter, skipping the header)
data = np.loadtxt('freefall.csv', delimiter=',', skiprows=1)
t = data[:, 0]
y = data[:, 1]

# TODO 2: compute velocity v = derivative of y w.r.t. t (np.gradient)
# and acceleration a = derivative of v w.r.t. t (np.gradient again)
# Print the mean acceleration. Is it close to -9.81? Is it noisy?
dt = t[1] - t[0]
v = np.gradient(y, dt)
a = np.gradient(v, dt)

mean_acc = np.mean(a)
print(f"Mean acceleration: {mean_acc:.2f}")

# TODO 3: integrate a back up to recover velocity and position
# (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]

# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
# vs time. Mark the true -9.81 line on the acceleration panel.
# Save it as motion.png
fig, axs = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

axs[0].plot(t, y, label='Original Position', color='blue')
axs[0].plot(t, y_rec, '--', label='Recovered Position', color='orange')
axs[0].set_ylabel('Position (m)')
axs[0].legend()
axs[0].grid(True)

axs[1].plot(t, v, label='Velocity (from gradient)', color='green')
axs[1].plot(t, v_rec, '--', label='Recovered Velocity', color='purple')
axs[1].set_ylabel('Velocity (m/s)')
axs[1].legend()
axs[1].grid(True)

axs[2].plot(t, a, label='Acceleration', color='red')
axs[2].axhline(-9.81, color='black', linestyle=':', label='True g (-9.81)')
axs[2].set_ylabel('Acceleration (m/s^2)')
axs[2].set_xlabel('Time (s)')
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.savefig('motion.png')
print("Script has been completed!")