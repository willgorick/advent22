
def mix_values(iterations:int, key: int, inp: list):
  #turn values to ints and multiply by key if necessary
  inp = [int(i)*key for i in inp]
  l = len(inp)
  ind_array = [i for i in range(l)]
  for _ in range(iterations):
    for i, val in enumerate(inp):
      if val == 0:
        continue
      #current index for the value originally at the index i
      current_ind = ind_array.index(i)
      #remove it from the array so we can move it
      ind_array.pop(current_ind)
      #calculate the new index by adding the current value to the current index and modding by len -1 (becuase circle)
      new_ind = (current_ind + val) % (l - 1)
      #insert the index i back into our array at the new index
      ind_array.insert(new_ind, i)

  # each value in ind_array corresponds to the index in inp where you can find the value that should be here
  # i.e., if we have [1, 0, 2] in our ind_array, that would mean that the proper order for our mixed array is
  # [inp[1], inp[0], inp[2]]
  mixed = [inp[i] for i in ind_array]

  #find 0
  start = mixed.index(0)

  #return 1000th + 2000th + 3000th after 0 (using mod to prevent index out of bounds)
  return sum(mixed[i] for i in ((start+add)%l for add in [1000, 2000, 3000]))