
class Opcode:
  def __init__(self, code: list[str], custom_input=1):
    self.initify_input(code)
    self.code = code
    self.custom_input = custom_input
    self.output = []

  def split_code(self, full_code: str) -> list[int]:
    listcode = []
    str_opcode = str(full_code)
    if len(str_opcode) < 5:
      for _ in range(5-len(str_opcode)):
        listcode.append(0)
    for i in range(len(str_opcode)):
      listcode.append(int(str_opcode[i]))
    return listcode

  def initify_input(self, code: list[str]) -> list[int]:
    for i in range(len(code)):
      code[i] = int(code[i])
    return code[i]

  def get_value(self, i: int, mode: int):
    if mode == 0:
      return self.code[self.code[i]]
    else:
      return self.code[i]

  def process(self) -> int:
    i = 0
    #1 is addition, 2 is multiplication, 3 saves input to location, 4 outputs value at location
    while self.code[i] != 99:
      full_code = self.split_code(self.code[i])
      opcode = full_code[4]
      first_param = full_code[2]
      second_param = full_code[1]
      third_param = full_code[0]

      if opcode == 1 or opcode == 2:
        a = i+1
        b = i+2
        a_val = self.get_value(a, first_param)
        b_val = self.get_value(b, second_param)
        loc = self.code[i+3]
        if opcode == 1:
          self.code[loc] = a_val + b_val
        if opcode ==2:
          self.code[loc] = a_val * b_val
        i += 4
      
      if opcode == 3 or opcode == 4:
        a = i+1
        if opcode == 3:
          self.code[self.code[a]] = self.custom_input
        if opcode == 4:
          self.output.append(self.get_value(a, first_param))
        i += 2