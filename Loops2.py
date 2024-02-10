def print_positive_numbers(list1):
   for num in list1:
    if num > 0:
      print(num)

# Example 
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

print("Positive numbers in list1:")
print_positive_numbers(list1)

print("\nPositive numbers in list2:")
print_positive_numbers(list2)
