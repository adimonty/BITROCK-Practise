def remove_unwanted_elements(roll_number, sample_dict):

  unwanted_elements = []
  for item in roll_number:
    if item not in sample_dict.values():
      unwanted_elements.append(item)

  for item in unwanted_elements:
    roll_number.remove(item)

  return roll_number

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

roll_number = remove_unwanted_elements(roll_number, sample_dict)

print("after removing unwanted elements from list:", roll_number)
