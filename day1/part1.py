import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)

from solution import Solution

TEST_CASES = [
  {
      "input": """
        199
        200
        208
        210
        200
        207
        240
        269
        260
        263
      """,
      "solution": 7
    },
    {
      "input": """
      """,
      "solution": 0
    }
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp):
    res = 0
    for i in range(len(inp)):
      if i != 0 and int(inp[i]) > int(inp[i-1]):
        res += 1
    return res
    

if __name__ == "__main__":
  main()