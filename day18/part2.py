import sys
import os.path
from collections import defaultdict, deque

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution

TEST_CASES = [
{
"input": """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5""",
"solution": 58
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    cube_set = set()
    for line in inp:
      x,y,z = line.split(',')
      cube_set.add((int(x), int(y), int(z)))

    surface_area_candidates = defaultdict(lambda: 0)
    self.grid = [[['.' for _ in range(23)] for _ in range(23)] for _ in range(23)]

    for cube in cube_set:
      x, y, z = cube
      self.grid[x][y][z] = "#"
      if (x+1, y, z) not in cube_set:
        surface_area_candidates[(x+1, y, z)] += 1
      if (x-1, y, z) not in cube_set:
        surface_area_candidates[(x-1, y, z)] += 1
      if (x, y+1, z) not in cube_set:
        surface_area_candidates[(x, y+1, z)] += 1
      if (x, y-1, z) not in cube_set:
        surface_area_candidates[(x, y-1, z)] += 1
      if (x, y, z+1) not in cube_set:
        surface_area_candidates[(x, y, z+1)] += 1
      if (x, y, z-1) not in cube_set:
        surface_area_candidates[(x, y, z-1)] += 1
    
    self.bfs_water(0, 0, 0)
    
    res = 0
    for candidate, count in surface_area_candidates.items():
      x, y, z = candidate
      if self.grid[x][y][z] == "~":
        res += count
    return res
    
  def bfs_water(self, x, y, z):
    water_stack = deque()
    water_stack.append((x, y, z))
    while water_stack:
      x, y, z = water_stack.popleft()
      if x+1 < 23 and self.grid[x+1][y][z] == ".":
        self.grid[x+1][y][z] = "~"
        water_stack.append((x+1, y, z))
      if x-1 >= 0 and self.grid[x-1][y][z] == ".":
        self.grid[x-1][y][z] = "~"
        water_stack.append((x-1, y, z))
      if y+1 < 23 and self.grid[x][y+1][z] == ".":
        self.grid[x][y+1][z] = "~"
        water_stack.append((x, y+1, z))
      if y-1 >= 0 and self.grid[x][y-1][z] == ".":
        self.grid[x][y-1][z] = "~"
        water_stack.append((x, y-1, z))
      if z+1 < 23 and self.grid[x][y][z+1] == ".":
        self.grid[x][y][z+1] = "~"
        water_stack.append((x, y, z+1))
      if z-1 >= 0 and self.grid[x][y][z-1] == ".":
        self.grid[x][y][z-1] = "~"
        water_stack.append((x, y, z-1))

if __name__ == "__main__":
  main()