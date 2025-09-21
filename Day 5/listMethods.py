numbers = [10, 20, 30, 40, 20]

print(len(numbers))       # 5 (length of list)
print(numbers.count(20))  # 2 (count occurrences)
print(numbers.index(30))  # 2 (index of first occurrence)

numbers.reverse()         # Reverse list
numbers.sort()            # Sort ascending
numbers.sort(reverse=True) # Sort descending

copy_list = numbers.copy()  # Make a copy
numbers.clear()             # Empty the list
