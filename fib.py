# =====================================================================
# File 1: fib.py (Save this code in a file named exactly this)
# =====================================================================

def fibo(n):
    """Generates a Fibonacci sequence up to n terms and returns it as a list."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_l = [0, 1]
        for _ in range(2, n):
            next_number = fib_l[-1] + fib_l[-2]
            fib_l.append(next_number)
        return fib_l

