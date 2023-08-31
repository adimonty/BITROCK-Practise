def odd_even_list(list1, list2):
  odd_even_elements = list(zip(list1[1::2], list2[0::2]))
  return list(enumerate(odd_even_elements))

list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]

odd_even_list = odd_even_list(list1, list2)
print(odd_even_list)