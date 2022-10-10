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


class Polynomial(object):
    def __init__(self, coefficients):
        self.coeff = coefficients

    def __call__(self, x):
        return sum([c*x**i for i, c in enumerate(self.coeff)])

    def __add__(self, other):
        maxlength = max(len(self), len(other))
        # Extend both lists with zeros to this maxlength
        self.coeff += [0]*(maxlength - len(self.coeff))
        other.coeff += [0]*(maxlength - len(other.coeff))
        result_coeff = self.coeff
        for i in range(maxlength):
            result_coeff[i] += other.coeff[i]
        return Polynomial(result_coeff)
