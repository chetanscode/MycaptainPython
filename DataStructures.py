def get_sets(message):
  user_input = input(message)
  # Split the input into a list, remove extra spaces, and convert to integers
  elements = [int(x.strip()) for x in user_input.split(",")]
  return set(elements)

# Get set elements from the user
set_E = get_sets("Enter elements for set E: ")
set_N = get_sets("Enter elements for set N: ")

# Perform set operations
union = set_E.union(set_N)
intersection = set_E.intersection(set_N)
difference = set_E.difference(set_N)
symmetric_difference = set_E.symmetric_difference(set_N)

# Print the results
print("Union of E and N is", union)
print("Intersection of E and N is", intersection)
print("Difference of E and N is", difference)
print("Symmetric difference of E and N is", symmetric_difference)
