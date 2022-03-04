class Dog:
    def __init__(self, name, weight, color, voiceText):
        self.name = name
        self.weight = weight
        self.color = color
        self.voiceText = voiceText

    def Voice(self):
        print(f'{self.name} {self.voiceText}')

obj = Dog('Rex:','weight', 'color', 'Gav Gav')
obj.Voice()

class Cat:
    def __init__(self, name, weight, color, voiceText):
        self.name = name
        self.weight = weight
        self.color = color
        self.voiceText = voiceText

    def Voice(self):
        print(f'{self.name} {self.voiceText}')

obj = Cat('Cat:','weight', 'color', 'myau myau')
obj.Voice()

class Cow:
    def __init__(self, name, weight, color, voiceText):
        self.name = name
        self.weight = weight
        self.color = color
        self.voiceText = voiceText

    def Voice(self):
        print(f'{self.name} {self.voiceText}')

obj = Cow('Cow:','weight', 'color', 'muu muu')
obj.Voice()

class Bear:
    def __init__(self, name, weight, color, voiceText):
        self.name = name
        self.weight = weight
        self.color = color
        self.voiceText = voiceText


    def Voice(self):
        print(f'{self.name} {self.voiceText}')

obj = Bear('mixalych:','weight', 'color', 'arr arr')
obj.Voice()

