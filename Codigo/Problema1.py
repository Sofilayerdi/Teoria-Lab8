import time
import matplotlib.pyplot as plt
import math

n_values = [1, 10, 100, 1000, 10000, 100000]
SAFE_MAX_N = 10000

def iterations(n):
    # Loop i
    iters_i = n - n//2 + 1
    
    # Loop j
    iters_j = n - n//2
    
    # Loop k
    if n <= 0:
        iters_k = 0
    else:
        iters_k = int(math.log2(n)) + 1
    
    return iters_i * iters_j * iters_k

def measure_time(n):
    start = time.perf_counter()
    
    counter = 0
    for i in range(n//2, n + 1):
        for j in range(1, n - n//2 + 1):
            k = 1
            while k <= n:
                counter += 1 
                k *= 2
    
    return time.perf_counter() - start

def iteration_workflow():
    results = []
    
    print("Ejecutando profiling...")
    print()
    
    for n in n_values:
        iters = iterations(n)
        
        if n <= SAFE_MAX_N:
            print(f"Midiendo n={n:>7}...", end=" ", flush=True)
            t = measure_time(n)
            print(f"✓ {t:.6f}s")
            results.append((n, iters, t, None))
        else:
            print(f"Saltando n={n:>7} (too large, estimaría ~{iters:,} iteraciones)")
            results.append((n, iters, None, "too large"))
    
    print()
    print("=" * 60)
    print(f"{'n':>10} {'Iterations':>15} {'Time (s)':>15}")
    print("─" * 60)
    for n, iters, t, note in results:
        if t is not None:
            time_str = f"{t:.6f}"
            print(f"{n:>10,} {iters:>15,} {time_str:>15}")
        else:
            print(f"{n:>10,} {iters:>15,} {note:>15}")
    print("=" * 60)
    
    measured = [(n, t) for n, _, t, _ in results if t is not None]
    if measured:
        ns, times = zip(*measured)
        
        plt.figure(figsize=(10, 6))
        plt.loglog(ns, times, 'bo-', label='Measured', linewidth=2, markersize=8)
        plt.xlabel('n (log scale)', fontsize=12)
        plt.ylabel('Time (seconds, log scale)', fontsize=12)
        plt.title('Time Complexity Analysis - O(log2 n)', fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3, which='both', linestyle='--')
        plt.legend(fontsize=11)
        plt.tight_layout()
        plt.show()

iteration_workflow()