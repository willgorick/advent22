import sys
import os.path
import functools

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution

TEST_CASES = [
{
"input": """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""",
"solution": 140
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()

class Packet:
  def __init__(self, vals: list):
    self.vals = vals

  def __lt__(self, other):
    return self.packet_comparison(self.vals, other.vals) < 0

  def __gt__(self, other):
    return self.packet_comparison(self.vals, other.vals) > 0

  def __eq__(self, other):
    return self.packet_comparison(self.vals, other.vals) == 0
  
  def __ne__(self, other):
    return self.packet_comparison(self.vals, other.vals) != 0

  def __ge__(self, other):
    return self.packet_comparison(self.vals, other.vals) >= 0

  def __le__(self, other):
    return self.packet_comparison(self.vals, other.vals) <= 0

  #return -1 if left < right, return 0 if need to continue, return 1 if right < left
  def packet_comparison(self, left, right): 
    # print(left, right)
    #base case for ints, just return comparison
    if isinstance(left, int) and isinstance(right, int):
      if left < right:
        return -1
      elif right < left:
        return 1
      return 0

    #base case for lists, compare each item
    if isinstance(left, list) and isinstance(right, list):
      i = 0
      while i < len(left) and i < len(right):
        comp = self.packet_comparison(left[i], right[i])
        if comp == -1:
          return -1
        elif comp == 1:
          return 1
        i += 1

      #handle uneven length cases
      if i == len(left) and i == len(right):
        return 0
      elif i < len(left):
        return 1
      else:
        return -1

    elif isinstance(left, int) and isinstance(right, list):
      return self.packet_comparison([left], right)

    elif isinstance(left, list) and isinstance(right, int):
      return self.packet_comparison(left, [right])

  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    packet_list = []
    for i in range(0, len(inp), 3):
      ind = i//3 + 1
      left = inp[i]
      right = inp[i+1]
      l_packet = Packet(self.parse_nested_list(left))
      r_packet = Packet(self.parse_nested_list(right))

      packet_list.append(l_packet)
      packet_list.append(r_packet)

    a, b = 0, 0
    packet_a = Packet([[2]])
    packet_b = Packet([[6]])
    packet_list.append(packet_a)
    packet_list.append(packet_b)
    packet_list.sort()
    for i in range(len(packet_list)):
      print(packet_list[i].vals)
      if packet_list[i].vals == [[2]]:
        a = i+1 
      if packet_list[i].vals == [[6]]:
        b = i+1 
    return a*b
    
  def parse_nested_list(self, nested_list: str) -> list:
    nested_list = nested_list.replace("[", "[ ").replace(",", ", ").replace("]"," ] ")
    nested_list = nested_list.replace(",", "") 
    nested_list = nested_list.split(" ")

    final_list_container = []
    stack = [final_list_container]

    for ch in nested_list: 
        curr_list = stack[-1] 
        if ch == "[":
            new_list = []
            curr_list.append(new_list)
            stack.append(new_list)
        elif ch == "]":
            stack.pop()
        elif ch != "":
            curr_list.append(int(ch))

    result = final_list_container[0]
    return result

if __name__ == "__main__":
  main()