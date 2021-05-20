class Sublevel:
  def __init__(self, name, pel):
    self.name = name
    self.pel = pel
    if name == "s":
      self.max_amt_electrons = 2
    elif name == "p":
      self.max_amt_electrons = 6
    elif name == "d":
      self.max_amt_electrons = 10
    elif name == "f":
      self.max_amt_electrons = 14
    else:
      raise ValueError(f"There are no subleves with a {name} name")

def count(arr, item):
  num = 0
  for value in arr:
    if value == item:
      num += 1
  return num
    
s1 = Sublevel("s",1)
s2 = Sublevel("s",2)
s3 = Sublevel("s",3)
s4 = Sublevel("s",4)
s5 = Sublevel("s",5)
s6 = Sublevel("s",6)
s7 = Sublevel("s",7)

p2 = Sublevel("p",2)
p3 = Sublevel("p",3)
p4 = Sublevel("p",4)
p5 = Sublevel("p",5)
p6 = Sublevel("p",6)
p7 = Sublevel("p",7)

d3 = Sublevel("d",3)
d4 = Sublevel("d",4)
d5 = Sublevel("d",5)
d6 = Sublevel("d",6)

f4 = Sublevel("f",4)
f5 = Sublevel("f",5)

permOrder = [s1,s2,p2,s3,p3,s4,d3,p4,s5,d4,p5,s6,f4,d5,p6,s7,f5,d6,p7]
tempOrder = permOrder.copy()
electronConfiguration = ""
i = 0

if name == "__main__":

  amtOfElectrons = int(input("How many electrons does this element have?\n"))
  while amtOfElectrons > 0:
    i += 1
    if amtOfElectrons >= tempOrder[0].max_amt_electrons:
      electronConfiguration += str(tempOrder[0].pel) + tempOrder[0].name + "^"  + str(tempOrder[0].max_amt_electrons)
      amtOfElectrons -= tempOrder[0].max_amt_electrons
      tempOrder = tempOrder[1:]
    else:
      
      electronConfiguration += str(tempOrder[0].pel) + tempOrder[0].name + "^" + str(amtOfElectrons)
      amtOfElectrons -= tempOrder[0].max_amt_electrons
    electronConfiguration += ""

  if electronConfiguration[-1] == " ":
    electronConfiguration = electronConfiguration[:-1]

  print(electronConfiguration)
