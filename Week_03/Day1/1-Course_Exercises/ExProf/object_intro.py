class Animal:

    def __init__(self, name='Animal'): # init - initialization of the object
        self.name = name # self - reference to the object


obj1 = Animal(name='Dog')
print(obj1.name)

obj2 = Animal(name='Zebra')
print(obj2.name)

Animal()