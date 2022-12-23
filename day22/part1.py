import sys
import os.path
import re

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution

TEST_CASES = [
{
"input": 
"""        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5""",
"solution": 6032
},
# {
# "input": 
# """        ...#
#         .#..
#         #...
#         ....
# ...#.......#
# ........#...
# ..#....#....
# ..........#.
#         ...#....
#         .....#..
#         .#......
#         ......#.

# 1L1L1L1L""",
# "solution": 1036
# },
# {
# "input": 
# """        ...#
#         .#..
#         #...
#         ....
# ...#.......#
# ........#...
# ..#....#....
# ..........#.
#         ...#....
#         .....#..
#         .#......
#         ......#.

# 2L""",
# "solution": 1047
# },
# {
# "input": 
# """        ...#
#         .#..
#         #...
#         ....
# ...#.......#
# ........#...
# ..#....#....
# ..........#.
#         ...#....
#         .....#..
#         .#......
#         ......#.

# 3R""",
# "solution": 1045
# }
]
  
def main():
  sys.argv.append('unstrip')
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    self.dir_deltas = {
      0: (0, 1),  #Right
      1: (1, 0),  #Down
      2: (0, -1), #Left
      3: (-1, 0)  #Up
    }

    if test:
      self.grid_size = 16
    if not test:
      self.grid_size = 200
      # return 
    self.grid = [[" " for _ in range(self.grid_size)] for _ in range(self.grid_size)]
    self.max_len = 0
    for i, line in enumerate(inp):
      if len(line) == 0:
        break
      for j in range(len(list(line))):
        self.grid[i][j] = line[j]

    curr_dir = 0
    row, col = 0, 0
    while self.grid[row][col] == " ":
      col += 1
    d_row, d_col = self.dir_deltas[curr_dir]
    directions = inp[i+1]
    matches = re.findall("(([0-9]+)([L|R])?)", directions)
    
    for match in matches:
      moves = int(match[1])
      turn = match[2]
      for _ in range(moves):
        new_row, new_col = row, col
        if d_col == 0:
          new_row = self.wrap_val(row + d_row)
          while self.grid[new_row][new_col] == " ":
            new_row = self.wrap_val(new_row + d_row)
        if d_row == 0:
          new_col = self.wrap_val(col + d_col)
          while self.grid[new_row][new_col] == " ":
            new_col = self.wrap_val(new_col + d_col)
        if self.grid[new_row][new_col] == "#":
          break
        row, col = new_row, new_col
      if turn == "R":
        curr_dir = (curr_dir + 1) % 4
      elif turn == "L":
        curr_dir = (curr_dir - 1) % 4
      d_row, d_col = self.dir_deltas[curr_dir]

    res = 1000 * (row+1) + 4 * (col+1) + curr_dir
    print(res)
    return res
    
  def wrap_val(self, val):
    return val % self.grid_size

if __name__ == "__main__":
  main()