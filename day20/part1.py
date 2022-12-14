import sys
import os.path
from time import perf_counter
REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution
from mix import mix_values

TEST_CASES = [
{
"input": """1
2
-3
3
-2
0
4""",
"solution": 3
}
]
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev = None
    self.moved = False

def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    tic = perf_counter()
    res = mix_values(1, 1, inp)
    toc = perf_counter()
    print(f"took {toc - tic:0.6f} seconds")
    return res
    

if __name__ == "__main__":
  main()