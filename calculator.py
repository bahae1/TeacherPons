class Calculadora():
  #class calculator, with init and two methods
  
  def __init__(self,nombre):
    self.nombre=nombre
    
  def modelo(self):
    return self.nombre
  
  
  
  #sumar method
  @staticmethod
  def sumar(x,y):
    return x+y

a=Calculadora("basica")
