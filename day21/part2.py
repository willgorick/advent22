import sys
import os.path
from collections import deque

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
"solution": 301
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()

class Elf:
  def __init__(self, name: str, number: int = None, operand: str = None, elves: list = [], equation_string: str = ""):
    self.name = name
    self.number = number
    self.equation_string = equation_string
    self.equation_stack = None
    self.operand = operand
    self.elves = elves
  
  def __str__(self):
    if self.number:
      return f"{self.name}: {self.number}"
    elif self.equation_string:
      return f"{self.name}: {self.equation_string}"
    return f"{self.name}: {self.elves[0]} {self.operand} {self.elves[1]}"

class Operation:
  def __init__(self, a, b, operand: str):
    self.a = a
    self.b = b
    self.operand = operand
  
  def __str__(self):
    return f"{self.a} {self.operand} {self.b}"

class PartSolution(Solution):
  def solve(self, inp, test=False):
    res = 0
    self.graph = {}
    self.opposites = {
      "+": "-",
      "-": "+",
      "/": "*",
      "*": "/",
    }
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
    
    #figure out which number we need to match
    a, b = self.graph["root"].elves
    a_present = self.dfs_check_for_humn(a)
    if a_present:
      res = self.dfs(b)
      self.dfs_equation(a)
      op_stack = self.graph[a].equation_stack
    else:
      res = self.dfs(a)
      self.dfs_equation(b)
      op_stack = self.graph[b].equation_stack
    
    while op_stack:
      operation = op_stack.pop()
      #x is the int, y is the stack, a_int denotes if a is the int
      a_int = False
      if type(operation.a) == int:
        a_int = True

      x = operation.a if a_int else operation.b
      y = operation.a if not a_int else operation.b

      #for + or *, order doesn't matter
      if operation.operand == "+":
        res -= x
      if operation.operand == "*":
        res //= x
      if operation.operand == "-":
        #int - stack = res, int = res + stack, stack = int - res, 
        if a_int:
          res = res-x
          res = -res
        #stack - int = res, res + int = stack, so just add int to res
        else:
          res += x
      if operation.operand == "/":
        #int / stack = res, res*stack = int, stack = int/res
        if a_int:
          res = x // res
        else:
          res *= x
      if type(y) == deque:
        op_stack = y

    print(res)
    return res

  def dfs_equation(self, elf_name: str):
    curr_elf = self.graph[elf_name]
    if curr_elf.number:
      if curr_elf.name == "humn":
        curr_elf.equation_stack = "x"
        return deque(["x"])
      else:
        return curr_elf.number
    a, b = curr_elf.elves 
    a_num = self.dfs_equation(a)
    b_num = self.dfs_equation(b)

    if type(a_num) == int and type(b_num) == int:
      if curr_elf.operand == "+":
        curr_elf.number = a_num + b_num
      elif curr_elf.operand == "-":
        curr_elf.number = a_num - b_num
      elif curr_elf.operand == "/":
        curr_elf.number = a_num // b_num
      elif curr_elf.operand == "*":
        curr_elf.number = a_num * b_num
      return curr_elf.number
    else:
      a_val = self.graph[a].equation_stack if self.graph[a].equation_stack else self.graph[a].number
      b_val = self.graph[b].equation_stack if self.graph[b].equation_stack else self.graph[b].number
      curr_elf.equation_string = f"{a_val} {curr_elf.operand} {b_val}"
      curr_elf.equation_stack = deque([Operation(a_val, b_val, curr_elf.operand)])
      return curr_elf.equation_stack

  def dfs_check_for_humn(self, elf_name: str):
    curr_elf = self.graph[elf_name]
    if curr_elf.name == "humn":
      return True
    if not curr_elf.elves:
      return False
    a, b = curr_elf.elves 
    a_num = self.dfs_check_for_humn(a)
    b_num = self.dfs_check_for_humn(b)
    return True if a_num or b_num else False

  def dfs(self, elf_name: str):
    curr_elf = self.graph[elf_name]
    if curr_elf.number:
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