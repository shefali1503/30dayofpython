students = {
    1: {"name": "Shefali", "age": 20},
    2: {"name": "Riya", "age": 21}
}

for id, info in students.items():
    print("ID:", id)
    for key in info:
        print(key, ":", info[key])
    print()
