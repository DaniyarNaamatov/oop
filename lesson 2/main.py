"""абст"""
class Animal:
    def __int__(self,name,type,color,voiceText):
        self.name = name
        self.type = type
        self.color = color
        self.voiceText = voiceText

    def voice(self):
        print(self.voiceText)

    """насл"""
class Dog(Animal):
    def __init__(self, name, type, color, voiceText):
        super().__init__(name, type, color, voiceText)

rex = Dog ('Rex','DONESTIC','BLACK','GAF GAF')
rex.voice()

class Cat(Animal):
    def __init__(self, name, type, color, voiceText):
        super().__init__(name, type, color, voiceText)
rex = Dog(
            'Rex',
            'DONESTIC',
            'BLACK',
            'GAF GAF')
rex.voice()


"""поли"""
class Horse(Animal):
    def __init__(self,name,type,color,voiceText,speed,weight):
        super().__init__(name,type,color, voiceText)
        self.speed = speed
        self.weight = weight


        """полли"""
    def voice(self):
        print(f"{self.name}:{self.voiceText}")

mustang = Horse('mustang', 'donestik', 'brown', 'ihaa ihaa', 30, 250)
mustang.voice()

"""Ипккап"""





