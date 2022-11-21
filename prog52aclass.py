class shape:
  def __init__(self, length, width):
    self.length = length
    self.width = width
    self.area = 0
    self.perim = 0

  def getArea(self):
    return self.area

  def getperim(self):
    return self.perim

def main():
  self.area = self.length * self.width 
  self.perim = 2 * self.length * self.width
  len = int(input("enter lenth: "))
  wid = int(input("enter width: "))
  shape = shape(len, wid)
  shape.calc()
  area = shape.getArea()
  perim = shape.getPerim()
  print("area:", area)
  print("Perimeter:", perim)
  pass
if __name__ == "__main__":
  main()