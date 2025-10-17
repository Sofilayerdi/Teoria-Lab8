import time
import matplotlib.pyplot as plt

n_values = [1, 10, 100, 1000, 10000, 100000, 1000000]
SAFE_MAX_N = 1000000 

def iterations(n):
    
    if n <= 1:
        return 0
    
    # Loop i 
    iters_i = n  # O(n)

    # Loop j ejecuta solo 1 vez por el break
    iters_j = 1  

    return iters_i*iters_j 

def measure_time(n):
    
    if n <= 1:
        return 0.0
    
    start = time.perf_counter()
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # printf("Sequence\n") - simulamos sin imprimir
            pass
            break  # break después del printf
    
    return time.perf_counter() - start

def iteration_workflow():
    results = []
    
    print()
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
        plt.plot(ns, times, 'bo-', label='Measured', linewidth=2, markersize=8)
        plt.xlabel('Tamaño de entrada (n)', fontsize=12)
        plt.ylabel('Tiempo de ejecución (s)', fontsize=12)
        plt.title('Tiempo vs Tamaño de Input - Problema 2', fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3, linestyle='--')
        plt.legend(fontsize=11)
        plt.tight_layout()
        plt.show()


iteration_workflow()