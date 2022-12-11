import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution

TEST_CASES = [
{
"input": """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""",
"solution": 13140
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  # solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    #result, line in input, clock cycle, addend
    res, inp_line, register, addend = 0, 0, 1, 0
    res = [['.'] * 40 for _ in range(6)]

    adding = False
    for clock_cycle in range(1, 241):
      rel_clock_cycle = clock_cycle % 40
      if register <= rel_clock_cycle and rel_clock_cycle <= register+2:
        row = (clock_cycle) // 40
        col = (clock_cycle % 40) -1 
        res[row][col] = "#"
      instruction = inp[inp_line]
      if instruction == "noop":
        inp_line += 1
      elif instruction[0:4] == "addx" and not adding:
        addend = int(instruction[5:])
        adding = True
      elif instruction[0:4] == "addx" and adding: #we added this value last round
        register += addend
        inp_line += 1
        adding = False
    for i in range(len(res)):
      print("".join(res[i]))
    return res
    

if __name__ == "__main__":
  main()