import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)

from solution import Solution

TEST_CASES = [
]

local_tests = [
  111111,
  223450,
  123789,
  367479,
  122345,
  111123,
  133567
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    if test:
      for i in local_tests:
        print(self.valid(i))
    lower, upper = inp[0].split('-')
    res = sum(1 for i in range(int(lower), int(upper)) if self.valid(i))
    return res
    
  def valid(self, i):
    # don't need to check for six digits because of our range
    str_i = str(i)
    adj = False
    prev = -1
    if len(str_i) != 6:
      return False
    for j in range(len(str_i)):
      curr = str_i[j]
      if curr == prev:
        adj = True
      if int(curr) < int(prev):
        return False
      prev = str_i[j]
    return adj

if __name__ == "__main__":
  main()