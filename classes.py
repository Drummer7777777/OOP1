class Animal():
  size = "unknown"
  is_feed = False
  
  def set_size(self, newsize):
    self.size = newsize
  
  def get_size(self):
    print(self.size)
  
  def feed(self):
    self.is_feed = True 
  
  def need_to_feed(self):
    if self.is_feed == False:
      print("Yes")
    else:
      print("No")  
  
    

  
class Cat(Animal):
  id = 0
  def __init__(self):
    print("Cat was created")
    self.id += 1

  def feed(self, food):
    if food == "milk":
      self.is_feed = True
      print("Meow")
    else:
      print("Cat's eat only milk!")
 

class Dog(Animal):
  id = 0
  def __init__(self):
    print("Dog was created")
    self.id += 1
  
  def feed(self, food):
    if food == "meat":
      self.is_feed = True
      print("Woof")
    else:
      print("Dog's eat only meat!")

      