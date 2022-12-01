import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)

from solution import Solution

TEST_CASES = [
{
"input": """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83""",
"solution": 159
},
{
"input": """R8,U5,L5,D3
U7,R6,D4,L4""",
"solution": 6
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  # SET OF TUPLES
  def solve(self, inp, test=False):
    res = float("inf")
    self.set1 = set()
    self.set2 = set()
    # print(inp)
    self.trace(self.set1, inp[0])
    self.trace(self.set2, inp[1])
    # print(self.set1)
    # print(self.set2)
    for point in self.set1:
      if point in self.set2 and point != (0,0):
        res = min(res, self.manhattan(point))
    return res
  
  def trace(self, curr_set: set, dirs: str):
    curr_pos = (0,0)
    dirs = dirs.split(',')
    # print(dirs)
    for dir_ in dirs:
      # print(dir_)
      if dir_[0] == "R":
        for i in range(1, int(dir_[1:])+1):
          curr_set.add((curr_pos[0],curr_pos[1]+i))
        curr_pos = (curr_pos[0],curr_pos[1]+i)
      if dir_[0] == "L":
        for i in range(1, int(dir_[1:])+1):
          curr_set.add((curr_pos[0],curr_pos[1]-i))
        curr_pos = (curr_pos[0],curr_pos[1]-i)
      if dir_[0] == "U":
        for i in range(1, int(dir_[1:])+1):
          curr_set.add((curr_pos[0]+i,curr_pos[1]))
        curr_pos = (curr_pos[0]+i,curr_pos[1])
      if dir_[0] == "D":
        for i in range(1, int(dir_[1:])+1):
          curr_set.add((curr_pos[0]-i,curr_pos[1]))
        curr_pos = (curr_pos[0]-i,curr_pos[1])

  def manhattan(self, point):
    # print(point, abs(point[0]) + abs(point[1]))
    return abs(point[0]) + abs(point[1])

if __name__ == "__main__":
  main()