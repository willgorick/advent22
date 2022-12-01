import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)

from solution import Solution

TEST_CASES = [
{
"input": """1,9,10,3,2,3,11,0,99,30,40,50""",
"solution": 3500
},
{
"input": """1,1,1,4,99,5,6,0,99""",
"solution": 30
},
{
"input": """2,4,4,5,99,0""",
"solution": 2
},
{
"input": """2,3,0,3,99""",
"solution": 2
},
{
"input": """1,0,0,0,99""",
"solution": 2
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp: list[str], test=False):
    i = 0
    if not test:
      inp[1] = '12'
      inp[2] = '2'
    while i < len(inp):
      if inp[i] == "99":
        return int(inp[0])
      opcode = [int(inp[i]), int(inp[i+1]), int(inp[i+2]), int(inp[i+3])]
      if opcode[0] == 1:
        inp[int(inp[i+3])] = str(int(inp[opcode[1]]) + int(inp[opcode[2]]))
      if opcode[0]  == 2:
        inp[opcode[3]] = str(int(inp[opcode[1]]) * int(inp[opcode[2]]))
      i += 4
      # if test:
      #   print(','.join(inp), end="\n\n\n")
    

if __name__ == "__main__":
  main()