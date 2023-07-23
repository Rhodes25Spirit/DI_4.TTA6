class Animal:

    def __init__(self, legs, name='Animal'): # init - initialization of the object
        self.name = name # self - reference to the object
        self.legs = legs

    def voice(self): # method
        print(f"{self.name} is doing a voice")

    def jump(self): # method
        if self.legs == 0:
            print(f"{self.name} cannot jump!")
        else:
            print(f"{self.name} jumps with {self.legs} legs")

obj1 = Animal(legs=4, name='Dog') # __init__

obj1.voice()

obj2 = Animal(legs=4, name='Zebra')

obj2.voice()

obj3 = Animal(legs=0, name="Snake")

obj3.jump()