from collections import defaultdict
import re

class Blueprint:
  def __init__(self, blueprint_id: int, ore_cost: int, clay_cost: int, obsidian_costs: list[int], geode_costs: list[int]):
    self.id = blueprint_id
    self.robot_costs = {
      'ore': {'ore': ore_cost},
      'clay': {'ore': clay_cost},
      'obsidian': {'ore': obsidian_costs[0], 'clay': obsidian_costs[1]},
      'geode': {'ore': geode_costs[0], 'obsidian': geode_costs[1]}
    }

    self.ore_max = max([ore_cost, clay_cost, obsidian_costs[0], geode_costs[0]]) 
    self.clay_max = obsidian_costs[1]
    self.obsidian_max = geode_costs[1]
    self.max = 0
    self.visited = set()

  def __str__(self):
    return (f"Blueprint {self.id}:\n"
    f"Ore robot costs: {self.robot_costs['ore']['ore']} ore\n"
    f"Clay robot costs: {self.robot_costs['clay']['ore']} ore\n"
    f"Obsidian robot costs: {self.robot_costs['obsidian']['ore']} ore and {self.robot_costs['obsidian']['clay']} clay\n"
    f"Geode robot costs: {self.robot_costs['geode']['ore']} ore and {self.robot_costs['geode']['obsidian']} obsidian")

  def get_quality_level(self,  mins: int, ore_bot: int, clay_bot: int, obsidian_bot: int, geode_bot: int, ore_count: int, clay_count: int, obsidian_count: int, geode_count: int):  
    if (mins, ore_bot, clay_bot, obsidian_bot, geode_bot, ore_count, clay_count, obsidian_count, geode_count) in self.visited:
      return
    self.visited.add((mins, ore_bot, clay_bot, obsidian_bot, geode_bot, ore_count, clay_count, obsidian_count, geode_count))
    #building something on the last step doesn't matter
    if mins == 1:
      self.max = max(self.max, geode_count+geode_bot)
      return

    total_geodes_possible = geode_count
    for i in range(mins):
      total_geodes_possible += geode_bot + i
    if total_geodes_possible < self.max:
      return

    geode = False
    #if you can afford a geode robot do it
    if obsidian_bot and not(ore_count < self.robot_costs["geode"]["ore"] or obsidian_count < self.robot_costs["geode"]["obsidian"]):
      self.get_quality_level(mins-1, ore_bot, clay_bot, obsidian_bot, geode_bot+1, ore_count-self.robot_costs["geode"]["ore"]+ore_bot, clay_count+clay_bot, obsidian_count+obsidian_bot-self.robot_costs["geode"]["obsidian"], geode_count+geode_bot)
      geode = True

    if not geode:
      # one branch purchases obsidian robot if possible and reasonable
      if clay_bot and obsidian_bot * mins + obsidian_count < mins * self.obsidian_max and not(ore_count < self.robot_costs["obsidian"]["ore"] or clay_count < self.robot_costs["obsidian"]["clay"]):
        self.get_quality_level(mins-1, ore_bot, clay_bot, obsidian_bot+1, geode_bot, ore_count-self.robot_costs["obsidian"]["ore"]+ore_bot, clay_count-self.robot_costs["obsidian"]["clay"]+clay_bot, obsidian_count+obsidian_bot, geode_count+geode_bot)

      # one branch purchases clay robot if possible and reasonable
      if ore_count >= self.robot_costs["clay"]["ore"] and clay_bot * mins + clay_count < mins * self.clay_max:
        self.get_quality_level(mins-1, ore_bot, clay_bot+1, obsidian_bot, geode_bot, ore_count-self.robot_costs["clay"]["ore"]+ore_bot, clay_count+clay_bot, obsidian_count+obsidian_bot, geode_count+geode_bot)
        
      # one branch purchases ore robot if possible and reasonable
      if not obsidian_bot and ore_bot * mins + ore_count < mins * self.ore_max and ore_count >= self.robot_costs["ore"]["ore"]:
        self.get_quality_level(mins-1, ore_bot+1, clay_bot, obsidian_bot, geode_bot, ore_count-self.robot_costs["ore"]["ore"]+ore_bot, clay_count+clay_bot, obsidian_count+obsidian_bot, geode_count+geode_bot)
        
      #proceed without purchasing
      self.get_quality_level(mins-1, ore_bot, clay_bot, obsidian_bot, geode_bot, ore_count+ore_bot, clay_count+clay_bot, obsidian_count+obsidian_bot, geode_count+geode_bot)

def get_blueprint_list(inp: list[str]) -> list[Blueprint]:
  blueprint_list = []
  for line in inp:
    m = re.match(r"Blueprint ([0-9]*): Each ore robot costs ([0-9]*) ore. Each clay robot costs ([0-9]*) ore. Each obsidian robot costs ([0-9]*) ore and ([0-9]*) clay. Each geode robot costs ([0-9]*) ore and ([0-9]*) obsidian.", line)
    bloop = Blueprint(int(m.group(1)),int(m.group(2)), int(m.group(3)), [int(m.group(4)), int(m.group(5))], [int(m.group(6)), int(m.group(7))])
    blueprint_list.append(bloop)

  return blueprint_list
