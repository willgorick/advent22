import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution
from mix import mix_values
from time import perf_counter

TEST_CASES = [
{
"input": """1
2
-3
3
-2
0
4""",
"solution": 1623178306
}
]

DECRYPTION_KEY = 811589153

def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    tic = perf_counter()
    res = mix_values(10, DECRYPTION_KEY, inp)
    toc = perf_counter()
    print(f"took {toc - tic:0.4f} seconds")
    return res
    

if __name__ == "__main__":
  main()