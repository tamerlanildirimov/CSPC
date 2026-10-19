import numpy as np
from scipy.optimize import minimize, newton

# --- Part 2A: Easy convex function ---
# Function: f(x) = (x - 3)^2 + 1, derivative: f'(x) = 2(x - 3)
def f(x):
    return (x - 3)**2 + 1

def f_prime(x):
    return 2 * (x - 3)

print("--- 2A. Easy function f(x) = (x - 3)^2 + 1 (starting from x0 = 0) ---")

# 1. Gradient descent by hand
x = 0.0
lr = 0.1  # learning rate
for _ in range(50):
    x = x - lr * f_prime(x)
print(f"1. Gradient descent: x ≈ {x:.4f}")

# 2. Newton's method via scipy.optimize.newton for f'(x) = 0
x_newton = newton(f_prime, x0=0.0)
print(f"2. Newton's method:  x ≈ {x_newton:.4f}")

# 3. SLSQP via scipy.optimize.minimize
res_slsqp = minimize(f, x0=0.0, method="SLSQP")
print(f"3. SLSQP:          x ≈ {res_slsqp.x[0]:.4f}")


# --- Part 2B: Harder landscape ---
# Function: g(x) = x^4 - 3x^2 + x + 5
# Derivative: g'(x) = 4x^3 - 6x + 1
# Second derivative: g''(x) = 12x^2 - 6
def g(x):
    return x**4 - 3*x**2 + x + 5

def g_prime(x):
    return 4*x**3 - 6*x + 1

def g_prime2(x):
    return 12*x**2 - 6

print("\n--- 2B. Harder landscape g(x) = x^4 - 3x^2 + x + 5 ---")

for x0 in [0.0, 2.0]:
    print(f"\nStarting point x0 = {x0}:")
    
    # 1. Gradient descent by hand for g(x)
    x_gd = x0
    for _ in range(100):
        x_gd = x_gd - 0.05 * g_prime(x_gd)
    print(f"  - Gradient descent: x ≈ {x_gd:.4f}, g(x) = {g(x_gd):.4f}")
    
    # 2. Newton's method for g'(x) = 0
    try:
        x_n = newton(g_prime, x0=x0)
        curvature = g_prime2(x_n)
        point_type = "minimum" if curvature > 0 else "maximum / saddle"
        print(f"  - Newton's method:  x ≈ {x_n:.4f}, g''(x) = {curvature:.2f} ({point_type})")
    except RuntimeError:
        print("  - Newton's method:  did not converge")
        
    # 3. SLSQP
    res_g = minimize(g, x0=x0, method="SLSQP")
    print(f"  - SLSQP:            x ≈ {res_g.x[0]:.4f}, g(x) = {res_g.fun:.4f}")