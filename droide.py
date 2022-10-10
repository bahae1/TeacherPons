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
