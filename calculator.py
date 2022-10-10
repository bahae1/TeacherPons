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
  
  

class Tool:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name.upper()

class Droid:
    def __init__(self, name, serial_number, tool):
        self.name = name
        self.serial_number = serial_number
        self.tool = tool  # agregación

    def __str__(self):
        return f'Droid {self.name} armed with a {self.tool}'

a=Calculadora("basica")
