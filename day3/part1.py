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
"solution": 157
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    res = 0
    for line in inp:
      length = len(line)
      first, second = line[0:(length//2)], line[(length//2):]
      set1 = set()
      set2 = set()
      for letter in first:
        set1.add(letter)
      for letter in second:
        set2.add(letter)
      for letter in set1:
        if letter in set2:
          special = letter
      if special.islower():
        res += ord(special) -96
      else:
        res += ord(special) - 38

    #Write your own solution!
    return res
    

if __name__ == "__main__":
  main()