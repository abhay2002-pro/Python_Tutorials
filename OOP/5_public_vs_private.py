class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print('run')
    
    def speak(self):
        print(f'I am {self._name}, and I am {self._age} years old')

# There's nothing like private in python
# As a programmer we can only mention that a vairable or method is private using _
# But that doesn't add anything to the interpreter

player1 = PlayerCharacter('player1', 12)
player1.speak()