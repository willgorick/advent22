import sys
import os.path
from heapq import *

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

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
"solution": 45000
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    heap = []
    curr = 0
    for _, cals_str in enumerate(inp):
      cals_str = cals_str.strip()
      if cals_str != "":
        cals = int(cals_str)
        curr += cals
      elif curr != 0:
        heappush(heap, -curr)
        curr = 0
    res = 0

    for _ in range(3):
      res += -heappop(heap)
    return res

if __name__ == "__main__":
  main()