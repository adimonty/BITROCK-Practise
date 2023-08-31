def get_unique_pairs(first_list, second_list):

  result = set()
  for i, j in enumerate(first_list):
    for k in second_list:
      result.add((j, k))

  return result

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

result = get_unique_pairs(first_list, second_list)
print(result)