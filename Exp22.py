class NegativeAgeError(Exception):
    """Raised when age entered is negative"""
    def __init__(self, age):
        self.age = age
        super().__init__(f"Invalid age: {age}. Age can't be negative.")
 
def validate_age(age):
    if age < 0:
        raise NegativeAgeError(age)
    return f"Valid age: {age}"
 

 
num = int(input("Enter your age: "))
try:
    print(validate_age(num))
except NegativeAgeError as e:
    print("Caught user-defined exception:\n",e)
