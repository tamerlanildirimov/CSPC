import numpy as np
import matplotlib.pyplot as plt

# 1. Read trajectory.csv into time t, x, and y
data = np.loadtxt('trajectory.csv', delimiter=',', skiprows=1)
t = data[:, 0]
x = data[:, 1]
y = data[:, 2]

# 2. Compute time step dt and velocities using np.gradient
dt = t[1] - t[0]
vx = np.gradient(x, dt)
vy = np.gradient(y, dt)

# Compute speed over time: sqrt(vx^2 + vy^2)
speed = np.sqrt(vx**2 + vy**2)

# 3. Create a figure with 2 subplots: 2D path and speed over time
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Subplot 1: 2D Trajectory (x vs y)
axs[0].plot(x, y, label='Trajectory (x vs y)', color='b')
axs[0].set_title('2D Tracked Trajectory')
axs[0].set_xlabel('X Position (m)')
axs[0].set_ylabel('Y Position (m)')
axs[0].grid(True)
axs[0].legend()

# Subplot 2: Speed over time
axs[1].plot(t, speed, label='Speed', color='r')
axs[1].set_title('Speed over Time')
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('Speed (m/s)')
axs[1].grid(True)
axs[1].legend()

plt.tight_layout()
plt.savefig('trajectory_plot.png')
print("Bonus trajectory analysis completed, trajectory_plot.png saved successfully!")