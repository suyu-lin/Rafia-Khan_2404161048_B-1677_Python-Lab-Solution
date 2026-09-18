
# =====================================================================
# File 2: main_program.py (Save this in the same folder and run it)
# =====================================================================

# Import the custom module we defined above
import fib

print("--- Fibonacci Sequence Generator ---")
num_terms = int(input("Enter the number of terms you want in the Fibonacci series: "))

# Call the function from the imported module using the dot operator
result = fib.fibo(num_terms)

print(f"The first {num_terms} terms of the Fibonacci series are:")
print(result)