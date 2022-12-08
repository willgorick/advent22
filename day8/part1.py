import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution

TEST_CASES = [
{
"input": """30373
25512
65332
33549
35390""",
"solution": 21
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv, '2d')
  solution.test_cases = TEST_CASES
  solution.run('2d')
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    visible = [[False for _ in inp[i]] for i in range(len(inp))]

    #method: 4n, we'll go left to right, right to left, up to down, down to up
    #this means we'll look at each value of our input twice
  
    #l to r
    for i in range(len(inp)):
      local_max = -1 #so 0 is shorter
      for j in range(len(inp[i])):
        if inp[i][j] > local_max:
          visible[i][j] = True
          local_max = inp[i][j]

    #r to l
    for i in range(len(inp)):
      local_max = -1 #so 0 is shorter
      for j in range(len(inp[i])-1, -1, -1):
        if inp[i][j] > local_max:
          visible[i][j] = True
          local_max = inp[i][j]

    #top to bottom
    for i in range(len(inp)):
      local_max = -1 #so 0 is shorter
      for j in range(len(inp[i])):
        if inp[j][i] > local_max:
          visible[j][i] = True
          local_max = inp[j][i]

    #bottom to top
    for i in range(len(inp)):
      local_max = -1 #so 0 is shorter
      for j in range(len(inp[i])-1, -1, -1):
        if inp[j][i] > local_max:
          visible[j][i] = True
          local_max = inp[j][i]

    return sum([sum(visible[i]) for i in range(len(inp))])
  
if __name__ == "__main__":
  main()