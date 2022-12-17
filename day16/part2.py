import sys
import os.path
import re
from collections import deque, defaultdict

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution

TEST_CASES = [
{
"input": """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""",
"solution": 1707
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    self.res = 0
    self.graph = {}
    self.flows = {}
    self.valves_to_open = set()
    self.visited = defaultdict(lambda:-1)
    self.opened_valves = set()

    #build self.graph and flow map
    for line in inp:
      m = re.match(r"Valve ([A-Z]{2}) has flow rate=([0-9]*); tunnel[s]? lead[s]? to valve[s]? (([A-Z]{2}(, )?)*)", line)
      source = m.group(1)
      flow = int(m.group(2))
      dests = m.group(3).split(", ")
      self.graph[source] = dests
      self.flows[source] = flow
      if flow > 0:
        self.valves_to_open.add(source)
    
    self.dfs(1, "AA", "AA", 0)
    print(self.res)
    return self.res

  def dfs(self, mins: int, curr: str, elephant: str, total: int):
    #prune this branch, we've already gotten here with a higher total
    if self.visited[(mins, curr, elephant)] >= total:
      return

    #set (mins, curr) to my total if not visited or visited with lower total
    self.visited[(mins, curr, elephant)] = total

    #we've hit 30 mins so we want to compare all branches here  
    if mins >= 26:
      self.res = max(self.res, total)
      return

    #increment total by the amount that the total pressure increases this minute
    total += sum([self.flows[x] for x in self.opened_valves])

    #if we've opened all valves, just chill
    if len(self.opened_valves) == len(self.valves_to_open):
      self.dfs(mins+1, curr, elephant, total)
      return

    #I can open the valve 
    if curr not in self.opened_valves and self.flows[curr]:
      #add curr to opened valves, dfs with opening this valve
      #consider both elephant opening his valve and elephant moving
      self.opened_valves.add(curr)

      #elephant can choose to open his valve
      if elephant not in self.opened_valves and self.flows[elephant]:
        self.opened_valves.add(elephant)
        self.dfs(mins+1, curr, elephant, total+self.flows[elephant]+self.flows[curr])
        #remove elephant so we can consider elephant moving instead
        self.opened_valves.remove(elephant)
      
      for elephant_neighbor in self.graph[elephant]:
        self.dfs(mins+1, curr, elephant_neighbor, total+self.flows[curr])

      self.opened_valves.remove(curr)
    
    #I can move instead of opening my valve
    for neighbor in self.graph[curr]:
      #elephant can choose to open his valve
      if elephant not in self.opened_valves and self.flows[elephant]:
        self.opened_valves.add(elephant)
        self.dfs(mins+1, neighbor, elephant, total+self.flows[elephant])
        self.opened_valves.remove(elephant)

      #elephant can also choose to move instead of opening his valve
      for elephant_neighbor in self.graph[elephant]:
        self.dfs(mins+1, neighbor, elephant_neighbor, total)

if __name__ == "__main__":
  main()