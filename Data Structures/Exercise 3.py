def rev_chunk(sample_list):
  """
  This function takes a list as input and improves the code
  that reverses the chunks of the list.

  Args:
    sample_list: The list to be improved.

  Returns:
    None.
  """

  length = len(sample_list)
  chunk_size = int(length / 3)
  start = 0
  end = chunk_size

  # run loop 3 times
  for i, _ in enumerate(sample_list):
    # get indexes
    indexes = slice(start, end)
    
    # reverse chunk in place
    sample_list[indexes] = list(reversed(sample_list[indexes]))
    print("Chunk ", i, sample_list[indexes])

    start = end
    end += chunk_size

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
rev_chunk(sample_list)