sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list ", sample_list)

count_dict = {}
for item in sample_list:
  count = count_dict.get(item, 0)
  count_dict[item] = count + 1

print("Printing count of each item  ", count_dict)