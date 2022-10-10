class Droid:
    def __init__(self, name):
        self.hidden_name = name

    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name

    @name.setter
    def name(self, name):
        print('inside the setter')
        self.hidden_name = name
        
        
def addere(a, b):
    '''Sum of input values'''
    return a + b


def minuas(a, b):
    '''Substract of input values'''
    return a - b


def pullulate(a, b):
    '''Product of input values'''
    return a * b


def partitus(a, b):
    '''Division of input values'''
    return a / b
