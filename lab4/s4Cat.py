
class Animal:
       def __init__(self, m):
              self.movement = m
       def printAnimal(self):
              print("Movement: "+self.movement)

class Mammal(Animal):
       def __init__(mml, wb, m):
              Animal.__init__(mml, m)
              mml.warm_blooded= wb
       def printMammal(self):
              self.printAnimal()
              print("Warm blooded: "+self.warm_blooded)

class Cat(Mammal):
       def __init__(kt, c, nol, wb, m):
              Mammal.__init__(kt, wb, m)
              kt.color = c
              kt.no_of_legs= nol
       def printCat(kt):
              kt.printMammal()
              print("Color: "+kt.color+"\n"+
                    "Number of Legs: "+str(kt.no_of_legs))

C1=Cat("White", 4, "Yes", "Yes")
print("\nDetailed Information of Cat:\n")
C1.printCat()

M1=Mammal("Yes", "Yes")
print("\nDetailed Information of Mammal:\n")
M1.printMammal()
