class Dog:
    def __init__(self, weight, color, voiceText):
        self.weight = weight
        self.color = color
        self.voiceText = voiceText
        """instance"""

    def Voice(self):
        print(f'{self.voiceText}')

obj = Dog('weight', 'color', 'Gav Gav')
obj.Voice()

class Cat:
    def __init__(self, weight, color, voiceText):
        self.weight = weight
        self.color = color
        self.voiceText = voiceText
        """instance"""

    def Voice(self):
        print(f'{self.voiceText}')

obj = Cat('weight', 'color', 'myau myau')
obj.Voice()

class Cow:
    def __init__(self, weight, color, voiceText):
        self.weight = weight
        self.color = color
        self.voiceText = voiceText
        """instance"""

    def Voice(self):
        print(f'{self.voiceText}')

obj = Cow('weight', 'color', 'muu muu')
obj.Voice()

class Bear:
    def __init__(self, weight, color, voiceText):
        self.weight = weight
        self.color = color
        self.voiceText = voiceText
        """instance"""

    def Voice(self):
        print(f'{self.voiceText}')

obj = Bear('weight', 'color', 'arr arr')
obj.Voice()
