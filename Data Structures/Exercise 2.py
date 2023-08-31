def improve_list(sample_list):

  for index, element in enumerate(sample_list):
    if index == 4:
      sample_list.pop(index)
    elif index == 2:
      sample_list.insert(index, element)
    else:
      sample_list.append(element)

  print("The improved list is: ", sample_list)

sample_list = [34, 54, 67, 89, 11, 43, 94]
improve_list(sample_list)