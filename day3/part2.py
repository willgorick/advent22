import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)

from solution import Solution

TEST_CASES = [
{
"input": """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83""",
"solution": 610
},
{
"input": """R8,U5,L5,D3
U7,R6,D4,L4""",
"solution": 30
},
{
"input": """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7""",
"solution": 410
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
    self.set1 = dict()
    self.set2 = dict()
    self.trace(self.set1, inp[0])
    self.trace(self.set2, inp[1])

    for point in self.set1:
      if point in self.set2 and point != (0,0):
        print(self.set1[point], self.set2[point])
        res = min(res, (self.set1[point]+self.set2[point]))
    return res
  
  def trace(self, curr_set: set, dirs: str):
    curr_pos = (0,0)
    steps = 0
    dirs = dirs.split(',')
    for dir_ in dirs:
      if dir_[0] == "R":
        for _ in range(1, int(dir_[1:])+1):
          steps += 1
          curr_pos = (curr_pos[0],curr_pos[1]+1)
          curr_set[curr_pos] = steps
      if dir_[0] == "L":
        for _ in range(1, int(dir_[1:])+1):
          steps += 1
          curr_pos = (curr_pos[0],curr_pos[1]-1)
          curr_set[curr_pos] = steps
      if dir_[0] == "U":
        for _ in range(1, int(dir_[1:])+1):
          steps += 1
          curr_pos = (curr_pos[0]+1, curr_pos[1])
          curr_set[curr_pos] = steps
      if dir_[0] == "D":
        for _ in range(1, int(dir_[1:])+1):
          steps += 1
          curr_pos = (curr_pos[0]-1,curr_pos[1])
          curr_set[curr_pos] = steps

if __name__ == "__main__":
  main()