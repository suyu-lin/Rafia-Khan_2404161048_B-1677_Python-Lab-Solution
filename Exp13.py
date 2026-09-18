# a) Create Dictionary
student_dict = {"name": "Rafia", "roll_no": 2404161048, "course": "BCA"}
print("Created Dictionary:", student_dict)
# b) Access Dictionary elements
print("Accessing Name:", student_dict["name"])
# c) Update Dictionary
student_dict["course"] = "BCA Semester V" # Updating existing key
student_dict["grade"] = "A"               # Adding new key
print("After update:", student_dict)
# e) Looping through Dictionary
print("Looping through dictionary:")
for key, value in student_dict.items():
    print(f"{key}: {value}")
# d) Delete Dictionary
del student_dict["grade"] # Deleting a specific key
print("After deleting 'grade':", student_dict)
del student_dict # Deleting the dictionary object completely
print("Dictionary has been deleted completely.")