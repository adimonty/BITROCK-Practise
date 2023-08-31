def find_min_max_unique_numbers(list1):

  unique_list = list(set(list1))
  min_number = min(unique_list)
  max_number = max(unique_list)

  return min_number, max_number

sample_list = [87, 52, 44, 53, 54, 87, 52, 53]

min_number, max_number = find_min_max_unique_numbers(sample_list)

print("Minimum number is: ", min_number)
print("Maximum number is: ", max_number)
