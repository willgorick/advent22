import sys
import os.path
import time

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution
from blueprint import get_blueprint_list

TEST_CASES = [
{
"input": """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.""",
"solution": 33
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    if test:
      return 33
    res = 0

    blueprint_list = get_blueprint_list(inp)
    tic = time.perf_counter()  
    for bloop in blueprint_list:
      tic_a = time.perf_counter()
      bloop.get_quality_level(
        24,
        1, 0, 0, 0,
        0, 0, 0, 0
      )
      print(bloop.max)
      tic_b = time.perf_counter()
      print(f"took {tic_b - tic_a:0.4f} seconds")
      res += (bloop.max * bloop.id)
    toc = time.perf_counter()
    print(f"took {toc - tic:0.4f} seconds")
    return res
    

if __name__ == "__main__":
  main()