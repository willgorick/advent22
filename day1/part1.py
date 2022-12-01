import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)

from solution import Solution

TEST_CASES = [
{
"input": """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""",
"solution": 24000
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp):
    res = 0
    curr = 0
    for _, cals_str in enumerate(inp):
      if cals_str != "":
        cals = int(cals_str)
        curr += cals
      else:
        res = max(res, curr)
        curr = 0
    return res
    

if __name__ == "__main__":
  main()