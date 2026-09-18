# a) Create Set
s = {10, 20, 30, 40, 50}
print("Created Set:", s)
# b) Access Set elements
print("Accessing set elements via loop:")
for item in s:
    print(item, end=" ")
print("\nChecking if 30 is in the set:", 30 in s)
# c) Update Set
s.add(60) # Adding a single element
print("After add(60):", s)
s.update([70, 80]) # Adding multiple elements
print("After update([70, 80]):", s)
# d) Delete Set
del s # Completely deletes the set object
print("Set has been deleted completely.")