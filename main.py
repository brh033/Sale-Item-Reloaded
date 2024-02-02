#####################################################################
# author: Blaine Hord
# date: 1/17/24
# description: A basic point of sale reporting system using classes and inheritance.
#####################################################################
# An Item has a name, cost and price, all of which are passed in as
# arguments to its constructor. It has accessors and mutators that carry
# out range checking. It also has profit, applySale, and __str__
# functions that carry out the tasks as described in the assignment
# documentation.
class Item:
  def __init__(self, name, cost, price):
    self.name = name
    self.cost = cost
    self.price = price

  #accessor for name
  @property
  def name(self):
    return self._name
  
  #mutator for name
  @name.setter
  def name(self, name):
    self._name = name
  
  #accessor for cost
  @property
  def cost(self):
    return self._cost
  
  #mutator for cost
  @cost.setter
  def cost(self, cost):
    if (cost > 0):
      self._cost = cost
    else:
      self._cost = 0
  
  #accessor for price
  @property
  def price(self):
    return self._price
  
  #mutator for price
  @price.setter
  def price(self, price):
    if (price > 0):
      self._price = price
    else:
      self._price = 0
      
  #profit function
    def profit(self):
      return self.price - self.cost
  
  # SaleItem also has a applySale function that adjusts the price of the
  # item using the percentage provided as an argument to that function.
    def applySale(self, percentage):
      self.price = self.price - ((self.price * percentage)/100)
      return self.price

  # __str__ overload function
  def __str__(self):
    return f"{self.name}\t{self.cost:.2f}\t{self.price:.2f}"
  
#####################################################################
# A Clothing is an Item. In addition to name, cost and price, it also
# has a brand, and size. It receives all 5 pieces of information as
# arguments to its constructor. It overloads the __str__ function and
# also has appropriate accessors and mutators.
class Clothing(Item):
  def __init__(self, name, brand, cost, price, size):
    super().__init__(name, cost, price)
    self.brand = brand
    self.size = size

  @property
  def brand(self):
    return self._brand

  @brand.setter
  def brand(self, brand):
    self._brand = brand

  @property
  def size(self):
    return self._size

  @size.setter
  def size(self, size):
    if (size >= 0):
      self._size = size
    else:
      self._size = "None"
  def __str__(self):
    return f"{self.name}\t{self.cost:.2f}\t{self.price:.2f}\t{self.brand}\tsize:{self.size}"
#####################################################################
# A Food is an Item. In addition to name, cost and price, it also has a
# shelfLife. It only receives name, cost and price as arguments to its
# constructor. It sets all objects created to have a shelfLife of 7 by
# default. It also overloads the __str__ function.
class Food(Item):
  def __init__(self, name, cost, price):
    super().__init__(name, cost, price)
    self.shelfLife = 7

  @property
  def shelfLife(self):
    return self._shelfLife

  @shelfLife.setter
  def shelfLife(self, shelfLife):
    if (shelfLife > 0):
      self._shelfLife = shelfLife
    else:
      self._shelfLife = "None"
      
  def __str__(self):
    return f"{self.name}\t{self.cost:.2f}\t{self.price:.2f}\texpires in {self.shelfLife} days"
#####################################################################
# A Shoe is a Clothing. It only receives cost, price and size as
# arguments to its constructor. It sets all Shoe objects to have a name
# of "Crocs" and brand of "Nike" by default.
class Shoe(Clothing):
  def __init__(self, cost, price, size):
    super().__init__("Crocs", "Nike", cost, price, size)
    
#####################################################################
# A Chips is a Food. It does not receive any arguments for its
# constructor. It sets the name, cost, price and shelfLife to be "Lays",
# 2, 3.50 and 21 respectively.
class Chips(Food):
  def __init__(self):
    super().__init__("Lays", 2, 3.50)
    self.shelfLife = 21