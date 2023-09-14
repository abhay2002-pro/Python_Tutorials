# multiple inhertiance is allowed in python

class User:
    def sign_in(self):
        print('logged in')
    
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    pass

class Archer(User):
    def __init__(self, name, num_of_arrows):
        self.name = name
        self.num_of_arrows = num_of_arrows
    pass

wizrd1 = Wizard('merlin', 50)
print(wizrd1.sign_in())
print(wizrd1.name)

print(isinstance(wizrd1, Wizard))
print(isinstance(wizrd1, User)) # As for creating wizrd1 we had to run User class as well
print(isinstance(wizrd1, object)) # object is the base class from which everything inherits dunder mthods 