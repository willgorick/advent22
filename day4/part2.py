import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution

TEST_CASES = [
{
"input": """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""",
"solution": 4
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    res = 0
    for first, second in [pair.split(',') for pair in inp]:
      first_start, first_end = [int(x) for x in first.split('-')]
      second_start, second_end = [int(x) for x in second.split('-')]
      
      if any(
          [
            first_start <= second_end and first_end >= second_start,
            second_start <= first_end and second_end >= first_start
          ]
        ):
        res += 1

    return res
    

if __name__ == "__main__":
  main()