import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution

TEST_CASES = [
{
"input": """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""",
"solution": 70
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    res = 0
    set1 = set()
    set2 = set()
    set3 = set()
    for i, line in enumerate(inp):
      if i % 3 == 0:
        set1.clear()
        for letter in line:
          set1.add(letter)
      if i % 3 == 1:
        set2.clear()
        for letter in line:
          set2.add(letter)
      if i % 3 == 2:
        set3.clear()
        for letter in line:
          set3.add(letter)
        for letter in set1:
          if letter in set2 and letter in set3:
            special = letter
        if special.islower():
          res += ord(special) - 96
        else:
          res += ord(special) - 38
    return res
    

if __name__ == "__main__":
  main()