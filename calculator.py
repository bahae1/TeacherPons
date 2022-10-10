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



class circulo():
	def __init__(self,radio):
		self.radio=radio
	
	@property
	def radio(self):
		print("Estoy dando el radio")
		return self._radio	

	@radio.setter
	def radio(self,radio):
		if radio>=0:
			self._radio = radio
		else:
			raise ValueError("Radio positivo")
			self._radio=0
