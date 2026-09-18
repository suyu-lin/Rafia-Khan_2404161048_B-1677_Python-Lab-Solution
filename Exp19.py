class Employee:
    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary
 
    def __str__(self):
        return f"{self.emp_id} | {self.name} | {self.department} | Rs.{self.salary}"
 
 
def update_salary_by_department(employees, department, hike_amount):
    for emp in employees:
        if emp.department == department:
            emp.salary += hike_amount
    return employees
 
 
employees = [
    Employee("Komal", "E101", "IT", 30000),
    Employee("Anany", "E102", "HR", 28000),
    Employee("Unnati", "E103", "Finance", 35000),
    Employee("Rafia", "E104", "IT", 32000),
]
 
print("Before Update:")
for emp in employees:
    print(emp)
 
update_salary_by_department(employees, "IT", 5000)
 
print("\nAfter updating salary for IT department (+5000):")
for emp in employees:
    print(emp)

