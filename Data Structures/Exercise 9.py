def unique_speeds(speed):

  speed_list = list(speed.values())
  unique_speeds = []

  for speed in speed_list:
    if speed not in unique_speeds:
      unique_speeds.append(speed)

  return unique_speeds

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53,
         'july': 54, 'Aug': 44, 'Sept': 54}

unique_speeds = unique_speeds(speed)

print("unique list", unique_speeds)
