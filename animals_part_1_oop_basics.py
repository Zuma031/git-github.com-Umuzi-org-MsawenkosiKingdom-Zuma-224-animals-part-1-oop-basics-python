class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
    
        return f"{self.name} eats"

    def sound(self):
        return "sound..."


class Dog(Animal):
    def __init__(self, __name__="Rax"):
        self.name = __name__

    def sound(self):
        return "Bark"


class Cat(Animal):
    def __init__(self, __name__="Stormy"):
        self.name = __name__

    def sound(self):
        return "Meow"


class Home:
    def __init__(self):
        self.animal = []

    def adopt_pet(self, animal):
        if animal in self.animal:
            raise Exception("Cannot adopt the same pet twice!")
        else:
            self.animal.append(animal)
        return len(self.animal)

    def make_all_sounds(self):
        sound_list = []
        sound = ""
        for animal in self.animal:
            sound_list.append(animal.sound())
        for animal in sound_list:
            sound = "\n".join(str(animal) for animal in sound_list)
        return sound


if __name__ == "__main__":

    dog1 = Dog()
    dog2 = Dog("Simba")

    dog1.eat()
    dog1.sound()

    dog2.eat()
    dog2.sound()

    cat1 = Cat()
    cat2 = Cat("Smokey")

    cat2.eat()
    cat2.sound()

    home = Home()
    dog1 = Dog()
    dog2 = Dog()
    cat1 = Cat()

    home.make_all_sounds()
    print(home.adopt_pet(dog1))

    home.make_all_sounds()
    print(home.adopt_pet(cat1))

    home.make_all_sounds()
    home.adopt_pet(dog2)

    print(home.make_all_sounds())

    # home.adopt_pet(dog1)

    # home.adopt_pet(cat1)

    # home.adopt_pet(dog2)

    # home.make_all_sounds()

    # (home.adopt_pet(Animal))


# class animal():

#     def __init__(self, name = None):
#         self.name = name

#     def eat(self):
#         print(self.name + " eats")

#     def sound(self):
#         print("sound...")

# class Dog(animal):
#     def sound(self):
#         print("Dog barks")


# class Cat(animal):
#     def sound(self):
#         print("Cat meows")


# class Home():
#     animal = []
#     def adopt_pet(self, animal):
#         if animal in self.animal:
#             raise Exception('Already adopted!')
#         else:
#             self.animal.append(animal)

#     def make_all_sounds(self):
#         for pet in self.animal:
#             pet.sound()


# home = Home()
# dog_1 = Dog()
# dog_2 = Dog()
# cat = Cat()
# home.make_all_sounds()
# home.adopt_pet(dog_1)
# home.make_all_sounds()
# home.adopt_pet(cat)
# home.make_all_sounds()
# home.adopt_pet(dog_2)
# home.make_all_sounds()

# class Home():
#     def __init__(self):
#         self.animal = []
#     def adopt_pet(self, animal):
#         self.animal = []
#         if animal in self.animal:
#             raise Exception('Already adopted!')
#         else:
#             self.animal.append(animal)

#     def make_all_sounds(self):
#         for pet in self.animal:
#             pet.sound()


#    animal = []
#     def append(self, animal=[]):
#         if animal == []:
#             self.animal = []
#             animal.append([animal])
#         return animal == []


# def make_all_sounds(self):
#         sounds = []
#         for pet in self.animal:
#             sounds.append(pet.sound())
#         for n in sounds:
#             me = "\n".join(str (n)for n in sounds)
#         return me
