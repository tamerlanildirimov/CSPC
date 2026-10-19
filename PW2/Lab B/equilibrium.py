import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize, newton

# --- Part 4: Chemical equilibrium ---
# Reaction: H2 + I2 <=> 2HI, K = 16.0 (matching lab check: x ≈ 0.66, HI ≈ 1.33 mol)
K = 16.0

def k_imbalance(x):
    if x <= 0.0:
        return -K
    if x >= 1.0:
        return 1e6
    return ((2 * x)**2) / ((1 - x)**2) - K

def k_imbalance_prime(x):
    # Derivative of k_imbalance with respect to x for Newton's method
    return (8 * x * (1 - x)**2 + 8 * (x**2) * (1 - x)) / ((1 - x)**4)

# 1. Solve using scipy.optimize.newton with fprime
x_newton = newton(k_imbalance, x0=0.5, fprime=k_imbalance_prime)

# 2. Solve using minimize with SLSQP to confirm
res_slsqp = minimize(lambda x: k_imbalance(x[0])**2, x0=[0.5], method='SLSQP', bounds=[(0.01, 0.99)])
x_slsqp = res_slsqp.x[0]

print(f"Equilibrium extent x (Newton): {x_newton:.4f}")
print(f"Equilibrium extent x (SLSQP):  {x_slsqp:.4f}")

# Calculate equilibrium amounts for H2, I2, HI
h2_eq = 1.0 - x_newton
i2_eq = 1.0 - x_newton
hi_eq = 2.0 * x_newton

print(f"Equilibrium composition:")
print(f"  [H2] = {h2_eq:.4f} mol")
print(f"  [I2] = {i2_eq:.4f} mol")
print(f"  [HI] = {hi_eq:.4f} mol")

# Plot how H2, I2, HI change with x
x_vals = np.linspace(0.0, 0.99, 200)
h2_vals = 1.0 - x_vals
i2_vals = 1.0 - x_vals
hi_vals = 2.0 * x_vals

plt.figure(figsize=(8, 5))
plt.plot(x_vals, h2_vals, label='H2', color='blue')
plt.plot(x_vals, i2_vals, label='I2', color='green', linestyle='--')
plt.plot(x_vals, hi_vals, label='HI', color='red')

# Mark the equilibrium point
plt.axvline(x_newton, color='purple', linestyle=':', label=f'Equilibrium x ≈ {x_newton:.2f}')
plt.scatter([x_newton, x_newton, x_newton], [1.0 - x_newton, 1.0 - x_newton, 2.0 * x_newton], color='purple')

plt.xlabel('Reaction Extent (x)')
plt.ylabel('Amount (moles)')
plt.title('Chemical Equilibrium: H2 + I2 <=> 2HI')
plt.legend()
plt.grid(True)
plt.savefig('equilibrium.png')
print("Plot saved successfully as equilibrium.png")