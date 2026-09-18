import inspect

# (a) Get list of parameters name from a function
def sample_function(student_name, roll_no, course="BCA"):
    pass

print("(a) Getting parameter names:")
# Method 1: Using __code__ attribute
print("Using __code__:", sample_function.__code__.co_varnames)

# Method 2: Using the inspect module
sig = inspect.signature(sample_function)
print("Using inspect module:", list(sig.parameters.keys()))


# (b) Print Multiple Arguments
print("\n(b) Printing Multiple Arguments (*args):")
def print_multiple_args(*args):
    for index, arg in enumerate(args):
        print(f"Argument {index}: {arg}")

print_multiple_args("Python", 101, True, 3.14)


# (c) Functions that accept variable length key value pair
print("\n(c) Variable length key-value pairs (**kwargs):")
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_kwargs(name="Rafia", enrollment="B-1677", semester=5)