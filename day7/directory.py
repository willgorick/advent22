from collections import defaultdict

class Directory():
  def __init__(self, name: str, children: defaultdict, res: int, parent=None, root=None):
    self.children = children
    self.parent = parent
    self.name = name
    self.type = "dir"
    self.res = res
    self.size_list = []
    self.root = root

  def print_dfs(self, ind):
    if ind == 0:
      print(self.name + " (dir) ")
      ind += 1
    for name, child in self.children.items():
      print("  "*ind + "- " + name + " (" + child.type, end="")
      if child.type == "file":
        print(f", size={child.size})")
      if child.type == "dir":
        print(")")
        child.print_dfs(ind+1)

  def count_dfs(self):
    curr_sum = 0
    for _, child in self.children.items():
      if child.type == "file":
        curr_sum += child.size
      if child.type == "dir":
        curr_sum += child.count_dfs()
    if curr_sum < 100000:
      self.root.res += curr_sum
    self.root.size_list.append(curr_sum)
    return curr_sum

class File():
  def __init__(self, name: str, size: int, parent: Directory):
    self.parent = parent
    self.size = size
    self.name = name
    self.type = "file"


def create_dir(inp: list[str]):
    curr_dir = Directory("/", {}, 0)
    curr_dir.root = curr_dir
    for i in range(len(inp)):
      line = inp[i]
      #commands
      if line[0] == "$":
        #cd commands
        if line[2] == "c":
          # cd up
          if line == "$ cd ..":
            curr_dir = curr_dir.parent
          # cd all the way up
          elif line == "$ cd /":
            while curr_dir.parent:
              curr_dir = curr_dir.parent
          # cd'ing into specific one
          else:
            new_dir = line.split(" ")[2]
            curr_dir = curr_dir.children[new_dir]
            
        #ls commands can effectively be ignored
        
      #if not a command, we're inside an ls
      else:
        #first is file size or dir
        #second is file or dir name
        first, second = line.split(" ")
        #file
        if first.isdigit():
          curr_dir.children[second] = (File(second, int(first), curr_dir))
        #dir
        else:
          curr_dir.children[second] = Directory(second, {}, 0, curr_dir, curr_dir.root)

    while curr_dir.parent:
        curr_dir = curr_dir.parent
    return curr_dir