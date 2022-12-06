def solve_sliding(inp: list[str], goal: int):
  i, j = 0, 0
  unique_chars = {}
  inp_str = inp[0]
  while j - i < goal:
    curr_letter = inp_str[j]
    if curr_letter not in unique_chars:
      unique_chars[curr_letter] = j
    else:
      i = max(i, unique_chars.get(curr_letter) + 1)
      unique_chars[curr_letter] = j
    j += 1
  print(j)
  return j