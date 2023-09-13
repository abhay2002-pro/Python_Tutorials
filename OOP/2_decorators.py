# Class should be singular and it should start with capital letter
class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        if self.membership:
            self.name = name # regular class attributes
            self.age = age
    
    def run(self):
        print(f'run {self.name}')
        return 'done'
    
    # kind of static method
    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2
    
    @classmethod
    def create_object(cls, num1, num2):
        return cls('Teddy', num1 + num2)
    
    @staticmethod # static method doesn't give access to class method
    def create_object(num1, num2):
        return num1 + num2
    
player1 = PlayerCharacter('Abhay', 21)
player2 = PlayerCharacter('Alok', 19)

print(PlayerCharacter.adding_things(1, 2))

playerCharacter = PlayerCharacter.create_object(2, 3)
print(playerCharacter.age)