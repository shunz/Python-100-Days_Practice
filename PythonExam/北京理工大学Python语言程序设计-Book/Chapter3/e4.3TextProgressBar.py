import time
scale = 50
print('Begin'.center(scale + 14, '-'))
# t = time.clock()
"""
- DeprecationWarning: time.clock has been deprecated in Python 3.3 and will be
  removed from Python 3.8: use time.perf_counter or time.process_time instead.

- Help on built-in function process_time in module time:

process_time(...)
    process_time() -> float
    
    Process time for profiling: sum of the kernel and user-space CPU time

- Help on built-in function perf_counter in module time:

perf_counter(...)
    perf_counter() -> float
    
    Performance counter for benchmarking.
"""
start = time.perf_counter()
for i in range(scale+1):
    a = '•' * i
    b = '◦' * (scale - i)
    c = i / scale
    t = time.perf_counter() - start  # 记录运行时长
    print(f'\r{c:^3.0%} [{a}➤➤{b}]{t:.2f}s', end='')
    time.sleep(0.05)
print('\n'+'End'.center(scale + 14, '-'))
