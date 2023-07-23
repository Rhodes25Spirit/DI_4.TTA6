#_______________Exercise 1_____________________________________

class Cat:
    instances = {}
    def __init__(self, kat_name, kat_age):
        self.name = kat_name
        self.age = kat_age
        Cat.instances.update({kat_name: kat_age})

lucky = Cat('Lucky', 5)
grey = Cat('Grey', 11)
usha = Cat('Usha', 13)

def oldest_cat():
    sorted_cats_by_age = sorted(Cat.instances.items(), key = lambda x:x[1], reverse = True)
    return sorted_cats_by_age[0]

print(f'{oldest_cat()} is the oldest cat')

#_______________Exercise 2_____________________________________
class Dog:
    instances = {}
    def __init__(self, name, height):
        self.name = name
        self.height = height
        Dog.instances.update({name:height})
    def bark(self):
        print(f'{self.name} goes Wooof!')
    def jump(self):
        print(f'{self.name} jumps {self.height * 2} cm high!')

davids_dog = Dog('Rex', 50)
print(davids_dog.name, davids_dog.height)
Dog.bark(davids_dog)
Dog.jump(davids_dog)
sarahs_dog = Dog('Teacup', 20)
print(sarahs_dog.name, sarahs_dog.height)
Dog.bark(sarahs_dog)
Dog.jump(sarahs_dog)

sorted_dogs_by_height = sorted(Dog.instances.items(), key = lambda x:x[1], reverse = True)
print(f'{sorted_dogs_by_height[0]} is bigger')

#_______________Exercise 3_____________________________________
class Song:
    def __init__(self, lyrics = []):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        song_str = ''
        for i in range(len(self.lyrics)):
            song_str = song_str + self.lyrics[i] + '\n'
        return song_str

stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
print(Song.sing_me_a_song(stairway))

#_______________Exercise 4_____________________________________
class Zoo:
    animals = []
    def __init__(self, zoo_name):
        self.name = zoo_name
    def add_animal(new_animal):
        if not new_animal in Zoo.animals:
            Zoo.animals.append(new_animal)
    def get_animals():
        print(Zoo.animals)
    def sell_animal(animal):
        if animal in Zoo.animals:
            Zoo.animals.remove(animal)
    def sort_animals():
        animal_catalogue = {}
        Zoo.animals.sort()
        i = 1
        for item in Zoo.animals:
            if item[0].upper() in [k[0] for k in animal_catalogue.keys()]: 
                i += 1
                animal_catalogue[item[0].upper()].append(item) 
            else: 
                i = 1
                animal_catalogue[item[0].upper()] = []
                animal_catalogue[item[0].upper()].append(item)
        return animal_catalogue 
    def get_groups():
        Zoo.sort_animals()
        print(Zoo.sort_animals())

def ramat_gan_safari():
    choice = int(input('What shall we do with the zoo? 1 - show available animals, 2 - add an animal, 3 - sell animal '))
    if choice == 1:
        Zoo.get_groups()
    elif choice == 2:
        animal_input = input('Type the animal you want to purchase. First letter should be capital ')
        Zoo.add_animal(animal_input)
    elif choice == 3:
        animal_input = input('Type the name an animal you want to sell. First letter should be capital')
        Zoo.sell_animal(animal_input)
    else:
        print('Unknown command')
    ramat_gan_safari()

ramat_gan_safari()
    

        

# to be sure that everything works
Zoo.add_animal('Monkey')
Zoo.add_animal('Cheetah')
Zoo.add_animal('Lion')
Zoo.add_animal('Bear')
Zoo.add_animal('Flamingo')
Zoo.add_animal('Kangaroo')
Zoo.add_animal('Panda')
Zoo.add_animal('Sloth')
Zoo.add_animal('Camel')
Zoo.sell_animal('Elephant')
Zoo.get_animals()
Zoo.sort_animals()
Zoo.get_groups() 