x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# using temporary variable
temp = x
x = y
y = temp
print("After swapping: x =", x, ", y =", y)

# without temporary variable
x, y = y, x
print("Swapped back: x =", x, ", y =", y)
