def check_subset_superset(first_set, second_set):

  is_subset = first_set.issubset(second_set)
  is_superset = first_set.issuperset(second_set)
  is_equal = first_set == second_set

  return is_subset, is_superset, is_equal

first_set = {57, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

is_subset, is_superset, is_equal = check_subset_superset(first_set, second_set)

print("First set is subset of second set -", is_subset)
print("Second set is subset of First set - ", is_superset)
print("First set is Super set of second set - ", is_superset)
print("Second set is Super set of First set - ", is_superset)

if is_subset:
  first_set.clear()

if is_superset:
  second_set.clear()

print("First Set ", first_set)
print("Second Set ", second_set)
