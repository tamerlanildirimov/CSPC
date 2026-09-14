import time
from decay import simulate, simulate_loop

N0 = 1000000
p = 0.01
steps = 200

# Measuring time for slow case (loop)
t0 = time.perf_counter()
simulate_loop(N0, p, steps)
t1 = time.perf_counter()
time_loop = t1 - t0

# Measuring time for fast case (NumPy)
t0 = time.perf_counter()
simulate(N0, p, steps)
t1 = time.perf_counter()
time_numpy = t1 - t0

print(f"Loop time: {time_loop:.4f} seconds")
print(f"NumPy time: {time_numpy:.4f} seconds")
print(f"Speedup: {time_loop / time_numpy:.2f}x")
