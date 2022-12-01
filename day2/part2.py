import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)

from solution import Solution

TEST_CASES = [
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp: list[str], test=False):
    if test:
      return
    
    for i in range(100):
      for j in range(100):
        if self.attempt(inp.copy(), i, j):
          return 100 * i + j
    
  def attempt(self, inp: list[str], noun: int, verb: int) -> bool:
    i = 0
    inp[1] = str(noun)
    inp[2] = str(verb)

    while i < len(inp):
      if inp[i] == "99":
        return inp[0] == "19690720"
      opcode = [int(inp[i]), int(inp[i+1]), int(inp[i+2]), int(inp[i+3])]
      if opcode[0] == 1:
        inp[int(inp[i+3])] = str(int(inp[opcode[1]]) + int(inp[opcode[2]]))
      if opcode[0]  == 2:
        inp[opcode[3]] = str(int(inp[opcode[1]]) * int(inp[opcode[2]]))
      i += 4

if __name__ == "__main__":
  main()