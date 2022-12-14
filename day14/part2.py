import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution

TEST_CASES = [
{
"input": """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""",
"solution": 93
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):

    self.res = 0
    self.grid = [['.' for _ in range(800)] for _ in range(200)]
    self.max_depth = -1
    
    for line in inp:
      coords = line.split(" -> ")
      start_x, start_y = -1, -1
      for coord in coords:
        x, y = coord.split(",")
        if start_x != -1:
          self.draw(start_x, x, start_y, y)
        start_x = x
        start_y = y
    for x in range(len(self.grid[self.max_depth + 2])):
      self.grid[self.max_depth + 2][x] = "#"

    while(self.can_drop()):
      self.res += 1
    return self.res+1
  
  def can_drop(self):
    x, y = 500, -1
    can_drop = True
    while can_drop:
      if self.grid[y+1][x] != "#":
        y += 1
      elif self.grid[y+1][x-1] != "#":
        y += 1
        x -= 1
      elif self.grid[y+1][x+1] != "#":
        y += 1
        x += 1
      else:
        can_drop == False
        break
    self.grid[y][x] = "#"
    if y == 0:
      return False
    return True

  def draw(self, start_x, x, start_y, y):
    start_x = int(start_x)
    x = int(x)
    start_y = int(start_y)
    y = int(y)

    if y > self.max_depth:
      self.max_depth = y

    if start_y > self.max_depth:
      self.max_depth = start_y

    while start_x < x:
      self.grid[start_y][start_x] = "#"
      start_x += 1

    while start_x > x:
      self.grid[start_y][start_x] = "#"
      start_x -= 1

    while start_y < y:
      self.grid[start_y][start_x] = "#"
      start_y += 1

    while start_y > y:
      self.grid[start_y][start_x] = "#"
      start_y -= 1

    self.grid[y][x] = "#"
if __name__ == "__main__":
  main()