import time

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
dur = {}
slow = False
for i in range(60):
    if not slow:
        start = time.time()
        f = fib(i)
        duration = time.time() - start
        dur[i] = duration
        print(f'f({i:3d}) = {f:15d} in {duration:8.3f} seconds')
        if duration > 10:
            slow = True
            print("too slow from now on")
    else:
        dur[i] = dur[i-1] + dur[i-2]
        if dur[i] < 3600:
            print(f'f({i:3d}) would take about {dur[i]:8.0f} seconds')
        else:
            print(f'f({i:3d}) would take about {dur[i]/3600:8.1f} hours')
        