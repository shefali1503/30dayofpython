student = {"name": "Shefali", "age": 20, "course": "BCA"}

# Remove specific key
student.pop("age")

# Remove last inserted key
student.popitem()

print(student)
