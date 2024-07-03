
class ocean():
  def __init__(self):
    self.N = int(input())
    self.field = []
    for _ in range(self.N):
      self.field.append(list(map(int,input().split())))
    self.time = 0
    self.level = 2
    self.pos = ()
    for i in range(self.N):
      for j in range(self.N):
        if self.field[i][j] == 9:
          self.pos = (i,j)
    self.path = []

    self.target = ()
  def __str__(self):
    rstr = ''
    rstr += f"=====field===== t={self.time}\n"
    for i in range(self.N):
      rstr += " ".join(self.field[i])
      rstr += "\n"
    rstr += f" --> lv:{self.level}\n"
    return rstr

  def find_path(self, x:tuple, y:tuple):
    pass

  def find_new_target(self):
    pass
  
  def run(self):
    if self.path:
      pass # move the path
    else:
      self.find_new_target()
      self.find_path(self.pos, self.target)
      self.run()
    pass
  
if __name__ == "__main__":
  oc = ocean()
  oc.run()
  print(oc.time)
