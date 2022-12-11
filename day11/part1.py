import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution
import monkey

TEST_CASES = [
{
"input": """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""",
"solution": 10605
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):

    monkey_list = []
    for i in range(len(inp) // 7 + 1):
      offset = i*7
      new_monkey = monkey.Monkey(inp[0+offset].strip(), inp[1+offset].strip(), inp[2+offset].strip(), inp[3+offset].strip(), inp[4+offset].strip(), inp[5+offset].strip())
      monkey_list.append(new_monkey)
    
    for _ in range(20):
      for monke in monkey_list:
        while monke.items:
          monke.inspects += 1
          item = monke.items.popleft()
          curr = monke.execute_operation(item)
          curr = curr // 3
          test = monke.execute_test(curr)
          idx = monke.if_false
          if test:
            idx = monke.if_true
          monkey_list[idx].items.append(curr)

    inspect_list = []
    for monke in monkey_list:
      inspect_list.append(monke.inspects)
    sorted_inspect_list = sorted(inspect_list)
    res = sorted_inspect_list[-1] * sorted_inspect_list[-2]

    return res
    
    
if __name__ == "__main__":
  main()