import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# --- Part 3: Fit a reaction rate ---
# Read data from kinetics.csv
data = np.loadtxt('kinetics.csv', delimiter=',', skiprows=1)
time = data[:, 0]
concentration = data[:, 1]

# Set C0 to the first concentration value
C0 = concentration[0]

# Define the total error function (sum of squared residuals)
def total_error(k_val):
    model = C0 * np.exp(-k_val * time)
    return np.sum((concentration - model)**2)

# Minimize the error using SLSQP, bounds=[(0, 5)], initial guess x0=0.5
result = minimize(total_error, x0=[0.5], method='SLSQP', bounds=[(0, 5)])
fitted_k = result.x[0]

print(f"Fitted rate constant k: {fitted_k:.4f}")

# Plot the measured data and the fitted curve
plt.figure(figsize=(8, 5))
plt.scatter(time, concentration, color='red', label='Measured Data (Noisy)')

t_smooth = np.linspace(time[0], time[-1], 200)
c_smooth = C0 * np.exp(-fitted_k * t_smooth)
plt.plot(t_smooth, c_smooth, color='blue', label=f'Fitted Curve (k = {fitted_k:.4f})')

plt.xlabel('Time')
plt.ylabel('Concentration')
plt.title('Reaction Rate Fitting (First-Order Kinetics)')
plt.legend()
plt.grid(True)
plt.savefig('kinetics.png')
print("Plot saved successfully as kinetics.png")