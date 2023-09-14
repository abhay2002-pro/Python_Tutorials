# Encoasulation allows to have fields and functions in a singl entity
# If classes weren't there we would have to create funcctions and variables

player = {'name': 'Abhay', 'age': 12}
print(player['name']) 

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

player2 = PlayerCharacter('Abhay', 21)
print(player2.name)