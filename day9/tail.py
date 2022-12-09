def t_dont_move( t_loc, h_loc):
  if abs(t_loc[1] - h_loc[1]) <= 1 and abs(t_loc[0] - h_loc[0]) <= 1: #x and y overlapping or 1 in either directions
    return True
  return False

def t_catchup(t_loc, h_loc):
  if t_dont_move(t_loc, h_loc):
    return t_loc

  #aligned on one axis, move one coord closer
  if t_loc[0] == h_loc[0]: #same x coord
    if t_loc[1] < h_loc[1]-1:  #more than 1 spot below
      t_loc[1] += 1
    elif t_loc[1] > h_loc[1]+1: #more than 1 spot above
      t_loc[1] -= 1

  elif t_loc[1] == h_loc[1]: #same y coord
    if t_loc[0] < h_loc[0]-1: #more than 1 spot left
      t_loc[0] += 1
    elif t_loc[0] > h_loc[0]+1: #more than 1 spot right
      t_loc[0] -= 1

  #neither x or y is the same, and they're not overlapping so we must move

  # tail is left and below
  elif t_loc[0] < h_loc[0] and t_loc[1] < h_loc[1]:
    t_loc[0] += 1
    t_loc[1] += 1

  # tail is left and above
  elif t_loc[0] < h_loc[0] and t_loc[1] > h_loc[1]:
    t_loc[0] += 1
    t_loc[1] -= 1

  # tail is right and below
  elif t_loc[0] > h_loc[0] and t_loc[1] < h_loc[1]:
    t_loc[0] -= 1
    t_loc[1] += 1

  # tail is right and above
  elif t_loc[0] > h_loc[0] and t_loc[1] > h_loc[1]:
    t_loc[0] -= 1
    t_loc[1] -= 1
    
  return t_loc