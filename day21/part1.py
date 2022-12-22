import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution

TEST_CASES = [
{
"input": """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32""",
"solution": 152
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()

class Elf:
  def __init__(self, name: str, number: int = None, operand: str = None, elves: list = []):
    self.name = name
    self.number = number
    self.operand = operand
    self.elves = elves
  
  def __str__(self):
    if self.number:
      return f"{self.name}: {self.number}"
    return f"{self.name}: {self.elves[0]} {self.operand} {self.elves[1]}"

class PartSolution(Solution):
  def solve(self, inp, test=False):
    if not test:
      return
    res = 0
    self.graph = {}
    for line in inp:
      elf_name, equation = line.split(": ")        
      if len(equation) < 8:
        number = int(equation)
        elf = Elf(name=elf_name, number=number)
        self.graph[elf_name] = elf
      else:
        if "+" in equation:
          a, b = equation.split(" + ")
          operand = "+"
        elif "/" in equation:
          a, b = equation.split(" / ")
          operand = "/"
        elif "*" in equation:
          a, b = equation.split(" * ")
          operand = "*"
        elif "-" in equation:
          a, b = equation.split(" - ")
          operand = "-"

        elf = Elf(name=elf_name, number=None, operand=operand, elves = [a, b])
        self.graph[elf_name] = elf
    res = self.dfs("root")
    print(res)
    return res
    
  def dfs(self, elf_name: str):
    curr_elf = self.graph[elf_name]
    if curr_elf.number:
      print(curr_elf.name, curr_elf.number)
      return curr_elf.number

    a, b = curr_elf.elves 
    a_num = self.dfs(a)
    b_num = self.dfs(b)
    if curr_elf.operand == "+":
      curr_elf.number = a_num + b_num
    elif curr_elf.operand == "-":
      curr_elf.number = a_num - b_num
    elif curr_elf.operand == "/":
      curr_elf.number = a_num // b_num
    elif curr_elf.operand == "*":
      curr_elf.number = a_num * b_num
    return curr_elf.number

if __name__ == "__main__":
  main()