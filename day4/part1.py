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
"solution": 2
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
            first_start <= second_start and second_end <= first_end, 
            second_start <= first_start and first_end <= second_end
          ] 
       ):
        res += 1
        
    return res

  def solve_one_line(self, inp):
    return sum(any ([ranges[0][0] <= ranges[1][0] and ranges[1][1] <= ranges[0][1], ranges[1][0] <= ranges[0][0] and ranges[0][1] <= ranges[1][1]]) for ranges in [[[int(sub_val) for sub_val in val.split('-')] for val in split] for split in [pair.split(',') for pair in inp]])
    

if __name__ == "__main__":
  main()