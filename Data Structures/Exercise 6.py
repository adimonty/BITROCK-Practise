def remove_common_elements(first_set, second_set):

  intersection = first_set.intersection(second_set)
  for item in intersection:
    first_set.remove(item)

  return first_set

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

first_set = remove_common_elements(first_set, second_set)
print("First Set after removing common element ", first_set)
