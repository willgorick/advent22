import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)

from solution import Solution

TEST_CASES = [
]

local_tests = [
  111111,
  112233,
  123444,
  111122
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    # if test:
    for i in local_tests:
      print(self.valid(i))
    lower, upper = inp[0].split('-')
    res = sum(1 for i in range(int(lower), int(upper)) if self.valid(i))
    return res
    
  def valid(self, i):
    # don't need to check for six digits because of our range
    str_i = str(i)
    prev = -1
    found_double = False
    if len(str_i) != 6:
      return False
    l, r = 0, 1
    while r < 6:
      curr = str_i[r]
      prev = str_i[l]
      if curr != prev:
        if r - l == 2:
          found_double = True
        l = r
      if int(curr) < int(prev):
        return False
      r += 1
    return found_double or r-l == 2

if __name__ == "__main__":
  main()