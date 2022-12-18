import sys
import os.path
from collections import defaultdict
import re

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution

TEST_CASES = [
{
"input": """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>""",
"solution": 1514285714288
}
]
# [06, 16, 26, 36, 46, 56, 66]
# [05, 15, 25, 35, 45, 55, 65]
# [04, 14, 24, 34, 44, 54, 64]
# [03, 13, 23, 33, 43, 53, 63]
# [02, 12, 22, 32, 42, 52, 62]
# [01, 11, 21, 31, 41, 51, 61]
# [00, 10, 20, 30, 40, 50, 60] # floor

rock_type_coords = [
  [[2,0], [3,0], [4,0], [5,0]],
  [[3,0], [2,1], [3,1], [4,1], [3,2]],
  [[2,0], [3,0], [4,0], [4,1], [4,2]],
  [[2,0], [2,1], [2,2], [2,3]],
  [[2,0], [2,1], [3,0], [3,1]]
]

tetris_shapes = [
"####",

""""
 # 
###
 # 
""",

"""
  #
  #
###
""",

"""
#
#
#
#
""",

"""
##
##
"""
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
  #7 units wide
  #rock spans so that left edge is two units away from the left wall
  #its bottom edge is three units above the highest rock (highest + 4)

class PartSolution(Solution):
  def solve(self, inp, test=False):
    res = 0
    lotta_rocks = 1000000000000
    tallest = 0
    directions = list(inp[0])
    num_directions = len(directions)
    fallen = defaultdict(set)
    fallen[0] = set([0, 1, 2, 3, 4, 5, 6]) #floor
    windex = 0
    height_increase = []

    for i in range(5000): #just need enough rocks to find the pattern
      prev_tallest = tallest

      # ---- rock type
      rock_type = i% 5
      starting_coords = rock_type_coords[rock_type]
      new_coords = []
      for coord in starting_coords:
        new_coord = [coord[0], 0]
        new_coord[1] = coord[1] +tallest + 4
        new_coords.append(new_coord)

      rock_can_fall = True
      while rock_can_fall:
        #rock is blown sideways if possible
        move = directions[windex % num_directions]
        can_move_sideways = True
        if move == '>':
          for coord in new_coords:
            if coord[0] == 6 or coord[0]+1 in fallen[coord[1]]: #if already touching right wall, or another fallen rock can't move further right
              can_move_sideways = False
          if can_move_sideways:
            for coord in new_coords:
              coord[0] += 1
        elif move == '<':
          for coord in new_coords:
            if coord[0] == 0 or coord[0]-1 in fallen[coord[1]]: #if already touching left wall, or another fallen rock can't move further left
              can_move_sideways = False
          if can_move_sideways:
            for coord in new_coords:
              coord[0] -= 1
        
        #rock falls if possible, if not we break the loop
        for coord in new_coords:
          if coord[1] - 1 in fallen:
            if coord[0] in fallen[coord[1]-1]:
              rock_can_fall = False
        
        #if rock isn't directly above the floor or another rock, drop it
        if rock_can_fall:
          for coord in new_coords:
            coord[1] -= 1
        #if rock cannot fall, try to set a new tallest value
        else:
          for coord in new_coords:
            fallen[coord[1]].add(coord[0])
            tallest = max(tallest, coord[1])
        windex += 1
      height_increase.append(str(tallest-prev_tallest))
    
    height_str = "".join(height_increase)
    longest_repeating = self.longestRepeatedSubstring(height_str)
    first_ind = height_str.find(longest_repeating)

    before_pattern_sum = sum(int(height_increase[i]) for i in range(first_ind))
    pattern_len = len(longest_repeating)
    
    res += before_pattern_sum
    pattern_sum = sum(int(x) for x in longest_repeating)

    repeating_len = lotta_rocks - first_ind
    num_repeats = repeating_len // pattern_len
    remaining_after_repeats = repeating_len % pattern_len

    ind = first_ind
    res += pattern_sum * num_repeats
    ind += pattern_len * num_repeats

    for i in range(remaining_after_repeats):
      res += int(longest_repeating[i])
      ind += 1
    
    return res
    
  def longestRepeatedSubstring(self, str):
 
    n = len(str)
    LCSRe = [[0 for x in range(n + 1)]
                for y in range(n + 1)]
 
    res = "" # To store result
    res_length = 0 # To store length of result
 
    # building table in bottom-up manner
    index = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
             
            # (j-i) > LCSRe[i-1][j-1] to remove
            # overlapping
            if (str[i - 1] == str[j - 1] and
                LCSRe[i - 1][j - 1] < (j - i)):
                LCSRe[i][j] = LCSRe[i - 1][j - 1] + 1
 
                # updating maximum length of the
                # substring and updating the finishing
                # index of the suffix
                if (LCSRe[i][j] > res_length):
                    res_length = LCSRe[i][j]
                    index = max(i, index)
                 
            else:
                LCSRe[i][j] = 0
 
    # If we have non-empty result, then insert
    # all characters from first character to
    # last character of string
    if (res_length > 0):
        for i in range(index - res_length + 1,
                                    index + 1):
            res = res + str[i - 1]
 
    return res
if __name__ == "__main__":
  main()