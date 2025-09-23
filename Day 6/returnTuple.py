def calc(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    return add, sub, mul   # returns a tuple

result = calc(10, 5)
print("Results:", result)
