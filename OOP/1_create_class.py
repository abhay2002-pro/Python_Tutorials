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
    
player1 = PlayerCharacter('Abhay', 21)
player2 = PlayerCharacter('Alok', 19)

# help(PlayerCharacter)

print(player1.run())

PlayerCharacter.membership = False

print(player1.membership)
print(player2.membership)