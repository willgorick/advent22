import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')
from collections import deque

from solution import Solution

TEST_CASES = [

]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    inp_str = inp[0]
    current = deque()
    for i in range(len(inp_str)):
      current.append(inp_str[i])
      if len(current) > 13:
        curr_set = set(current)
        if len(curr_set) == 14:
          return i +1
        current.popleft()
    res = 0
    return res
    

if __name__ == "__main__":
  main()