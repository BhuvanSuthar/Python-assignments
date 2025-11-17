students = {
    "Aman": 85,
    "Rahul": 78,
    "Priya": 92,
    "Neha": 88,
    "Sahil": 76
}
name = input("Enter student name: ")

if name in students:
    print("Marks of", name, ":", students[name])
else:
    print("Student not found in the dictionary.")
