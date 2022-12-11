from collections import deque

class Monkey:
  def __init__(self, m_id: str, items: str, operation: str, test: str, if_true: str, if_false: str): 
    self.id = self.parse_id(m_id)
    self.items = self.parse_items(items)
    self.operation = operation.replace("Operation: new = old ", "")
    self.test = int(test.replace("Test: divisible by ", ""))
    self.if_true = int(if_true.replace("If true: throw to monkey ", ""))
    self.if_false = int(if_false.replace("If false: throw to monkey ", ""))
    self.inspects = 0

  def parse_id(self, m_id: str) -> int:
    m_id = m_id.replace("Monkey ", "").replace(":", "")
    return int(m_id)

  def parse_items(self, items: str) -> deque:
    item_queue = deque()
    items = items.replace("Starting items: ", "")
    item_list = items.split(", ")
    for item in item_list:
      item_queue.append(int(item))
    return item_queue

  def execute_operation(self, val: int) -> int:
    if self.operation == "* old":
      return val*val
    else:
      parts = self.operation.split(" ")
      if parts[0] == "*":
        return val * int(parts[1])
      else:
        return val + int(parts[1])

  def execute_test(self, val: int) -> bool:
    return val % self.test == 0