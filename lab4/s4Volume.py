class Calculation:
       def calcVolume(self,arg1,arg2=None, arg3=None):
              if arg2 != None:
                     return arg1*arg2*arg3
              else:
                     return 4*3.14*arg1**3/3      

class Sphere(Calculation):
       def __init__(sphr, r):
              sphr.baseRadius = r

       def displaySphere(self):
              print("Sphere volume: ", end='')
              print(self.calcVolume(self.baseRadius))
                    
class Cube(Calculation):
       def __init__(cb, l, w, h):
              cb.length = l
              cb.width = w
              cb.height = h

       def displayCube(c):
              print("Cube volume: ", end='')
              print (c.calcVolume(c.length,
                                   c.width,c.height))


S1=Sphere(float(input("\nSpere Radious:")))
print("\nSphere Volume Calculation")
S1.displaySphere()

C1=Cube(float(input("\nCube length:")),float(input("Cube width:")),
        float(input("Cube height:")))
print("\nCube Volume Calculation")
C1.displayCube()
